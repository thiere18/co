#!/usr/bin/env python3

from app.db.crud import create_user
from app.db.schemas import UserCreate
from app.db.session import SessionLocal


def init() -> None:
    db = SessionLocal()
    try:

        create_user(
            db,
            UserCreate(
                email="admin@curascuras.com",
                password="password",
                is_active=True,
                is_superuser=True,
                role="ADMIN",
            ),
        )
        print("Creating superuser admin@curascuras.com")
        print("Superuser created")
    except Exception:
        print("User created creating")


if __name__ == "__main__":
    init()
