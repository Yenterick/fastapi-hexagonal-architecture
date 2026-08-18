from src.domain.entities.user import User
from src.application.dto.loan_dto import ListLoansResponse
from src.application.ports.repositories.loan_repository import LoanRepository


class ListLoansUseCase:
    def __init__(self, loan_repository: LoanRepository):
        self.loan_repository = loan_repository

    async def execute(self, user: User) -> ListLoansResponse:
        pass
