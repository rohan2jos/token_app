import datetime
import logging
import sys
import pytz

from dba.timeslot_dba import TimeslotDBA

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
    timeslot_dba = TimeslotDBA()

    # check if the timeslots db is present.  If not, we need to create a new one and set index
    does_db_exist = timeslot_dba.does_timeslot_db_exist()
    date_today = generate_utc_date()

    if not does_db_exist:
        LOGGER.info('[SETUP] timeslot collection does not exist, creating')
        collection_create_response = timeslot_dba.create_collection()
        LOGGER.info('[SETUP] Creating index on newly created db')
        _ = timeslot_dba.create_timeslot_index('timeslot_index')
        if not collection_create_response:
            sys.exit()

    # check if there is a doc with todays date, if it exists, we don't need to create an index
    LOGGER.info('[SETUP] Checking if there is a doc with todays date')
    does_today_doc_exist = timeslot_dba.check_today_doc_exist(date_today)
    if not does_today_doc_exist:
        generated_timeslots = generate_time_slots_from_range('9:00', '18:00')
        insert_response = timeslot_dba.insert_generated_timeslots(generated_timeslots,
                                                                  date_today)
        if not insert_response:
            LOGGER.error('There was a problem generating and inserting the timeslots')
            sys.exit()

    LOGGER.info("[SETUP] The timeslots were setup")


def generate_time_slots_from_range(start, end):
    """
    :param start:       The start of the time range from which the time slots need
                        to be broken out
    :param end:         The end of the time range to which the time slots need to
                        be broken out
    """
    LOGGER.info('[SETUP] Calculating and populating the time slots')
    LOGGER.info('[SETUP] calculating the timeslots between ' + start + " and " + end)

    slot_time = 15
    hours = []
    time = datetime.datetime.strptime(start, '%H:%M')
    end = datetime.datetime.strptime(end, '%H:%M')

    while time <= end:
        hours.append(time.strftime("%H:%M"))
        time += datetime.timedelta(minutes=slot_time)
    LOGGER.info("[SETUP] printing the timeslots that have been generated for today")
    LOGGER.info(hours)
    return hours


def generate_utc_date():
    """
    Generate the date now from UTC
    """
    date_today = datetime.datetime.now(pytz.utc).strftime("%m%d%Y")
    return date_today


def get_local_time_date_now():
    """
    Generate the UTC time and convert to IST
    Return a dict containing the converted date and time in the required format
    """
    local_tz = pytz.timezone('Asia/Calcutta')
    time_date_utc = datetime.datetime.now(pytz.utc)
    converted_date_time = time_date_utc.replace(tzinfo=pytz.utc).astimezone(local_tz)
    hours_mins = converted_date_time.strftime("%H:%M")
    mmddyy = converted_date_time.strftime("%m%d%Y")
    return {
        "converted_time": hours_mins,
        "converted_date": mmddyy
    }
