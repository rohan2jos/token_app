import os
import logging

from flask import Flask
from flask_restplus import Api

from controller.tokens import tokens_ns

APP = Flask(__name__)
API = Api(APP, version='1.0', title='Token apis', description='All the token apis')
API.add_namespace(tokens_ns, '/')

LOGGER = logging.getLogger(__name__)
# set the basic logging config for the python logging module
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s:%(message)s')

@APP.route('/', methods=['GET'])
def root_fun():
    """
    The root path
    Returns string

    #TODO:          This path has to be blocked on the gateway; Add redirect
    """
    LOGGER.info('Called GET on /')
    return 'you are at the root, should not be here!'


# TODO: Change for production
if __name__ == "__main__":
    APP.debug = True
    # get the port from the environment variable
    # if running on localhost, use the localhost
    # port
    port = int(os.environ.get("PORT", 5002))
    APP.run(host='0.0.0.0', port=port)
