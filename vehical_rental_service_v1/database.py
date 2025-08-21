import motor.motor_asyncio
import os
from dotenv import load_dotenv

load_dotenv()

mongo_url=os.getenv("mongo_url")
db_name=os.getenv("db_name")

client=motor.motor_asyncio.AsyncIOMotorClient(mongo_url)
db=client[db_name]