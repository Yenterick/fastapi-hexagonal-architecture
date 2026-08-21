from fastapi import APIRouter, Depends
from typing import Annotated

from src.domain.entities.user import User
from src.application.ports.repositories.loan_repository import LoanRepository
from src.application.ports.repositories.book_repository import BookRepository
from src.application.use_cases.loan.list_loans_use_case import ListLoansUseCase
from src.application.use_cases.loan.make_loan_use_case import MakeLoanUseCase
from src.application.use_cases.loan.return_loan_use_case import ReturnLoanUseCase
from src.application.dto.loan_dto import (
    MakeLoanRequest,
    MakeLoanResponse,
    ReturnLoanRequest,
    ReturnLoanResponse,
    ListLoansResponse,
)
from src.presentation.api.deps import (
    get_current_user,
    get_loan_repository,
    get_book_repository,
)

router = APIRouter(
    prefix="/loan", tags=["loan"], dependencies=[Depends(get_current_user)]
)


@router.get(
    "/",
    response_model=ListLoansResponse,
    summary="List your loans",
    description="Return every loan belonging to the currently authenticated user.",
)
async def list_loans(
    current_user: Annotated[User, Depends(get_current_user)],
    loan_repository: Annotated[LoanRepository, Depends(get_loan_repository)],
) -> ListLoansResponse:
    use_case = ListLoansUseCase(loan_repository)
    return await use_case.execute(current_user)


@router.post(
    "/",
    response_model=MakeLoanResponse,
    summary="Borrow a book",
    description="Create a new loan of a book for the currently authenticated user.",
)
async def make_loan(
    body: MakeLoanRequest,
    current_user: Annotated[User, Depends(get_current_user)],
    loan_repository: Annotated[LoanRepository, Depends(get_loan_repository)],
    book_repository: Annotated[BookRepository, Depends(get_book_repository)],
) -> MakeLoanResponse:
    use_case = MakeLoanUseCase(loan_repository, book_repository)
    return await use_case.execute(current_user, body)


@router.post(
    "/return",
    response_model=ReturnLoanResponse,
    summary="Return a book",
    description="Return a loan that belongs to the currently authenticated user.",
)
async def return_loan(
    body: ReturnLoanRequest,
    current_user: Annotated[User, Depends(get_current_user)],
    loan_repository: Annotated[LoanRepository, Depends(get_loan_repository)],
) -> ReturnLoanResponse:
    use_case = ReturnLoanUseCase(loan_repository)
    return await use_case.execute(current_user, body)
