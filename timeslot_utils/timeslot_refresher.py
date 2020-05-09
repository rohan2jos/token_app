import time
import atexit
import logging

from apscheduler.schedulers.background import BackgroundScheduler

from timeslot_utils import timeslot_engine

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
scheduler.add_job(func=create_timeslots_at_interval, trigger="interval", seconds=5)
scheduler.start()


# shut down the scheduler when exiting the app
LOGGER.info("Trying to gracefully shut down the scheduler")
try:
    atexit.register(lambda: scheduler.shutdown())
except Exception as scheduler_shutdown_excp:
    LOGGER.error("THERE WAS A PROBLEM WHEN SHUTTING DOWN THE SCHEDULER")
    LOGGER.error(scheduler_shutdown_excp)
    atexit.register(lambda: scheduler.shutdown())
