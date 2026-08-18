from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.domain.entities.user import User
from src.application.ports.repositories.user_repository import UserRepository
from src.infrastructure.database.models.user import User as UserModel


class SqlAlchemyUserRepository(UserRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def save(self, user: User) -> User:
        db_user: UserModel = UserModel(
            full_name=user.full_name,
            username=user.username,
            password=user.password,
        )

        self.session.add(db_user)
        await self.session.commit()

        return self._to_domain(db_user)

    async def get_by_id(self, user_id: int) -> User | None:
        result = await self.session.execute(select(UserModel).where(UserModel.id == user_id))  # type: ignore
        result = result.scalar_one_or_none()

        if not result:
            return None
        else:
            return self._to_domain(result)

    async def get_by_username(self, username: str) -> User | None:
        result = await self.session.execute(select(UserModel).where(UserModel.username == username))  # type: ignore
        result = result.scalar_one_or_none()

        if not result:
            return None
        else:
            return self._to_domain(result)

    @staticmethod
    def _to_domain(db_user: UserModel) -> User:
        return User(
            id=db_user.id,
            full_name=db_user.full_name,
            username=db_user.username,
            password=db_user.password,
            created_at=db_user.created_at,
        )
