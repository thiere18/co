"""create role table

Revision ID: cac274c8acd8
Revises: b19600d85fa0
Create Date: 2022-02-19 20:23:57.949473

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "cac274c8acd8"
down_revision = "b19600d85fa0"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "roles",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
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
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_foreign_key(
        "user_role_fk",
        source_table="users",
        referent_table="roles",
        local_cols=["role_id"],
        remote_cols=["id"],
        ondelete="CASCADE",
    )


def downgrade():
    op.drop_table("roles")