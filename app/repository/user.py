
from fastapi import HTTPException,status
from sqlalchemy.orm import Session
from app.config import models, schemas, utils
from app.config.database import get_db
from app.config import utils




def create_user(user: schemas.UserCreate, db: Session,current_user:int):

    is_admin = utils.is_admin(current_user.role_id,db)
    if not is_admin:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail='you must be an admin to create new user '
                            )
    hashed_password = utils.hash(user.password)
    user.password = hashed_password
    
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

def get_user(id: int, db: Session  ):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id: {id} does not exist")

    return user
