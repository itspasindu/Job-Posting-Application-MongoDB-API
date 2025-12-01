from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URL = "mongodb://127.0.0.1:27017"

client = AsyncIOMotorClient(MONGO_URL)

db = client["job-posting-API"]   # Database name
collection = db["company"]    # Collection name
collection = db["job-posting"] 
collection = db["applicants"] 