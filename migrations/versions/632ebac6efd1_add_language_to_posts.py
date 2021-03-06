"""add language to posts

Revision ID: 632ebac6efd1
Revises: 77f6a36f4456
Create Date: 2020-01-05 17:33:40.144309

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '632ebac6efd1'
down_revision = '77f6a36f4456'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('language', sa.String(length=5), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'language')
    # ### end Alembic commands ###
