from pymongo import MongoClient
from bson import ObjectId
import os
from dotenv import load_dotenv
 
load_dotenv()
client = MongoClient(os.getenv("MONGO_URL"))
db = client["resume_scanner"]
user_collection = db["users"]
 