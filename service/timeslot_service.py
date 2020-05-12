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


def get_available_timeslots(local_time_date):
    """
    :param local_time_date:     The date time object converted from UTC to the local
                                time zone
    call the dba method to fetch the available timeslots after the current date and
    time
    """
    timeslot_dba = TimeslotDBA()
    return timeslot_dba.get_availale_timeslots(local_time_date)