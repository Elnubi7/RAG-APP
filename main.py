from fastapi import FastAPI

app = FastAPI()
@app.get("/1")
def w():
    return "Hello, World!"
