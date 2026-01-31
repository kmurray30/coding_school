# Role-Based Access Control (RBAC) implementation.

from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# User model with role
class User(BaseModel):
    id: int
    username: str
    role: str  # "admin", "moderator", "user"

# Fake current user (in production, get from JWT)
def get_current_user() -> User:
    # Simulated - would decode JWT in production
    return User(id=1, username="alice", role="user")

# Permission checker
def require_role(required_role: str):
    """Dependency that checks user has required role"""
    def role_checker(current_user: User = Depends(get_current_user)):
        role_hierarchy = {
            "admin": 3,
            "moderator": 2,
            "user": 1
        }
        
        user_level = role_hierarchy.get(current_user.role, 0)
        required_level = role_hierarchy.get(required_role, 999)
        
        if user_level < required_level:
            raise HTTPException(
                status_code=403,
                detail=f"Requires {required_role} role"
            )
        
        return current_user
    return role_checker

# Public endpoint (no auth required)
@app.get("/public")
def public_endpoint():
    return {"message": "public data"}

# Authenticated endpoint (any logged-in user)
@app.get("/protected")
def protected_endpoint(current_user: User = Depends(get_current_user)):
    return {"message": f"Hello {current_user.username}"}

# User-only endpoint
@app.get("/user/dashboard")
def user_dashboard(current_user: User = Depends(require_role("user"))):
    return {"dashboard": "user dashboard", "user": current_user.username}

# Moderator-only endpoint
@app.delete("/posts/{post_id}/moderate")
def moderate_post(
    post_id: int,
    current_user: User = Depends(require_role("moderator"))
):
    return {"message": f"Post {post_id} moderated by {current_user.username}"}

# Admin-only endpoint
@app.delete("/users/{user_id}")
def delete_user(
    user_id: int,
    current_user: User = Depends(require_role("admin"))
):
    return {"message": f"User {user_id} deleted by admin {current_user.username}"}

# Resource-based authorization (user owns resource)
class Post(BaseModel):
    id: int
    title: str
    author_id: int

posts_db = {
    1: Post(id=1, title="My Post", author_id=1),
    2: Post(id=2, title="Other Post", author_id=2)
}

@app.put("/posts/{post_id}")
def update_post(
    post_id: int,
    title: str,
    current_user: User = Depends(get_current_user)
):
    post = posts_db.get(post_id)
    if not post:
        raise HTTPException(404, detail="post not found")
    
    # Check ownership or admin
    if post.author_id != current_user.id and current_user.role != "admin":
        raise HTTPException(403, detail="can only edit own posts")
    
    post.title = title
    return {"post": post}

# Run with: uvicorn exercise7_rbac:app --reload
#
# Change get_current_user() to return different roles and test:
#
# role="user":
# ✅ GET /protected
# ✅ GET /user/dashboard
# ❌ DELETE /posts/1/moderate → 403 (requires moderator)
# ❌ DELETE /users/1 → 403 (requires admin)
#
# role="moderator":
# ✅ GET /protected
# ✅ GET /user/dashboard
# ✅ DELETE /posts/1/moderate
# ❌ DELETE /users/1 → 403 (requires admin)
#
# role="admin":
# ✅ Everything (admin has highest privilege)
#
# RBAC best practices:
# ✅ Define clear roles and permissions
# ✅ Use role hierarchy (admin > moderator > user)
# ✅ Check authorization on every protected endpoint
# ✅ Combine role-based and resource-based authorization
# ✅ Log authorization failures
