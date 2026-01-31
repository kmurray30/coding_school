# Structured logging with JSON format for better searchability.

import logging
import json
from datetime import datetime

# Basic logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Traditional logging (bad for production)
logger.info("User logged in")
logger.info("User alice logged in from IP 192.168.1.1")

# Structured logging (good for production)
class StructuredLogger:
    def __init__(self, name: str):
        self.name = name
    
    def log(self, level: str, message: str, **context):
        log_entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "level": level,
            "logger": self.name,
            "message": message,
            **context
        }
        print(json.dumps(log_entry))

struct_logger = StructuredLogger("app")

# Log with context
struct_logger.log(
    "INFO",
    "User logged in",
    user_id=123,
    username="alice",
    ip_address="192.168.1.1",
    user_agent="Mozilla/5.0"
)

struct_logger.log(
    "WARNING",
    "Failed login attempt",
    username="bob",
    ip_address="10.0.0.1",
    reason="invalid_password"
)

struct_logger.log(
    "ERROR",
    "Database connection failed",
    database="postgres",
    host="db.example.com",
    error="connection timeout"
)

# Expected output (JSON):
# {"timestamp": "2024-01-15T10:30:00", "level": "INFO", "message": "User logged in", "user_id": 123, ...}
# {"timestamp": "2024-01-15T10:30:05", "level": "WARNING", "message": "Failed login attempt", ...}
#
# Benefits of structured logging:
# ✅ Easy to search/filter (grep for user_id=123)
# ✅ Easy to parse (log aggregation tools)
# ✅ Can query by fields (find all WARNING logs)
# ✅ Context is structured, not buried in strings
# ❌ Harder to read in raw form (use log viewer)
