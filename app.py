import logging
from flask import Flask, request

APP = Flask(__name__)
LOGGER = logging.getLogger(__name__)

# set the basic logging config for the python logging module
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s:%(message)s')

@APP.route('/', methods=['GET'])
def root_fun():
    """
    The root path
    Returns string
    """
    LOGGER.info('Called GET on /')
    return 'you are at the root, should not be here!'


@APP.route('/tokens', methods=['GET'])
def getTokens():
    """
    Return all the current tokens
    """
    LOGGER.info('called the GET on tokens')
    return 'Under Construction'


# run the app on 5002 for localhost
# TODO: Change for production
if __name__ == "__main__":
    APP.debug = True
    APP.run(host='0.0.0.0', port=5002)
