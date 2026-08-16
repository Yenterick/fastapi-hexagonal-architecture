from fastapi import FastAPI

from src.infrastructure.config.settings import settings
from src.presentation.api.routes import health

app = FastAPI(
    title=settings.APP_NAME, version=settings.APP_VERSION, debug=settings.DEBUG
)

app.include_router(health.router)
