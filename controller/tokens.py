import logging

from flask import Flask,jsonify
from flask_restplus import Namespace, Resource

LOGGER = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s:%(message)s')


app = Flask(__name__)
tokens_ns = Namespace('Tokens', description='All the tokens apis')


@tokens_ns.route('tokens', methods=['GET'])
class Tokens(Resource):

    def get(self):
        token = [
            {'token_id': '1', 'name': 'ramesh', 'time': '11:00'},
            {'token_id': '2', 'name': 'suresh', 'time': '11:15'},
            {'token_id': '3', 'name': 'mahesh', 'time': '11:30'},
            {'token_id': '4', 'name': 'maheskhota', 'time': '11:35'}
        ]

        return jsonify(token)
