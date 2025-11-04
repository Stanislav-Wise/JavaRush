import uvicorn
from fastapi import FastAPI
from routers.main_routers import router as main_router
from routers.movie_routers import router as movie_router


app = FastAPI()
app.include_router(main_router, tags=["main"])
app.include_router(movie_router, tags=["api movie"], prefix="/api/v2/movies" )


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)