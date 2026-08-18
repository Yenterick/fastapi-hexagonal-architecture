from src.domain.entities.user import User
from src.application.dto.loan_dto import ReturnLoanRequest, ReturnLoanResponse
from src.application.ports.repositories.loan_repository import LoanRepository


class ReturnLoanUseCase:
    def __init__(self, loan_repository: LoanRepository):
        self.loan_repository = loan_repository

    async def execute(self, user: User, body: ReturnLoanRequest) -> ReturnLoanResponse:
        pass
