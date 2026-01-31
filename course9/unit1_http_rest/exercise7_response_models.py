# Response models ensure your API returns consistent, typed responses.
# Run with: uvicorn exercise7_response_models:app --reload
# Visit http://localhost:8000/...

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Task(BaseModel):
    id: int
    title: str
    completed: bool

# Create an endpoint that returns a Task object
# Use response_model to specify the return type

@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    return Task(id=task_id, title="Sample task", completed=False)

# Create a UserResponse model with id, username, and created_at (str)
# Make an endpoint that returns a UserResponse
# The response_model ensures only specified fields are returned (useful for hiding passwords)

...

# Expected:
# GET /tasks/1 → {"id": 1, "title": "Sample task", "completed": false}
# GET /users/1 → {"id": 1, "username": "alice", "created_at": "2024-01-15"}
#
# Response models auto-validate output and appear in API docs
