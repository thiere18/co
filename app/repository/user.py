from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.config import models, schemas, utils


def create_user(user: schemas.UserCreate, db: Session, current_user: int):

    is_admin = utils.is_admin(current_user.role_id, db)
    if not is_admin:
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
    user_role = (
        db.query(models.Role).filter(models.Role.name == "normal").first()
    )  # noqa
    if not user_role:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Not allowed to register ",
        )
    new_user = models.User(role_id=user_role.id, **user.dict())
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
    id: int, updated_role: schemas.RoleUpdate, db: Session, current_user: int
):
    is_admin = utils.is_admin(current_user.role_id, db)
    if not is_admin:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="you must be an admin to create new user ",
        )
    role_query = db.query(models.Role).filter(models.Role.id == id)
    role = role_query.first()
    if role is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"role with id: {id} does not exist",
        )
    check_duplicate_role = db.query(models.Role).filter(
        models.Role.name == updated_role.name
    )  # noqa
    if check_duplicate_role.first():
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"role {updated_role.name} already exist",
        )
    role_query.update(updated_role.dict(), synchronize_session=False)
    db.commit()
    return role_query.first()
