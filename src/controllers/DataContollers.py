from .BaseControllers import BaseControllers
from fastapi import UploadFile 
class DataControllers:
    def __init__(self):
        #self.base_controller = BaseControllers()
        super().__init__()
    def validate_data(self,file : UploadFile):
        if file.content_type not in self.app_settings.FILE_ALLOWED_EXTENSIONS:
            return False
        if file.spool_max_size > self.app_settings.MAX_FILE_SIZE_MB * 1024 * 1024:
            return False
        return True
