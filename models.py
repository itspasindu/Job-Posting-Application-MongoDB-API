from pydantic import BaseModel, Field
from typing import Optional

class company(BaseModel):
    name: str
    location: str
    industry: str
    contactEmail: str
    hiringStatus: bool

class jobPosting(BaseModel):
    title: str
    companyID: int
    salary: int
    location: str
    skills: str

class applicants(BaseModel):
    name: str
    email: str
    phone: int
    skills: str
    experience: str
    location: str

class companyDB(company):
    id: str = Field(alias="_id")

class jobPostingDB(jobPosting):
    id: str = Field(alias="_id")

class applicantsDB(applicants):
    id: str = Field(alias="_id")