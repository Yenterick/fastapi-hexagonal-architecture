from abc import ABC, abstractmethod

from src.domain.entities.user import User
from src.application.dto.user_dto import RegisterUserRequest, RegisterUserResponse


class RegisterUserService(ABC):
    @abstractmethod
    async def register(body: RegisterUserRequest) -> RegisterUserResponse: ...
