# Handle complex schema changes with custom migrations.

# Scenario: Rename a column
# This requires custom migration because auto-generate can't detect renames.
# Auto-generate would drop old column and add new one (losing data).

# Example: Rename users.username to users.display_name

# Instructions:
# 
# 1. Create empty migration:
#    $ alembic revision -m "rename username to display_name"
# 
# 2. Edit migration file manually:

"""
from alembic import op
import sqlalchemy as sa

def upgrade():
    # PostgreSQL syntax
    op.alter_column('users', 'username', new_column_name='display_name')
    
    # SQLite doesn't support column rename, would need:
    # 1. Add new column
    # 2. Copy data
    # 3. Drop old column
    # op.add_column('users', sa.Column('display_name', sa.String(50)))
    # op.execute('UPDATE users SET display_name = username')
    # op.drop_column('users', 'username')

def downgrade():
    # Reverse the rename
    op.alter_column('users', 'display_name', new_column_name='username')
"""

# 3. Update your model:
#    display_name = Column(String(50))  # was: username
# 
# 4. Apply migration:
#    $ alembic upgrade head


# ANOTHER COMPLEX CASE: Split a column
# ------------------------------------
# You have: full_name = "Alice Smith"
# You want: first_name = "Alice", last_name = "Smith"

"""
def upgrade():
    # Add new columns
    op.add_column('users', sa.Column('first_name', sa.String(50)))
    op.add_column('users', sa.Column('last_name', sa.String(50)))
    
    # Migrate data (split full_name)
    op.execute(\"\"\"
        UPDATE users 
        SET first_name = split_part(full_name, ' ', 1),
            last_name = split_part(full_name, ' ', 2)
    \"\"\")
    
    # Drop old column
    op.drop_column('users', 'full_name')

def downgrade():
    # Add full_name back
    op.add_column('users', sa.Column('full_name', sa.String(100)))
    
    # Combine first and last name
    op.execute(\"\"\"
        UPDATE users 
        SET full_name = first_name || ' ' || last_name
    \"\"\")
    
    # Drop split columns
    op.drop_column('users', 'first_name')
    op.drop_column('users', 'last_name')
"""


# KEY LESSONS:
# - Auto-generate can't handle renames or complex transformations
# - Write custom migrations for these cases
# - Always test upgrade() AND downgrade()
# - Be careful with data transformations (they might not be perfect)
# - Consider keeping old column temporarily while you verify new ones work
