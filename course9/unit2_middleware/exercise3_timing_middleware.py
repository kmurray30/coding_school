# Add request timing to middleware. How long did each request take?

from fastapi import FastAPI, Request
import time

app = FastAPI()

@app.middleware("http")
async def timing_middleware(request: Request, call_next):
    # Record start time
    start_time = ...
    
    # Process the request
    response = await call_next(request)
    
    # Calculate duration
    duration = ...
    
    # Log it
    print(f"{request.method} {request.url.path} took {duration:.4f} seconds")
    
    return response

@app.get("/fast")
def fast_endpoint():
    return {"speed": "blazing"}

@app.get("/slow")
def slow_endpoint():
    time.sleep(0.5)  # Simulate slow operation
    return {"speed": "not so blazing"}

# Run with: uvicorn exercise3_timing_middleware:app --reload
#
# Visit /fast and /slow
# Expected console output:
# GET /fast took 0.0012 seconds
# GET /slow took 0.5034 seconds
