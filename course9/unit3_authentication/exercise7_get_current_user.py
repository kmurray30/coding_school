# Create a dependency that extracts the current user from JWT.
# Inject it into routes with Depends().

from fastapi import FastAPI, Depends, HTTPException, Header
from jose import jwt, JWTError

app = FastAPI()

SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"

# Create a dependency that:
# 1. Gets Authorization header
# 2. Extracts and verifies JWT
# 3. Returns user data from token
# 4. Raises 401 if missing or invalid

def get_current_user(authorization: str = Header(None)):
    if not authorization:
        raise HTTPException(status_code=401, detail="not authenticated")
    
    try:
        # Extract token (remove "Bearer " prefix)
        token = authorization.replace("Bearer ", "")
        # Decode and verify
        payload = ...
        return payload
    except JWTError:
        raise HTTPException(status_code=401, detail="invalid token")

# Now inject this dependency into routes

@app.get("/me")
def get_my_profile(current_user: dict = Depends(get_current_user)):
    return {"profile": current_user}

@app.get("/dashboard")
def get_dashboard(current_user: dict = Depends(get_current_user)):
    return {
        "message": f"Welcome {current_user.get('username')}!",
        "user_id": current_user.get("user_id")
    }

# Run with: uvicorn exercise7_get_current_user:app --reload
#
# Both /me and /dashboard require authentication via the dependency.
# No need to duplicate auth logic in every route.
#
# Expected:
# GET /me (no auth) → 401
# GET /me (with Bearer token) → {"profile": {"user_id": 1, "username": "alice", ...}}
# GET /dashboard (with token) → {"message": "Welcome alice!", "user_id": 1}
