#!/usr/bin/env python3

from app.db.session import get_db
from app.db.crud import create_user
from app.db.schemas import UserCreate
from app.db.session import SessionLocal
from app.db.models import User


def init() -> None:
    db = SessionLocal()
    create_user(
            db,
            UserCreate(
                email="admin@curascuras.com",
                password="password",
                is_active=True,
                is_superuser=True,
                role='ADMIN'
            ),
        )
    print("Creating superuser admin@curascuras.com")
    print("Superuser created")


if __name__ == "__main__":
    init()
