# Rate limiting to prevent brute force and abuse.

from fastapi import FastAPI, HTTPException, Request
from collections import defaultdict
from datetime import datetime, timedelta
import time

app = FastAPI()

# Simple in-memory rate limiter (use Redis in production)
class RateLimiter:
    def __init__(self):
        self.requests = defaultdict(list)  # IP → list of timestamps
    
    def is_allowed(self, key: str, max_requests: int, window_seconds: int) -> bool:
        """Check if request is allowed"""
        now = time.time()
        cutoff = now - window_seconds
        
        # Remove old requests
        self.requests[key] = [
            timestamp for timestamp in self.requests[key]
            if timestamp > cutoff
        ]
        
        # Check if under limit
        if len(self.requests[key]) >= max_requests:
            return False
        
        # Allow and record
        self.requests[key].append(now)
        return True

rate_limiter = RateLimiter()

# Rate limit login attempts (strict)
@app.post("/login")
async def login(username: str, password: str, request: Request):
    client_ip = request.client.host
    
    # Allow 5 login attempts per minute per IP
    if not rate_limiter.is_allowed(f"login:{client_ip}", max_requests=5, window_seconds=60):
        raise HTTPException(
            status_code=429,
            detail="Too many login attempts. Try again in 1 minute."
        )
    
    # Process login...
    return {"message": "login processed"}

# Rate limit API calls (relaxed)
@app.get("/api/data")
async def get_data(request: Request):
    client_ip = request.client.host
    
    # Allow 100 requests per minute per IP
    if not rate_limiter.is_allowed(f"api:{client_ip}", max_requests=100, window_seconds=60):
        raise HTTPException(
            status_code=429,
            detail="Rate limit exceeded. Max 100 requests per minute."
        )
    
    return {"data": "some data"}

# Rate limit per user (not just IP)
@app.post("/send-email")
async def send_email(email: str, request: Request):
    # Rate limit by email address
    if not rate_limiter.is_allowed(f"email:{email}", max_requests=3, window_seconds=3600):
        raise HTTPException(
            status_code=429,
            detail="You can only send 3 emails per hour."
        )
    
    # Send email...
    return {"message": "email sent"}

# Run with: uvicorn exercise4_rate_limiting:app --reload
#
# Test:
# 1. POST /login 5 times quickly → Last one succeeds
# 2. POST /login 6th time → 429 Too Many Requests
# 3. Wait 60 seconds → POST /login works again
#
# Rate limiting strategies:
# - Per IP: Prevent single attacker
# - Per user: Prevent abuse by authenticated users
# - Per endpoint: Different limits for different sensitivity
# - Sliding window: More sophisticated than fixed window
#
# Production:
# - Use Redis for distributed rate limiting
# - Return Retry-After header
# - Log rate limit violations
# - Alert on suspicious patterns
# - Consider using library like slowapi
