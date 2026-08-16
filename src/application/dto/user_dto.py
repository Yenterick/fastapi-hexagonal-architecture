from pydantic import BaseModel, Field, ConfigDict


class RegisterUserRequest(BaseModel):
    """Request model for registering a new user"""

    full_name: str = Field(description="The full name of the user")
    username: str = Field(description="The unique username for the user")
    password: str = Field(description="The password for the user account")


class RegisterUserResponse(BaseModel):
    """Response model for user registration"""

    model_config = ConfigDict(from_attributes=True)

    id: int = Field(description="The unique identifier of the user")
    full_name: str = Field(description="The full name of the user")
    username: str = Field(description="The username of the user")


class LoginUserRequest(BaseModel):
    """Request model for user login"""

    username: str = Field(description="The username of the user")
    password: str = Field(description="The password of the user")


class LoginUserResponse(BaseModel):
    """Response model for user login"""

    model_config = ConfigDict(from_attributes=True)

    id: int = Field(description="The unique identifier of the user")
    full_name: str = Field(description="The full name of the user")
    username: str = Field(description="The username of the user")
