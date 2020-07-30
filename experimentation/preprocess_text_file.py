# References:
# https://archive.org/stream/OneHundredYearsOfSolitude_201710/One_Hundred_Years_of_Solitude_djvu.txt
# https://spacy.io/usage/spacy-101
# https://spacy.io/api/annotation#named-entities

import pandas as pd
import re
import spacy

def get_chapters(book: str) -> [str]:
    return [c.strip() for c in re.split('Chapter \d', book)][1:]

def get_pages(book):
    pagination_map = [int(p) for p in re.findall('\n(\d+) \\n?', book)]
    pages = re.split('\n\d+ \\n', book)
    return pages, pagination_map

def get_token_to_page_map():
    pass


if __name__ == "__main__":
    
    book_path = 'data/one_hundred_years_of_solitude_EN.txt'

    with open(book_path, 'r') as f:
        book = f.read()

    import ipdb; ipdb.set_trace(context=30)

    pages, pagination_map = get_pages(book)
    chapters = get_chapters(book)

    print (f'Nº chapters: {len(chapters)}')

    first_page = pages[0]
    first_chapter = chapters[0]

    nlp = spacy.load("en_core_web_sm")
    doc = nlp(first_page)

    for ent in doc.ents:
        if ent.label_ == 'PERSON':
            print(ent.text, ent.start_char, ent.end_char, ent.label_)

    for token in doc:
        if token.pos_ == 'PRON':
            print (token)
