# Idempotency keys for safe retries of critical operations.

from fastapi import FastAPI, HTTPException, Header
from pydantic import BaseModel
import redis
from typing import Optional
import json

app = FastAPI()

cache = redis.Redis(host='localhost', port=6379, decode_responses=True)

class PaymentRequest(BaseModel):
    amount: float
    customer_id: int
    description: str

@app.post("/payments")
def process_payment(
    payment: PaymentRequest,
    idempotency_key: str = Header(...)
):
    """Process payment with idempotency key"""
    
    cache_key = f"payment:idempotency:{idempotency_key}"
    
    # Check if already processed
    cached_result = cache.get(cache_key)
    if cached_result:
        # Return cached result (same response for duplicate requests)
        print(f"Duplicate request detected: {idempotency_key}")
        return json.loads(cached_result)
    
    # Validate amount
    if payment.amount <= 0:
        raise HTTPException(status_code=400, detail="invalid amount")
    
    # Process payment (expensive operation!)
    print(f"Processing payment: ${payment.amount}")
    payment_id = 12345  # Simulated
    
    # Store result in cache (24 hour TTL)
    result = {
        "payment_id": payment_id,
        "amount": payment.amount,
        "status": "completed"
    }
    cache.setex(cache_key, 86400, json.dumps(result))
    
    return result

# Run with: uvicorn exercise5_idempotency_keys:app --reload
#
# Test:
# 1. POST /payments with header "Idempotency-Key: abc123"
#    {"amount": 100.0, "customer_id": 1, "description": "test"}
#    → {"payment_id": 12345, "amount": 100.0, "status": "completed"}
#
# 2. POST same request again (network retry)
#    → Same response (payment not processed twice!)
#
# 3. POST with different Idempotency-Key
#    → New payment processed
#
# Why idempotency keys matter:
# - Network issues cause retries
# - Without idempotency: charge customer twice
# - With idempotency: safe to retry
#
# Critical for:
# - Payments
# - Order creation
# - Any operation that shouldn't happen twice
#
# Implementation:
# ✅ Client generates unique key (UUID)
# ✅ Server checks if key was used before
# ✅ Server returns cached result for duplicate keys
# ✅ Keys expire after reasonable time (24 hours)
