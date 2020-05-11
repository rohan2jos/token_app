import logging

from dba.token_dba import Token_dba as token_dba

LOGGER = logging.getLogger(__name__)
# set the basic logging config for the python logging module
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s:%(message)s')

def get_all_users():
    """
    Call the dba method to get all users in the database
    """
    LOGGER.info('called the user service to get all users')
    token_dba_obj = token_dba()
    return token_dba_obj.get_all_users()
