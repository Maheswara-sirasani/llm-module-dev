import logging
import os
 
LOG_DIR = os.path.join(os.path.dirname(__file__), "logs")
LOG_FILE = os.path.join(LOG_DIR, "user_auth.log")
 
os.makedirs(LOG_DIR, exist_ok=True)
 
logger = logging.getLogger("user_auth_logger")
logger.setLevel(logging.INFO)
 
file_handler = logging.FileHandler(LOG_FILE)
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
 
if not logger.handlers:
    logger.addHandler(file_handler)
 