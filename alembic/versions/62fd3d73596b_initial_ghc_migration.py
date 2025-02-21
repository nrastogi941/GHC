"""Initial ghc migration

Revision ID: 62fd3d73596b
Revises: 
Create Date: 2024-08-30 17:57:55.702624

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '62fd3d73596b'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('checkout',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_email', sa.String(length=120), nullable=False),
    sa.Column('checkout_time', sa.DateTime(), nullable=False),
    sa.Column('order_placed', sa.Boolean(), nullable=True),
    sa.Column('messages_sent', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('checkout')
    # ### end Alembic commands ###
