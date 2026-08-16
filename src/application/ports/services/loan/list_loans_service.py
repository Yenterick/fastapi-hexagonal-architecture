from abc import ABC, abstractmethod

from src.domain.entities.user import User
from src.application.dto.loan_dto import ListLoansResponse


class ListLoansService(ABC):
    @abstractmethod
    async def list(user: User) -> ListLoansResponse: ...
