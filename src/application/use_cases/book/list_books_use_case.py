from src.domain.entities.book import Book
from src.application.ports.repositories.book_repository import BookRepository
from src.application.dto.book_dto import ListBooksResponse


class ListBooksUseCase:
    def __init__(self, book_repository: BookRepository):
        self.book_repository = book_repository

    async def execute(self) -> ListBooksResponse:
        books: list[Book] = await self.book_repository.list()

        return ListBooksResponse(books=books)
