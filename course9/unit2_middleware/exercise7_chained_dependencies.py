# Dependencies can depend on other dependencies. Compose them.

from fastapi import FastAPI, Depends, HTTPException

app = FastAPI()

def get_token_from_header(authorization: str = None):
    """Extract token from Authorization header"""
    if not authorization:
        raise HTTPException(status_code=401, detail="no auth header")
    return authorization.replace("Bearer ", "")

def verify_token(token: str = Depends(get_token_from_header)):
    """Verify the token is valid (simplified check)"""
    if token != "secret-token":
        raise HTTPException(status_code=401, detail="invalid token")
    return {"user_id": 123, "username": "alice"}

@app.get("/protected")
def protected_route(current_user: dict = Depends(verify_token)):
    # verify_token depends on get_token_from_header
    # Both run automatically before this handler
    return {
        "message": "you're authenticated",
        "user": current_user
    }

# Run with: uvicorn exercise7_chained_dependencies:app --reload
#
# Test in /docs or with curl:
# curl http://localhost:8000/protected
#   → 401 error (no auth header)
# 
# curl -H "Authorization: Bearer wrong-token" http://localhost:8000/protected
#   → 401 error (invalid token)
#
# curl -H "Authorization: Bearer secret-token" http://localhost:8000/protected
#   → {"message": "you're authenticated", "user": {"user_id": 123, "username": "alice"}}
