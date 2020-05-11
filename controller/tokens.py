import json
import logging

from flask import Flask, jsonify, request
from flask_restplus import Namespace, Resource, fields
import service.token_service as token_service
from utils import token_controller_utils
import utils.api_utils as api_utils

LOGGER = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s:%(message)s')


app = Flask(__name__)
tokens_ns = Namespace('Tokens', description='All the tokens apis')

"""
Section to define the models of the payloads expected by the api endpoints.  These models
are only verified by the swagger, and the swagger will raise a failed validation exception
when the api endpoint is called through it with the wrong payload
"""
TOKEN_PAYLOAD = tokens_ns.model("token body payload model", {
    "name": fields.String(required=True,
                          description="The name of the user trying to generate a token"),
    "phone": fields.String(required=True,
                           description="The phone number of the user trying to generate a token"),
    "email": fields.String(required=True,
                           description="The email id of the user trying to generate a token")
})

TOKEN_LIST_SUCCESS = tokens_ns.model("get token list success response", {
    "tokens": fields.List(fields.Nested(TOKEN_PAYLOAD))
})

TOKEN_POST_400 = tokens_ns.model("validation failed", {
    "message": fields.String(example="Payload required/Payload validation failed"),
    "status": fields.String(example="400")
})


@tokens_ns.route('tokens', methods=['GET'])
@tokens_ns.response(200, 'success', TOKEN_LIST_SUCCESS)
class Tokens(Resource):

    def get(self):
        """
        GET list of tokens in the database
        Name: Get list of tokens
        Version: 1.0
        This API endpoint returns a list of tokens that are present in the database
        """
        LOGGER.info('trying to retrieve all tokens')
        result, status = token_service.get_all_tokens()
        return result, status


@tokens_ns.route('token')
@tokens_ns.response(200, 'success', TOKEN_PAYLOAD)
@tokens_ns.response(400, 'bad request', TOKEN_POST_400)
@tokens_ns.expect(TOKEN_PAYLOAD, validate=True)
class CreateGetToken(Resource):

    def post(self):
        '''
        POST a token in the database
        Name: POST a token
        Version: 1.0
        This API endpoint creates a new token in the database
        '''
        data = request.get_json()
        if not data:
            response = api_utils.generate_response('Payload required', 400)
            return response, 400
        is_data_payload_valid = token_controller_utils.check_data_payload_validity(data)

        if not is_data_payload_valid:
            response = api_utils.generate_response('payload validation failed', 400)
            return response, 400

        LOGGER.info('Creating token for %s', data.get('name'))
        response, status = token_service.create_token(data)
        if response:
            LOGGER.info('token created successfully!')
            return data, 200
        return None, 400


@tokens_ns.expect(TOKEN_PAYLOAD, validate=True)
@tokens_ns.route('generate_token')
class GenerateToken(Resource):

    def post(self):
        """
        POST a token, and associate an available timeslot
        Name: Create a token with timeslot
        Version: 1.0
        This API creates a token and associates a timeslot to it if available
        """
        data = request.get_json()
        if not data:
            response = api_utils.generate_response('Payload required', 400)
            return response, 400
        is_data_payload_valid = token_controller_utils.check_data_payload_validity(data)

        if not is_data_payload_valid:
            response = api_utils.generate_response('payload validation failed', 400)
            return response, 400
        generation_response, status = token_service.generate_token(data)
        return generation_response, status
