from abc import ABC, abstractmethod

from src.domain.entities.user import User


class UserRepository(ABC):
    @abstractmethod
    async def save(user: User) -> User: ...

    @abstractmethod
    async def get_by_id(user_id: int) -> User | None: ...

    @abstractmethod
    async def get_by_username(username: str) -> User | None: ...
