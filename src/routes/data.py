from fastapi import APIRouter, FastAPI, Depends,UploadFile,status
from fastapi.responses import JSONResponse
import os 
from helpers.config import get_settings, settings
from controllers import DataControllers
from controllers import ProjectControllers
import aiofiles # type: ignore
from models import ResponseStatus


controller = DataControllers()
data_router = APIRouter(
    prefix="/v1/data",
    tags=["data"],
)
@data_router.post("/upload/{project_id}",)
async def get_data(project_id: str, file : UploadFile,
                   app_setings : settings = Depends(get_settings)):
    isValid , res = controller.validate_data(file)
    if not isValid:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"message": res})
    project_path = ProjectControllers().get_project_path(project_id)
    file_location , file_id = controller.gene_namr(
        name=file.filename,
        project_id=project_id
    )
    async with aiofiles.open(file_location, 'wb') as out_file:
        while content := await file.read(app_setings.FLIE_CHUNK_SIZE):
            await out_file.write(content)

    return JSONResponse(status_code=status.HTTP_200_OK, content={"message": ResponseStatus.file_uploaded.value})