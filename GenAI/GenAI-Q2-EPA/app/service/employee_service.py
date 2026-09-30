"""
Service Layer — Employee business logic.
Sits between the API routers and the repository layer; applies business
rules and raises domain exceptions.
"""
from typing import Optional
from sqlalchemy.orm import Session

from app.repository.employee_repository import EmployeeRepository
from app.schemas.employee import EmployeeCreate, EmployeeUpdate
from app.core.exceptions import NotFoundException, AlreadyExistsException


class EmployeeService:
    def __init__(self, db: Session):
        self.repo = EmployeeRepository(db)

    def create_employee(self, data: EmployeeCreate):
        if self.repo.get_by_email(data.email):
            raise AlreadyExistsException(f"Employee with email '{data.email}' already exists.")
        return self.repo.create(data)

    def get_employee(self, employee_id: int):
        employee = self.repo.get_by_id(employee_id)
        if not employee:
            raise NotFoundException(f"Employee {employee_id} not found.")
        return employee

    def list_employees(
        self,
        page: int = 1,
        page_size: int = 10,
        department: Optional[str] = None,
        designation: Optional[str] = None,
        min_experience: Optional[float] = None,
        min_performance: Optional[float] = None,
        search: Optional[str] = None,
        sort_by: str = "employee_id",
        sort_order: str = "asc",
    ):
        items, total = self.repo.list(
            page=page,
            page_size=page_size,
            department=department,
            designation=designation,
            min_experience=min_experience,
            min_performance=min_performance,
            search=search,
            sort_by=sort_by,
            sort_order=sort_order,
        )
        return items, total

    def update_employee(self, employee_id: int, data: EmployeeUpdate):
        employee = self.get_employee(employee_id)
        if data.email and data.email != employee.email and self.repo.get_by_email(data.email):
            raise AlreadyExistsException(f"Email '{data.email}' already in use.")
        return self.repo.update(employee, data)

    def delete_employee(self, employee_id: int):
        employee = self.get_employee(employee_id)
        self.repo.delete(employee)

    def all_employees(self):
        return self.repo.all()
