from abc import ABC, abstractmethod
from datetime import timedelta

from src.domain.entities.user import User


class AuthService(ABC):
    @abstractmethod
    def verify_password(plain: str, hash: str) -> bool: ...

    @abstractmethod
    def get_hash(plain: str) -> str: ...

    @abstractmethod
    def get_current_user(token: str) -> User | None: ...

    @abstractmethod
    def auth_user(name: str, plain: str) -> User | None: ...

    @abstractmethod
    def create_access_token(data: dict, expires: timedelta | None = None): ...
