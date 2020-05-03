import logging
from flask import Flask, request

APP = Flask(__name__)
LOGGER = logging.getLogger(__name__)

@APP.route('/', methods=['GET'])
def root_fun():
    """
    The root path
    Returns string
    """
    LOGGER.info('Called GET on /')
    return 'you are at the root, should not be here!'


if __name__ == "__main__":
    APP.debug = True
    APP.run(host='0.0.0.0', port=5002)