from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.infrastructure.config.settings import settings
from src.presentation.api.routes import health, book, user, loan
from src.application.exceptions import ApplicationError
from src.presentation.api.error_handler import application_error_handler

app = FastAPI(
    title=settings.APP_NAME, version=settings.APP_VERSION, debug=settings.DEBUG
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_exception_handler(ApplicationError, application_error_handler)  # type: ignore

app.include_router(health.router)
app.include_router(book.router)
app.include_router(user.router)
app.include_router(loan.router)
