from dataclasses import dataclass
from datetime import datetime


@dataclass
class Book:
    id: int | None
    isbn: str
    author: str
    publisher: str
    price: float
    genres: list[str]
    created_at: datetime | None
