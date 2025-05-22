"""create users table

Revision ID: 890d28ea1a26
Revises: 
Create Date: 2025-03-29 16:00:41.054344

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '890d28ea1a26'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(255), nullable=False),
        sa.Column('email', sa.String(255), nullable=False, unique=True)
    )
    # ### end Alembic commands ###

def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('users')
