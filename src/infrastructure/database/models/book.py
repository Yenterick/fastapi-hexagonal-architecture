from datetime import datetime, timezone
from sqlmodel import JSON, Field, SQLModel, Column, DateTime, Numeric


class Book(SQLModel, table=True):
    __tablename__ = "books"  # type: ignore

    id: int | None = Field(default=None, primary_key=True)
    isbn: str
    author: str
    publisher: str
    price: float = Field(
        sa_column=Column(Numeric(6, 2, asdecimal=False), nullable=False)
    )
    genres: list[str] = Field(default=[], sa_column=Column(JSON))
    created_at: datetime | None = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        sa_column=Column(DateTime(timezone=True), nullable=False),
    )
