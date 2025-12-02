import uvicorn
from fastapi import FastAPI
from routers.main_routers import router as main_router
from routers.movie_routers import router as movie_router
from routers.html_movie_routers import router as html_movie_router


app = FastAPI(
    title='Cinema API',
    description='Учебный проект кинотеатра',
    version='1.1.0',
)
app.include_router(main_router, tags=["main"])
app.include_router(html_movie_router, tags=["html movie"], prefix="/movies" )
app.include_router(movie_router, tags=["api movie"], prefix="/api/v1/movies" )



if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)