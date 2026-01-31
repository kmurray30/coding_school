# Build a security-hardened API with all best practices.

from fastapi import FastAPI, Depends, HTTPException, Request, Header
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr, Field, validator
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker, Session
from passlib.context import CryptContext
from jose import jwt, JWTError
from datetime import datetime, timedelta
import secrets
from collections import defaultdict
import time

app = FastAPI(title="Secure API")

# Security configuration
SECRET_KEY = secrets.token_urlsafe(32)  # Generate strong secret
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Database
engine = create_engine('sqlite:///./secure.db')
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    hashed_password = Column(String(100), nullable=False)
    role = Column(String(20), default="user")

Base.metadata.create_all(engine)
SessionLocal = sessionmaker(bind=engine)

# Rate limiter
class RateLimiter:
    def __init__(self):
        self.requests = defaultdict(list)
    
    def check(self, key: str, max_req: int, window: int) -> bool:
        now = time.time()
        self.requests[key] = [t for t in self.requests[key] if t > now - window]
        if len(self.requests[key]) >= max_req:
            return False
        self.requests[key].append(now)
        return True

rate_limiter = RateLimiter()

# CORS (restrict origins in production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Specific origins only
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"]
)

# Security headers middleware
@app.middleware("http")
async def add_security_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["X-XSS-Protection"] = "1; mode=block"
    return response

# Pydantic models with validation
class UserCreate(BaseModel):
    username: str = Field(..., min_length=3, max_length=50, pattern="^[a-zA-Z0-9_]+$")
    email: EmailStr
    password: str = Field(..., min_length=8)
    
    @validator('password')
    def password_strength(cls, v):
        if not any(c.isdigit() for c in v):
            raise ValueError('password must contain a number')
        if not any(c.isupper() for c in v):
            raise ValueError('password must contain uppercase')
        return v

class LoginRequest(BaseModel):
    username: str
    password: str

# Dependencies
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_current_user(
    authorization: str = Header(None),
    db: Session = Depends(get_db)
):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(401, detail="not authenticated")
    
    token = authorization.replace("Bearer ", "")
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if not username:
            raise HTTPException(401, detail="invalid token")
    except JWTError:
        raise HTTPException(401, detail="invalid token")
    
    user = db.query(User).filter(User.username == username).first()
    if not user:
        raise HTTPException(401, detail="user not found")
    
    return user

def require_admin(current_user: User = Depends(get_current_user)):
    if current_user.role != "admin":
        raise HTTPException(403, detail="admin access required")
    return current_user

# Routes
@app.post("/register")
def register(user_data: UserCreate, request: Request, db: Session = Depends(get_db)):
    # Rate limiting
    if not rate_limiter.check(f"register:{request.client.host}", 5, 3600):
        raise HTTPException(429, detail="too many registrations")
    
    # Check if user exists
    if db.query(User).filter(User.username == user_data.username).first():
        raise HTTPException(400, detail="username already exists")
    
    # Create user with hashed password
    hashed_password = pwd_context.hash(user_data.password)
    user = User(
        username=user_data.username,
        email=user_data.email,
        hashed_password=hashed_password
    )
    db.add(user)
    db.commit()
    
    return {"message": "user created", "username": user.username}

@app.post("/login")
def login(credentials: LoginRequest, request: Request, db: Session = Depends(get_db)):
    # Rate limiting (prevent brute force)
    if not rate_limiter.check(f"login:{request.client.host}", 5, 60):
        raise HTTPException(429, detail="too many login attempts")
    
    # Verify user
    user = db.query(User).filter(User.username == credentials.username).first()
    if not user or not pwd_context.verify(credentials.password, user.hashed_password):
        raise HTTPException(401, detail="invalid credentials")
    
    # Create token
    token_data = {"sub": user.username, "exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)}
    token = jwt.encode(token_data, SECRET_KEY, algorithm=ALGORITHM)
    
    return {"access_token": token, "token_type": "bearer"}

@app.get("/me")
def get_profile(current_user: User = Depends(get_current_user)):
    return {
        "username": current_user.username,
        "email": current_user.email,
        "role": current_user.role
    }

@app.delete("/users/{user_id}")
def delete_user(
    user_id: int,
    current_user: User = Depends(require_admin),
    db: Session = Depends(get_db)
):
    # Only admins can delete users
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(404, detail="user not found")
    
    db.delete(user)
    db.commit()
    return {"message": "user deleted"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

# Run with: uvicorn exercise10_secure_api:app --reload
#
# Security features:
# ✅ Input validation (Pydantic)
# ✅ SQL injection prevention (ORM)
# ✅ Password hashing (bcrypt)
# ✅ JWT authentication
# ✅ Role-based authorization (RBAC)
# ✅ Rate limiting (login, registration)
# ✅ CORS (restricted origins)
# ✅ Security headers
# ✅ Strong password requirements
# ✅ No secrets in code
# ✅ Proper HTTP status codes (401, 403)
#
# Test:
# POST /register {"username": "alice", "email": "alice@example.com", "password": "Password123"}
# POST /login {"username": "alice", "password": "Password123"}
# GET /me (with Authorization: Bearer <token>)
