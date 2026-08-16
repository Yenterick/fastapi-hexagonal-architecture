from pydantic import BaseModel, Field, ConfigDict, model_validator
from datetime import date


class MakeLoanRequest(BaseModel):
    """Request model for making a new loan"""

    book_id: int = Field(description="The unique identifier of the book")
    user_id: int = Field(description="The unique identifier of the user")
    loan_date: date = Field(description="The date when the book is loaned")
    due_date: date = Field(description="The date when the book is due to be returned")

    @model_validator(mode="after")
    def validate_dates(self):
        if self.due_date < self.loan_date:
            raise ValueError("due_date must be later than or equal to loan_date")
        return self


class MakeLoanResponse(BaseModel):
    """Response model for making a loan"""

    model_config = ConfigDict(from_attributes=True)

    id: int = Field(description="The unique identifier of the loan")
    book_id: int = Field(description="The unique identifier of the book")
    user_id: int = Field(description="The unique identifier of the user")
    loan_date: date = Field(description="The date when the book is loaned")
    due_date: date = Field(description="The date when the book is due to be returned")


class ReturnLoanRequest(BaseModel):
    """Request model for returning a loaned book"""

    loan_id: int = Field(description="The unique identifier of the loan")


class ReturnLoanResponse(BaseModel):
    """Response model for returning a loaned book"""

    model_config = ConfigDict(from_attributes=True)

    id: int = Field(description="The unique identifier of the loan")
    book_id: int = Field(description="The unique identifier of the book")
    user_id: int = Field(description="The unique identifier of the user")
    loan_date: date = Field(description="The date when the book was loaned")
    due_date: date = Field(description="The date when the book was due to be returned")


class ListLoansResponse(BaseModel):
    """All the loans in the database for the current user"""

    model_config = ConfigDict(from_attributes=True)

    loans: list[MakeLoanResponse] = Field(
        description="A list with all the loans in the database."
    )
