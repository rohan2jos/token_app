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


def get_available_timeslots(requested_time, requested_date):
    """
    :param requested_time:      The time after which the timeslots are available
    :param requested_date:      The date for which the timeslots that are available
                                are requested
    call the dba method to fetch the available timeslots for the requested date and
    after the requested time
    """
    