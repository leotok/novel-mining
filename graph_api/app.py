import joblib
from flask import Flask, jsonify, request, abort
from flask_cors import CORS
from time import time
from graph_api.graph import RelationshipGraph


api = Flask(__name__)
CORS(api)


g = RelationshipGraph()

@api.route('/healthcheck', methods=['GET'])
def health():
    return 'Graph-API'

@api.route('/graph', methods=['GET'])
def graph():
    try:
        page = request.args.get("page")
        if page:
            subgraph = g.get_subgraph_until_page(int(page))
            return jsonify({
                'graph': subgraph,
                'nodes': g.get_characters(subgraph),
                'edges': g.get_edges(subgraph),
            })
        return jsonify({
            'graph': g.get_graph(),
            'nodes': g.get_characters(g.graph),
            'edges': g.get_edges(g.graph),
        })

    except Exception as e:
        return jsonify({
            'msg': f'Failed to get graph with Exception: {e}'
        }), 500


if __name__ == "__main__":
    api.run(host='0.0.0.0', port=8000, debug=True)
