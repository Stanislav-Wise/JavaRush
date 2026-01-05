# Точка входа
from fastapi import FastAPI
import uvicorn
from app.config import settings
from app.api import api_router


app = FastAPI(
    title="Newsbot API",
    version="0.1.0",
    description="Newsbot API",
    debug=True,
)


@app.get("/")
async def root():
    return {
        "message": "Hello World!",
        "debug": settings.debug,
    }

app.include_router(api_router)


if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8000)

# print(settings.debug)