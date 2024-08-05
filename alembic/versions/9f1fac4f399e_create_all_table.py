"""create all table

Revision ID: 9f1fac4f399e
Revises: 
Create Date: 2024-08-05 17:09:50.723565

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9f1fac4f399e'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=63), nullable=False),
    sa.Column('hashed_password', sa.Text(), nullable=False),
    sa.Column('email', sa.String(length=127), nullable=False),
    sa.Column('bio', sa.String(length=255), nullable=True),
    sa.Column('birth_date', sa.Date(), nullable=False),
    sa.Column('profile_picture', sa.String(length=127), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=False)
    op.create_index(op.f('ix_user_id'), 'user', ['id'], unique=False)
    op.create_table('auth_token',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('token', sa.String(length=255), nullable=False),
    sa.Column('expiry_date', sa.Date(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_auth_token_id'), 'auth_token', ['id'], unique=False)
    op.create_index(op.f('ix_auth_token_token'), 'auth_token', ['token'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_auth_token_token'), table_name='auth_token')
    op.drop_index(op.f('ix_auth_token_id'), table_name='auth_token')
    op.drop_table('auth_token')
    op.drop_index(op.f('ix_user_id'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###
