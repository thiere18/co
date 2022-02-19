from fastapi import status, HTTPException
from sqlalchemy.orm import Session
from app.config import models, schemas


def get_roles(db: Session):
    return db.query(models.Role).all()


def create_role(role: schemas.RoleCreate, db: Session):
    new_role = models.Role(**role.dict())
    db.add(new_role)
    db.commit()
    db.refresh(new_role)
    return new_role


def get_role(id: int, db: Session):
    role = db.query(models.Role).filter(models.Role.id == id).first()
    if not role:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"role with id: {id} was not found",
        )
    return role


def delete_role(id: int, db: Session):
    role_query = db.query(models.Role).filter(models.Role.id == id)

    role = role_query.first()

    if role is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"role with id: {id} does not exist",
        )

    role_query.delete(synchronize_session=False)
    db.commit()  # Response(status_code=status.HTTP_204_NO_CONTENT)


def update_role(id: int, updated_role: schemas.RoleUpdate, db: Session):
    role_query = db.query(models.Role).filter(models.Role.id == id)
    role = role_query.first()
    if role is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"role with id: {id} does not exist",
        )
    role_query.update(updated_role.dict(), synchronize_session=False)
    db.commit()
    return role_query.first()
