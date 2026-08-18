from abc import ABC, abstractmethod
from datetime import timedelta

from src.domain.entities.user import User


class AuthService(ABC):
    @abstractmethod
    def verify_password(self, plain: str, hash: str) -> bool:
        """Hash <plain> and compare with <hash> from the database"""

    @abstractmethod
    def get_hash(self, plain: str) -> str:
        """Return the hash of a <plain> string"""

    @abstractmethod
    def get_current_user(self, token: str) -> User | None:
        """Decode an OAuth access <token> and return the User"""

    @abstractmethod
    def auth_user(self, user: User, plain: str) -> User | None:
        """Authenticate user <user> and <plain> password"""

    @abstractmethod
    def create_access_token(self, data: dict, expires: timedelta | None = None) -> str:
        """Return a JWT access token"""
