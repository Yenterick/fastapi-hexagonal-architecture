from abc import ABC, abstractmethod

from src.domain.entities.book import Book


class ListBooksService(ABC):
    @abstractmethod
    async def list() -> list[Book]: ...
