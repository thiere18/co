from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import List, Optional


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    role_id: int


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str
    permission: str


class TokenData(BaseModel):
    id: Optional[str] = None


class UserOutForRole(BaseModel):
    id: int
    username: str
    email: EmailStr

    class Config:
        orm_mode = True


class RoleCreate(BaseModel):
    name: str


class RoleOut(RoleCreate):
    id: int
    created_at: datetime
    updated_at: datetime
    users: List[UserOutForRole]

    class Config:
        orm_mode = True


class RoleUpdate(RoleCreate):
    pass


class RoleOutForUser(RoleCreate):
    id: int

    class Config:
        orm_mode = True


class UserOut(BaseModel):
    id: int
    username: str
    email: EmailStr
    created_at: datetime
    updated_at: datetime
    role: RoleOutForUser

    class Config:
        orm_mode = True


class UpdatePassword(BaseModel):
    actual_password: str
    new_password: str


class SignUserIn(BaseModel):
    username: str
    email: EmailStr
    password: str
