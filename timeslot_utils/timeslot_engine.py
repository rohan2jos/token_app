import datetime
import logging

LOGGER = logging.getLogger(__name__)
# set the basic logging config for the python logging module
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s:%(message)s')


# TODO: Add the time logging decorator
def setup_timeslot_db():
    """
    Method to setup the timeslot db
    If the db exists, and there is a redeploy, check the datetime
    of the timeslot and if not the same day, refresh the database
    and create a new one
    If the db exists and there is a redeploy on the same day with
    valid timeslots still in the database, keep it
    """
    LOGGER.info('=== setting up the timeslot database ===')
    populate_time_slots('9:00', '18:00')
    LOGGER.info('YET TO BE IMPLEMENTED')
    pass


def populate_time_slots(start, end):
    """
    :param start:       The start of the time range from which the time slots need
                        to be broken out
    :param end:         The end of the time range to which the time slots need to
                        be broken out
    """
    LOGGER.info('Calculating and populating the time slots')

    slot_time = 15
    hours = []
    time = datetime.datetime.strptime(start, '%H:%M')
    end = datetime.datetime.strptime(end, '%H:%M')

    while time <= end:
        hours.append(time.strftime("%H:%M"))
        time += datetime.timedelta(minutes=slot_time)
    LOGGER.info("printing the timeslots that have been generated for today")
    LOGGER.info(hours)
