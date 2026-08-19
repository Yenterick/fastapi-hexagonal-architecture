from dataclasses import dataclass
from datetime import date, datetime

from src.domain.entities.book import Book
from src.domain.entities.user import User


@dataclass
class Loan:
    id: int | None
    book: Book | None
    user: User | None
    loan_date: date
    due_date: date
    created_at: datetime | None

    def __post_init__(self):
        if self.due_date < self.loan_date:
            raise ValueError("due_date must be later than or equal to loan_date")
