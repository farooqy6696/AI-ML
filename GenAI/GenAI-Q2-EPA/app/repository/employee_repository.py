"""
Repository Layer
Encapsulates all direct database (ORM) access for Employee records.
Keeps SQL/ORM concerns out of the service layer.
"""
from typing import Optional, List, Tuple
from sqlalchemy.orm import Session
from sqlalchemy import or_

from app.models.employee import Employee
from app.schemas.employee import EmployeeCreate, EmployeeUpdate


class EmployeeRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, data: EmployeeCreate) -> Employee:
        employee = Employee(**data.model_dump())
        self.db.add(employee)
        self.db.commit()
        self.db.refresh(employee)
        return employee

    def get_by_id(self, employee_id: int) -> Optional[Employee]:
        return self.db.query(Employee).filter(Employee.employee_id == employee_id).first()

    def get_by_email(self, email: str) -> Optional[Employee]:
        return self.db.query(Employee).filter(Employee.email == email).first()

    def list(
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
    ) -> Tuple[List[Employee], int]:
        query = self.db.query(Employee)

        if department:
            query = query.filter(Employee.department.ilike(f"%{department}%"))
        if designation:
            query = query.filter(Employee.designation.ilike(f"%{designation}%"))
        if min_experience is not None:
            query = query.filter(Employee.experience >= min_experience)
        if min_performance is not None:
            query = query.filter(Employee.performance_score >= min_performance)
        if search:
            like = f"%{search}%"
            query = query.filter(
                or_(Employee.name.ilike(like), Employee.email.ilike(like), Employee.skills.ilike(like))
            )

        total = query.count()

        sort_column = getattr(Employee, sort_by, Employee.employee_id)
        if sort_order.lower() == "desc":
            sort_column = sort_column.desc()
        query = query.order_by(sort_column)

        items = query.offset((page - 1) * page_size).limit(page_size).all()
        return items, total

    def update(self, employee: Employee, data: EmployeeUpdate) -> Employee:
        for field, value in data.model_dump(exclude_unset=True).items():
            setattr(employee, field, value)
        self.db.commit()
        self.db.refresh(employee)
        return employee

    def delete(self, employee: Employee) -> None:
        self.db.delete(employee)
        self.db.commit()

    def all(self) -> List[Employee]:
        return self.db.query(Employee).all()
