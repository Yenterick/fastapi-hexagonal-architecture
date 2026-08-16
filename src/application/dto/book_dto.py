from pydantic import BaseModel, Field, ConfigDict

from src.domain.entities.book import Book


class ListBooksResponse(BaseModel):
    """All the books on the database"""

    model_config = ConfigDict(use_enum_values=True)

    books: list[Book] = Field(
        description="A list with all the books available in the database."
    )
