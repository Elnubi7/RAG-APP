from pydantic_settings import BaseSettings, SettingsConfigDict # type: ignore

class settings(BaseSettings):
    APP_NAME: str 
    APP_VERSION: str
    FILE_ALLOWED_EXTENSIONS: list
    MAX_FILE_SIZE_MB: int


    class Config: 
            env_file=".env",

      
def get_settings() -> settings:
    return settings()