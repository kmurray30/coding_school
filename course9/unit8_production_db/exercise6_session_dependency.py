# Proper database session management in FastAPI with dependencies.

from fastapi import FastAPI, Depends
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker, Session

app = FastAPI()

# Database setup
DATABASE_URL = "sqlite:///./session_management.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
Base = declarative_base()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True)

Base.metadata.create_all(engine)

# PROPER session dependency
def get_db():
    """
    Creates a new session for each request.
    Ensures session is closed after request completes.
    Handles commits and rollbacks automatically.
    """
    database = SessionLocal()
    try:
        yield database
    finally:
        database.close()

# Another pattern with explicit commit/rollback
def get_db_with_transaction():
    database = SessionLocal()
    try:
        yield database
        database.commit()
    except Exception:
        database.rollback()
        raise
    finally:
        database.close()

@app.post("/users")
def create_user(username: str, db: Session = Depends(get_db)):
    user = User(username=username)
    db.add(user)
    db.commit()  # Manual commit
    db.refresh(user)
    return {"id": user.id, "username": user.username}

@app.post("/users-auto")
def create_user_auto(username: str, db: Session = Depends(get_db_with_transaction)):
    user = User(username=username)
    db.add(user)
    # No need to call commit - dependency handles it
    # If error occurs, dependency rolls back automatically
    return {"username": user.username}

@app.get("/users")
def list_users(db: Session = Depends(get_db)):
    return db.query(User).all()

# ANTI-PATTERN: Don't do this!
# Creating session inside route without proper cleanup
@app.get("/users-bad")
def list_users_bad():
    db = SessionLocal()  # Created but never closed = connection leak!
    users = db.query(User).all()
    # Missing: db.close()
    return users

# Run with: uvicorn exercise6_session_dependency:app --reload
#
# Best practices:
# ✅ One session per request (use dependency)
# ✅ Always close sessions (try/finally)
# ✅ Handle commits/rollbacks properly
# ✅ Never create global session
# ✅ Never reuse session across requests
