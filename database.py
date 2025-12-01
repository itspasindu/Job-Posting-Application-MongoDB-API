from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URL = "mongodb://127.0.0.1:27017"

client = AsyncIOMotorClient(MONGO_URL)

db = client["job-posting-application-API"]   # Database name
companies_collection = db["companies"]          # for company data
jobs_collection = db["job_postings"]            # for job postings
applicants_collection = db["applicants"]        # for applicants