import os
import logging

from pymongo import MongoClient
from pymongo.errors import PyMongoError
from utils.constants import TOKENS_COLLECTION_NAME

DB_NAME = 'tokenapp'
COLLECTION_NAME = 'tokens'

MONGO_URL = os.environ.get('MONGO_URL')
if not MONGO_URL:
    MONGO_URL = "mongodb://localhost:27017"

LOGGER = logging.getLogger(__name__)
# set the basic logging config for the python logging module
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s:%(message)s')


class Token_dba:
    """ class for token database operations """

    def __init__(self):
        """
        Constructor for setup
        """
        self.client = MongoClient(MONGO_URL)
        self.db = self.client.tokenapp

    def get_all_users(self):
        """
        :return:            Return all the users in the databse
        """
        LOGGER.info('calling db to fetch all users')
        try:
            all_users = self.db[TOKENS_COLLECTION_NAME].find()

            user_list = []
            if all_users:
                for one_user in all_users:
                    one_user = {key: one_user[key] for key in one_user.keys() & {'name', 'phone', 'email'}}
                    user_list.append(one_user)
                return {"users": user_list}, 200
            return False, 404

        except (PyMongoError, ValueError) as retrieval_excp:
            LOGGER.exception('There was a problem during user retrieval: %s', retrieval_excp)

    def get_all_tokens(self):
        """
        :return:            Return all the tokens in the databse
        """
        LOGGER.info('calling db to fetch all tokens')
        try:
            all_tokens = self.db[TOKENS_COLLECTION_NAME].find()

            token_list = []
            if all_tokens:
                for one_token in all_tokens:
                    del one_token['_id']
                    token_list.append(one_token)
                return {"tokens": token_list}, 200
            return False, 404

        except (PyMongoError, ValueError) as retrieval_excp:
            LOGGER.exception('There was a problem during token retrieval: %s', retrieval_excp)


    def create_token(self, data):
        """
        :param data:        The data payload of the token that has to be inserted into the
                            database
        :return:            200: The created token and the status code
        """
        LOGGER.info('Called the dba to create token with name %s', data.get('name'))
        try:
            result = self.db[TOKENS_COLLECTION_NAME].insert_one(data)

            if result:
                del data['_id']
                return data, 200
            return None, False
        except (PyMongoError, ValueError) as insertion_excp:
            LOGGER.exception('There was an issue when inserting into the datbase %s', insertion_excp)


    def generate_token(self, data):
        """
        :param data:        The data payload of the token that has to be assigned a time
        :return:            The token with the timeslot assigned
                            200: If there is an available timeslot and the token was able
                            to be assigned one
                            404: If there is no available time slot
        """
        return {"message": "Yet to be implemented"}, 200