#!/usr/bin/env python3

from tests.database import TestingSessionLocal
from app.config.schemas import UserCreate
from app.config.utils import create_user

db = TestingSessionLocal()
primary_role = ["ADMIN", "NORMAL"]


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
    init_user()
