from fastapi import FastAPI
from dotenv import load_dotenv # type: ignore
load_dotenv(".env")

from routes.base import base_router
app = FastAPI()
app.include_router(base_router)
