from fastapi import APIRouter, FastAPI, Depends,UploadFile
import os 
from helpers.config import get_settings, settings
from controllers.DataContollers import DataControllers

data_router = APIRouter(
    prefix="/v1/data",
    tags=["data"],
)
@data_router.post("/upload/{project_id}",)
async def get_data(project_id: str, file : UploadFile,
                   app_setings : settings = Depends(get_settings)):
    isValid = DataControllers().validate_data(file)
    return isValid