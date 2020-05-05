import logging

from dba.token_dba import Token_dba as token_dba


LOGGER = logging.getLogger(__name__)
# set the basic logging config for the python logging module
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s:%(message)s')


def get_all_tokens():
    """
    Call the dba method to get all tokens in the database
    """
    LOGGER.info('called the token service to get all tokens')
    token_dba_obj = token_dba()
    return token_dba_obj.get_all_tokens()


def create_token(data):
    """
    :param data:        The data payload for the token that has to be created
    :return:            The created token and the status code for the creation
                        in the db
    Call the dba to create a token with the given data payload
    """
    token_dba_obj = token_dba()
    return token_dba_obj.create_token(data)
