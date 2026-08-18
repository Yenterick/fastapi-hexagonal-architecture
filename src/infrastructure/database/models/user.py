from datetime import datetime, timezone
from sqlmodel import Field, SQLModel, Column, DateTime


class User(SQLModel, table=True):
    __tablename__ = "users"  # type: ignore

    id: int | None = Field(default=None, primary_key=True)
    full_name: str
    username: str
    password: str
    created_at: datetime | None = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        sa_column=Column(DateTime(timezone=True), nullable=False),
    )
