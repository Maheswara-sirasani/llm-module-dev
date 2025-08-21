import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
 
# MongoDB connection
client = AsyncIOMotorClient("mongodb://localhost:27017")
db = client["vehicle_rental"]   # database name
users_collection = db["users"]  # collection name
 
async def test_mongo():
    # Insert a sample user
    result = await users_collection.insert_one({"name": "Mahesh", "email": "mahesh@example.com"})
    print("Inserted ID:", result.inserted_id)
 
    # Find the inserted user
    user = await users_collection.find_one({"_id": result.inserted_id})
    print("Fetched User:", user)
 
# Run the test
if __name__ == "__main__":
    asyncio.run(test_mongo())
 