# Middleware runs before and after every request. Log all requests here.

from fastapi import FastAPI, Request
import time

app = FastAPI()

@app.middleware("http")
async def log_requests(request: Request, call_next):
    # Runs before the route handler
    print(f"[{time.strftime('%H:%M:%S')}] {request.method} {request.url.path}")
    
    # Call the actual route handler
    response = await call_next(request)
    
    # Runs after the route handler
    print(f"[{time.strftime('%H:%M:%S')}] Response status: {response.status_code}")
    
    return response

@app.get("/")
def read_root():
    return {"message": "check the console for logs"}

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}

# Run with: uvicorn exercise2_logging_middleware:app --reload
#
# Visit http://localhost:8000/ and http://localhost:8000/users/5
# Watch your terminal. Every request is logged with timestamp, method, and path.
#
# Expected console output:
# [14:23:45] GET /
# [14:23:45] Response status: 200
# [14:23:47] GET /users/5
# [14:23:47] Response status: 200
