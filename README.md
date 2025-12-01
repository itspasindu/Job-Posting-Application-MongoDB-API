# Job Posting Application API with MongoDB

A RESTful API built with FastAPI and MongoDB for managing job postings, companies, and applicants.

## Features

- **Company Management**: Create, read, update, and delete company profiles
- **Job Postings**: Manage job listings with details like title, salary, location, and required skills
- **Applicant Tracking**: Store and manage applicant information including skills and experience
- **Full CRUD Operations**: Complete Create, Read, Update, Delete functionality for all entities
- **Async Database Operations**: Utilizes Motor for asynchronous MongoDB operations

## Tech Stack

- **FastAPI** - Modern, fast web framework for building APIs
- **MongoDB** - NoSQL database for flexible data storage
- **Motor** - Async MongoDB driver for Python
- **Pydantic** - Data validation using Python type annotations

## Prerequisites

- Python 3.8+
- MongoDB server running locally or remotely

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/itspasindu/Job-Posting-Application-MongoDB-API.git
   cd Job-Posting-Application-MongoDB-API
   ```

2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install fastapi motor uvicorn pydantic
   ```

4. Ensure MongoDB is running on `mongodb://127.0.0.1:27017`

5. Start the server:
   ```bash
   uvicorn main:app --reload
   ```

6. Access the API documentation at `http://127.0.0.1:8000/docs`

## API Endpoints

### Companies

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/company` | Create a new company |
| GET | `/company` | Get all companies |
| GET | `/company/{company_id}` | Get a company by ID |
| PUT | `/company/{company_id}` | Update a company |
| DELETE | `/company/{company_id}` | Delete a company |

### Job Postings

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/jobs` | Create a new job posting |
| GET | `/jobs` | Get all job postings |
| GET | `/jobs/{job_id}` | Get a job posting by ID |
| PUT | `/jobs/{job_id}` | Update a job posting |
| DELETE | `/jobs/{job_id}` | Delete a job posting |

### Applicants

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/applicants` | Create a new applicant |
| GET | `/applicants` | Get all applicants |
| GET | `/applicants/{applicant_id}` | Get an applicant by ID |
| PUT | `/applicants/{applicant_id}` | Update an applicant |
| DELETE | `/applicants/{applicant_id}` | Delete an applicant |

## Data Models

### Company
```json
{
  "name": "string",
  "location": "string",
  "industry": "string",
  "contactEmail": "string",
  "hiringStatus": true
}
```

### Job Posting
```json
{
  "title": "string",
  "companyID": 0,
  "salary": 0,
  "location": "string",
  "skills": "string"
}
```

### Applicant
```json
{
  "name": "string",
  "email": "string",
  "phone": 0,
  "skills": "string",
  "experience": "string",
  "location": "string"
}
```

## Database Configuration

The application connects to MongoDB using the following configuration:
- **Connection URL**: `mongodb://127.0.0.1:27017`
- **Database Name**: `job-posting-application-API`
- **Collections**:
  - `companies` - Stores company data
  - `job_postings` - Stores job posting data
  - `applicants` - Stores applicant data

To modify the database connection, update the `MONGO_URL` in `database.py`.

## License

This project is open source and available under the [MIT License](LICENSE).
