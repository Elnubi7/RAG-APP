from .BaseControllers import BaseControllers
from .ProjectControllers import ProjectControllers
from fastapi import UploadFile 
from models import ResponseStatus
import re
import os
class DataControllers(BaseControllers):
    def __init__(self):
        #self.base_controller = BaseControllers()
        super().__init__()
    def validate_data(self,file : UploadFile):
        if file.content_type not in self.app_settings.FILE_ALLOWED_EXTENSIONS:
            return False ,ResponseStatus.file_type_invalid.value
        file_size = 0
        file.file.seek(0, 2)  # Move to end of file to get size
        file_size = file.file.tell()
        file.file.seek(0)  # Reset file pointer to beginning
        max_size_bytes = self.app_settings.MAX_FILE_SIZE_MB * 1024 * 1024
        if file_size > max_size_bytes:
            return False ,ResponseStatus.file_size_exceeded.value
        return True,ResponseStatus.file_valid.value  
    def gene_namr(self, name:str,project_id:int ):
        random_name = self.generate_random_string()
        project_path=ProjectControllers().get_project_path(project_id=project_id)
        clname = self.clean_name(name=name)
        new_file_path = os.path.join(
            project_path,
            random_name + "_" + clname
        )
        while os.path.exists(new_file_path):
            random_name = self.generate_random_string()
            new_file_path = os.path.join(
                project_path,
                random_name + "_" + clname
            )
        return new_file_path, random_name + "_" + clname

    def clean_name(self,name:str):
        cleaned_name = re.sub(r'[^\w.]', '', name.strip())
        cleaned_name = cleaned_name.replace(" ", "_")
        return cleaned_name
        

