""" add role to users table

Revision ID: 90f23458f2b8
Revises: 91979b40eb38
Create Date: 2022-03-11 15:17:58.718758-08:00

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision = "90f23458f2b8"
down_revision = "91979b40eb38"
branch_labels = None
depends_on = None


def upgrade():
    role_status = postgresql.ENUM("ADMIN", "NORMAL", "RESTRICTED", name="role_status")
    role_status.create(op.get_bind())

    op.add_column(
        "user",
        sa.Column(
            "role",
            sa.Enum("ADMIN", "NORMAL", "RESTRICTED", name="role_status"),
            nullable=True,
        ),
    )


def downgrade():
    op.drop_column("user", "role")

    role_status = postgresql.ENUM("ADMIN", "NORMAL", "RESTRICTED", name="role_status")
    role_status.drop(op.get_bind())
