# Attach data to request.state in middleware. Access it in route handlers.

from fastapi import FastAPI, Request
import uuid

app = FastAPI()

@app.middleware("http")
async def attach_request_id(request: Request, call_next):
    # Generate unique request ID and attach to request state
    request.state.request_id = str(uuid.uuid4())
    
    response = await call_next(request)
    
    # Add it to response headers too
    response.headers["X-Request-ID"] = request.state.request_id
    
    return response

@app.get("/")
def read_root(request: Request):
    # Access the request ID from middleware
    return {
        "message": "hello",
        "request_id": request.state.request_id
    }

@app.get("/users/{user_id}")
def get_user(user_id: int, request: Request):
    # Every handler can access request.state.request_id
    return {
        "user_id": user_id,
        "request_id": request.state.request_id
    }

# Run with: uvicorn exercise5_request_context:app --reload
#
# Expected:
# GET / → {"message": "hello", "request_id": "abc-123-..."}
# GET /users/5 → {"user_id": 5, "request_id": "def-456-..."}
# Each request gets a different ID
