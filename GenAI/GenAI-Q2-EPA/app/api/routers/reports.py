"""
Reports Router — GET /reports (Excel/PDF/department/skills/dashboard).
"""
from fastapi import APIRouter, Depends, Query
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session

from app.database import get_db
from app.service.employee_service import EmployeeService
from app.service.report_service import report_service
from app.api.deps import get_current_user

router = APIRouter(prefix="/api/v1/reports", tags=["Reports"])


@router.get("")
def get_report(
    report_type: str = Query(..., pattern="^(excel|pdf|department|skills|dashboard)$"),
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    employees = EmployeeService(db).all_employees()

    if report_type == "excel":
        path = report_service.generate_excel_report(employees)
        return FileResponse(
            path,
            media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            filename="employee_report.xlsx",
        )

    if report_type == "pdf":
        path = report_service.generate_pdf_report(employees)
        return FileResponse(path, media_type="application/pdf", filename="employee_report.pdf")

    if report_type == "department":
        return {"message": "Department-wise Performance Report", "data": report_service.department_wise_report(employees)}

    if report_type == "skills":
        return {"message": "Skill Distribution Chart Data", "data": report_service.skill_distribution(employees)}

    if report_type == "dashboard":
        return {"message": "Employee Summary Dashboard", "data": report_service.summary_dashboard(employees)}
