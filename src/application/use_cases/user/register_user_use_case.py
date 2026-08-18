from src.domain.entities.user import User
from src.application.dto.user_dto import RegisterUserRequest, RegisterUserResponse
from src.application.ports.repositories.user_repository import UserRepository
from src.application.ports.services.auth_service import AuthService
from src.application.exceptions import UserAlreadyExistsError


class RegisterUserUseCase:
    def __init__(self, user_repository: UserRepository, auth_service: AuthService):
        self.user_repository = user_repository
        self.auth_service = auth_service

    async def execute(self, body: RegisterUserRequest) -> RegisterUserResponse:
        if await self.user_repository.get_by_username(body.username) is not None:
            raise UserAlreadyExistsError(body.username)

        user: User = await self.user_repository.save(
            User(
                id=None,
                full_name=body.full_name,
                username=body.username,
                password=self.auth_service.get_hash(body.password),
                created_at=None,
            )
        )

        return RegisterUserResponse(
            id=user.id, full_name=user.full_name, username=user.username
        )
