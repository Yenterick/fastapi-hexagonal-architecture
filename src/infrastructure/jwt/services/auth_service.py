from datetime import datetime, timedelta
from jose import jwt, JWTError
from passlib.context import CryptContext

from src.application.ports.repositories.user_repository import UserRepository
from src.application.ports.services.auth_service import AuthService
from src.domain.entities.user import User
from src.infrastructure.config.settings import settings

SECRET_KEY = settings.SECRET_KEY
ALGORITHM = "HS256"
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class JWTAuthService(AuthService):
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def _verify_password(self, plain: str, hash: str) -> bool:
        return pwd_context.verify(plain, hash)

    def get_hash(self, plain: str) -> str:
        return pwd_context.hash(plain)

    async def get_current_user(self, token: str) -> User | None:
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            if not (id := payload.get("sub")):
                return None
        except JWTError:
            return None

        user: User | None = await self.user_repository.get_by_id(id)
        return user

    def auth_user(self, user: User, plain: str) -> User | None:
        if not self._verify_password(plain, user.password):
            return None
        else:
            return user

    def create_access_token(self, id: int, expires: timedelta | None = None) -> str:
        now: datetime = datetime.now()

        if not expires:
            expires = timedelta(minutes=60)
        src: dict = {"sub": id, "exp": now + expires}

        encoded_jwt: str = jwt.encode(src, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt
