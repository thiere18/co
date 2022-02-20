#!/usr/bin/env python3

from tests.database import TestingSessionLocal
from app.config.schemas import UserCreate, RoleCreate
from app.config.utils import create_user, create_role

db = TestingSessionLocal()
primary_role = ["admin", "normal"]


def init_role() -> None:
    for role in primary_role:
        create_role(
            db,
            RoleCreate(name=role),
        )


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


if __name__ == "__main__":
    init_role()
    init_user()
