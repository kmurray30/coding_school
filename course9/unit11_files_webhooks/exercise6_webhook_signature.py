# Verify webhook signatures to prevent tampering.

from fastapi import FastAPI, Request, HTTPException, Header
import hmac
import hashlib
from typing import Optional

app = FastAPI()

# Webhook secret (shared with webhook sender)
WEBHOOK_SECRET = "webhook_secret_shared_with_sender"

def verify_webhook_signature(body: bytes, signature: str) -> bool:
    """Verify HMAC signature"""
    # Compute expected signature
    expected = hmac.new(
        WEBHOOK_SECRET.encode(),
        body,
        hashlib.sha256
    ).hexdigest()
    
    # Compare signatures (timing-safe)
    return hmac.compare_digest(signature, expected)

@app.post("/webhooks/stripe")
async def receive_stripe_webhook(
    request: Request,
    stripe_signature: Optional[str] = Header(None, alias="Stripe-Signature")
):
    """Receive and verify Stripe webhook"""
    # Get raw body (needed for signature verification)
    body = await request.body()
    
    # Verify signature
    if not stripe_signature:
        raise HTTPException(status_code=401, detail="Missing signature")
    
    # Stripe signature format: "t=timestamp,v1=signature"
    # For simplicity, we'll just verify basic HMAC
    
    # In real Stripe webhooks, you'd use stripe.Webhook.construct_event()
    # For this example, we'll verify a simple HMAC
    
    computed_signature = hmac.new(
        WEBHOOK_SECRET.encode(),
        body,
        hashlib.sha256
    ).hexdigest()
    
    # Extract signature from header (simplified)
    # Real Stripe format is more complex
    if not hmac.compare_digest(computed_signature, stripe_signature):
        raise HTTPException(status_code=401, detail="Invalid signature")
    
    # Signature valid - process webhook
    data = await request.json()
    print(f"Verified webhook: {data}")
    
    return {"status": "received and verified"}

@app.post("/webhooks/github-secure")
async def receive_github_webhook_secure(
    request: Request,
    x_hub_signature_256: Optional[str] = Header(None)
):
    """Receive and verify GitHub webhook"""
    body = await request.body()
    
    # GitHub signature format: "sha256=hexdigest"
    if not x_hub_signature_256:
        raise HTTPException(status_code=401, detail="Missing signature")
    
    # Compute expected signature
    expected_signature = "sha256=" + hmac.new(
        WEBHOOK_SECRET.encode(),
        body,
        hashlib.sha256
    ).hexdigest()
    
    # Verify
    if not hmac.compare_digest(expected_signature, x_hub_signature_256):
        raise HTTPException(status_code=401, detail="Invalid signature")
    
    # Process webhook
    data = await request.json()
    print(f"Verified GitHub webhook: {data.get('action')}")
    
    return {"status": "received"}

# Generic signature verification
@app.post("/webhooks/secure")
async def receive_secure_webhook(
    request: Request,
    x_webhook_signature: str = Header(...)
):
    """Generic webhook with signature verification"""
    body = await request.body()
    
    if not verify_webhook_signature(body, x_webhook_signature):
        raise HTTPException(status_code=401, detail="Invalid signature")
    
    data = await request.json()
    return {"status": "verified", "data": data}

# Run with: uvicorn exercise6_webhook_signature:app --reload
#
# Test:
# 1. Compute signature: echo -n '{"test": "data"}' | openssl dgst -sha256 -hmac "webhook_secret_shared_with_sender"
#    → signature: abc123...
#
# 2. Send webhook:
# curl -X POST http://localhost:8000/webhooks/secure \
#   -H "Content-Type: application/json" \
#   -H "X-Webhook-Signature: abc123..." \
#   -d '{"test": "data"}'
#
# 3. Try without signature → 401 Unauthorized
# 4. Try with wrong signature → 401 Unauthorized
#
# Why verify signatures:
# - Prevents attackers from sending fake webhooks
# - Ensures webhook actually came from expected service
# - Prevents webhook replay attacks
#
# All production webhook endpoints MUST verify signatures.
