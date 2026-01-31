# Data migrations: update existing data, not just schema.

# Sometimes you need to migrate data, not just add/remove columns.
# 
# Example: You add a "status" column with default "active"
# But you want to set existing users to "pending" instead.
# 
# Auto-generated migrations only handle schema.
# You write custom upgrade() code for data changes.

# Scenario:
# - Users table exists with username and email
# - Add status column (default: "active")
# - Set all existing users to "pending"

# Instructions:
# 
# 1. Create empty migration:
#    $ alembic revision -m "add status and migrate existing users"
# 
# 2. Edit the migration file manually:

"""
from alembic import op
import sqlalchemy as sa

def upgrade():
    # Add status column
    op.add_column('users', sa.Column('status', sa.String(20), server_default='active'))
    
    # Data migration: update existing rows
    op.execute("UPDATE users SET status = 'pending' WHERE status IS NULL")

def downgrade():
    # Remove column
    op.drop_column('users', 'status')
"""

# 3. Apply migration:
#    $ alembic upgrade head
# 
# 4. Verify: all existing users should have status='pending'
#    New users created after migration will have status='active' (default)
# 
# KEY POINT:
# - op.add_column() = schema change
# - op.execute() = run raw SQL for data migration
# 
# Use data migrations when:
# - Populating new columns with computed values
# - Splitting one column into two
# - Migrating data format (JSON string → JSON column)
# - Backfilling historical data
