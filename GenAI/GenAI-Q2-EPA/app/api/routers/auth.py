"""
Auth Router — POST /login (and /register to bootstrap users).
"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.user import User
from app.schemas.user import UserCreate, UserOut, LoginRequest, TokenResponse
from app.auth.security import hash_password, verify_password
from app.auth.jwt_handler import create_access_token
from app.core.exceptions import AlreadyExistsException, InvalidCredentialsException

router = APIRouter(prefix="/api/v1/auth", tags=["Authentication"])


@router.post("/register", response_model=UserOut, status_code=201)
def register(payload: UserCreate, db: Session = Depends(get_db)):
    if db.query(User).filter(User.username == payload.username).first():
        raise AlreadyExistsException("Username already taken.")
    if db.query(User).filter(User.email == payload.email).first():
        raise AlreadyExistsException("Email already registered.")

    user = User(
        username=payload.username,
        email=payload.email,
        hashed_password=hash_password(payload.password),
        role=payload.role,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


@router.post("/login", response_model=TokenResponse)
def login(payload: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == payload.username).first()
    if not user or not verify_password(payload.password, user.hashed_password):
        raise InvalidCredentialsException()

    token = create_access_token({"sub": user.username, "role": user.role.value})
    return TokenResponse(access_token=token, role=user.role)
