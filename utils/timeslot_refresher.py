import atexit
import logging

from apscheduler.schedulers.background import BackgroundScheduler

from utils import timeslot_engine

LOGGER = logging.getLogger(__name__)
# set the basic logging config for the python logging module
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s:%(message)s')

LOGGER.info("STARTING UTIL TO REFRESH TIMESLOTS")


def create_timeslots_at_interval():
    """
    function to recreate the timeslots at intervals
    """
    LOGGER.info("refreshing the timeslots")
    timeslot_engine.generate_time_slots_from_range('9:00', '18:00')
    LOGGER.info("done refreshing the timeslots...")


scheduler = BackgroundScheduler()
"""
run the scheduler from Monday to Friday at 12 am, resulting in a new set of timeslots
that are open and available
this will not run on weekends
NOTE: THIS WILL ERASE THE CURRENT MAPPING OF TOKEN TO TIMESLOT!!!
"""
scheduler.add_job(func=create_timeslots_at_interval, trigger="interval", day_of_week='mon-fri', hour='0')
scheduler.start()


# shut down the scheduler when exiting the app
LOGGER.info("Trying to gracefully shut down the scheduler")
try:
    atexit.register(lambda: scheduler.shutdown())
except Exception as scheduler_shutdown_excp:
    LOGGER.error("THERE WAS A PROBLEM WHEN SHUTTING DOWN THE SCHEDULER")
    LOGGER.error(scheduler_shutdown_excp)
    atexit.register(lambda: scheduler.shutdown())
