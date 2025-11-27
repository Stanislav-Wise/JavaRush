from fastapi import   APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

router = APIRouter()

templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse, name='index')
async def index(request: Request):
    context = {
        "request": request,
        "title": "Кинотеатр",
        "user": "Боб"
    }
    return templates.TemplateResponse("main/index.html", context=context)


@router.get("/about/", response_class=HTMLResponse, name='about')
async def about(request: Request):
    context = {
        "request": request,
        "title": "Кинотеатр",
    }
    return templates.TemplateResponse("main/about.html", context=context)