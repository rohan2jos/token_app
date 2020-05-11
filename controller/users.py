import json
import logging

from flask import Flask, jsonify, request
from flask_restplus import Namespace, Resource, fields
import service.user_service as user_service
from utils import token_controller_utils
import utils.api_utils as api_utils

LOGGER = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s:%(message)s')

app = Flask(__name__)
users_ns = Namespace('Users', description='All users apis')

USER_PAYLOAD = users_ns.model("token body payload model", {
    "name": fields.String(required=True,
                          description="The name of the user trying to generate a token"),
    "phone": fields.String(required=True,
                           description="The phone number of the user trying to generate a token"),
    "email": fields.String(required=True,
                           description="The email id of the user trying to generate a token")
})

USER_LIST_SUCCESS = users_ns.model("get user list success response", {
    "users": fields.List(fields.Nested(USER_PAYLOAD))
})

@users_ns.route('users', methods=['GET'])
@users_ns.response(200, 'success', USER_LIST_SUCCESS)
class Users(Resource):

    def get(self):
        """
        GET list of users in the database
        Name: Get list of users
        Version: 1.0
        This API endpoint returns a list of users that are present in the database
        """
        LOGGER.info('trying to retrieve all users')
        result, status = user_service.get_all_users()
        return result, status