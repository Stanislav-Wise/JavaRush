from fastapi import  HTTPException, Query, APIRouter, Depends, status, Request
from sqlalchemy.orm import Session
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from schemas.movie import MovieBase, MovieCreate, MovieUpdate, MovieInDB, MoviePublic
from db.session import SessionLocal, get_db
from models.genry import Genre
from models.movie import Movie
from models.review import Review

from .movie_routers import movies


router = APIRouter()
templates = Jinja2Templates(directory="templates")


router = APIRouter()


@router.get("/", response_class=HTMLResponse, name='html_movie_list')
async def movie_list(
    request: Request,
    db: Session = Depends(get_db),
    year: int = Query(None, description="Year of release"),
    title: str = Query(None, description="Movie title"),
):
    """Получить список фильмов."""
    query =  db.query(Movie)

    if year is not None:
        query = query.filter(Movie.year >= year)
    if title is not None:
        query = query.filter(Movie.title.ilike(f'%{title}%'))

    query = query.order_by(Movie.year.desc(), Movie.id.desc())
    all_movies = query.all()
    context = {
        "request": request,
        "title": "Список фильмов",
        "user": "Боб",
        'movies': all_movies
    }
    return templates.TemplateResponse("movies/movie_list.html", context=context)


@router.get("/{movie_id}/", response_class=HTMLResponse, name='html_movie_detail')
async def movie_details(request: Request, movie_id: int,     db: Session = Depends(get_db),):
    """Получаем информацию по фильму."""
    movie = db.query(Movie).filter(Movie.id == movie_id).first()

    if movie is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Фильм c {movie_id=} не найден')

    context = {
        "request": request,
        "title": "Кинотеатр",
        "user": "Боб",
        "movie": movie,
    }
    return templates.TemplateResponse("movies/movie_detail.html", context=context)


@router.get("/create", response_class=HTMLResponse, name='html_movie_create')
async def movie_create(request: Request):
    context = {
        "request": request,
    }
    return templates.TemplateResponse("movies/movie_create.html", context=context)