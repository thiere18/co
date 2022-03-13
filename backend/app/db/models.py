from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from sqlalchemy.dialects.postgresql import ENUM

from .session import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    first_name = Column(String)
    last_name = Column(String)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)
    created_at = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
    updated_at = Column(
        TIMESTAMP(timezone=False), server_default=text("now()"), onupdate=text("now()")
    )  # noqa
    role = Column(
        ENUM("ADMIN", "NORMAL", "RESTRICTED", name="role_status"),
        default="NORMAL",
        nullable=False,
    )
