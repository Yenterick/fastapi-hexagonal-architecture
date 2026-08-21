from fastapi import Request
from fastapi.responses import JSONResponse

from src.application.exceptions import (
    ApplicationError,
    AuthorizationError,
    InvalidCredentialsError,
    LoanNotFoundError,
    UserAlreadyExistsError,
    UserNotFoundError,
)

_STATUS_CODES: dict[type[ApplicationError], int] = {
    AuthorizationError: 401,
    InvalidCredentialsError: 401,
    UserNotFoundError: 401,
    UserAlreadyExistsError: 409,
    LoanNotFoundError: 404,
}


async def application_error_handler(
    request: Request, exc: ApplicationError
) -> JSONResponse:
    status_code = _STATUS_CODES.get(type(exc), 422)
    return JSONResponse(status_code=status_code, content={"detail": str(exc)})
