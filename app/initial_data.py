#!/usr/bin/env python3

from app.config.database import SessionLocal
from app.config.schemas import UserCreate, RoleCreate
from app.config.utils import create_user, create_role

db = SessionLocal()


def init_user() -> None:
    create_user(
        db,
        UserCreate(
            username="admin",
            email="admin@fan.com",
            password="password",
            role_id=1,
        ),
    )


def init_role() -> None:
    create_role(
        db,
        RoleCreate(name="admin"),
    )

if __name__ == "__main__":
    print("Creating admin user  admin@fan.com with admin as username")
    init_role()
    init_user()
    print("Superuser created")
