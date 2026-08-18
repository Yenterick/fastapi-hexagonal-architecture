from abc import ABC, abstractmethod

from src.domain.entities.book import Book


class BookRepository(ABC):
    @abstractmethod
    async def list(self) -> list[Book]: ...

    @abstractmethod
    async def get_by_id(self, book_id: int) -> Book | None: ...
