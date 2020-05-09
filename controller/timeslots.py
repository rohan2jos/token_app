import json
import logging

from flask import Flask, jsonify, request
from flask_restplus import Namespace, Resource, fields

import service.timeslot_service as timeslot_service

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
        return timeslot_service.get_all_tokens()
