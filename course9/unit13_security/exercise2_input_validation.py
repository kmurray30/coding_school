# Input validation with Pydantic catches bad data early.

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr, Field, validator
from typing import Optional

app = FastAPI()

# Pydantic model with validation
class User(BaseModel):
    username: str = Field(..., min_length=3, max_length=50, pattern="^[a-zA-Z0-9_]+$")
    email: EmailStr  # Auto-validates email format
    age: int = Field(..., ge=13, le=120)  # Greater than or equal 13, less than or equal 120
    bio: Optional[str] = Field(None, max_length=500)
    
    @validator('username')
    def username_must_not_be_admin(cls, v):
        if v.lower() in ['admin', 'root', 'system']:
            raise ValueError('reserved username')
        return v

@app.post("/users")
def create_user(user: User):
    """Pydantic validates automatically before this runs"""
    return {"message": "user created", "username": user.username}

# Test validation:
# ✅ POST {"username": "alice", "email": "alice@example.com", "age": 25}
# ❌ POST {"username": "a", ...} → 422: username too short
# ❌ POST {"username": "admin", ...} → 422: reserved username
# ❌ POST {"username": "alice!", ...} → 422: invalid characters
# ❌ POST {"email": "not-an-email", ...} → 422: invalid email
# ❌ POST {"age": 10, ...} → 422: must be 13+
# ❌ POST {"age": 200, ...} → 422: must be <=120

# SQL Injection prevention (ORM handles it)
from sqlalchemy.orm import Session

def get_user_by_id_safe(db: Session, user_id: int):
    """Safe: SQLAlchemy uses parameterized queries"""
    return db.query(User).filter(User.id == user_id).first()
    # Generates: SELECT * FROM users WHERE id = ? [user_id]

def get_user_by_id_unsafe(db: Session, user_id: str):
    """UNSAFE: String formatting"""
    # DON'T DO THIS!
    # query = f"SELECT * FROM users WHERE id = {user_id}"
    # user_id = "1 OR 1=1" → returns all users
    pass

# XSS Prevention
class Comment(BaseModel):
    text: str = Field(..., max_length=1000)
    
    @validator('text')
    def sanitize_text(cls, v):
        # In production, use library like bleach to sanitize HTML
        # For now, just check for script tags
        if '<script' in v.lower():
            raise ValueError('script tags not allowed')
        return v

@app.post("/comments")
def create_comment(comment: Comment):
    # Text is validated and sanitized
    return {"comment": comment.text}

# Run with: uvicorn exercise2_input_validation:app --reload
#
# Validation best practices:
# ✅ Validate all input (Pydantic does this)
# ✅ Whitelist allowed characters
# ✅ Set min/max lengths
# ✅ Validate email/URL formats
# ✅ Reject suspicious patterns
# ❌ Don't trust client-side validation
# ❌ Don't skip server-side validation
