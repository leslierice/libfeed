"""empty message

Revision ID: 50d734f7cb1f
Revises: 119c2d9f303d
Create Date: 2016-04-30 08:33:59.025643

"""

# revision identifiers, used by Alembic.
revision = '50d734f7cb1f'
down_revision = '119c2d9f303d'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('person', sa.Column('img', sa.String(length=256), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('person', 'img')
    ### end Alembic commands ###
