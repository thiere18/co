from fastapi import Response, status, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List
from app.repository import role
from app.config import schemas, oauth2
from app.config.database import get_db


router = APIRouter(prefix="/api/v1/roles", tags=["Roles"])


@router.get("/", response_model=List[schemas.RoleOut])
def get_roles(
    response: Response,
    db: Session = Depends(get_db),
    current_user: int = Depends(oauth2.get_current_user),
):
    return role.get_roles(db)


@router.post("/", status_code=status.HTTP_201_CREATED,
             response_model=schemas.RoleOut
             )
def create_role(
    post: schemas.RoleCreate,
    db: Session = Depends(get_db),
    current_user: int = Depends(oauth2.get_current_user),
):
    return role.create_role(post, db, current_user)


@router.get("/{id}", response_model=schemas.RoleOut)
def get_role(
    id: int,
    db: Session = Depends(get_db),
    current_user: int = Depends(oauth2.get_current_user),
):
    return role.get_role(id, db)


@router.delete("/{id}", response_model_exclude_none=True)
def delete_role(
    id: int,
    db: Session = Depends(get_db),
    current_user: int = Depends(oauth2.get_current_user),
):
    return role.delete_role(id, db, current_user)


@router.put("/{id}", response_model=schemas.RoleOut)
def update_role(
    id: int,
    updated_role: schemas.RoleCreate,
    db: Session = Depends(get_db),
    current_user: int = Depends(oauth2.get_current_user),
):
    return role.update_role(id, updated_role, db, current_user)
