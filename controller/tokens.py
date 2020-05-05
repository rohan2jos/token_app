import json
import logging

from flask import Flask, jsonify, request
from flask_restplus import Namespace, Resource
import service.token_service as token_service

LOGGER = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s:%(message)s')


app = Flask(__name__)
tokens_ns = Namespace('Tokens', description='All the tokens apis')


@tokens_ns.route('tokens', methods=['GET'])
class Tokens(Resource):

    def get(self):
        # token = [
        #     {'token_id': '1', 'name': 'ramesh', 'time': '11:00'},
        #     {'token_id': '2', 'name': 'suresh', 'time': '11:15'},
        #     {'token_id': '3', 'name': 'mahesh', 'time': '11:30'},
        #     {'token_id': '4', 'name': 'maheskhota', 'time': '11:35'}
        # ]

        # return jsonify(token)
        LOGGER.info('trying to retrieve all tokens')
        result, status = token_service.get_all_tokens()
        return result, status


@tokens_ns.route('token')
class CreateGetToken(Resource):

    def post(self):
        '''
        :data-payload:      The data payload of the token that has to
                            be created in the database
                            #TODO: Body validation
        :return:            200: The created token and the status
                            400: Bad body - Validation failed
        '''
        data = request.get_json()
        LOGGER.info('Creating token for %s', data.get('name'))
        response, status = token_service.create_token(data)
        if response:
            LOGGER.info('token created successfully!')
            return data, 200
        return None, 400
