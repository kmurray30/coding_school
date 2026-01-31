# Trigger background jobs from FastAPI endpoints.

from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel
import time

app = FastAPI()

# Simple background task (using FastAPI's BackgroundTasks)
def send_email_simple(email: str, message: str):
    """Simple background task that runs after response is sent"""
    print(f"Sending email to {email}...")
    time.sleep(2)  # Simulate email sending
    print(f"Email sent to {email}: {message}")

class EmailRequest(BaseModel):
    to: str
    subject: str
    body: str

@app.post("/send-email")
def send_email_endpoint(
    email: EmailRequest,
    background_tasks: BackgroundTasks
):
    # Add task to run in background
    background_tasks.add_task(
        send_email_simple,
        email.to,
        f"{email.subject}: {email.body}"
    )
    
    # Response returns immediately (before email is sent)
    return {"message": "email queued", "to": email.to}

# Background task for file processing
def process_file(filename: str):
    print(f"Processing file: {filename}")
    time.sleep(5)  # Simulate heavy processing
    print(f"File {filename} processed!")

@app.post("/upload")
def upload_file(filename: str, background_tasks: BackgroundTasks):
    # Queue file processing in background
    background_tasks.add_task(process_file, filename)
    
    return {"message": "file uploaded", "processing": "in background"}

# Multiple background tasks
@app.post("/register")
def register_user(username: str, email: str, background_tasks: BackgroundTasks):
    # Add multiple background tasks
    background_tasks.add_task(send_email_simple, email, "Welcome!")
    background_tasks.add_task(send_email_simple, "admin@example.com", f"New user: {username}")
    
    return {"message": "registered", "username": username}

# Run with: uvicorn exercise4_task_from_api:app --reload
#
# Test:
# POST /send-email {"to": "user@example.com", "subject": "Test", "body": "Hello"}
#   → Returns immediately
#   → Email sends in background (watch terminal)
#
# POST /upload?filename=data.csv
#   → Returns immediately
#   → File processes in background
#
# Note: FastAPI BackgroundTasks are simple but limited:
# - No retries
# - No persistence (lost if server crashes)
# - For real production, use ARQ/Celery
