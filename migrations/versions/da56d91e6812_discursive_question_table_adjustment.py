"""Discursive Question table adjustment

Revision ID: da56d91e6812
Revises: 644b5c3a6e06
Create Date: 2024-12-09 17:51:48.114029

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'da56d91e6812'
down_revision = '644b5c3a6e06'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('discursive_question', schema=None) as batch_op:
        batch_op.drop_column('answer')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('discursive_question', schema=None) as batch_op:
        batch_op.add_column(sa.Column('answer', sa.TEXT(), nullable=False))

    # ### end Alembic commands ###
