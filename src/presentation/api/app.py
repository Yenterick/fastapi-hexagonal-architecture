from fastapi import FastAPI

from src.presentation.api.routes import health

app = FastAPI()

app.include_router(health.router)
