"""
Exception Module
Custom exception hierarchy and global FastAPI exception handlers.
"""
from fastapi import Request, status
from fastapi.responses import JSONResponse


class AppException(Exception):
    """Base class for all application-specific exceptions."""
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    message = "An unexpected error occurred."

    def __init__(self, message: str = None):
        self.message = message or self.message
        super().__init__(self.message)


class NotFoundException(AppException):
    status_code = status.HTTP_404_NOT_FOUND
    message = "Resource not found."


class AlreadyExistsException(AppException):
    status_code = status.HTTP_409_CONFLICT
    message = "Resource already exists."


class InvalidCredentialsException(AppException):
    status_code = status.HTTP_401_UNAUTHORIZED
    message = "Invalid username or password."


class UnauthorizedException(AppException):
    status_code = status.HTTP_401_UNAUTHORIZED
    message = "Authentication required."


class ForbiddenException(AppException):
    status_code = status.HTTP_403_FORBIDDEN
    message = "You do not have permission to perform this action."


class ValidationException(AppException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
    message = "Validation failed."


class AIServiceException(AppException):
    status_code = status.HTTP_502_BAD_GATEWAY
    message = "AI service error."


class MLModelException(AppException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    message = "Machine learning model error."


class FileProcessingException(AppException):
    status_code = status.HTTP_400_BAD_REQUEST
    message = "File processing error."


def register_exception_handlers(app):
    @app.exception_handler(AppException)
    async def app_exception_handler(request: Request, exc: AppException):
        return JSONResponse(
            status_code=exc.status_code,
            content={"success": False, "error": exc.__class__.__name__, "message": exc.message},
        )

    @app.exception_handler(Exception)
    async def unhandled_exception_handler(request: Request, exc: Exception):
        return JSONResponse(
            status_code=500,
            content={"success": False, "error": "InternalServerError", "message": str(exc)},
        )
