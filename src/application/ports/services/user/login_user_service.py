from abc import ABC, abstractmethod

from src.domain.entities.user import User
from src.application.dto.user_dto import LoginUserRequest, LoginUserResponse


class LoginUserService(ABC):
    @abstractmethod
    async def login(body: LoginUserRequest) -> LoginUserResponse: ...
