"""create users table

Revision ID: 140a6466aea5
Revises: 
Create Date: 2022-02-21 23:40:53.268750

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "140a6466aea5"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("username", sa.String(), nullable=False),
        sa.Column("email", sa.String(), nullable=False),
        sa.Column("password", sa.String(), nullable=False),
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "role", sa.Enum("ADMIN", "NORMAL", "RESTRICTED", name="role"), nullable=True
        ),  # noqa
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
        sa.UniqueConstraint("username"),
    )


def downgrade():
    pass
