# Author: Leonardo Edelman Wajnsztok
# Date: 07/2020

import json


class RelationshipGraph:

    def __init__(self, mock=False, mock_data=None):
        if mock_data:
            self.characters_info = mock_data
        elif mock:
            self.characters_info = {
                'ursula': {
                    'name': 'Ursula',
                    'pages': [1],
                    'first_page': 1,
                    'last_page': 100,
                    'description': 'asd',
                    'relations': [{'to': 'Jose Arcadio Buendia', 'label': 'esposa'}, {'to': 'Jose Arcadio', 'label': 'mae'}, {'to': 'Aureliano', 'label': 'mae'}, {'to': 'Rebeca', 'label': 'mae'}]
                },
                'jose arcadio buendia': {
                    'name': 'Jose Arcadio Buendia',
                    'pages': [2],
                    'first_page': 2,
                    'last_page': 100,
                    'description': 'asd',
                    'relations': [{ 'to': 'Ursula', 'label': 'marido'}, { 'to': 'Jose Arcadio', 'label': 'pai'}, { 'to': 'Aureliano', 'label': 'pai'}, { 'to': 'Rebeca', 'label': 'pai'}]
                },
                'jose arcadio': {
                    'name': 'Jose Arcadio',
                    'pages': [10],
                    'first_page': 10,
                    'last_page': 100,
                    'description': 'asd',
                    'relations': [{ 'to': 'Ursula', 'label': 'filho'}, { 'to': 'Jose Arcadio Buendia', 'label': 'filho'}, { 'to': 'Aureliano', 'label': 'irmao'}, { 'to': 'Rebeca', 'label': 'irmao'}],
                },
                'aureliano': {
                    'name': 'Aureliano',
                    'pages': [35],
                    'first_page': 35,
                    'last_page': 100,
                    'description': 'asd',
                    'relations': [{ 'to': 'Ursula', 'label': 'filho'}, { 'to': 'Jose Arcadio Buendia', 'label': 'filho'}, { 'to': 'Jose Arcadio', 'label': 'irmao'}, { 'to': 'Rebeca', 'label': 'irmao'}],
                },
                'rebeca': {
                    'name': 'Rebeca',
                    'pages': [70],
                    'first_page': 70,
                    'last_page': 100,
                    'description': 'asd',
                    'relations': [{ 'to': 'Ursula', 'label': 'filha'}, { 'to': 'Jose Arcadio Buendia', 'label': 'filha'}, { 'to': 'Aureliano', 'label': 'irma'}, { 'to': 'Jose Arcadio', 'label': 'irma'}],
                }
            }
        else:
            self.characters_info = json.load(open('data/entities_info.json'))

        self.max_page = 0
        for info in self.characters_info.values():
            if info['last_page'] > self.max_page:
                self.max_page = info['last_page']

    # Returns the complete relationship graph
    # @return dict
    def get_graph(self):
        return self.characters_info

    # Return a list of characters of a given relationship graph
    # @param graph: dict representing a subgraph of the relationship graph
    # @return list of characters
    def get_characters(self, graph):
        return [{**v, 'id': k} for k, v in self.characters_info.items() if k in graph]

    # Return a list of relationships of a given relationship graph
    # @param graph: dict representing a subgraph of the relationship graph
    # @param ignore_direction: boolean indication if should consider a directed graph
    # @return list of relationships
    def get_edges(self, graph, ignore_direction=True):
        if ignore_direction:
            edges = set()
            for a, v in graph.items():
                for b in v['relations']:
                    if a > b['to']:
                        edges.add((a,b['to']))
                    else:
                        edges.add((b['to'], a))
            return sorted([{'from': a, 'to': b} for a, b in edges], key=lambda x: x['from'])
        return sorted([{'from': a, 'to': b['to']} for a, v in graph.items() for b in v['relations']], key=lambda x: x['from'])

    # Return a subgraph of the relationship graph considering information known until the specified page
    # @param page: int
    # @return dict representing a subgraph of the relationship graph
    def get_subgraph_until_page(self, page):
        subgraph = {}
        for c1, info in self.characters_info.items():
            if info['first_page'] > page:
                continue
            subgraph[c1] = {
                **info,
                'relations': [c2 for c2 in info['relations'] if self.characters_info[c2['to']]['first_page'] <= page],
            }
        return subgraph
