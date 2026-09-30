from typing import Optional, List
from pydantic import BaseModel, EmailStr, Field


class EmployeeBase(BaseModel):
    name: str
    email: EmailStr
    department: str
    designation: str
    experience: float = Field(0, ge=0)
    skills: Optional[str] = ""            # comma-separated string on input
    certifications: Optional[str] = ""
    performance_score: Optional[float] = Field(0, ge=0, le=100)
    attendance: Optional[float] = Field(0, ge=0, le=100)
    salary: Optional[float] = Field(0, ge=0)
    projects_completed: Optional[int] = Field(0, ge=0)
    manager_feedback: Optional[str] = ""


class EmployeeCreate(EmployeeBase):
    pass


class EmployeeUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    department: Optional[str] = None
    designation: Optional[str] = None
    experience: Optional[float] = None
    skills: Optional[str] = None
    certifications: Optional[str] = None
    performance_score: Optional[float] = None
    attendance: Optional[float] = None
    salary: Optional[float] = None
    projects_completed: Optional[int] = None
    manager_feedback: Optional[str] = None


class EmployeeOut(EmployeeBase):
    employee_id: int

    model_config = {"from_attributes": True}


class PaginatedEmployees(BaseModel):
    total: int
    page: int
    page_size: int
    items: List[EmployeeOut]


class PerformancePredictionRequest(BaseModel):
    experience: float
    attendance: float
    projects_completed: int
    num_skills: Optional[int] = None
    num_certifications: Optional[int] = None


class PerformancePredictionResponse(BaseModel):
    predicted_category: str
    confidence: float
    recommended_training: List[str]
