import joblib
from flask import Flask, jsonify, request, abort
from flask_cors import CORS
from time import time
from graph_api.graph import RelationshipGraph


api = Flask(__name__)
CORS(api)


g_real = RelationshipGraph(mock=False)
g_mock = RelationshipGraph(mock=True)

@api.route('/healthcheck', methods=['GET'])
def health():
    return 'Graph-API'

@api.route('/graph', methods=['GET'])
def graph():
    try:
        page = request.args.get("page")
        mock = request.args.get("mock", 0)

        if bool(int(mock)):
            g = g_mock
        else:
            g = g_real

        if page:
            subgraph = g.get_subgraph_until_page(int(page))
            return jsonify({
                'graph': subgraph,
                'nodes': g.get_characters(subgraph),
                'edges': g.get_edges(subgraph),
                'max_page': 201,
                'first_page': 9,
                'book_name': 'One Hundred Years of Solitude',
            })
        graph = g.get_graph()
        return jsonify({
            'graph': graph,
            'nodes': g.get_characters(graph),
            'edges': g.get_edges(graph),
            'max_page': 201, # TODO: get from data
            'first_page': 9,
            'book_name': 'One Hundred Years of Solitude',
        })

    except Exception as e:
        return jsonify({
            'msg': f'Failed to get graph with Exception: {e}'
        }), 500


if __name__ == "__main__":
    api.run(host='0.0.0.0', port=8000, debug=True)
