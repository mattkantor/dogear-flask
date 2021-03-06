"""empty message

Revision ID: 4dced2405f8
Revises: 2221a0f94a4
Create Date: 2018-08-01 22:18:04.647043

"""

# revision identifiers, used by Alembic.
revision = '4dced2405f8'
down_revision = '2221a0f94a4'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['users.id'], )
    )
    op.drop_table('follows')
    op.alter_column('feed', 'uuid',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('groups', 'name',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('groups', 'uuid',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('news', 'uuid',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.create_unique_constraint(None, 'users', ['email'])
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='unique')
    op.alter_column('news', 'uuid',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('groups', 'uuid',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('groups', 'name',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('feed', 'uuid',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.create_table('follows',
    sa.Column('uuid', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('follower_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('following_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='follows_pkey')
    )
    op.drop_table('followers')
    ### end Alembic commands ###
