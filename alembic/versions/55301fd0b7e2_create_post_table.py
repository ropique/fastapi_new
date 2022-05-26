"""create post table

Revision ID: 55301fd0b7e2
Revises: 
Create Date: 2022-05-26 11:46:27.294594

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '55301fd0b7e2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False,
    primary_key=True), sa.Column('title', sa.String(), nullable=False), sa.Column('category', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_table('posts')
    pass
