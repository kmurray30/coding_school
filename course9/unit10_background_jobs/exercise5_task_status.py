# Check status of background jobs.

from fastapi import FastAPI
from arq import create_pool
from arq.connections import RedisSettings, ArqRedis
from arq.jobs import Job
import asyncio

app = FastAPI()

# Task that takes a while
async def long_running_task(ctx, data: str):
    """Simulates a task that takes 10 seconds"""
    await asyncio.sleep(10)
    return {"result": f"Processed: {data}"}

# ARQ settings
redis_settings = RedisSettings(host='localhost', port=6379)

class WorkerSettings:
    functions = [long_running_task]
    redis_settings = redis_settings

# Global redis pool
redis_pool: ArqRedis = None

@app.on_event("startup")
async def startup():
    global redis_pool
    redis_pool = await create_pool(redis_settings)

@app.on_event("shutdown")
async def shutdown():
    await redis_pool.close()

@app.post("/tasks")
async def create_task(data: str):
    """Enqueue a task and return task ID"""
    job = await redis_pool.enqueue_job('long_running_task', data)
    return {"task_id": job.job_id, "status": "queued"}

@app.get("/tasks/{task_id}")
async def get_task_status(task_id: str):
    """Check status of a task"""
    job = Job(task_id, redis_pool)
    info = await job.info()
    
    if info is None:
        return {"task_id": task_id, "status": "not found"}
    
    status = info.job_status.name if info.job_status else "unknown"
    
    result = {
        "task_id": task_id,
        "status": status,
        "enqueue_time": str(info.enqueue_time) if info.enqueue_time else None
    }
    
    # If job finished, include result
    if status == "complete":
        job_result = await job.result()
        result["result"] = job_result
    
    return result

# Run worker: arq unit10_background_jobs.exercise5_task_status.WorkerSettings
# Run API: uvicorn exercise5_task_status:app --reload
#
# Test flow:
# 1. POST /tasks?data=test
#    → Returns {"task_id": "abc123", "status": "queued"}
# 
# 2. GET /tasks/abc123 immediately
#    → {"status": "in_progress", ...}
#
# 3. GET /tasks/abc123 after 10 seconds
#    → {"status": "complete", "result": {...}}
#
# This is how you track long-running jobs!
