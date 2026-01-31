# Implement CRUD operations using different HTTP methods.
# GET = read, POST = create, PUT = update, DELETE = delete

from fastapi import FastAPI

app = FastAPI()

# In-memory storage for this exercise
tasks = {}
task_id_counter = 1

# Create: POST /tasks
# Accept a task name and add it to storage
# Return the created task with its ID

# Read: GET /tasks/{task_id}
# Return the task with the given ID
# If not found, return {"error": "task not found"}

# Update: PUT /tasks/{task_id}
# Accept a new task name and update the task
# Return the updated task

# Delete: DELETE /tasks/{task_id}
# Remove the task from storage
# Return {"message": "deleted"}

...

# Run with: uvicorn exercise5_http_methods:app --reload
# Test in /docs
#
# Expected flow:
# POST /tasks with {"name": "learn fastapi"} → {"id": 1, "name": "learn fastapi"}
# GET /tasks/1 → {"id": 1, "name": "learn fastapi"}
# PUT /tasks/1 with {"name": "master fastapi"} → {"id": 1, "name": "master fastapi"}
# DELETE /tasks/1 → {"message": "deleted"}
