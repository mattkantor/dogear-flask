"""empty message

Revision ID: 4848e18b9d1
Revises: 4d923db91b4
Create Date: 2018-07-28 07:07:27.377478

"""

# revision identifiers, used by Alembic.
revision = '4848e18b9d1'
down_revision = '4d923db91b4'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###

    op.create_foreign_key(None, 'flask_dance_oauth', 'users', ['user_id'], ['id'], referent_schema='public')
    ### end Alembic commands ###
    op.create_table('feed',
                    sa.Column('uuid', sa.VARCHAR(), autoincrement=False, nullable=False),
                    sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
                    sa.Column('id', sa.INTEGER(), nullable=False),
                    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
                    sa.Column('from_user_id', sa.INTEGER(), autoincrement=False, nullable=False),
                    sa.Column('news_id', sa.INTEGER(), autoincrement=False, nullable=False),
                    sa.Column('from_group_id', sa.INTEGER(), autoincrement=False, nullable=False),

                    sa.PrimaryKeyConstraint('id', name='feed_pkey')
                    )


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'flask_dance_oauth', type_='foreignkey')
    op.drop_table('feed')
    ### end Alembic commands ###
