"""user confirmatiion

Revision ID: a326469e153
Revises: 3ead3f5b6f77
Create Date: 2015-02-09 14:24:32.647412

"""

# revision identifiers, used by Alembic.
revision = 'a326469e153'
down_revision = '3ead3f5b6f77'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('activated', sa.Boolean(), nullable=True))
    op.add_column('users', sa.Column('confirmed', sa.Boolean(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'confirmed')
    op.drop_column('users', 'activated')
    ### end Alembic commands ###
