# Middleware can add custom headers to every response.

from fastapi import FastAPI, Request
import uuid

app = FastAPI()

@app.middleware("http")
async def add_custom_headers(request: Request, call_next):
    response = await call_next(request)
    
    # Add custom headers to the response
    response.headers["X-Request-ID"] = ...  # Generate a unique ID
    response.headers["X-Server-Version"] = ...  # Add a version number
    
    return response

@app.get("/")
def read_root():
    return {"message": "check response headers"}

# Run with: uvicorn exercise4_custom_headers:app --reload
#
# Visit http://localhost:8000/ 
# Open browser dev tools → Network tab → Click the request → Headers
# Look for X-Request-ID and X-Server-Version in Response Headers
#
# Expected headers:
# X-Request-ID: some-unique-uuid
# X-Server-Version: 1.0.0
