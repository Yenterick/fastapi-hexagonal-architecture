from fastapi import APIRouter

router = APIRouter(prefix="/health", tags=["health"])


@router.get("/", description="Endpoint to check the server health.")
async def health_check():
    return {"status": "ok", "message": "Library API is up and running!"}
