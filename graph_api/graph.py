import json


class RelationshipGraph:

    def __init__(self, mock=False):
        if mock:
            self.characters_info = {
                'Ursula': {
                    'pages': [1],
                    'first_page': 1,
                    'last_page': 100,
                    'description': 'asd',
                },
                'Jose Arcadio Buendia': {
                    'pages': [2],
                    'first_page': 2,
                    'last_page': 100,
                    'description': 'asd',
                },
                'Jose Arcadio': {
                    'pages': [10],
                    'first_page': 10,
                    'last_page': 100,
                    'description': 'asd',
                },
                'Aureliano': {
                    'pages': [35],
                    'first_page': 35,
                    'last_page': 100,
                    'description': 'asd',
                },
                'Rebeca': {
                    'pages': [70],
                    'first_page': 70,
                    'last_page': 100,
                    'description': 'asd',
                }
            }
            self.graph = {
                'Ursula': [{'to': 'Jose Arcadio Buendia', 'label': 'esposa'}, {'to': 'Jose Arcadio', 'label': 'mae'}, {'to': 'Aureliano', 'label': 'mae'}, {'to': 'Rebeca', 'label': 'mae'}],
                'Jose Arcadio Buendia': [{ 'to': 'Ursula', 'label': 'marido'}, { 'to': 'Jose Arcadio', 'label': 'pai'}, { 'to': 'Aureliano', 'label': 'pai'}, { 'to': 'Rebeca', 'label': 'pai'}],
                'Jose Arcadio': [{ 'to': 'Ursula', 'label': 'filho'}, { 'to': 'Jose Arcadio Buendia', 'label': 'filho'}, { 'to': 'Aureliano', 'label': 'irmao'}, { 'to': 'Rebeca', 'label': 'irmao'}],
                'Aureliano': [{ 'to': 'Ursula', 'label': 'filho'}, { 'to': 'Jose Arcadio Buendia', 'label': 'filho'}, { 'to': 'Jose Arcadio', 'label': 'irmao'}, { 'to': 'Rebeca', 'label': 'irmao'}],
                'Rebeca': [{ 'to': 'Ursula', 'label': 'filha'}, { 'to': 'Jose Arcadio Buendia', 'label': 'filha'}, { 'to': 'Aureliano', 'label': 'irma'}, { 'to': 'Jose Arcadio', 'label': 'irma'}],
            }
        else:
            self.characters_info = json.load(open('data/entities_info.json'))
            self.graph = {e: [] for e in self.characters_info.keys()}
        
        self.max_page = 0
        for info in self.characters_info.values():
            if info['last_page'] > self.max_page:
                self.max_page = info['last_page']

    def get_graph(self):
        return { c: {'relations': r, 'name': c, **self.characters_info[c] }for c, r in self.graph.items()}

    def get_characters(self, graph):
        return [{'name': k, **v} for k, v in self.characters_info.items() if k in graph]

    def get_edges(self, graph):
        return [{'from': a, 'to': b['to']} for a, v in graph.items() for b in v['relations']]

    def get_subgraph_until_page(self, page):
        subgraph = {}
        for c1, relations in self.graph.items():
            if self.characters_info[c1]['first_page'] > page:
                continue
            subgraph[c1] = {
                'relations': [c2 for c2 in relations if self.characters_info[c2['to']]['first_page'] <= page],
                'name': c1,
                **self.characters_info[c1],
            }
        return subgraph
