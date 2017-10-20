"""create an address table

Revision ID: b2ec3f7fb212
Revises: 
Create Date: 2017-10-14 15:35:18.647291

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b2ec3f7fb212'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        'address',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('address', sa.String(50), nullable=False),
        sa.Column('city', sa.String(50), nullable=False),
        sa.Column('state', sa.String(20), nullable=False),
    )

def downgrade():
    op.drop_table('address')
