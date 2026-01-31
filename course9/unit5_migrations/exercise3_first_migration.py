# Create your first migration with Alembic.

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)

# Instructions:
# 
# 1. Make sure alembic is initialized (see exercise2)
# 
# 2. Create migration from this model:
#    $ alembic revision --autogenerate -m "create users table"
# 
# 3. Check alembic/versions/ for the generated migration file
#    Open it and look at upgrade() and downgrade() functions
# 
# 4. Apply the migration:
#    $ alembic upgrade head
# 
# 5. Check the database - users table should exist
#    $ psql course9_db
#    \dt  (list tables)
#    \d users  (describe users table)
# 
# 6. Check migration status:
#    $ alembic current
# 
# Expected alembic current output:
# [migration_id] (head), create users table
# 
# The migration file will look like:
# 
# def upgrade():
#     op.create_table('users',
#         sa.Column('id', sa.Integer(), nullable=False),
#         sa.Column('username', sa.String(50), nullable=False),
#         sa.Column('email', sa.String(100), nullable=False),
#         sa.PrimaryKeyConstraint('id'),
#         sa.UniqueConstraint('username'),
#         sa.UniqueConstraint('email')
#     )
# 
# def downgrade():
#     op.drop_table('users')
