import logging

from dba.timeslot_dba import TimeslotDBA

LOGGER = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s:%(message)s')


def get_all_tokens():
    """
    Call the dba to fetch all the available timeslots in the db
    """
    timeslot_dba = TimeslotDBA()
    return timeslot_dba.get_all_timeslots()
