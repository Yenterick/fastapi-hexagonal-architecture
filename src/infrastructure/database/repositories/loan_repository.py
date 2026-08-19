from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.domain.value_objects.loan import Loan
from src.application.ports.repositories.loan_repository import LoanRepository
from src.application.ports.repositories.user_repository import UserRepository
from src.application.ports.repositories.book_repository import BookRepository
from src.infrastructure.database.models.loan import Loan as LoanModel
from src.application.exceptions import UserNotFoundError


class SqlAlchemyLoanRepository(LoanRepository):
    def __init__(
        self,
        session: AsyncSession,
        user_repository: UserRepository,
        book_repository: BookRepository,
    ):
        self.session = session
        self.user_repository = user_repository
        self.book_repository = book_repository

    async def save(self, loan: Loan) -> Loan:
        db_loan: LoanModel = LoanModel(
            book_id=loan.book.id,  # type: ignore
            user_id=loan.user.id,  # type: ignore
            loan_date=loan.loan_date,
            due_date=loan.due_date,
        )

        self.session.add(db_loan)
        await self.session.commit()

        return await self._to_domain(db_loan)

    async def delete(self, loan_id: int) -> Loan | None:
        result = await self.session.execute(select(LoanModel).where(LoanModel.id == loan_id))  # type: ignore
        result = result.scalar_one_or_none()

        await self.session.delete(result)
        await self.session.commit()

        if isinstance(result, LoanModel):
            return await self._to_domain(result)

    async def get_by_user_id(self, user_id: int | None) -> list[Loan]:
        if user_id is None:
            raise UserNotFoundError(str(user_id))

        result = await self.session.scalars(select(LoanModel).where(LoanModel.user_id == user_id))  # type: ignore
        db_loans = result.all()

        return [await self._to_domain(loan) for loan in db_loans]

    async def _to_domain(self, db_loan: LoanModel) -> Loan:
        return Loan(
            id=db_loan.id,
            book=await self.book_repository.get_by_id(db_loan.book_id),  # type: ignore
            user=await self.user_repository.get_by_id(db_loan.user_id),  # type: ignore
            loan_date=db_loan.loan_date,
            due_date=db_loan.due_date,
            created_at=db_loan.created_at,
        )
