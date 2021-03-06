"""init3

Revision ID: 37fb8ef44d07
Revises: 93dfbf328fcb
Create Date: 2022-06-08 16:38:27.926886

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '37fb8ef44d07'
down_revision = '93dfbf328fcb'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('api_data',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('url', sa.String(), nullable=True),
    sa.Column('columns', postgresql.ARRAY(sa.String(), dimensions=1), nullable=True),
    sa.Column('file_src', sa.String(), nullable=True),
    sa.Column('file_size', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_api_data_created_at'), 'api_data', ['created_at'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_api_data_created_at'), table_name='api_data')
    op.drop_table('api_data')
    # ### end Alembic commands ###
