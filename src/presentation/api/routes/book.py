from fastapi import APIRouter, Depends
from typing import Annotated

from src.application.ports.repositories.book_repository import BookRepository
from src.application.use_cases.book.list_books_use_case import ListBooksUseCase
from src.presentation.api.deps import get_book_repository, get_current_user
from src.application.dto.book_dto import ListBooksResponse

router = APIRouter(
    prefix="/book", tags=["book"], dependencies=[Depends(get_current_user)]
)


@router.get(
    "/",
    response_model=ListBooksResponse,
    summary="List all books",
    description="Return every book currently available in the library catalog.",
)
async def get_all_books(
    book_repository: Annotated[BookRepository, Depends(get_book_repository)],
) -> ListBooksResponse:
    use_case = ListBooksUseCase(book_repository)
    return await use_case.execute()
