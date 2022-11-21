"""\"private message\"

Revision ID: fc21bcca1a08
Revises: 2acb95df56fe
Create Date: 2022-11-20 21:28:22.502316

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'fc21bcca1a08'
down_revision = '2acb95df56fe'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('message',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sender_id', sa.Integer(), nullable=True),
    sa.Column('recipient_id', sa.Integer(), nullable=True),
    sa.Column('body', sa.String(length=140), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['recipient_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['sender_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('message', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_message_timestamp'), ['timestamp'], unique=False)

    op.drop_table('test')
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('last_message_read_time', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('last_message_read_time')

    op.create_table('test',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('stock_name', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.Column('operation', postgresql.ENUM('Buy', 'Sell', name='oper'), autoincrement=False, nullable=True),
    sa.Column('operation_day', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('price', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='users_pkey')
    )
    with op.batch_alter_table('message', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_message_timestamp'))

    op.drop_table('message')
    # ### end Alembic commands ###