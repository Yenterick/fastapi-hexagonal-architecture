from abc import ABC, abstractmethod

from src.domain.entities.user import User
from src.application.dto.loan_dto import MakeLoanRequest, MakeLoanResponse


class MakeLoanService(ABC):
    @abstractmethod
    async def make(user: User, body: MakeLoanRequest) -> MakeLoanResponse: ...
