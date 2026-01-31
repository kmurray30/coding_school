# CORS middleware lets browsers call your API from different domains.
# Without it, browser security blocks cross-origin requests.

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React apps often run on 3000
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

@app.get("/api/data")
def get_data():
    return {"message": "CORS is enabled, browsers can access this"}

# Run with: uvicorn exercise1_cors_middleware:app --reload
# 
# Test CORS in browser console (open any webpage):
# fetch('http://localhost:8000/api/data')
#   .then(r => r.json())
#   .then(console.log)
#
# Without CORS middleware, this would fail with a CORS error.
# With it, you'll see the response.
#
# Expected: {"message": "CORS is enabled, browsers can access this"}
