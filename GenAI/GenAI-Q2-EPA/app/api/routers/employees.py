"""
Employees Router
CRUD, search/filter/pagination, document upload, and combined
"employee-analysis" endpoint (AI summary + skill extraction in one call).
"""
import math
from typing import Optional

from fastapi import APIRouter, Depends, Query, UploadFile, File
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.employee import (
    EmployeeCreate, EmployeeUpdate, EmployeeOut, PaginatedEmployees,
)
from app.service.employee_service import EmployeeService
from app.service.ai_service import ai_service
from app.utils.file_utils import save_upload, extract_text
from app.mongodb import documents_collection
from app.api.deps import require_roles, get_current_user
from app.models.user import RoleEnum

router = APIRouter(prefix="/api/v1", tags=["Employees"])


@router.post("/employees", response_model=EmployeeOut, status_code=201)
def create_employee(
    payload: EmployeeCreate,
    db: Session = Depends(get_db),
    current_user=Depends(require_roles(RoleEnum.ADMIN, RoleEnum.HR)),
):
    return EmployeeService(db).create_employee(payload)


@router.get("/employees", response_model=PaginatedEmployees)
def list_employees(
    page: int = Query(1, ge=1),
    page_size: int = Query(10, ge=1, le=100),
    department: Optional[str] = None,
    designation: Optional[str] = None,
    min_experience: Optional[float] = None,
    min_performance: Optional[float] = None,
    search: Optional[str] = None,
    sort_by: str = "employee_id",
    sort_order: str = "asc",
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    items, total = EmployeeService(db).list_employees(
        page=page, page_size=page_size, department=department, designation=designation,
        min_experience=min_experience, min_performance=min_performance, search=search,
        sort_by=sort_by, sort_order=sort_order,
    )
    return PaginatedEmployees(total=total, page=page, page_size=page_size, items=items)


@router.get("/employees/{employee_id}", response_model=EmployeeOut)
def get_employee(employee_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    return EmployeeService(db).get_employee(employee_id)


@router.put("/employees/{employee_id}", response_model=EmployeeOut)
def update_employee(
    employee_id: int,
    payload: EmployeeUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(require_roles(RoleEnum.ADMIN, RoleEnum.HR, RoleEnum.MANAGER)),
):
    return EmployeeService(db).update_employee(employee_id, payload)


@router.delete("/employees/{employee_id}", status_code=204)
def delete_employee(
    employee_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(require_roles(RoleEnum.ADMIN)),
):
    EmployeeService(db).delete_employee(employee_id)
    return None


@router.post("/upload-document")
def upload_document(
    employee_id: int,
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user=Depends(require_roles(RoleEnum.ADMIN, RoleEnum.HR)),
):
    employee = EmployeeService(db).get_employee(employee_id)  # 404s if missing
    path = save_upload(file)
    text = extract_text(path)

    doc_record = {
        "employee_id": employee.employee_id,
        "file_name": file.filename,
        "stored_path": path,
        "extracted_text_preview": text[:2000],
    }
    result = documents_collection.insert_one(doc_record)

    return {
        "message": "Document Uploaded",
        "document_id": str(result.inserted_id),
        "file_name": file.filename,
        "extracted_characters": len(text),
    }


@router.post("/employee-analysis")
def employee_analysis(
    employee_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    """Runs the full AI pipeline for an employee using their most recent uploaded document."""
    employee = EmployeeService(db).get_employee(employee_id)

    doc = documents_collection.find_one(
        {"employee_id": employee_id}, sort=[("_id", -1)]
    )
    document_text = ""
    if doc:
        from app.utils.file_utils import extract_text as _extract
        document_text = _extract(doc["stored_path"])

    summary = ai_service.summarize_document(employee_id, document_text) if document_text else "No document uploaded for this employee yet."
    extracted_skills = ai_service.extract_skills(employee_id, document_text) if document_text else employee.skills_list()
    learning_path = ai_service.recommend_learning_path(employee_id, extracted_skills, employee.designation)
    interview_questions = ai_service.generate_interview_questions(employee_id, employee.designation, extracted_skills)
    career_growth = ai_service.suggest_career_growth(
        employee_id, employee.designation, employee.performance_score or 0, employee.experience
    )

    return {
        "message": "Skill Analysis Completed",
        "employee_id": employee_id,
        "document_summary": summary,
        "extracted_skills": extracted_skills,
        "recommended_learning_path": learning_path,
        "interview_questions": interview_questions,
        "career_growth_plan": career_growth,
    }
