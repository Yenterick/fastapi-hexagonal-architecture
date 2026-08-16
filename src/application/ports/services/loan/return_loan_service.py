from abc import ABC, abstractmethod

from src.domain.entities.user import User
from src.application.dto.loan_dto import ReturnLoanRequest, ReturnLoanResponse


class ReturnLoanService(ABC):
    @abstractmethod
    async def return_loan(
        user: User, body: ReturnLoanRequest
    ) -> ReturnLoanResponse: ...
