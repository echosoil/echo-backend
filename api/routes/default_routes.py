from fastapi import APIRouter
from api.config.settings import settings

default_route = APIRouter()


@default_route.get("/")
async def index():
    return {"message": f"Hello, wellcome to {settings.app_name}"}
