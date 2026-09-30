"""
Employee model — the core entity, matching the required Entity Fields:
Employee ID, Name, Email, Department, Designation, Experience, Skills,
Certifications, Performance Score, Attendance, Salary, Projects Completed,
Manager Feedback.
"""
from sqlalchemy import Column, Integer, String, Float, Text, DateTime, func
from app.database import Base


class Employee(Base):
    __tablename__ = "employees"

    employee_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(150), nullable=False, index=True)
    email = Column(String(150), unique=True, nullable=False, index=True)
    department = Column(String(100), nullable=False, index=True)
    designation = Column(String(100), nullable=False)
    experience = Column(Float, nullable=False, default=0.0)          # years
    skills = Column(Text, nullable=True)                             # comma-separated
    certifications = Column(Text, nullable=True)                     # comma-separated
    performance_score = Column(Float, nullable=True, default=0.0)    # 0-100
    attendance = Column(Float, nullable=True, default=0.0)           # percentage
    salary = Column(Float, nullable=True, default=0.0)
    projects_completed = Column(Integer, nullable=True, default=0)
    manager_feedback = Column(Text, nullable=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    def skills_list(self):
        return [s.strip() for s in (self.skills or "").split(",") if s.strip()]

    def certifications_list(self):
        return [c.strip() for c in (self.certifications or "").split(",") if c.strip()]
