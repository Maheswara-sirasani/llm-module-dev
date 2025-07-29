import logging
import os
 
LOG_FILE = os.path.join("logs", "user_auth.log")
os.makedirs("logs", exist_ok=True)
 
logger = logging.getLogger("user_logger")
logger.setLevel(logging.INFO)
 
file_handler = logging.FileHandler(LOG_FILE)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
 
if not logger.hasHandlers():
    logger.addHandler(file_handler)
 