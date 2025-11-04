from fastapi import   APIRouter


router = APIRouter()

@router.get("/")
async def index():
    return {"message": "Hello World"}


@router.get("/about/")
@router.get("/contacts/")
async def about():
    return {"message": "About us"}