# Simple background task with ARQ (async task queue for Python).

import asyncio
from arq import create_pool
from arq.connections import RedisSettings

# Background task function
async def send_email_task(ctx, to: str, subject: str, body: str):
    """Simulates sending an email"""
    print(f"Sending email to {to}")
    print(f"Subject: {subject}")
    print(f"Body: {body}")
    
    # Simulate email sending delay
    await asyncio.sleep(2)
    
    print(f"Email sent to {to}!")
    return {"status": "sent", "to": to}

# Worker class
class WorkerSettings:
    functions = [send_email_task]
    redis_settings = RedisSettings(host='localhost', port=6379)

# Enqueue tasks (in your FastAPI app)
async def enqueue_email():
    redis = await create_pool(RedisSettings(host='localhost', port=6379))
    
    # Enqueue the task
    job = await redis.enqueue_job('send_email_task', 
                                    'user@example.com',
                                    'Welcome!',
                                    'Thanks for signing up!')
    
    print(f"Job enqueued: {job.job_id}")
    return job.job_id

# To run:
# 1. Start worker in terminal: arq unit10_background_jobs.exercise2_simple_task.WorkerSettings
# 2. Run this to enqueue: python -c "import asyncio; from exercise2_simple_task import enqueue_email; asyncio.run(enqueue_email())"
#
# Expected:
# Worker terminal shows: "Sending email...", "Email sent!"
# Task runs in background, not blocking main process
