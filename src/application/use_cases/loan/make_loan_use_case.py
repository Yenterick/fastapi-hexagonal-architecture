from src.domain.entities.user import User
from src.domain.value_objects.loan import Loan
from src.application.dto.loan_dto import MakeLoanRequest, MakeLoanResponse
from src.application.ports.repositories.book_repository import BookRepository
from src.application.ports.repositories.loan_repository import LoanRepository


class MakeLoanUseCase:
    def __init__(
        self, loan_repository: LoanRepository, book_repository: BookRepository
    ):
        self.loan_repository = loan_repository
        self.book_repository = book_repository

    async def execute(self, user: User, body: MakeLoanRequest) -> MakeLoanResponse:
        loan = await self.loan_repository.save(
            Loan(
                id=None,
                book=await self.book_repository.get_by_id(body.book_id),
                user=user,
                loan_date=body.loan_date,
                due_date=body.due_date,
                created_at=None,
            )
        )

        return MakeLoanResponse(
            id=loan.id,
            book_id=loan.book.id,  # type: ignore
            user_id=loan.user.id,  # type: ignore
            loan_date=loan.loan_date,
            due_date=loan.due_date,
        )
