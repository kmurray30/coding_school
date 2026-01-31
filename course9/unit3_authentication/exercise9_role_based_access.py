# Add roles to users. Protect routes based on role (authorization).

from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError

app = FastAPI()

SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Get current user from token
async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(status_code=401, detail="invalid token")

# Create a dependency that checks if user has admin role
def require_admin(current_user: dict = Depends(get_current_user)):
    if current_user.get("role") != "admin":
        raise HTTPException(status_code=403, detail="admin access required")
    return current_user

@app.get("/public")
def public_route():
    return {"message": "anyone can access"}

@app.get("/user-only")
def user_route(current_user: dict = Depends(get_current_user)):
    return {"message": "any authenticated user", "user": current_user}

@app.get("/admin-only")
def admin_route(current_user: dict = Depends(require_admin)):
    return {"message": "admin access", "user": current_user}

# For testing, create tokens manually:
# Regular user token:
regular_token = jwt.encode({"user_id": 1, "username": "bob", "role": "user"}, SECRET_KEY, ALGORITHM)
print(f"Regular user token: {regular_token}")

# Admin token:
admin_token = jwt.encode({"user_id": 2, "username": "alice", "role": "admin"}, SECRET_KEY, ALGORITHM)
print(f"Admin token: {admin_token}")

# Run with: uvicorn exercise9_role_based_access:app --reload
#
# Test with regular user token:
# GET /user-only → 200 OK
# GET /admin-only → 403 Forbidden (not admin)
#
# Test with admin token:
# GET /user-only → 200 OK
# GET /admin-only → 200 OK (is admin)
#
# 401 = not authenticated (who are you?)
# 403 = not authorized (I know who you are, but you can't do this)
