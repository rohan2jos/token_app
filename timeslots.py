import json
import logging

from flask import Flask, jsonify, request, render_template
from flask_restplus import Namespace, Resource, fields
import utils.timeslot_engine as timeslot_engine

import service.timeslot_service as timeslot_service
import utils.api_utils as api_utils

LOGGER = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s:%(message)s')

app = Flask(__name__)
timeslot_ns = Namespace("Timeslots", description="The timeslot apis")


@timeslot_ns.route("timeslots")
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


@timeslot_ns.route('available_timeslots')
class AvailableTimeSlots(Resource):
    """class to get the available timeslots based on the time"""

    def get(self):
        """
        Return all the available time slots based on the time
        """
        time_and_date_local = timeslot_engine.get_local_time_date_now()
        response, status = timeslot_service.get_available_timeslots(time_and_date_local)
        test = []
        for a_doc in response:
            test.append(a_doc.get('timeslot'))
        # return response, status
        if response:
            LOGGER.info("====================================")
            LOGGER.info(test)
            LOGGER.info("Found the timeslots, rendering template")
            return render_template('home.html', timeslots=test, test_string='test')

