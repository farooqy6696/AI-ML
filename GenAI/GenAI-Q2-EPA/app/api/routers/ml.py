"""
ML Router — POST /predict-performance and salary outlier detection.
"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.employee import PerformancePredictionRequest, PerformancePredictionResponse
from app.service.ml_service import ml_service
from app.service.employee_service import EmployeeService
from app.api.deps import get_current_user

router = APIRouter(prefix="/api/v1", tags=["Machine Learning"])


@router.post("/predict-performance", response_model=PerformancePredictionResponse)
def predict_performance(
    payload: PerformancePredictionRequest,
    current_user=Depends(get_current_user),
):
    category, confidence, recommendations = ml_service.predict_performance(
        experience=payload.experience,
        attendance=payload.attendance,
        projects_completed=payload.projects_completed,
        num_skills=payload.num_skills,
        num_certifications=payload.num_certifications,
    )
    return PerformancePredictionResponse(
        predicted_category=category, confidence=round(confidence, 3), recommended_training=recommendations
    )


@router.get("/predict-performance/{employee_id}", response_model=PerformancePredictionResponse)
def predict_performance_for_employee(
    employee_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    employee = EmployeeService(db).get_employee(employee_id)
    category, confidence, recommendations = ml_service.predict_for_employee(employee)
    return PerformancePredictionResponse(
        predicted_category=category, confidence=round(confidence, 3), recommended_training=recommendations
    )


@router.get("/salary-outliers")
def salary_outliers(db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    employees = EmployeeService(db).all_employees()
    outliers = ml_service.detect_salary_outliers(employees)
    return {"message": "Salary Outliers Detected" if outliers else "No Outliers Found", "outliers": outliers}
