import os
import logging

from pymongo import MongoClient, ASCENDING, DESCENDING
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

    def insert_generated_timeslots(self, timeslots, date_now):
        """
        :param timeslots:       list of generated timeslots that have to be entered into
                                the database
        :param date_now:        The date now in UTC
        Creates correct documents from the timeslots list and enters them into the database
        """
        LOGGER.info("[SETUP] Populating the timeslots")
        LOGGER.info("[SETUP] the date today is: " + str(date_now))
        try:
            timeslot_docs = []
            for a_timeslot in timeslots:
                timeslot_docs.append(timeslot_dba_utils.generate_timeslot_doc(a_timeslot))

            doc_to_insert = {
                "date": date_now,
                "timeslots": timeslot_docs
            }

            insertion_result = self.db[TIMESLOT_COLLECTION_NAME].insert_one(doc_to_insert)
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

    def create_timeslot_index(self, index_name):
        """
        :param index_name:      The name of the index that has to be created
        :return:                The name of the index that has been created
        Create an index on the timeslot collection
        """
        LOGGER.info('[SETUP] Creating index on timeslot collection')
        try:
            _ = self.db[TIMESLOT_COLLECTION_NAME].create_index("date",
                                                               name=index_name,
                                                               unique=True)
            LOGGER.info('Created collection name ' + index_name)
            return True
        except (PyMongoError, ValueError) as index_exception:
            LOGGER.error('There was an exception when creating index on the timeslot collection')
            LOGGER.error(index_exception)
            return False

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

    def check_today_doc_exist(self, date_today):
        """
        :param date_today:      The date today in string format
        :return:                True: if there is a document matching todays date
                                False: if there is no document matching todays date
        """
        try:
            query_filter = {"date": date_today}
            doc_present = False
            doc_with_today_date = self.db.timeslots.find_one(query_filter)

            if doc_with_today_date:
                LOGGER.info('[SETUP] There is a doc with todays date')
                return True
            return False
        except (PyMongoError, ValueError) as get_today_doc_excp:
            LOGGER.error("there was a problem checking todays doc")
            LOGGER.error(get_today_doc_excp)
            return True

    def get_availale_timeslots(self, local_date_time):
        """
        :param local_date_time: The datetime object that has been converted from IST to
                                the local time zone
        Fetch the available timeslots for the requested date after the requested time
        """
        try:
            # TODO: write query to fetch the timeslots after the requsted time and on the requested date
            """
            db.getCollection('timeslots').aggregate( [
{$unwind: '$timeslots'},
{$match: { $and: [{'date': '05112020'}, {'timeslots.timeslot': { $gt: '11:00' } }] } }
] )
            """
            pass
        except (PyMongoError, ValueError) as retrieval_excp:
            LOGGER.error("There was an exception while fetching the available timeslots")
            LOGGER.error(retrieval_excp)
            return False, 400
