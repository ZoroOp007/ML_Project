"""
Logger is used in python to track the event that occur during the execution of a program.
Logging is important for software developing, debugging, and running.

Here we have developed a custom logger which report the occurence of any event with the timestamp and the module name where it happened along with the full description.

Types of logging level in python

1.DEBUG
2.INFO
3.WARNING
4.ERROR
5.CRITICAL

"""

import os 
import sys 
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s %(message)s]"

log_dir = "logs"
log_filepath = os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir, exist_ok = True)

logging.basicConfig(
    level = logging.INFO,
    format = logging_str,

    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("mlProjectLogger")