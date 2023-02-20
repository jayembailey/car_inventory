"""empty message

Revision ID: cfaf09cafb83
Revises: 
Create Date: 2023-02-20 14:08:20.848656

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cfaf09cafb83'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('first_name', sa.String(length=150), nullable=True),
    sa.Column('last_name', sa.String(length=150), nullable=True),
    sa.Column('email', sa.String(length=150), nullable=False),
    sa.Column('password', sa.String(), nullable=True),
    sa.Column('g_auth_verify', sa.Boolean(), nullable=True),
    sa.Column('token', sa.String(), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('token')
    )
    op.create_table('car',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('year', sa.Integer(), nullable=True),
    sa.Column('make', sa.String(length=50), nullable=True),
    sa.Column('model', sa.String(length=50), nullable=True),
    sa.Column('color', sa.String(length=50), nullable=True),
    sa.Column('user_token', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['user_token'], ['user.token'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('car')
    op.drop_table('user')
    # ### end Alembic commands ###
