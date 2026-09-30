"""
Shared API dependencies: current-user extraction (JWT) and
role-based authorization (Authorization Module).
"""
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.database import get_db
from app.auth.jwt_handler import decode_access_token
from app.core.exceptions import UnauthorizedException, ForbiddenException
from app.models.user import User, RoleEnum

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")


def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> User:
    payload = decode_access_token(token)
    username: str = payload.get("sub")
    if username is None:
        raise UnauthorizedException("Invalid token payload.")
    user = db.query(User).filter(User.username == username).first()
    if user is None:
        raise UnauthorizedException("User not found.")
    return user


def require_roles(*allowed_roles: RoleEnum):
    """Dependency factory enforcing Role-Based Authorization."""

    def role_checker(current_user: User = Depends(get_current_user)) -> User:
        if current_user.role not in allowed_roles:
            raise ForbiddenException(
                f"Role '{current_user.role.value}' is not permitted for this action."
            )
        return current_user

    return role_checker
