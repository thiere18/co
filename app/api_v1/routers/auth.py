from fastapi import APIRouter, Depends
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.config import schemas
from app.config.database import get_db
from app.repository import auth

router = APIRouter(prefix="/api/v1", tags=["Authentication"])


@router.post("/login", response_model=schemas.Token)
def login(db: Session = Depends(get_db), user_credentials: OAuth2PasswordRequestForm=Depends() ):
    return auth.login(db, user_credentials)
