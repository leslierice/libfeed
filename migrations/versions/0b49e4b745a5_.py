"""empty message

Revision ID: 0b49e4b745a5
Revises: 522700caea10
Create Date: 2016-04-28 09:14:42.903767

"""

# revision identifiers, used by Alembic.
revision = '0b49e4b745a5'
down_revision = '522700caea10'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('library_copy', sa.Column('library_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'library_copy', 'library', ['library_id'], ['id'])
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'library_copy', type_='foreignkey')
    op.drop_column('library_copy', 'library_id')
    ### end Alembic commands ###
