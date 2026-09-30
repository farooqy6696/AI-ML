from pydantic import BaseModel, EmailStr
from app.models.user import RoleEnum


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    role: RoleEnum = RoleEnum.MANAGER


class UserOut(BaseModel):
    id: int
    username: str
    email: EmailStr
    role: RoleEnum

    model_config = {"from_attributes": True}


class LoginRequest(BaseModel):
    username: str
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    role: RoleEnum
