from src.domain.entities.user import User
from src.application.dto.loan_dto import ListLoansResponse, MakeLoanResponse
from src.application.ports.repositories.loan_repository import LoanRepository


class ListLoansUseCase:
    def __init__(self, loan_repository: LoanRepository):
        self.loan_repository = loan_repository

    async def execute(self, user: User) -> ListLoansResponse:
        loans = await self.loan_repository.get_by_user_id(user.id)

        return ListLoansResponse(
            loans=[
                MakeLoanResponse(
                    id=loan.id,
                    book_id=loan.book.id,  # type: ignore
                    user_id=loan.user.id,  # type: ignore
                    loan_date=loan.loan_date,
                    due_date=loan.due_date,
                )
                for loan in loans
            ]
        )
