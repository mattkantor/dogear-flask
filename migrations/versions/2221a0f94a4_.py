"""empty message

Revision ID: 2221a0f94a4
Revises: 4d923db91b4
Create Date: 2018-07-31 21:58:53.282663

"""

# revision identifiers, used by Alembic.
revision = '2221a0f94a4'
down_revision = '4d923db91b4'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('follows',
    sa.Column('uuid', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('follower_id', sa.Integer(), nullable=False),
    sa.Column('following_id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )

    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###


    op.drop_table('follows')
    ### end Alembic commands ###
