from src.domain.entities.user import User
from src.application.dto.user_dto import LoginUserRequest, LoginUserResponse
from src.application.ports.repositories.user_repository import UserRepository
from src.application.ports.services.auth_service import AuthService
from src.application.exceptions import UserNotFoundError, InvalidCredentialsError


class LoginUserUseCase:
    def __init__(self, user_repository: UserRepository, auth_service: AuthService):
        self.user_repository = user_repository
        self.auth_service = auth_service

    async def execute(self, body: LoginUserRequest) -> LoginUserResponse:
        user = await self.user_repository.get_by_username(body.username)

        if user is None:
            raise UserNotFoundError(body.username)

        if not self.auth_service.verify_password(body.password, user.password):
            raise InvalidCredentialsError()

        token = self.auth_service.create_access_token(user.id)  # type: ignore
        return LoginUserResponse(id=user.id, token=token)  # type: ignore
