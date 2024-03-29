"""empty message

Revision ID: 80c89f1f29b2
Revises: 
Create Date: 2024-02-27 23:45:50.447778

"""
from alembic import op
import sqlalchemy as sa


revision = '80c89f1f29b2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():    
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password_hash', sa.String(length=128), nullable=True))
        batch_op.drop_column('password')    


def downgrade():    
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password', sa.VARCHAR(length=100), nullable=False))
        batch_op.drop_column('password_hash')

   
