# Track requests across services with correlation IDs.

from fastapi import FastAPI, Request
import uuid
import logging
import json
from datetime import datetime

app = FastAPI()

# Structured logger
class StructuredLogger:
    @staticmethod
    def log(level: str, message: str, **context):
        log_entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "level": level,
            "message": message,
            **context
        }
        print(json.dumps(log_entry))

logger = StructuredLogger()

@app.middleware("http")
async def add_correlation_id(request: Request, call_next):
    # Generate or extract correlation ID
    correlation_id = request.headers.get("X-Correlation-ID", str(uuid.uuid4()))
    
    # Attach to request state
    request.state.correlation_id = correlation_id
    
    # Log request with correlation ID
    logger.log(
        "INFO",
        "Request started",
        correlation_id=correlation_id,
        method=request.method,
        path=request.url.path
    )
    
    # Process request
    response = await call_next(request)
    
    # Add correlation ID to response headers
    response.headers["X-Correlation-ID"] = correlation_id
    
    # Log response
    logger.log(
        "INFO",
        "Request completed",
        correlation_id=correlation_id,
        status_code=response.status_code
    )
    
    return response

@app.get("/users/{user_id}")
def get_user(user_id: int, request: Request):
    # All logs in this request include correlation_id
    correlation_id = request.state.correlation_id
    
    logger.log("DEBUG", "Querying database", correlation_id=correlation_id, user_id=user_id)
    
    # Simulate database query
    logger.log("DEBUG", "Query successful", correlation_id=correlation_id, rows=1)
    
    return {"user_id": user_id, "name": "Alice"}

@app.post("/orders")
def create_order(request: Request):
    correlation_id = request.state.correlation_id
    
    logger.log("INFO", "Creating order", correlation_id=correlation_id)
    
    # Step 1: Validate inventory
    logger.log("DEBUG", "Checking inventory", correlation_id=correlation_id)
    
    # Step 2: Process payment
    logger.log("DEBUG", "Processing payment", correlation_id=correlation_id)
    
    # Step 3: Create order
    logger.log("INFO", "Order created", correlation_id=correlation_id, order_id=123)
    
    return {"order_id": 123}

# Run with: uvicorn exercise3_correlation_ids:app --reload
#
# Test:
# curl http://localhost:8000/users/1
#   → Response includes X-Correlation-ID header
#   → All logs for this request have same correlation_id
#
# curl -H "X-Correlation-ID: my-trace-123" http://localhost:8000/orders
#   → Uses provided correlation ID
#
# Benefits:
# - Trace single request across all services
# - Find all logs related to one request
# - Debug distributed systems
#
# Example: User reports error at 2:30 PM
# 1. Find correlation_id from user's request
# 2. Search logs for that correlation_id
# 3. See all operations for that request
# 4. Find where it failed
