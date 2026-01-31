# Health check endpoints for monitoring and load balancers.

from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine, text
import redis

app = FastAPI()

# Database and cache connections
db_engine = create_engine('sqlite:///./health.db')
cache = redis.Redis(host='localhost', port=6379, decode_responses=True)

@app.get("/health")
def health_check():
    """Basic health check - is app running?"""
    return {"status": "healthy"}

@app.get("/health/detailed")
def detailed_health():
    """Detailed health check - check dependencies"""
    health_status = {
        "status": "healthy",
        "checks": {}
    }
    
    # Check database
    try:
        with db_engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        health_status["checks"]["database"] = "healthy"
    except Exception as e:
        health_status["checks"]["database"] = f"unhealthy: {str(e)}"
        health_status["status"] = "unhealthy"
    
    # Check Redis
    try:
        cache.ping()
        health_status["checks"]["redis"] = "healthy"
    except Exception as e:
        health_status["checks"]["redis"] = f"unhealthy: {str(e)}"
        health_status["status"] = "unhealthy"
    
    # Return 503 if unhealthy
    if health_status["status"] == "unhealthy":
        raise HTTPException(status_code=503, detail=health_status)
    
    return health_status

@app.get("/health/ready")
def readiness_check():
    """Readiness: Can app handle requests?"""
    # Check if app is ready (DB migrated, cache warm, etc.)
    try:
        with db_engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        cache.ping()
        return {"status": "ready"}
    except Exception:
        raise HTTPException(status_code=503, detail={"status": "not ready"})

@app.get("/health/live")
def liveness_check():
    """Liveness: Is app alive (not deadlocked)?"""
    # Simple check - if this responds, app is alive
    return {"status": "alive"}

# Run with: uvicorn exercise5_health_check:app --reload
#
# Test:
# GET /health → 200 OK (basic check)
# GET /health/detailed → 200 OK with dependency status
# GET /health/ready → 200 if ready, 503 if not
# GET /health/live → 200 if alive
#
# Readiness vs Liveness (Kubernetes):
# - Readiness: Should load balancer send traffic?
#   - Not ready during startup (migrations running)
#   - Not ready if dependencies down
# - Liveness: Should Kubernetes restart the pod?
#   - Unhealthy if app deadlocked/crashed
#   - Usually just "does it respond?"
#
# Load balancer usage:
# - LB pings /health every 5 seconds
# - If 3 failures → remove from pool
# - Prevents sending traffic to dead servers
