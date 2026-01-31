# SQL injection demo and prevention.

from sqlalchemy import create_engine, Column, Integer, String, text
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('sqlite:///injection.db')
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50))
    password = Column(String(100))

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

# Setup test data
session = Session()
session.query(User).delete()
session.add(User(username="alice", password="secret123"))
session.add(User(username="bob", password="password456"))
session.commit()

print("=== SQL INJECTION DEMO ===\n")

# VULNERABLE: String concatenation
def login_vulnerable(username: str, password: str):
    """DON'T DO THIS! Vulnerable to SQL injection"""
    # Build query with string formatting (DANGEROUS!)
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    print(f"Query: {query}")
    
    result = session.execute(text(query)).fetchall()
    return len(result) > 0

# Normal usage
print("Normal login:")
print(f"alice / secret123: {login_vulnerable('alice', 'secret123')}")  # True
print(f"alice / wrong: {login_vulnerable('alice', 'wrong')}\n")  # False

# SQL Injection attack!
print("SQL Injection attack:")
malicious_username = "alice' OR '1'='1"
malicious_password = "anything"
print(f"Username: {malicious_username}")
print(f"Password: {malicious_password}")
result = login_vulnerable(malicious_username, malicious_password)
print(f"Login successful: {result}\n")  # True! Bypassed password check
# Query becomes: SELECT * FROM users WHERE username = 'alice' OR '1'='1' AND password = 'anything'
# '1'='1' is always true!

# SAFE: Parameterized queries (SQLAlchemy ORM)
def login_safe(username: str, password: str):
    """SAFE: Uses parameterized queries"""
    user = session.query(User).filter(
        User.username == username,
        User.password == password
    ).first()
    return user is not None

print("Safe version:")
print(f"alice / secret123: {login_safe('alice', 'secret123')}")  # True
print(f"alice / wrong: {login_safe('alice', 'wrong')}\n")  # False

print("SQL Injection attempt on safe version:")
print(f"Malicious input: {login_safe(malicious_username, malicious_password)}")  # False!
# SQLAlchemy escapes the input properly

session.close()

# Prevention:
# ✅ Use ORM (SQLAlchemy) - handles parameterization automatically
# ✅ Use parameterized queries if writing raw SQL
# ✅ Validate input format
# ❌ NEVER concatenate user input into SQL
# ❌ NEVER use string formatting for SQL queries

# Example of safe raw SQL:
def safe_raw_sql(user_id: int):
    # Use text() with bound parameters
    query = text("SELECT * FROM users WHERE id = :user_id")
    result = session.execute(query, {"user_id": user_id})
    return result.fetchall()
