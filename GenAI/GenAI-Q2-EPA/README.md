# AI-Based Employee Performance Analyzer

Employee Performance Management System built with **FastAPI**, using a clean
layered architecture, JWT authentication with role-based authorization,
**Google Gemini** for AI features, a **scikit-learn** performance-prediction
model, and Excel/PDF reporting.

## Tech Stack
- **FastAPI** — REST API framework
- **PostgreSQL / MySQL** (via SQLAlchemy) — structured employee & user data
- **MongoDB** — uploaded document metadata + AI output logs
- **Google Gemini API** — document summarization, skill extraction, learning
  path recommendations, interview questions, skill comparison, career growth
- **Scikit-learn + Pandas** — performance-category prediction, training
  recommendations, salary outlier detection
- **openpyxl / reportlab** — Excel and PDF report generation

## Project Structure
```
app/
├── main.py                 # FastAPI app entrypoint
├── config.py                # Configuration Module (.env settings)
├── database.py               # PostgreSQL/MySQL connection (SQLAlchemy)
├── mongodb.py                 # MongoDB connection
├── models/                     # Models (SQLAlchemy ORM: Employee, User)
├── schemas/                     # Schemas (Pydantic request/response models)
├── repository/                   # Repository Layer (DB access)
├── service/                       # Service Layer (business logic,
│                                     AI service, ML bridge, report service)
├── api/
│   ├── deps.py                      # Authentication/Authorization deps
│   └── routers/                      # API Routers
│       ├── auth.py                     # POST /login, /register
│       ├── employees.py                 # Employee CRUD, upload, analysis
│       ├── ai.py                          # Standalone AI endpoints
│       ├── ml.py                           # /predict-performance
│       └── reports.py                       # GET /reports
├── auth/                       # Authentication Module (JWT, hashing)
├── core/exceptions.py           # Exception Module (custom errors + handlers)
├── ml/                            # ML Module (training script, predictor)
└── utils/file_utils.py             # File upload + text extraction
```

## Setup

```bash
# 1. Create a virtual environment
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Configure environment
cp .env.example .env
# edit .env: set DATABASE_URL (Postgres or MySQL), MONGO_URI, SECRET_KEY,
# and GEMINI_API_KEY (get one at https://aistudio.google.com/apikey)

# 4. Run the API
python run.py
# or: uvicorn app.main:app --reload
```

The API will be live at **http://localhost:8000**, with interactive docs at
**http://localhost:8000/docs**.

Tables are created automatically on startup. The ML performance-prediction
model auto-trains a default model on first use (synthetic data) — for
production, run:
```bash
python -m app.ml.train_model
```
after pointing it at a real historical CSV (see `app/ml/train_model.py`).

## Authentication & Roles

1. `POST /api/v1/auth/register` — create a user (`role`: `Admin`, `HR`, or `Manager`)
2. `POST /api/v1/auth/login` — returns a JWT `access_token`
3. Send `Authorization: Bearer <token>` on all other requests

| Action                  | Allowed roles         |
|--------------------------|------------------------|
| Create / upload document | Admin, HR              |
| Update employee          | Admin, HR, Manager     |
| Delete employee          | Admin                  |
| Read / reports / AI / ML | Any authenticated user |

## Key Endpoints

```
POST   /api/v1/auth/register
POST   /api/v1/auth/login
POST   /api/v1/employees
GET    /api/v1/employees            (search: department, designation,
                                      min_experience, min_performance,
                                      search, sort_by, sort_order, pagination)
GET    /api/v1/employees/{id}
PUT    /api/v1/employees/{id}
DELETE /api/v1/employees/{id}
POST   /api/v1/upload-document?employee_id=1   (multipart file: PDF/DOCX)
POST   /api/v1/employee-analysis?employee_id=1  (full AI pipeline)
GET    /api/v1/ai/compare-employees?employee_id_a=1&employee_id_b=2
POST   /api/v1/predict-performance
GET    /api/v1/predict-performance/{employee_id}
GET    /api/v1/salary-outliers
GET    /api/v1/reports?report_type=excel|pdf|department|skills|dashboard
```

## Example Flow

1. Register an Admin user and log in to get a token.
2. `POST /api/v1/employees` to add an employee.
3. `POST /api/v1/upload-document` with a PDF/DOCX resume for that employee.
4. `POST /api/v1/employee-analysis` — Gemini summarizes the doc, extracts
   skills, recommends a learning path, generates interview questions, and
   suggests a career growth plan.
5. `POST /api/v1/predict-performance` or the `/{employee_id}` variant —
   scikit-learn predicts a performance category (Poor/Average/Good/Excellent)
   with training recommendations.
6. `GET /api/v1/reports?report_type=excel` — download a full Excel workbook
   with a department-performance chart, or `report_type=pdf` for a PDF report.
