# Capture exceptions with context for error tracking.

from fastapi import FastAPI, Request, HTTPException
from datetime import datetime
import traceback
import json

app = FastAPI()

class ErrorTracker:
    """Simulates error tracking service (like Sentry)"""
    
    @staticmethod
    def capture_exception(exc: Exception, context: dict = None):
        """Capture exception with context"""
        error_data = {
            "timestamp": datetime.utcnow().isoformat(),
            "exception_type": type(exc).__name__,
            "exception_message": str(exc),
            "traceback": traceback.format_exc(),
            "context": context or {}
        }
        
        # In production, send to error tracking service (Sentry, Rollbar, etc.)
        # For now, just print
        print("\n=== ERROR CAPTURED ===")
        print(json.dumps(error_data, indent=2))
        print("======================\n")
        
        return error_data

error_tracker = ErrorTracker()

@app.middleware("http")
async def error_tracking_middleware(request: Request, call_next):
    """Catch and log all unhandled exceptions"""
    try:
        response = await call_next(request)
        return response
    except Exception as exc:
        # Capture exception with request context
        error_tracker.capture_exception(exc, context={
            "request_method": request.method,
            "request_url": str(request.url),
            "request_headers": dict(request.headers),
            "client_ip": request.client.host if request.client else None
        })
        
        # Re-raise to let FastAPI handle the response
        raise

@app.get("/error-example")
def trigger_error():
    """Endpoint that raises an error"""
    # This error will be captured with full context
    raise ValueError("Something went wrong!")

@app.get("/divide/{a}/{b}")
def divide(a: int, b: int, request: Request):
    """Endpoint that might raise ZeroDivisionError"""
    try:
        result = a / b
        return {"result": result}
    except ZeroDivisionError as e:
        # Capture error with custom context
        error_tracker.capture_exception(e, context={
            "operation": "division",
            "operand_a": a,
            "operand_b": b,
            "user_id": request.state.get("user_id"),  # If you have auth
            "correlation_id": request.state.get("correlation_id")
        })
        raise HTTPException(status_code=400, detail="Cannot divide by zero")

@app.post("/process-data")
async def process_data(data: dict):
    """Process data with error tracking"""
    try:
        # Simulate processing
        if not data.get("valid"):
            raise ValueError("Invalid data structure")
        
        # Process...
        return {"status": "processed"}
    
    except Exception as e:
        # Capture with relevant context
        error_tracker.capture_exception(e, context={
            "function": "process_data",
            "data_keys": list(data.keys()),
            "data_size": len(str(data))
        })
        raise

# Run with: uvicorn exercise7_error_tracking:app --reload
#
# Test:
# GET /error-example → Error captured with full request context
# GET /divide/10/0 → ZeroDivisionError captured with operands
# POST /process-data {"invalid": true} → ValueError captured
#
# Error context should include:
# ✅ Exception type and message
# ✅ Full stack trace
# ✅ Request details (URL, method, headers)
# ✅ User context (if authenticated)
# ✅ Custom context (operation-specific data)
# ✅ Timestamp
# ✅ Environment (production, staging, etc.)
#
# Error tracking services (Sentry, Rollbar):
# - Aggregate similar errors
# - Track error frequency/trends
# - Alert on new errors
# - Show affected users
# - Provide context for debugging
