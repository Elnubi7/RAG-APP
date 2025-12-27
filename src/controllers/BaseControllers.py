from helpers.config import get_settings, settings

class BaseControllers:
    

    def __init__(self):
        self.app_settings : settings = get_settings()
    
        