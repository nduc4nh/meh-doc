import logging
from datetime import datetime

def log(mess, logtype = "INFO"):
    if logtype == "INFO":
        logging.info("[{}] {}".format(datetime.now(), mess))