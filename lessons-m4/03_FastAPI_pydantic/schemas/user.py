from pydantic import BaseModel, HttpUrl, EmailStr, ValidationError, validator


class User(BaseModel):
    username: str
    age: int
    email: EmailStr
    website: HttpUrl

    @validator("age")
    def check_age(cls, value):
        if value < 18:
            raise ValueError("age must be at least 18")
        return value