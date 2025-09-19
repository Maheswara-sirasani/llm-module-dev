from pymongo import MongoClient
from sqlalchemy import create_engine
import os
 
# MongoDB
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
mongo_client = MongoClient(MONGO_URI)
mongo_db = mongo_client["user_management"]
users_collection = mongo_db["users"]
password_resets = mongo_db["password_resets"]
 
# Optional MySQL (skip if not needed)
MYSQL_URI = os.getenv("MYSQL_URI", "mysql+pymysql://root:password@localhost/userdb")
try:
    mysql_engine = create_engine(MYSQL_URI)
except Exception as e:
    print("MySQL connection skipped:", e)
 