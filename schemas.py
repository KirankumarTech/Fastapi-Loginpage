from pydantic import BaseModel
from typing import Optional


class SignUpModel(BaseModel):
    id: Optional[int]
    username: str
    email: str
    password: str

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "username": "johndoe",
                "email": "johndoe@gmail.com",
                "password": "password"
            }
        }


class Settings(BaseModel):
    authjwt_secret_key: str = '5ae9b61604cb37be518b8591227497f691d71a6e59b6ec0ba4dd95fb90148ab3'


class LoginModel(BaseModel):
    username: str
    password: str
