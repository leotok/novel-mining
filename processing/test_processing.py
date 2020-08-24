import unittest
from processing import book_processing
import pandas as pd


class TestBookProcessing(unittest.TestCase):

    def setUp(self):
        self.book = (
            'Chapter 1\n'
            '\n'
            'asdasdasd\n'
            '\n'
            '1 \n' 
            '\n'
            'asdasd\n'
            '\n'
            '2 \n'
            '\n'
            'Chapter 2\n'
            '\n'
            '123123\n'
            '\n'
            '3 \n'
            '\n'
            '23423243\n'
            '\n'
            '4 \n'
            '\n'
            'asdasdasd\n'
            '\n'
            '5 \n' 
        )

    def test_split_chapters(self):
        chapters = book_processing.get_chapters(self.book)
        self.assertEqual(len(chapters), 2)

    def test_split_pages(self):
        pages = book_processing.get_pages(self.book)
        self.assertEqual(len(pages), 5)

    def test_clean_text(self):
        text_cleaned = book_processing.clean_text('  THIS is À TÉst  ')
        self.assertEqual(text_cleaned, 'this is a test')

    def test_force_match_person(self):
        df = pd.DataFrame([
            ['john', 'PERSON'], 
            ['mary', 'PERSON'],
            ['john', 'ORG'],
        ], columns=['text_clean', 'label'])

        df_fix = book_processing.force_match_person_entities(df)
        self.assertTrue([df_fix.label_fix == 'PERSON'][0].all())

    def test_generate_relationship_graph(self):
        df = pd.DataFrame([
            ['John', 'john', 'PERSON', '1', '1', '1', '3'], 
            ['John', 'john', 'PERSON', '3', '4', '1', '3'], 
            ['Mary', 'mary', 'PERSON', '1', '2', '1', '2'],
            ['Mary', 'mary', 'PERSON', '2', '3', '1', '2'],
            ['Jose', 'jose', 'PERSON', '3', '5', '3', '3'],
        ], columns=['text', 'text_clean', 'label_fix', 'page', 'pos', 'first_page', 'last_page'])
        graph = book_processing.generate_relationship_graph(df)
        expected_graph = {
            'john': {
                'first_page': '1',
                'last_page': '3',
                'type': 'PERSON',
                'pos': ['1', '4'],
                'pages': ['1', '3'],
                'name': 'John',
                'relations': [{
                    'from': 'john',
                    'to': 'jose'
                }, {
                    'from': 'john',
                    'to': 'mary'
                }]
            },
            'mary': {
                'first_page': '1',
                'last_page': '2',
                'type': 'PERSON',
                'pos': ['2', '3'],
                'pages': ['1', '2'],
                'name': 'Mary',
                'relations': [{
                    'from': 'mary',
                    'to': 'john'
                }]
            },
            'jose': {
                'first_page': '3',
                'last_page': '3',
                'type': 'PERSON',
                'pos': ['5'],
                'pages': ['3'],
                'name': 'Jose',
                'relations': [{
                    'from': 'jose',
                    'to': 'john'
                }]
            }
        }
        self.maxDiff = None
        self.assertEqual(expected_graph, graph)

if __name__ == '__main__':
    unittest.main()