# Complete system: file uploads with webhook notifications.

from fastapi import FastAPI, File, UploadFile, HTTPException, BackgroundTasks, Request
from pydantic import BaseModel
from pathlib import Path
import hmac
import hashlib
import httpx
from datetime import datetime
from typing import Optional

app = FastAPI(title="File Upload & Webhook System")

# Configuration
UPLOAD_DIR = Path("./uploads")
UPLOAD_DIR.mkdir(exist_ok=True)
WEBHOOK_SECRET = "shared_secret"
WEBHOOK_URL = "http://localhost:8001/webhooks/file-processed"

# File processing simulation
async def process_file_task(filename: str, file_id: str):
    """Simulate file processing (resize, scan, etc.)"""
    print(f"Processing file: {filename}")
    
    # Simulate processing time
    import asyncio
    await asyncio.sleep(3)
    
    print(f"File processed: {filename}")
    
    # Send webhook notification
    await send_webhook({
        "event_type": "file.processed",
        "event_id": f"evt_{file_id}",
        "data": {
            "file_id": file_id,
            "filename": filename,
            "status": "processed",
            "processed_at": datetime.utcnow().isoformat()
        }
    })

async def send_webhook(payload: dict):
    """Send webhook with signature"""
    import json
    
    body = json.dumps(payload)
    signature = hmac.new(
        WEBHOOK_SECRET.encode(),
        body.encode(),
        hashlib.sha256
    ).hexdigest()
    
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                WEBHOOK_URL,
                json=payload,
                headers={"X-Webhook-Signature": signature},
                timeout=10.0
            )
            print(f"Webhook sent: {response.status_code}")
    except Exception as e:
        print(f"Webhook failed: {e}")

@app.post("/upload")
async def upload_file(
    file: UploadFile = File(...),
    background_tasks: BackgroundTasks = None
):
    """Upload file and process in background"""
    
    # Validate
    MAX_SIZE = 10 * 1024 * 1024  # 10MB
    contents = await file.read()
    
    if len(contents) > MAX_SIZE:
        raise HTTPException(status_code=400, detail="File too large")
    
    # Save file
    file_id = f"file_{int(datetime.utcnow().timestamp())}"
    file_path = UPLOAD_DIR / f"{file_id}_{file.filename}"
    
    with open(file_path, "wb") as f:
        f.write(contents)
    
    # Queue processing
    if background_tasks:
        background_tasks.add_task(process_file_task, file.filename, file_id)
    
    return {
        "file_id": file_id,
        "filename": file.filename,
        "size": len(contents),
        "status": "processing",
        "message": "File uploaded, processing started"
    }

# Webhook receiver (for testing - run on separate port)
@app.post("/webhooks/file-processed")
async def receive_file_webhook(
    request: Request,
    x_webhook_signature: str = None
):
    """Receive webhook notification"""
    
    body = await request.body()
    
    # Verify signature
    if x_webhook_signature:
        expected = hmac.new(
            WEBHOOK_SECRET.encode(),
            body,
            hashlib.sha256
        ).hexdigest()
        
        if not hmac.compare_digest(expected, x_webhook_signature):
            raise HTTPException(status_code=401, detail="Invalid signature")
    
    data = await request.json()
    
    print(f"Received webhook: {data['event_type']}")
    print(f"File processed: {data['data']['filename']}")
    
    # In production:
    # - Update database
    # - Send email to user
    # - Trigger next step in workflow
    
    return {"status": "received"}

# Run with: uvicorn exercise9_file_webhook_system:app --reload
#
# Test flow:
# 1. POST /upload with file
#    → File saved, returns {"file_id": "...", "status": "processing"}
#
# 2. Wait 3 seconds (processing)
#
# 3. Webhook sent to /webhooks/file-processed
#    → Signature verified, notification logged
#
# Production enhancements:
# - Store file metadata in database
# - Use S3 for file storage
# - Queue processing with ARQ/Celery
# - Send webhook to external URL
# - Generate signed download URLs
# - Track file processing status
# - Send email when processing completes
