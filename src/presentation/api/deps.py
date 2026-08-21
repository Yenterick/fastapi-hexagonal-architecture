from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from src.domain.entities.user import User
from src.infrastructure.database.session import AsyncSessionLocal
from src.application.ports.repositories.user_repository import UserRepository
from src.application.ports.repositories.book_repository import BookRepository
from src.application.ports.repositories.loan_repository import LoanRepository
from src.application.ports.services.auth_service import AuthService
from src.infrastructure.database.repositories.user_repository import (
    SqlAlchemyUserRepository,
)
from src.infrastructure.database.repositories.book_repository import (
    SqlAlchemyBookRepository,
)
from src.infrastructure.database.repositories.loan_repository import (
    SqlAlchemyLoanRepository,
)
from src.infrastructure.jwt.services.auth_service import JWTAuthService

bearer_scheme = HTTPBearer()


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """Dependency for FastAPI to inject sessions into routes"""
    async with AsyncSessionLocal() as session:
        yield session


def get_user_repository(
    session: AsyncSession = Depends(get_db),
) -> UserRepository:
    return SqlAlchemyUserRepository(session)


def get_book_repository(
    session: AsyncSession = Depends(get_db),
) -> BookRepository:
    return SqlAlchemyBookRepository(session)


def get_loan_repository(
    session: AsyncSession = Depends(get_db),
    user_repository: UserRepository = Depends(get_user_repository),
    book_repository: BookRepository = Depends(get_book_repository),
) -> LoanRepository:
    return SqlAlchemyLoanRepository(session, user_repository, book_repository)


def get_auth_service(
    user_repository: UserRepository = Depends(get_user_repository),
) -> AuthService:
    return JWTAuthService(user_repository)


async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme),
    auth_service: AuthService = Depends(get_auth_service),
) -> User:
    user = await auth_service.get_current_user(credentials.credentials)

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return user
