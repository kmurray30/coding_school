# Define a SQLAlchemy model and create a table.

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# Create database connection
# For this exercise, we'll use SQLite (file-based, no setup needed)
engine = create_engine('sqlite:///test.db', echo=True)

Base = declarative_base()

# Define a User model
class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), nullable=False)

# Create the table
Base.metadata.create_all(engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Insert a user
new_user = User(username="alice", email="alice@example.com")
session.add(new_user)
session.commit()

# Query the user
user = session.query(User).filter_by(username="alice").first()
print(f"Found user: {user.username}, {user.email}, id={user.id}")

session.close()

# Run this and check test.db was created
# Expected output:
# CREATE TABLE users (...)  -- SQLAlchemy generates SQL
# INSERT INTO users ...
# SELECT ...
# Found user: alice, alice@example.com, id=1
