from fastapi import APIRouter, Depends
from typing import Annotated

from src.application.ports.repositories.user_repository import UserRepository
from src.application.ports.services.auth_service import AuthService
from src.application.use_cases.user.register_user_use_case import RegisterUserUseCase
from src.application.use_cases.user.login_user_use_case import LoginUserUseCase
from src.application.dto.user_dto import (
    RegisterUserRequest,
    RegisterUserResponse,
    LoginUserRequest,
    LoginUserResponse,
)
from src.presentation.api.deps import get_user_repository, get_auth_service

router = APIRouter(prefix="/auth", tags=["user", "auth"])


@router.post(
    "/register",
    response_model=RegisterUserResponse,
    summary="Register a new user",
    description="Create a new user account with a full name, username, and password.",
)
async def register(
    body: RegisterUserRequest,
    user_repository: Annotated[UserRepository, Depends(get_user_repository)],
    auth_service: Annotated[AuthService, Depends(get_auth_service)],
) -> RegisterUserResponse:
    use_case = RegisterUserUseCase(user_repository, auth_service)
    return await use_case.execute(body)


@router.post(
    "/login",
    response_model=LoginUserResponse,
    summary="Log in",
    description="Authenticate with a username and password and receive a JWT access token to use on protected routes.",
)
async def login(
    body: LoginUserRequest,
    user_repository: Annotated[UserRepository, Depends(get_user_repository)],
    auth_service: Annotated[AuthService, Depends(get_auth_service)],
) -> LoginUserResponse:
    use_case = LoginUserUseCase(user_repository, auth_service)
    return await use_case.execute(body)
