"""empty message

Revision ID: abd9d48a75f4
Revises: bafb9bac8c8d
Create Date: 2023-09-20 14:07:04.066059

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'abd9d48a75f4'
down_revision = 'bafb9bac8c8d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('books', schema=None) as batch_op:
        batch_op.create_unique_constraint(None, ['title'])
        batch_op.drop_column('page_count')

    with op.batch_alter_table('publishers', schema=None) as batch_op:
        batch_op.drop_column('founding_year')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('publishers', schema=None) as batch_op:
        batch_op.add_column(sa.Column('founding_year', sa.INTEGER(), nullable=False))

    with op.batch_alter_table('books', schema=None) as batch_op:
        batch_op.add_column(sa.Column('page_count', sa.INTEGER(), nullable=False))
        batch_op.drop_constraint(None, type_='unique')

    # ### end Alembic commands ###
