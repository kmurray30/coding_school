# Production API with full observability: logging, metrics, health checks.

from fastapi import FastAPI, Request, Depends
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker, Session
import uuid
import json
import time
from datetime import datetime

app = FastAPI(title="Observable API")

# Database
engine = create_engine('sqlite:///./observable.db')
Base = declarative_base()

class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))

Base.metadata.create_all(engine)
SessionLocal = sessionmaker(bind=engine)

# Structured logger
class Logger:
    @staticmethod
    def log(level: str, message: str, **context):
        log_entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "level": level,
            "message": message,
            **context
        }
        print(json.dumps(log_entry))

logger = Logger()

# Metrics (in-memory for demo, use Prometheus client in production)
metrics = {
    "requests_total": 0,
    "errors_total": 0,
    "request_duration_sum": 0.0
}

@app.middleware("http")
async def observability_middleware(request: Request, call_next):
    """Add correlation ID, logging, and timing"""
    # Correlation ID
    correlation_id = request.headers.get("X-Correlation-ID", str(uuid.uuid4()))
    request.state.correlation_id = correlation_id
    
    # Start timer
    start_time = time.time()
    
    # Log request
    logger.log(
        "INFO",
        "Request started",
        correlation_id=correlation_id,
        method=request.method,
        path=request.url.path,
        client_ip=request.client.host if request.client else None
    )
    
    # Process request
    try:
        response = await call_next(request)
        
        # Calculate duration
        duration = time.time() - start_time
        
        # Update metrics
        metrics["requests_total"] += 1
        metrics["request_duration_sum"] += duration
        
        # Log response
        logger.log(
            "INFO",
            "Request completed",
            correlation_id=correlation_id,
            status_code=response.status_code,
            duration_ms=round(duration * 1000, 2)
        )
        
        # Add headers
        response.headers["X-Correlation-ID"] = correlation_id
        response.headers["X-Response-Time"] = f"{duration:.3f}s"
        
        return response
    
    except Exception as e:
        # Log error
        metrics["errors_total"] += 1
        logger.log(
            "ERROR",
            "Request failed",
            correlation_id=correlation_id,
            error=str(e),
            error_type=type(e).__name__
        )
        raise

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/items")
def list_items(request: Request, db: Session = Depends(get_db)):
    correlation_id = request.state.correlation_id
    
    logger.log("DEBUG", "Listing items", correlation_id=correlation_id)
    items = db.query(Item).all()
    
    logger.log("DEBUG", "Items retrieved", correlation_id=correlation_id, count=len(items))
    
    return {"items": [{"id": i.id, "name": i.name} for i in items]}

@app.post("/items")
def create_item(name: str, request: Request, db: Session = Depends(get_db)):
    correlation_id = request.state.correlation_id
    
    logger.log("INFO", "Creating item", correlation_id=correlation_id, name=name)
    
    item = Item(name=name)
    db.add(item)
    db.commit()
    db.refresh(item)
    
    logger.log("INFO", "Item created", correlation_id=correlation_id, item_id=item.id)
    
    return {"id": item.id, "name": item.name}

@app.get("/metrics")
def get_metrics():
    """Expose metrics (Prometheus format in production)"""
    avg_duration = (
        metrics["request_duration_sum"] / metrics["requests_total"]
        if metrics["requests_total"] > 0 else 0
    )
    
    return {
        "requests_total": metrics["requests_total"],
        "errors_total": metrics["errors_total"],
        "error_rate": (
            metrics["errors_total"] / metrics["requests_total"] * 100
            if metrics["requests_total"] > 0 else 0
        ),
        "avg_response_time_seconds": round(avg_duration, 3)
    }

@app.get("/health")
def health_check(db: Session = Depends(get_db)):
    """Health check with dependency verification"""
    try:
        # Check database
        db.execute("SELECT 1")
        return {"status": "healthy", "database": "connected"}
    except Exception as e:
        logger.log("ERROR", "Health check failed", error=str(e))
        return {"status": "unhealthy", "database": str(e)}, 503

# Run with: uvicorn exercise8_observable_api:app --reload
#
# Features:
# ✅ Structured JSON logging
# ✅ Correlation IDs (trace requests)
# ✅ Request timing
# ✅ Metrics (requests, errors, duration)
# ✅ Health checks
# ✅ Error logging with context
# ✅ Response headers (correlation ID, timing)
#
# Test:
# POST /items?name=test → Check logs for correlation_id
# GET /items → Same correlation_id in all logs for this request
# GET /metrics → See request count, error rate, avg response time
# GET /health → Verify health status
