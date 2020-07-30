class RelationshipGraph:

    def __init__(self):
        self.character_to_page = {
            'Ursula': 1,
            'Jose Arcadio Buendia': 2,
            'Jose Arcadio': 10,
            'Aureliano': 35,
            'Rebeca': 70
        }
        self.graph = {
            'Ursula': [{'to': 'Jose Arcadio Buendia', 'label': 'esposa'}, {'to': 'Jose Arcadio', 'label': 'mae'}, {'to': 'Aureliano', 'label': 'mae'}, {'to': 'Rebeca', 'label': 'mae'}],
            'Jose Arcadio Buendia': [{ 'to': 'Ursula', 'label': 'marido'}, { 'to': 'Jose Arcadio', 'label': 'pai'}, { 'to': 'Aureliano', 'label': 'pai'}, { 'to': 'Rebeca', 'label': 'pai'}],
            'Jose Arcadio': [{ 'to': 'Ursula', 'label': 'filho'}, { 'to': 'Jose Arcadio Buendia', 'label': 'filho'}, { 'to': 'Aureliano', 'label': 'irmao'}, { 'to': 'Rebeca', 'label': 'irmao'}],
            'Aureliano': [{ 'to': 'Ursula', 'label': 'filho'}, { 'to': 'Jose Arcadio Buendia', 'label': 'filho'}, { 'to': 'Jose Arcadio', 'label': 'irmao'}, { 'to': 'Rebeca', 'label': 'irmao'}],
            'Rebeca': [{ 'to': 'Ursula', 'label': 'filha'}, { 'to': 'Jose Arcadio Buendia', 'label': 'filha'}, { 'to': 'Aureliano', 'label': 'irma'}, { 'to': 'Jose Arcadio', 'label': 'irma'}],
        }

    def get_characters(self, graph):
        return list(graph.keys())

    def get_edges(self, graph):
        return [{'from': a, 'to': b['to']} for a, v in graph.items() for b in v]

    def get_subgraph_until_page(self, page):
        subgraph = {}
        for c1, relations in self.graph.items():
            if self.character_to_page[c1] > page:
                continue
            subgraph[c1] = [c2 for c2 in relations if self.character_to_page[c2['to']] <= page]
        return subgraph
