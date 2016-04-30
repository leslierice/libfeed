"""empty message

Revision ID: 04100625f92a
Revises: bbecce189ed8
Create Date: 2016-04-28 09:09:58.322942

"""

# revision identifiers, used by Alembic.
revision = '04100625f92a'
down_revision = 'bbecce189ed8'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('relationship',
    sa.Column('person1', sa.Integer(), nullable=False),
    sa.Column('person2', sa.Integer(), nullable=False),
    sa.Column('date', sa.Date(), nullable=True),
    sa.ForeignKeyConstraint(['person1'], ['person.id'], ),
    sa.ForeignKeyConstraint(['person2'], ['person.id'], ),
    sa.PrimaryKeyConstraint('person1', 'person2')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('relationship')
    ### end Alembic commands ###