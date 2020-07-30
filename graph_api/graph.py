class RelationshipGraph:

    def __init__(self):
        self.characters_info = {
            'Ursula': {
                'page': 1,
                'description': 'asd',
            },
            'Jose Arcadio Buendia': {
                'page': 2,
                'description': 'asd',
            },
            'Jose Arcadio': {
                'page': 10,
                'description': 'asd',
            },
            'Aureliano': {
                'page': 35,
                'description': 'asd',
            },
            'Rebeca': {
                'page': 70,
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

    def get_characters(self, graph):
        return [{'name': k, **v} for k, v in self.characters_info.items() if k in graph]

    def get_edges(self, graph):
        return [{'from': a, 'to': b['to']} for a, v in graph.items() for b in v]

    def get_subgraph_until_page(self, page):
        subgraph = {}
        for c1, relations in self.graph.items():
            if self.characters_info[c1]['page'] > page:
                continue
            subgraph[c1] = [c2 for c2 in relations if self.characters_info[c2['to']]['page'] <= page]
        return subgraph
