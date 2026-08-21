from src.domain.entities.user import User
from src.application.dto.loan_dto import ReturnLoanRequest, ReturnLoanResponse
from src.application.ports.repositories.loan_repository import LoanRepository
from src.application.exceptions import LoanNotFoundError


class ReturnLoanUseCase:
    def __init__(self, loan_repository: LoanRepository):
        self.loan_repository = loan_repository

    async def execute(self, user: User, body: ReturnLoanRequest) -> ReturnLoanResponse:
        user_loans = await self.loan_repository.get_by_user_id(user.id)

        if not any(loan.id == body.loan_id for loan in user_loans):
            raise LoanNotFoundError(body.loan_id)

        loan = await self.loan_repository.delete(body.loan_id)

        return ReturnLoanResponse(
            id=loan.id,  # type: ignore
            book_id=loan.book.id,  # type: ignore
            user_id=loan.user.id,  # type: ignore
            loan_date=loan.loan_date,  # type: ignore
            due_date=loan.due_date,  # type: ignore
        )
