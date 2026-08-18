class ApplicationError(Exception):
    """Base exception for all application/use-case errors"""


class UserNotFoundError(ApplicationError):
    def __init__(self, identifier: str | int):
        super().__init__(f"User not found: {identifier}")


class UserAlreadyExistsError(ApplicationError):
    def __init__(self, username: str):
        super().__init__(f"Username already taken: {username}")


class InvalidCredentialsError(ApplicationError):
    def __init__(self):
        super().__init__("Invalid username or password")
