"""Updated Columns

Revision ID: d0c1052860b5
Revises: 
Create Date: 2024-05-30 13:44:30.029276

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd0c1052860b5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('payment', schema=None) as batch_op:
        batch_op.add_column(sa.Column('url', sa.String(length=128), nullable=True))
        batch_op.add_column(sa.Column('message', sa.String(length=128), nullable=True))
        batch_op.add_column(sa.Column('status', sa.String(length=128), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('payment', schema=None) as batch_op:
        batch_op.drop_column('status')
        batch_op.drop_column('message')
        batch_op.drop_column('url')

    # ### end Alembic commands ###
