"""empty message

Revision ID: 9580ecd28924
Revises: bdbdca1877d9
Create Date: 2023-02-19 23:50:13.590217

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9580ecd28924'
down_revision = 'bdbdca1877d9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('chat_ai', sa.Column('me_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'chat_ai', 'chat_me', ['me_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'chat_ai', type_='foreignkey')
    op.drop_column('chat_ai', 'me_id')
    # ### end Alembic commands ###
