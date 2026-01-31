# Handle duplicate webhooks with idempotency keys.

from fastapi import FastAPI, Request, HTTPException, Header
from pydantic import BaseModel
from typing import Optional
import redis

app = FastAPI()

# Redis for storing processed webhook IDs
cache = redis.Redis(host='localhost', port=6379, decode_responses=True)

class WebhookEvent(BaseModel):
    event_id: str  # Unique ID for this event
    event_type: str
    data: dict

@app.post("/webhooks/idempotent")
async def receive_idempotent_webhook(event: WebhookEvent):
    """Process webhook only once using event_id"""
    
    # Check if we've already processed this event
    cache_key = f"webhook:processed:{event.event_id}"
    
    if cache.exists(cache_key):
        print(f"Duplicate webhook {event.event_id} - already processed")
        # Return 200 OK (don't make sender think it failed)
        return {"status": "already_processed"}
    
    # Process the webhook
    print(f"Processing new webhook {event.event_id}")
    
    # Do actual work (update database, send email, etc.)
    # ...
    
    # Mark as processed (TTL: 24 hours)
    cache.setex(cache_key, 86400, "processed")
    
    return {"status": "processed"}

# Alternative: Database-based idempotency
from datetime import datetime

# In-memory "database" for example
processed_webhooks = {}

@app.post("/webhooks/db-idempotent")
async def receive_webhook_with_db(event: WebhookEvent):
    """Track processed webhooks in database"""
    
    # Check database
    if event.event_id in processed_webhooks:
        return {"status": "already_processed"}
    
    # Process webhook
    print(f"Processing {event.event_id}")
    
    # Store in database
    processed_webhooks[event.event_id] = {
        "processed_at": datetime.utcnow().isoformat(),
        "event_type": event.event_type
    }
    
    return {"status": "processed"}

# Using request headers for idempotency
@app.post("/webhooks/header-idempotent")
async def receive_webhook_idempotent_header(
    request: Request,
    idempotency_key: Optional[str] = Header(None, alias="Idempotency-Key")
):
    """Use Idempotency-Key header"""
    
    if not idempotency_key:
        raise HTTPException(
            status_code=400,
            detail="Idempotency-Key header required"
        )
    
    cache_key = f"webhook:idempotency:{idempotency_key}"
    
    # Check if already processed
    if cache.exists(cache_key):
        # Return cached result
        cached_result = cache.get(cache_key)
        return {"status": "cached", "result": cached_result}
    
    # Process webhook
    body = await request.json()
    print(f"Processing webhook with key {idempotency_key}")
    
    result = {"processed": True, "data": body}
    
    # Cache result (24 hour TTL)
    import json
    cache.setex(cache_key, 86400, json.dumps(result))
    
    return result

# Run with: uvicorn exercise7_idempotency:app --reload
#
# Test duplicate webhooks:
# 1. POST /webhooks/idempotent {"event_id": "evt_123", "event_type": "test", "data": {}}
#    → {"status": "processed"}
#
# 2. POST same event again
#    → {"status": "already_processed"}
#
# Why idempotency matters:
# - Webhooks can be sent multiple times (network issues, retries)
# - Without idempotency, you might charge customer twice
# - Without idempotency, you might send duplicate emails
# - Idempotent handlers are safe to retry
#
# Implementation strategies:
# 1. Event ID in payload (best - sender provides unique ID)
# 2. Idempotency-Key header (good)
# 3. Hash of payload (okay, but payload might vary slightly)
# 4. Database unique constraint (database enforces uniqueness)
#
# Always make webhook handlers idempotent in production!
