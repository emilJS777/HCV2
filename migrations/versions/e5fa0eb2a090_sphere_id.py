"""sphere_id

Revision ID: e5fa0eb2a090
Revises: 46e4fb5e3d8d
Create Date: 2022-06-24 10:48:20.682629

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e5fa0eb2a090'
down_revision = '46e4fb5e3d8d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('firm', sa.Column('sphere_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'firm', 'sphere', ['sphere_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'firm', type_='foreignkey')
    op.drop_column('firm', 'sphere_id')
    # ### end Alembic commands ###