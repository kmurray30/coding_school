# Dependencies are reusable functions that run before route handlers.
# Use Depends() to inject them.

from fastapi import FastAPI, Depends
from datetime import datetime

app = FastAPI()

def get_current_timestamp():
    """Dependency that returns current timestamp"""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

@app.get("/")
def read_root(timestamp: str = Depends(get_current_timestamp)):
    # FastAPI calls get_current_timestamp() and injects the result
    return {"message": "hello", "timestamp": timestamp}

# Create a dependency that returns a random number between 1 and 100
# Inject it into a route handler

def get_random_number():
    ...

@app.get("/random")
def random_endpoint(...):
    ...

# Run with: uvicorn exercise6_simple_dependency:app --reload
#
# Expected:
# GET / → {"message": "hello", "timestamp": "2024-01-15 14:23:45"}
# GET /random → {"number": 42, "timestamp": "2024-01-15 14:23:46"}
