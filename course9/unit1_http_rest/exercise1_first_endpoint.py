# Your first FastAPI endpoint. Run with: uvicorn exercise1_first_endpoint:app --reload
# Visit http://localhost:8000 in your browser

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI!"}

# Expected output when you visit http://localhost:8000:
# {"message": "Hello from FastAPI!"}

# Visit http://localhost:8000/docs to see automatic API documentation
