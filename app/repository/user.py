from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.config import models, schemas, utils


def create_user(user: schemas.UserCreate, db: Session, current_user: int):

    role = current_user.role
    if role != "ADMIN":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="you must be an admin user to create new user ",
        )
    check_duplicate_email = db.query(models.User).filter(
        models.User.email == user.email
    )
    check_duplicate_username = db.query(models.User).filter(
        models.User.username == user.username
    )
    if check_duplicate_email.first():
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="a user with this email already exists",
        )
    if check_duplicate_username.first():
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="a user with this username already exists",
        )
    hashed_password = utils.hash(user.password)
    user.password = hashed_password

    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


def sign_up(user: schemas.SignUserIn, db: Session):

    check_duplicate_email = db.query(models.User).filter(
        models.User.email == user.email
    )
    check_duplicate_username = db.query(models.User).filter(
        models.User.username == user.username
    )
    if check_duplicate_email.first():
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="a user with this email already exists",
        )
    if check_duplicate_username.first():
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="a user with this username already exists",
        )
    hashed_password = utils.hash(user.password)
    user.password = hashed_password
    user_role = "NORMAL"
    new_user = models.User(role=user_role, **user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


def get_user(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id: {id} does not exist",
        )

    return user


def update_password(
    id: int,
    updated_password: schemas.UpdatePassword,
    db: Session,
):

    user_query = db.query(models.User).filter(models.User.id == id)
    user = user_query.first()
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"user with id: {id} does not exist",
        )
    if not utils.verify(updated_password.actual_password, user.password):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials"
        )
    hashed_password = utils.hash(updated_password.new_password)
    user.password = hashed_password
    db.commit()
    return user


def delete_user(id: int, db: Session, current_user: int):
    user_query = db.query(models.User).filter(models.User.id == id)
    user = user_query.first()
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"user with id: {id} does not exist",
        )
    if id != current_user.id and current_user.role != " ADMIN":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="You are not allowed to allowed to delete this user",
        )  # noqa
    if user.username == "admin":
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="this is the master user can't delete this user",
        )  # noqa
    user_query.delete(synchronize_session=False)
    db.commit()
