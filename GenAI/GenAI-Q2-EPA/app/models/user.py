"""
User model — holds login credentials and role for RBAC (Admin, HR, Manager).
"""
import enum
from sqlalchemy import Column, Integer, String, Enum, DateTime, func
from app.database import Base


class RoleEnum(str, enum.Enum):
    ADMIN = "Admin"
    HR = "HR"
    MANAGER = "Manager"


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100), unique=True, index=True, nullable=False)
    email = Column(String(150), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    role = Column(Enum(RoleEnum), default=RoleEnum.MANAGER, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
