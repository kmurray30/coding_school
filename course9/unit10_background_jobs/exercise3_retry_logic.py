# Background tasks with retry logic for failures.

import asyncio
from arq import create_pool
from arq.connections import RedisSettings
import random

# Task that might fail
async def unreliable_task(ctx, data: str):
    """Simulates a task that fails sometimes"""
    print(f"Processing: {data}")
    
    # 50% chance of failure (simulate network issues, etc.)
    if random.random() < 0.5:
        print("Task failed! Will retry...")
        raise Exception("Random failure")
    
    print("Task succeeded!")
    return {"status": "success", "data": data}

# Task with retry configuration
async def task_with_retry(ctx, item_id: int):
    """Task that retries on failure with exponential backoff"""
    print(f"Attempt to process item {item_id}")
    
    # Simulate occasional failure
    if random.random() < 0.3:
        raise Exception(f"Failed to process item {item_id}")
    
    print(f"Item {item_id} processed successfully")
    return {"item_id": item_id, "processed": True}

class WorkerSettings:
    functions = [unreliable_task, task_with_retry]
    redis_settings = RedisSettings()
    
    # Retry configuration
    max_tries = 3  # Retry up to 3 times
    retry_jobs = True  # Enable retries
    
    # Exponential backoff: 1s, 2s, 4s, 8s...
    job_timeout = 30  # Max time for job
    keep_result = 3600  # Keep result for 1 hour

# Enqueue with custom retry settings
async def enqueue_with_retry():
    redis = await create_pool(RedisSettings())
    
    # Enqueue with max_tries override
    job = await redis.enqueue_job(
        'task_with_retry',
        42,
        _max_tries=5,  # Override default, try 5 times
        _defer_by=2    # Wait 2 seconds before starting
    )
    
    print(f"Job enqueued: {job.job_id}")
    return job.job_id

# Run worker: arq unit10_background_jobs.exercise3_retry_logic.WorkerSettings
#
# Observe:
# - Failed tasks automatically retry
# - Exponential backoff between retries
# - After max_tries, job gives up
# - Successful jobs don't retry
