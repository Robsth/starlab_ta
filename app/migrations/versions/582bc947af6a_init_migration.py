"""init migration

Revision ID: 582bc947af6a
Revises: 
Create Date: 2023-03-18 01:27:48.711580

"""
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

from alembic import op

# revision identifiers, used by Alembic.
revision = "582bc947af6a"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index("ix_employees_id", table_name="employees")
    op.drop_table("employees")
    op.create_foreign_key(None, "employee", "employee", ["supervisor_id"], ["id"])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, "employee", type_="foreignkey")
    op.create_table(
        "employees",
        sa.Column("id", sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column("full_name", sa.VARCHAR(), autoincrement=False, nullable=False),
        sa.Column("position", sa.VARCHAR(), autoincrement=False, nullable=False),
        sa.Column("hire_date", sa.DATE(), autoincrement=False, nullable=False),
        sa.Column(
            "salary",
            postgresql.DOUBLE_PRECISION(precision=53),
            autoincrement=False,
            nullable=False,
        ),
        sa.Column("supervisor_id", sa.INTEGER(), autoincrement=False, nullable=True),
        sa.ForeignKeyConstraint(
            ["supervisor_id"], ["employees.id"], name="employees_supervisor_id_fkey"
        ),
        sa.PrimaryKeyConstraint("id", name="employees_pkey"),
    )
    op.create_index("ix_employees_id", "employees", ["id"], unique=False)
    # ### end Alembic commands ###
