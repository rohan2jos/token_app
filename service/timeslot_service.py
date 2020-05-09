import logging

from dba.timeslot_dba import TimeslotDBA

LOGGER = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s:%(message)s')


def get_all_timeslots():
    """
    Call the dba to fetch all the available timeslots in the db
    """
    timeslot_dba = TimeslotDBA()
    LOGGER.info("the timeslot service is calling the dba")
    return timeslot_dba.get_all_timeslots()
