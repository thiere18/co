from fastapi import status, Depends, APIRouter
from sqlalchemy.orm import Session
from app.config import schemas, oauth2
from app.config.database import get_db
from app.repository import user as u

r = APIRouter(prefix="/api/v1/users", tags=["Users"])


@r.post(
    "/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut
)  # noqa
def create_user(
    user: schemas.UserCreate,
    db: Session = Depends(get_db),
    current_user: int = Depends(oauth2.get_current_user),
):
    return u.create_user(user, db, current_user)


@r.post(
    "/sig", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut
)  # noqa
def Sign_up_user(
    user: schemas.SignUserIn,
    db: Session = Depends(get_db),
):

    return u.sign_up(user, db)


@r.get("/{id}", response_model=schemas.UserOut)
def get_user(
    id: int,
    db: Session = Depends(get_db),
):

    return u.get_user(id, db)
