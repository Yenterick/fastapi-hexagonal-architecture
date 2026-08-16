from abc import ABC, abstractmethod

from src.domain.value_objects.loan import Loan


class LoanRepository(ABC):
    @abstractmethod
    async def save(loan: Loan) -> Loan: ...

    @abstractmethod
    async def delete(loan_id: int) -> None: ...

    @abstractmethod
    async def get_by_user_id(user_id: int) -> list[Loan]: ...
