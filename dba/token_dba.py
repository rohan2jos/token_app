import logging

from pymongo import MongoClient
from pymongo.errors import PyMongoError

DB_NAME = 'tokenapp'
COLLECTION_NAME = 'tokens'

LOGGER = logging.getLogger(__name__)
# set the basic logging config for the python logging module
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s:%(message)s')


class Token_dba:
    """ class for token database operations """

    def __init__(self):
        """
        Constructor for setup
        """
        self.client = MongoClient('localhost', 27017)

    def get_all_tokens(self):
        """
        :return:        Return all the tokens in the databse
        """
        LOGGER.info('calling db to fetch all tokens')
        try:
            current_collection = self.client.DB_NAME.COLLECTION_NAME
            all_tokens = current_collection.find()

            token_list = []
            if all_tokens:
                for one_token in all_tokens:
                    token_list.append(one_token)
                return token_list, 200
            return False, 404

        except (PyMongoError, ValueError) as retrieval_excp:
            LOGGER.exception('There was a problem during token retrieval: %s', retrieval_excp)
