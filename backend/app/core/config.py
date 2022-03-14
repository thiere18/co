import os

PROJECT_NAME = "cura"

SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")

API_V1_STR = "/api/v1"

REDIS_URL = os.getenv("REDIS_URL")
