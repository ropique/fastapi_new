"""foreign key

Revision ID: 3129273900c1
Revises: 8673bf2237a2
Create Date: 2022-05-26 12:25:15.575805

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3129273900c1'
down_revision = '8673bf2237a2'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table="posts", referent_table="users", 
    local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint('post_users_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass
