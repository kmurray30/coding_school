# Create routes that require a valid JWT. Return 401 if missing or invalid.

from fastapi import FastAPI, HTTPException, Header
from jose import jwt, JWTError

app = FastAPI()

SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"

@app.get("/public")
def public_route():
    return {"message": "anyone can access this"}

# Create a protected endpoint that:
# 1. Requires Authorization header with Bearer token
# 2. Extracts token from header (format: "Bearer <token>")
# 3. Verifies the token with jwt.decode()
# 4. Returns protected data if valid
# 5. Raises 401 HTTPException if missing or invalid

@app.get("/protected")
def protected_route(authorization: str = Header(None)):
    ...

# Run with: uvicorn exercise6_protected_route:app --reload
#
# Test without token:
# GET /protected → 401 error
#
# Test with token (get one from exercise5_login_endpoint first):
# GET /protected with header: Authorization: Bearer <your-token>
#   → {"message": "this is protected data", "user": {...}}
