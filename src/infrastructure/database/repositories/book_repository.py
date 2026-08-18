from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.domain.entities.book import Book
from src.application.ports.repositories.book_repository import BookRepository
from src.infrastructure.database.models.book import Book as BookModel


class SqlAlchemyBookRepository(BookRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def list(self) -> list[Book]:
        result = await self.session.scalars(select(BookModel))
        db_books = result.all()

        return [self._to_domain(db_book) for db_book in db_books]

    async def get_by_id(self, book_id: int) -> Book | None:
        result = await self.session.execute(select(BookModel).where(BookModel.id == book_id))  # type: ignore
        result = result.scalar_one_or_none()

        if not result:
            return None
        else:
            return self._to_domain(result)

    @staticmethod
    def _to_domain(db_book: BookModel) -> Book:
        return Book(
            id=db_book.id,
            isbn=db_book.isbn,
            author=db_book.author,
            publisher=db_book.publisher,
            price=db_book.price,
            genres=db_book.genres,
            created_at=db_book.created_at,
        )
