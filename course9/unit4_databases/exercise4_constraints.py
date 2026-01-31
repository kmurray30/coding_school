# Constraints enforce data integrity. unique, nullable, default values.

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.exc import IntegrityError

engine = create_engine('sqlite:///constraints.db', echo=False)
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)  # Must be unique and present
    email = Column(String(100), unique=True, nullable=False)     # Must be unique and present
    bio = Column(String(500), nullable=True)                      # Optional field
    status = Column(String(20), default="active")                 # Default value

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Create a user
user1 = User(username="alice", email="alice@example.com")
session.add(user1)
session.commit()
print(f"Created user: {user1.username}, status={user1.status}")

# Try to create duplicate username (should fail)
try:
    user2 = User(username="alice", email="different@example.com")
    session.add(user2)
    session.commit()
except IntegrityError as e:
    print(f"Constraint violation: username must be unique")
    session.rollback()

# Try to create user without required field (should fail)
try:
    user3 = User(email="noname@example.com")  # Missing username
    session.add(user3)
    session.commit()
except IntegrityError as e:
    print(f"Constraint violation: username is required")
    session.rollback()

# Create user with optional bio
user4 = User(username="bob", email="bob@example.com", bio="I like databases")
session.add(user4)
session.commit()
print(f"Created user with bio: {user4.username}, bio={user4.bio}")

session.close()

# Expected output:
# Created user: alice, status=active (default value applied)
# Constraint violation: username must be unique
# Constraint violation: username is required
# Created user with bio: bob, bio=I like databases
