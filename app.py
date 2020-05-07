import logging
import os

from flask import Flask
from flask_restplus import Api
from flask_sslify import SSLify
from werkzeug.middleware.proxy_fix import ProxyFix

from controller.tokens import tokens_ns

APP = Flask(__name__)

APP.wsgi_app = ProxyFix(APP.wsgi_app, x_proto=1, x_host=1)

API = Api(APP, version='1.0', title='Token apis', description='All the token apis')
API.add_namespace(tokens_ns, '/')

LOGGER = logging.getLogger(__name__)
# set the basic logging config for the python logging module
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s:%(message)s')

# TODO: Change for production
if __name__ == "__main__":
    # get the port from the environment variable
    # if running on localhost, use the localhost
    # port
    LOGGER.info('<--Firing up the engines-->')
    port = int(os.environ.get("PORT", 5002))
    APP.run(host='0.0.0.0', port=port, ssl_context='adhoc')
