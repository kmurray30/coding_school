# Build a /login endpoint that verifies credentials and returns a JWT.

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta

app = FastAPI()

SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Fake user database (in production, use real database)
users_db = {
    "alice": {
        "username": "alice",
        "hashed_password": pwd_context.hash("alicepass"),
        "user_id": 1
    },
    "bob": {
        "username": "bob",
        "hashed_password": pwd_context.hash("bobpass"),
        "user_id": 2
    }
}

class LoginRequest(BaseModel):
    username: str
    password: str

# Create /login endpoint that:
# 1. Accepts username and password
# 2. Checks if user exists
# 3. Verifies password with pwd_context.verify()
# 4. If valid, creates JWT with user_id and username, expires in 30 minutes
# 5. Returns the token
# 6. If invalid, raise HTTPException with 401 status

@app.post("/login")
def login(credentials: LoginRequest):
    ...

# Run with: uvicorn exercise5_login_endpoint:app --reload
#
# Test in /docs:
# POST /login with {"username": "alice", "password": "alicepass"}
#   → {"access_token": "eyJhbGc...", "token_type": "bearer"}
#
# POST /login with {"username": "alice", "password": "wrong"}
#   → 401 Unauthorized error
