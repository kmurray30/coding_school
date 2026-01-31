# Send webhooks to external services with retry logic.

from fastapi import FastAPI, BackgroundTasks
import httpx
import asyncio
from typing import Dict
from datetime import datetime

app = FastAPI()

# Webhook configuration
WEBHOOK_ENDPOINTS = {
    "customer_created": "https://example.com/webhooks/customer-created",
    "payment_completed": "https://example.com/webhooks/payment"
}

WEBHOOK_SECRET = "shared_secret_with_receiver"

async def send_webhook_with_retry(
    url: str,
    payload: Dict,
    max_retries: int = 3
):
    """Send webhook with exponential backoff retry"""
    
    import hmac
    import hashlib
    import json
    
    # Compute signature
    body = json.dumps(payload)
    signature = hmac.new(
        WEBHOOK_SECRET.encode(),
        body.encode(),
        hashlib.sha256
    ).hexdigest()
    
    headers = {
        "Content-Type": "application/json",
        "X-Webhook-Signature": signature,
        "X-Webhook-Event": payload.get("event_type", "unknown")
    }
    
    for attempt in range(max_retries):
        try:
            print(f"Sending webhook (attempt {attempt + 1}/{max_retries})")
            
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    url,
                    json=payload,
                    headers=headers,
                    timeout=10.0
                )
            
            # Success!
            if 200 <= response.status_code < 300:
                print(f"Webhook delivered successfully: {response.status_code}")
                return {"status": "delivered", "attempt": attempt + 1}
            
            # Non-2xx response
            print(f"Webhook failed with status {response.status_code}")
            
        except httpx.RequestError as e:
            print(f"Webhook request failed: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")
        
        # Exponential backoff before retry
        if attempt < max_retries - 1:
            wait_time = 2 ** attempt  # 1s, 2s, 4s
            print(f"Waiting {wait_time}s before retry...")
            await asyncio.sleep(wait_time)
    
    # All retries failed
    print("Webhook delivery failed after all retries")
    # In production: store in dead letter queue for manual review
    return {"status": "failed", "attempts": max_retries}

@app.post("/customer")
async def create_customer(
    name: str,
    email: str,
    background_tasks: BackgroundTasks
):
    """Create customer and send webhook"""
    
    # Create customer in database
    customer = {
        "id": 123,
        "name": name,
        "email": email,
        "created_at": datetime.utcnow().isoformat()
    }
    
    # Queue webhook to be sent in background
    webhook_payload = {
        "event_type": "customer.created",
        "event_id": f"evt_{customer['id']}_{int(datetime.utcnow().timestamp())}",
        "data": customer
    }
    
    background_tasks.add_task(
        send_webhook_with_retry,
        WEBHOOK_ENDPOINTS["customer_created"],
        webhook_payload
    )
    
    return {"customer": customer, "webhook": "queued"}

@app.post("/payment")
async def process_payment(
    amount: float,
    customer_id: int,
    background_tasks: BackgroundTasks
):
    """Process payment and send webhook"""
    
    payment = {
        "id": 456,
        "amount": amount,
        "customer_id": customer_id,
        "status": "completed",
        "timestamp": datetime.utcnow().isoformat()
    }
    
    webhook_payload = {
        "event_type": "payment.completed",
        "event_id": f"evt_payment_{payment['id']}",
        "data": payment
    }
    
    background_tasks.add_task(
        send_webhook_with_retry,
        WEBHOOK_ENDPOINTS["payment_completed"],
        webhook_payload
    )
    
    return {"payment": payment, "webhook": "queued"}

# Run with: uvicorn exercise8_webhook_retry:app --reload
#
# Test:
# POST /customer?name=Alice&email=alice@example.com
#   → Creates customer, queues webhook
#   → Watch terminal for retry attempts
#
# Webhook sending best practices:
# ✅ Send in background (don't block request)
# ✅ Retry with exponential backoff
# ✅ Set reasonable timeouts
# ✅ Sign webhooks (so receiver can verify)
# ✅ Include event ID (for idempotency)
# ✅ Log all webhook attempts
# ❌ Don't retry infinitely (use dead letter queue)
# ❌ Don't send webhooks synchronously (slow)
#
# Webhook reliability:
# - Transient failures: Network issues, receiver temporarily down → Retry
# - Permanent failures: Wrong URL, receiver shut down → Dead letter queue
# - Track delivery success rate in production
