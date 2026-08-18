from src.domain.entities.user import User
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
        pass
