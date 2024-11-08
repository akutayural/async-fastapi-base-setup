import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr


class CreateUserSchema(BaseModel):
    first_name: str
    last_name: str
    birth_date: Optional[datetime.date]
    email: EmailStr
    username: str
    password: str



class UpdateUserSchema(BaseModel):
    first_name: str
    last_name: str
    birth_date: Optional[datetime.date]


class UserSchema(BaseModel):
    first_name: str
    last_name: str
    birth_date: Optional[datetime.date]
    email: EmailStr
    username: str


