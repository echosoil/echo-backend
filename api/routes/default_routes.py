from fastapi import APIRouter

from api.config import settings

router = APIRouter()

@router.get("/")
async def index():
    return {"message": f"Hello, wellcome to {settings.swagger_title}"}
