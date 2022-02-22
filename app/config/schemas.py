from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    role: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str
    permission: str


class TokenData(BaseModel):
    id: Optional[str] = None


class UserOut(BaseModel):
    id: int
    username: str
    email: EmailStr
    created_at: datetime
    updated_at: datetime
    role: str

    class Config:
        orm_mode = True


class UpdatePassword(BaseModel):
    actual_password: str
    new_password: str


class SignUserIn(BaseModel):
    username: str
    email: EmailStr
    password: str
