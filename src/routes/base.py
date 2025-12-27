from fastapi import APIRouter, FastAPI
import os 

base_router = APIRouter(
    prefix="/v1",
    tags=["base"],
)

@base_router.get("/")
async def w():
    app_name = os.getenv("APP_NAME")
    app_version = os.getenv("APP_VERSION")
    return {
        "app_name": app_name,
        "app_version": app_version
    }