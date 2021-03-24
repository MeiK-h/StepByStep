"""empty message

Revision ID: 7f981899ce19
Revises: 
Create Date: 2021-03-24 20:39:23.623698

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "7f981899ce19"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(
        op.f("ix_problems_problem_id"), "problems", ["problem_id"], unique=False
    )
    # ### end Alembic commands ###
    op.add_column("users", sa.Column("nickname", sa.String(length=64), default=""))
    op.add_column(
        "users", sa.Column("email", sa.String(length=64), unique=True, index=True)
    )


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_problems_problem_id"), table_name="problems")
    # ### end Alembic commands ###
