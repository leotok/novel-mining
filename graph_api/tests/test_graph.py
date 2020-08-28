# Author: Leonardo Edelman Wajnsztok
# Date: 07/2020

import unittest
from graph_api import graph
import pandas as pd


class TestBookProcessing(unittest.TestCase):

    def setUp(self):
        mock_data = {
            'john': {
                'first_page': 1,
                'last_page': 3,
                'type': 'PERSON',
                'pos': ['1', '4'],
                'pages': [1, 3],
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
                'first_page': 1,
                'last_page': 2,
                'type': 'PERSON',
                'pos': [2, 3],
                'pages': [1, 2],
                'name': 'Mary',
                'relations': [{
                    'from': 'mary',
                    'to': 'john'
                }]
            },
            'jose': {
                'first_page': 3,
                'last_page': 3,
                'type': 'PERSON',
                'pos': [5],
                'pages': [3],
                'name': 'Jose',
                'relations': [{
                    'from': 'jose',
                    'to': 'john'
                }]
            }
        }
        self.graph = graph.RelationshipGraph(mock_data=mock_data)

    def test_characters(self):
        subgraph = self.graph.get_graph()
        characters = self.graph.get_characters(subgraph)
        expected_characters = [{
            'first_page': 1,
            'last_page': 3,
            'type': 'PERSON',
            'pos': ['1', '4'],
            'pages': [1, 3],
            'name': 'John',
            'relations': [{
                'from': 'john',
                'to': 'jose'
            }, {
                'from': 'john',
                'to': 'mary'
            }],
            'id': 'john'
        }, {
            'first_page': 1,
            'last_page': 2,
            'type': 'PERSON',
            'pos': [2, 3],
            'pages': [1, 2],
            'name': 'Mary',
            'relations': [{
                'from': 'mary',
                'to': 'john'
            }],
            'id': 'mary'
        }, {
            'first_page': 3,
            'last_page': 3,
            'type': 'PERSON',
            'pos': [5],
            'pages': [3],
            'name': 'Jose',
            'relations': [{
                'from': 'jose',
                'to': 'john'
            }],
            'id': 'jose'
        }]
        self.assertEqual(expected_characters, characters)

    def test_edges(self):
        subgraph = self.graph.get_graph()
        edges = self.graph.get_edges(subgraph)
        expected_edges = [{'from': 'jose', 'to': 'john'}, {'from': 'mary', 'to': 'john'}]
        self.assertEqual(expected_edges, edges)

    def test_edges_page_two(self):
        subgraph = self.graph.get_subgraph_until_page(1)
        edges = self.graph.get_edges(subgraph)
        expected_edges = [{'from': 'mary', 'to': 'john'}]
        self.assertEqual(expected_edges, edges)

if __name__ == '__main__':
    unittest.main()