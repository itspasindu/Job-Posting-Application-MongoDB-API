from fastapi import FastAPI, HTTPException
from bson import ObjectId
from database import companies_collection, jobs_collection, applicants_collection
from models import company, companyDB, jobPosting, jobPostingDB, applicants, applicantsDB

app = FastAPI(title="Job Posting Application API With MongoDB")

# Create Company
@app.post("/company", response_model=companyDB)
async def create_company(Company: company):
    company_dict = Company.dict()
    result = await companies_collection.insert_one(company_dict)
    company_dict["_id"] = str(result.inserted_id)
    return company_dict

# Create jobPosting
@app.post("/jobs", response_model=jobPostingDB)
async def create_jobs(jobs: jobPosting):
    jobs_dict = jobs.dict()
    result = await jobs_collection.insert_one(jobs_dict)
    jobs_dict["_id"] = str(result.inserted_id)
    return jobs_dict

# Create applicants
@app.post("/applicants", response_model=applicantsDB)
async def create_applicants(candidates: applicants):
    candidates_dict = candidates.dict()
    result = await applicants_collection.insert_one(candidates_dict)
    candidates_dict["_id"] = str(result.inserted_id)
    return candidates_dict

# Read all companies
@app.get("/company", response_model=list[companyDB])
async def get_company():
    companies = []
    async for company in companies_collection.find():
        company["_id"] = str(company["_id"])
        companies.append(company)
    return companies

# Read all job postings
@app.get("/jobs", response_model=list[jobPostingDB])
async def get_jobs():
    jobs = []
    async for job in jobs_collection.find():
        job["_id"] = str(job["_id"])
        jobs.append(job)
    return jobs

# Read all applicants
@app.get("/applicants", response_model=list[applicantsDB])
async def get_applicant():
    applicants = []
    async for applicant in applicants_collection.find():
        applicant["_id"] = str(applicant["_id"])
        applicants.append(applicant)
    return applicants

# read company by id
@app.get("/company/{company_id}}", response_model=companyDB)
async def get_company(company_id: str):
    company = await companies_collection.find_one({"_id": ObjectId(company_id)})
    if not company:
        raise HTTPException(404, "User not found")
    company["_id"] = str(company["_id"])
    return company

# read job posting by id
@app.get("/jobs/{job_id}}", response_model=jobPostingDB)
async def get_jobs(job_id: str):
    job = await jobs_collection.find_one({"_id": ObjectId(job_id)})
    if not job:
        raise HTTPException(404, "job not found")
    job["_id"] = str(job["_id"])
    return job

# read applicants by id
@app.get("/applicants/{candidate_id}}", response_model=applicantsDB)
async def get_applicant(applicant_id: str):
    applicant = await applicants_collection.find_one({"_id": ObjectId(applicant_id)})
    if not applicant:
        raise HTTPException(404, "applicant not found")
    applicant["_id"] = str(applicant["_id"])
    return applicant

# update company details
@app.put("/company/{company_id}", response_model=companyDB)
async def update_company(company_id: str, Company: company):
    result = await companies_collection.update_one(
        {"_id": ObjectId(company_id)},
        {"$set": Company.dict()}
    )
    if result.modified_count == 0:
        raise HTTPException(404, "company not found")
    updated = await companies_collection.find_one({"_id": ObjectId(company_id)})
    updated["_id"] = str(updated["_id"])
    return updated

# delete company details
@app.delete("/company/{company_id}")
async def delete_company(company_id: str):
    result = await companies_collection.delete_one({"_id": ObjectId(company_id)})
    if result.deleted_count == 0:
        raise HTTPException(404, "company not found")
    return {"message": "company deleted successfully"}