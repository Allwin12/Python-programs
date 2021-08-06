import logging
from datetime import datetime

logger = logging.getLogger()
logger.setLevel(logging.NOTSET)

file_handler = logging.FileHandler(f"{datetime.now().strftime('%d-%m-%Y')}.log")
file_format = '%(asctime)s | %(message)s | %(levelname)s'
file_handler.setFormatter(logging.Formatter(file_format))
logger.addHandler(file_handler)
logging.info("info")
logging.debug("debug")
