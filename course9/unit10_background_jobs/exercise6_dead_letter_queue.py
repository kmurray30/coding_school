# Handle permanently failed tasks with dead letter queue.

import asyncio
from arq import create_pool
from arq.connections import RedisSettings

# Task that might fail permanently
async def risky_task(ctx, data: dict):
    """Task that validates data and might fail"""
    if not data.get('valid'):
        raise ValueError("Invalid data - will never succeed")
    
    # Process valid data
    await asyncio.sleep(1)
    return {"status": "processed", "data": data}

# Task to handle failures
async def on_job_failure(ctx, job_id: str, error: str, data: dict):
    """Called when a job fails permanently (after all retries)"""
    print(f"Job {job_id} failed permanently!")
    print(f"Error: {error}")
    print(f"Data: {data}")
    
    # Options:
    # 1. Log to error tracking service (Sentry, etc.)
    # 2. Store in database for manual review
    # 3. Send alert to admins
    # 4. Move to dead letter queue for later processing
    
    # For this example, just log it
    # In production, store in database:
    # await ctx['db'].save_failed_job(job_id, error, data)

class WorkerSettings:
    functions = [risky_task]
    redis_settings = RedisSettings()
    
    # Retry configuration
    max_tries = 3
    retry_jobs = True
    
    # Call on_job_failure when job fails after all retries
    on_job_failure = on_job_failure

# Enqueue tasks
async def test_dead_letter():
    redis = await create_pool(RedisSettings())
    
    # This will succeed
    job1 = await redis.enqueue_job('risky_task', {'valid': True, 'id': 1})
    print(f"Valid job: {job1.job_id}")
    
    # This will fail 3 times, then go to dead letter queue
    job2 = await redis.enqueue_job('risky_task', {'valid': False, 'id': 2})
    print(f"Invalid job: {job2.job_id}")
    
    await asyncio.sleep(10)  # Wait for processing
    
    # Check results
    result1 = await job1.result()
    print(f"Job 1 result: {result1}")
    
    result2 = await job2.result()
    print(f"Job 2 result: {result2}")  # Will be None (failed)

# Run worker: arq unit10_background_jobs.exercise6_dead_letter_queue.WorkerSettings
# Run test: python -c "import asyncio; from exercise6_dead_letter_queue import test_dead_letter; asyncio.run(test_dead_letter())"
#
# Expected output:
# - Job 1 processes successfully
# - Job 2 fails, retries 3 times, then calls on_job_failure
# - on_job_failure logs the error for manual review
#
# Dead letter queue pattern:
# - Retries handle transient failures (network issues)
# - After max retries, job goes to dead letter queue
# - Admin can review and fix issues
# - Prevents bad jobs from blocking the queue
