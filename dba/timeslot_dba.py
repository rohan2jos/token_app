import os
import logging

from pymongo import MongoClient
from pymongo.errors import PyMongoError
from utils.constants import TOKENS_COLLECTION_NAME
from timeslot_utils import timeslot_engine

MONGO_URL = os.environ.get('MONGO_URL')
if not MONGO_URL:
    MONGO_URL = "mongodb://localhost:27017"

LOGGER = logging.getLogger(__name__)
# set the basic logging config for the python logging module
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s:%(message)s')

class TimeslotDBA:
    """class for timeslot dba operations"""

    def __init__(self):
        """
        Constructor for setup
        """
        self.client = MongoClient(MONGO_URL)
        self.db = self.client.tokenapp


    def get_all_timeslots(self):
        """
        Return all the available timeslots in the database
        """
        LOGGER.info("calling the populate timeslots")
        timeslot_engine.populate_time_slots('9', '18')
        return 200
