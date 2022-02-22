#!/usr/bin/env python3

from app.config.database import SessionLocal
from app.config.schemas import UserCreate
from app.config.utils import create_user

db = SessionLocal()


def init_user() -> None:
    create_user(
        db,
        UserCreate(
            username="admin",
            email="admin@fan.com",
            password="password",
            role="ADMIN",
        ),
    )


if __name__ == "__main__":
    print("Creating admin user  admin@fan.com with admin as username")
    init_user()
    print("Superuser created")
