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
                return token_list, 200
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
