"""Add session

Revision ID: 620699f2ec04
Revises: 70b23008645a
Create Date: 2022-07-14 13:28:02.864683

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '620699f2ec04'
down_revision = '70b23008645a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('recipe', 'category_id',
               existing_type=sa.INTEGER(),
               nullable='False')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('recipe', 'category_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###