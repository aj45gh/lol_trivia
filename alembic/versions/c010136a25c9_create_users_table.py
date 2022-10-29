"""create users table

Revision ID: c010136a25c9
Revises: 
Create Date: 2022-10-28 22:34:48.686787

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c010136a25c9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('username', sa.String(255), nullable=False, unique=True),
        sa.Column('password', sa.String(255), nullable=False)
    )


def downgrade() -> None:
    op.drop_table('users')
