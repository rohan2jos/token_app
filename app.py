import logging
import os

from flask import Flask, render_template
from flask_restplus import Api, Resource
from werkzeug.middleware.proxy_fix import ProxyFix
from flask_bootstrap import Bootstrap

from controller.users import users_ns
from controller.tokens import tokens_ns
from timeslots import timeslot_ns
from utils import timeslot_engine

import service.timeslot_service as timeslot_service

# from timeslot_utils import timeslot_refresher

APP = Flask(__name__)
bootstrap = Bootstrap(APP)
# this is for heroku deployments where the https has to be enforced
APP.wsgi_app = ProxyFix(APP.wsgi_app, x_proto=1, x_host=1)

API = Api(APP, version='1.0', title='Token apis', description='All the token apis')
API.add_namespace(users_ns, '/user_api/')
API.add_namespace(tokens_ns, '/token_api/')
# API.add_namespace(timeslot_ns, '/timeslot_api/')

LOGGER = logging.getLogger(__name__)
# set the basic logging config for the python logging module
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s:%(message)s')

# setup when the deployment is coming up
timeslot_engine.setup_timeslot_db()

@APP.route('/home')
def home():
    LOGGER.info('hit the home')
    test_string = "rohan"
    l = [1,22]
    return render_template('home.html', test_string=test_string, l=l)

@APP.route("/timeslots")
class GetTimeSlots(Resource):
    """class to get all the available timeslots"""
    def get(self):
        """
        Return all the timeslots in the databse
        Tell the user to call the timeslots in the database
        #TODO: Add a filter to fetch only the available timeslots
        """
        LOGGER.info("Calling GET on the /timeslots")
        return timeslot_service.get_all_timeslots()


@APP.route('/available_timeslots')
def get():
    """
    Return all the available time slots based on the time
    """
    time_and_date_local = timeslot_engine.get_local_time_date_now()
    response, status = timeslot_service.get_available_timeslots(time_and_date_local)
    timeslots = []
    for a_doc in response:
        timeslots.append(a_doc.get('timeslot'))
    if a_doc:
        return render_template('available_timeslots.html', test_string='test', timeslots=timeslots)
    return render_template('error.html')


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
    APP.run(host='0.0.0.0', port=port, ssl_context='adhoc', debug=True)
