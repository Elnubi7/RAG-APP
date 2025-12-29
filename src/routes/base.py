from fastapi import APIRouter, FastAPI, Depends
import os 
from helpers.config import get_settings, settings

base_router = APIRouter( 
    
    prefix="/v1",
    tags=["base"],
)

@base_router.get("/")
async def w(app_settings : settings = Depends(get_settings)):

    app_name = get_settings().APP_NAME
    app_version = get_settings().APP_VERSION
    return {
        "app_name": app_name,
        "app_version": app_version
    }