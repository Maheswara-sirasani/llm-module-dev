from motor import AsynciOMotorClient
from config import settings

client=AsynciOMotorClient
db=client[settings.mongo_db]