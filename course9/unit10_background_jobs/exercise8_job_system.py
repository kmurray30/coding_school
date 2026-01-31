# Complete background job system with FastAPI and ARQ.

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from arq import create_pool
from arq.connections import RedisSettings, ArqRedis
from arq.jobs import Job
import asyncio
from typing import Optional

app = FastAPI(title="Background Job System")

# Task definitions
async def process_video_task(ctx, video_id: int, resolution: str):
    """Simulates video processing"""
    print(f"Processing video {video_id} to {resolution}")
    await asyncio.sleep(10)  # Simulate processing
    return {
        "video_id": video_id,
        "resolution": resolution,
        "url": f"/videos/{video_id}_{resolution}.mp4",
        "status": "completed"
    }

async def send_notification_task(ctx, user_id: int, message: str):
    """Send push notification"""
    print(f"Sending notification to user {user_id}: {message}")
    await asyncio.sleep(1)
    return {"sent": True}

# Worker settings
redis_settings = RedisSettings(host='localhost', port=6379)

class WorkerSettings:
    functions = [process_video_task, send_notification_task]
    redis_settings = redis_settings
    max_tries = 3
    retry_jobs = True

# Redis pool
redis_pool: Optional[ArqRedis] = None

@app.on_event("startup")
async def startup():
    global redis_pool
    redis_pool = await create_pool(redis_settings)

@app.on_event("shutdown")
async def shutdown():
    if redis_pool:
        await redis_pool.close()

# Pydantic models
class VideoProcessRequest(BaseModel):
    video_id: int
    resolution: str  # "720p", "1080p", "4k"

class JobResponse(BaseModel):
    job_id: str
    status: str

class JobStatusResponse(BaseModel):
    job_id: str
    status: str
    result: Optional[dict] = None
    error: Optional[str] = None

# Endpoints
@app.post("/jobs/process-video", response_model=JobResponse)
async def create_video_job(request: VideoProcessRequest):
    """Queue video processing job"""
    job = await redis_pool.enqueue_job(
        'process_video_task',
        request.video_id,
        request.resolution
    )
    
    return {
        "job_id": job.job_id,
        "status": "queued"
    }

@app.get("/jobs/{job_id}", response_model=JobStatusResponse)
async def get_job_status(job_id: str):
    """Check job status"""
    job = Job(job_id, redis_pool)
    info = await job.info()
    
    if info is None:
        raise HTTPException(status_code=404, detail="Job not found")
    
    status = info.job_status.name if info.job_status else "unknown"
    
    response = {
        "job_id": job_id,
        "status": status.lower()
    }
    
    # Include result if completed
    if status == "complete":
        result = await job.result()
        response["result"] = result
    
    # Include error if failed
    if status == "failed":
        # Get error info (would need to store separately in production)
        response["error"] = "Job failed after retries"
    
    return response

@app.post("/jobs/{job_id}/cancel")
async def cancel_job(job_id: str):
    """Cancel a queued job"""
    job = Job(job_id, redis_pool)
    info = await job.info()
    
    if info is None:
        raise HTTPException(status_code=404, detail="Job not found")
    
    if info.job_status.name != "queued":
        raise HTTPException(status_code=400, detail="Can only cancel queued jobs")
    
    await job.abort()
    return {"message": "Job cancelled", "job_id": job_id}

@app.get("/health")
async def health_check():
    """Check if worker is running"""
    # Try to check worker health
    # In production, you'd query worker status
    return {"status": "healthy", "workers": "check ARQ worker separately"}

# Run worker: arq unit10_background_jobs.exercise8_job_system.WorkerSettings
# Run API: uvicorn exercise8_job_system:app --reload
#
# Test flow:
# 1. POST /jobs/process-video {"video_id": 1, "resolution": "1080p"}
#    → {"job_id": "abc123", "status": "queued"}
#
# 2. GET /jobs/abc123
#    → {"job_id": "abc123", "status": "in_progress"}
#
# 3. Wait 10 seconds
#
# 4. GET /jobs/abc123
#    → {"job_id": "abc123", "status": "complete", "result": {...}}
#
# 5. POST /jobs/abc123/cancel (if still queued)
#    → {"message": "Job cancelled"}
#
# This is a complete job system with:
# - Job creation
# - Status tracking
# - Job cancellation
# - Error handling
# - Retries
