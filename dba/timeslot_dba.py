import os
import logging

from pymongo import MongoClient
from pymongo.errors import PyMongoError
from utils.constants import TIMESLOT_COLLECTION_NAME
import utils.timeslot_dba_utils as timeslot_dba_utils

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
        return 200

    def insert_generated_timeslots(self, timeslots):
        """
        :param timeslots:       list of generated timeslots that have to be entered into
                                the database
        Creates correct documents from the timeslots list and enters them into the database
        """
        LOGGER.info("[SETUP] Populating the timeslots")
        try:
            for a_timeslsot in timeslots:
                insertion_result = self.db[TIMESLOT_COLLECTION_NAME].insert_one(
                    timeslot_dba_utils.generate_timeslot_doc(a_timeslsot))
            if insertion_result:
                return True
            return False
        except (PyMongoError, ValueError) as setup_timeslot_excp:
            LOGGER.error('There was an exception when inserting timeslots')
            LOGGER.error(setup_timeslot_excp)
            return False

    def does_timeslot_db_exist(self):
        """
        Check if the collection is in the timeslot db
        :return:                True: The collection exists, the db has been created previously
                                False: The collection does not exist, this is a new db
        """
        collections = self.db.list_collection_names()
        if TIMESLOT_COLLECTION_NAME in collections:
            return True
        return False

    def create_timeslot_index(self):
        """
        Create an index on the timeslot collection
        """
        LOGGER.info('[SETUP] Creating collection on timeslot db')
        return True

    def create_collection(self):
        """
        Create the timeslot collection
        """
        try:
            created_collection = self.db[TIMESLOT_COLLECTION_NAME]
            if created_collection:
                return True
            return False
        except (PyMongoError, ValueError) as creation_excp:
            LOGGER.error("There was an exception when creating the timeslot collection")
            LOGGER.error(creation_excp)
            return False
