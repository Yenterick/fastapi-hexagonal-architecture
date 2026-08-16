from pydantic_settings import BaseSettings
from pydantic import ConfigDict


class Settings(BaseSettings):
    model_config = ConfigDict(env_file=".env", case_sensitive=True)

    # Database
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DATABASE: str
    DATABASE_ECHO: bool = False

    # App
    APP_NAME: str = "Library API"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = False

    # Security (if needed)
    SECRET_KEY: str
    ALGORITHM: str = "HS256"


settings = Settings()
