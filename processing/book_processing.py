import pandas as pd
import re
import unidecode
import spacy
from spacy.tokens import Doc, Token
import json

nlp = spacy.load("en_core_web_sm")

Token.set_extension("page", default=None, force=True)
Doc.set_extension("page", default=None, force=True)

def get_chapters(book: str) -> [str]:
    return [c.strip() for c in re.split('Chapter \d', book)][1:]

def get_pages(book):
    pages = []
    last_page_end = 0
    for p in re.finditer('\n(\d+) \\n?', book):
        pages.append((book[last_page_end:p.end()], {
        'start': p.start(), 
        'end': p.end(),
        'page': int(p.groups()[0])
        }))
        last_page_end = p.end()
    return pages


def load_book(book_path):
    with open(book_path, 'r') as f:
        book = f.read()
    return book

def get_documents(pages):
    docs = []
    for doc, context in nlp.pipe(pages, as_tuples=True):
        doc._.page = context["page"]
        for t in doc:
            t._.page = context["page"]
        docs.append(doc)
    return docs

def get_entities_df(docs):
    entities_lst = []
    for doc in docs:
        for ent in doc.ents:
            e = {'entity': ent, 'text': ent.text, 'label': ent.label_, 'pos': ent.start }
            entities_lst.append(e)
    return pd.DataFrame(entities_lst)

def clean_text(text):
    text = text.strip()
    text = text.lower()
    text = unidecode.unidecode(text)
    return text

def force_match_person_entities(entities_df):
    # all entities tokens that have at least one match as PERSON 
    # for the same token will be considered a PERSON entity in all occurances

    text_entities = entities_df.groupby(['text_clean', 'label']).size().reset_index(name='total').sort_values('total', ascending=False)
    person_df = entities_df[entities_df.label == 'PERSON'].groupby('text_clean').size().reset_index(name='total').sort_values('total', ascending=False)
    person_df = person_df.set_index('text_clean')

    text_entities['label_fix'] = text_entities.apply(lambda e: 'PERSON' if e.text_clean in person_df.index else e.label, axis=1)
    person_fix_df = text_entities[text_entities.label_fix == 'PERSON'].groupby(['label_fix', 'text_clean']).size().reset_index(name='total').sort_values('total', ascending=False)
    entities_person_fix_df = pd.merge(entities_df, person_fix_df, on='text_clean', how="left")
    entities_person_fix_df.label_fix = entities_person_fix_df.label_fix.fillna(entities_person_fix_df.label)
    return entities_person_fix_df.drop('total', axis=1)

def add_page_to_entities(entities_person_df):
    entities_person_df['page'] = entities_person_df.entity.apply(lambda e: e[0]._.page)
    first_and_last_page_df = entities_person_df.groupby('text_clean').agg(first_page=('page', 'min'), last_page=('page', 'max'))
    return pd.merge(entities_person_df, first_and_last_page_df, on='text_clean', how="left")

def generate_relationship_graph(entities_person_page_df):
    entities_info = {}
    entities_by_page = {}

    for i, row in entities_person_page_df.iterrows():
        key = row['text_clean']
        if row['label_fix'] != 'PERSON' or row['text'][0].islower():
            continue
            
        if row['page'] in entities_by_page:
            entities_by_page[row['page']].append(key)
        else:
            entities_by_page[row['page']] = [key]
        
        if key not in entities_info:
            entities_info[key] = {
                'first_page': row['first_page'],
                'last_page': row['last_page'],
                'type': row['label_fix'],
                'pos': [row['pos']],
                'pages': {row['page']},
                'name': row['text'],
            }
        else:
            entities_info[key]['pos'].append(row['pos'])
            entities_info[key]['pages'].add(row['page'])
            
    for k in entities_info.keys():
        entities_info[k]['pages'] = sorted(list(entities_info[k]['pages']))
        relations = set()
        for p in entities_info[k]['pages']:
            relations.update(set(entities_by_page[p]))
        entities_info[k]['relations'] = sorted([{'from': k, 'to': r} for r in relations if k != r], key=lambda x: x['to'])

    return entities_info


if __name__ == "__main__":
    
    book_name = 'One Hundred Years of Solitude'
    book_path = 'data/one_hundred_years_of_solitude_EN.txt'

    print (f'Starting to process the book "{book_name}"...')
    
    print (f'Reading book from "{book_path}"')
    book = load_book(book_path)

    pages = get_pages(book)
    print (f'Found {len(pages)} pages.')
    docs = get_documents(pages)

    entities_df = get_entities_df(docs)
    entities_df['text_clean'] = entities_df.text.apply(lambda t: clean_text(t))

    entities_person_df = force_match_person_entities(entities_df)

    num_characters = entities_person_df.query('label_fix == "PERSON"').shape[0]
    print (f'Found {num_characters} characters.')

    entities_person_page_df = add_page_to_entities(entities_person_df)

    print ('Generating relationship graph...')
    entities_info = generate_relationship_graph(entities_person_page_df)

    book_key = '_'.join(book_name.lower().split())
    graph_path = f'data/entities_info_{book_key}.json'

    print (f'Saving graph at "{graph_path}"')
    json.dump(entities_info, open(graph_path, 'w'))

    

