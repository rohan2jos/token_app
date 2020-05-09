import logging
import os

from flask import Flask
from flask_restplus import Api
from flask_sslify import SSLify
from werkzeug.middleware.proxy_fix import ProxyFix

from controller.tokens import tokens_ns
from controller.timeslots import timeslot_ns
from timeslot_utils import timeslot_engine
# from timeslot_utils import timeslot_refresher

APP = Flask(__name__)

# this is for heroku deployments where the https has to be enforced
APP.wsgi_app = ProxyFix(APP.wsgi_app, x_proto=1, x_host=1)

API = Api(APP, version='1.0', title='Token apis', description='All the token apis')
API.add_namespace(tokens_ns, '/token_api/')
API.add_namespace(timeslot_ns, '/timeslot_api/')

LOGGER = logging.getLogger(__name__)
# set the basic logging config for the python logging module
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s:%(message)s')

# setup when the deployment is coming up
timeslot_engine.setup_timeslot_db()

# refresh the timeslots at set interval
# commented for now
# timeslot_refresher.create_timeslots_at_interval()
# TODO: Change for production
if __name__ == "__main__":
    # get the port from the environment variable
    # if running on localhost, use the localhost
    # port
    LOGGER.info('<--Firing up the engines-->')
    port = int(os.environ.get("PORT", 5002))
    APP.run(host='0.0.0.0', port=port, ssl_context='adhoc')
