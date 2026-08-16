from dataclasses import dataclass
from datetime import date, datetime

from src.domain.entities.book import Book
from src.domain.entities.user import User

@dataclass
class Loan:
    id: int
    book: Book
    user: User
    loan_date: date
    due_date: date
    created_at: datetime

    def __post_init__(self):
        if self.due_date < self.loan_date:
            raise ValueError("due date cannot be earlier than loan date")