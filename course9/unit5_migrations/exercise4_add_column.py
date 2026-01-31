# Add a new column using a migration.

from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)  # NEW COLUMN

# Instructions:
# 
# 1. Add created_at column to the User model (already done above)
# 
# 2. Generate migration:
#    $ alembic revision --autogenerate -m "add created_at to users"
# 
# 3. Look at the generated migration file.
#    It should have:
#    - upgrade() that adds the column
#    - downgrade() that removes it
# 
# 4. Apply the migration:
#    $ alembic upgrade head
# 
# 5. Check the database:
#    $ psql course9_db
#    \d users  (created_at column should be there)
# 
# 6. Now add another column yourself:
#    - Add bio = Column(String(500)) to the User model
#    - Generate migration
#    - Apply it
#    - Verify in database
# 
# Expected migration upgrade():
# op.add_column('users', sa.Column('created_at', sa.DateTime(), nullable=True))
# 
# Expected migration downgrade():
# op.drop_column('users', 'created_at')
