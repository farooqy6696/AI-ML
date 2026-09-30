"""
Service Layer — Machine Learning integration.
Bridges Employee records with the ML predictor (performance category,
training recommendations, salary outlier detection).
"""
from app.ml.predictor import performance_predictor


class MLService:
    @staticmethod
    def predict_performance(experience: float, attendance: float, projects_completed: int,
                             num_skills: int = None, num_certifications: int = None):
        category, confidence, recommendations = performance_predictor.predict(
            experience=experience,
            attendance=attendance,
            projects_completed=projects_completed,
            num_skills=num_skills if num_skills is not None else 5,
            num_certifications=num_certifications if num_certifications is not None else 1,
        )
        return category, confidence, recommendations

    @staticmethod
    def predict_for_employee(employee):
        return MLService.predict_performance(
            experience=employee.experience,
            attendance=employee.attendance or 0,
            projects_completed=employee.projects_completed or 0,
            num_skills=len(employee.skills_list()),
            num_certifications=len(employee.certifications_list()),
        )

    @staticmethod
    def detect_salary_outliers(employees):
        records = [
            {
                "employee_id": e.employee_id,
                "name": e.name,
                "department": e.department,
                "salary": e.salary or 0,
            }
            for e in employees
        ]
        return performance_predictor.detect_salary_outliers(records)


ml_service = MLService()
