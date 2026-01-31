# Path parameters let you capture values from the URL.

from fastapi import FastAPI

app = FastAPI()

@app.get("/users/{user_id}")
def get_user(user_id: int):
    # Extract user_id from the URL path
    return {"user_id": user_id, "name": f"User #{user_id}"}

# Add another endpoint that accepts a username in the path
# Return the username and a welcome message

@app.get("/greet/...")
def greet_user(...):
    ...

# Run with: uvicorn exercise3_path_parameters:app --reload
# 
# Expected:
# GET /users/5 → {"user_id": 5, "name": "User #5"}
# GET /greet/alice → {"username": "alice", "message": "Welcome, alice!"}
