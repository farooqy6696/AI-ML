"""
AI Router — standalone AI utility endpoints beyond the combined
/employee-analysis pipeline (e.g. comparing two employees' skill profiles).
"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.service.employee_service import EmployeeService
from app.service.ai_service import ai_service
from app.api.deps import get_current_user

router = APIRouter(prefix="/api/v1/ai", tags=["AI Features"])


@router.get("/compare-employees")
def compare_employees(
    employee_id_a: int,
    employee_id_b: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    service = EmployeeService(db)
    employee_a = service.get_employee(employee_id_a)
    employee_b = service.get_employee(employee_id_b)

    comparison = ai_service.compare_skill_profiles(
        {"employee_id": employee_a.employee_id, "name": employee_a.name, "skills": employee_a.skills},
        {"employee_id": employee_b.employee_id, "name": employee_b.name, "skills": employee_b.skills},
    )
    return {"message": "Comparison Generated", "comparison": comparison}
