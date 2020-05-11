import json
import logging

from flask import Flask, jsonify, request
from flask_restplus import Namespace, Resource, fields

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
        The time needs to be passed as a query parameter to the endpoint
        """
        requested_time = request.args.get('requested_time')
        requested_date = request.args.get('requested_date')
        if not requested_time or requested_date:
            return api_utils.generate_response('Query params required', 400)
        return {'Yet to be implemented'}, 200
