from datetime import datetime, timezone, date
from sqlmodel import Field, SQLModel, Column, DateTime


class Loan(SQLModel, table=True):
    __tablename__ = "loans"  # type: ignore

    id: int | None = Field(default=None, primary_key=True)
    book_id: int = Field(foreign_key="books.id")
    user_id: int = Field(foreign_key="users.id")
    loan_date: date
    due_date: date
    created_at: datetime | None = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        sa_column=Column(DateTime(timezone=True), nullable=False),
    )
