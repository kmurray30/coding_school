# Receive webhooks from external services.

from fastapi import FastAPI, Request, HTTPException
from pydantic import BaseModel
import json

app = FastAPI()

# Webhook event from payment processor
class PaymentWebhook(BaseModel):
    event_type: str
    payment_id: str
    amount: float
    status: str
    customer_id: str

@app.post("/webhooks/payments")
async def receive_payment_webhook(webhook: PaymentWebhook):
    """Receive payment status updates from payment processor"""
    print(f"Received webhook: {webhook.event_type}")
    
    # Handle different event types
    if webhook.event_type == "payment.succeeded":
        print(f"Payment {webhook.payment_id} succeeded: ${webhook.amount}")
        # Update database, send confirmation email, etc.
        
    elif webhook.event_type == "payment.failed":
        print(f"Payment {webhook.payment_id} failed")
        # Notify customer, retry, etc.
        
    elif webhook.event_type == "payment.refunded":
        print(f"Payment {webhook.payment_id} refunded: ${webhook.amount}")
        # Process refund
    
    # ALWAYS return 200 OK quickly
    # Process webhook data asynchronously if needed
    return {"status": "received"}

# Generic webhook receiver (when schema varies)
@app.post("/webhooks/generic")
async def receive_generic_webhook(request: Request):
    """Receive webhooks with unknown schema"""
    # Get raw body
    body = await request.body()
    print(f"Raw webhook body: {body}")
    
    # Parse JSON
    try:
        data = json.loads(body)
    except json.JSONDecodeError:
        raise HTTPException(status_code=400, detail="Invalid JSON")
    
    # Log webhook for debugging
    print(f"Webhook data: {data}")
    
    # Store in database for processing
    # webhook_store.save(data)
    
    return {"status": "received"}

# Webhook for GitHub events
@app.post("/webhooks/github")
async def receive_github_webhook(request: Request):
    """Receive GitHub webhook events"""
    # GitHub sends event type in header
    event_type = request.headers.get("X-GitHub-Event")
    
    body = await request.json()
    
    print(f"GitHub event: {event_type}")
    
    if event_type == "push":
        # Code was pushed
        repo = body["repository"]["name"]
        pusher = body["pusher"]["name"]
        print(f"{pusher} pushed to {repo}")
        
    elif event_type == "pull_request":
        # PR opened/closed
        action = body["action"]
        pr_number = body["number"]
        print(f"PR #{pr_number} was {action}")
    
    return {"status": "received"}

# Run with: uvicorn exercise5_webhook_endpoint:app --reload
#
# Test with curl:
# curl -X POST http://localhost:8000/webhooks/payments \
#   -H "Content-Type: application/json" \
#   -d '{"event_type": "payment.succeeded", "payment_id": "pay_123", "amount": 99.99, "status": "completed", "customer_id": "cust_456"}'
#
# Webhook best practices:
# ✅ Return 200 OK immediately (don't make sender wait)
# ✅ Process webhook asynchronously (background job)
# ✅ Verify webhook signatures (next exercise)
# ✅ Handle idempotency (same webhook sent twice)
# ✅ Log all webhooks for debugging
# ❌ Don't process inline (slow webhooks timeout and retry)
