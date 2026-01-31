# Use appropriate log levels for different events.

import logging

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

# DEBUG: Detailed information for diagnosing problems
logger.debug("Processing request with parameters: user_id=123, action=login")
logger.debug("Cache lookup: key=user:123, result=hit")

# INFO: General informational messages
logger.info("User 123 logged in successfully")
logger.info("API request: POST /api/users (200 OK, 45ms)")

# WARNING: Something unexpected happened, but app continues
logger.warning("API rate limit approaching: 950/1000 requests used")
logger.warning("Deprecated API endpoint called: /api/v1/users")
logger.warning("Slow query detected: 2.5 seconds")

# ERROR: Error occurred, feature broken but app still running
logger.error("Failed to send email to user@example.com: SMTP timeout")
logger.error("Database query failed: connection pool exhausted")

# CRITICAL: Severe error, app might crash
logger.critical("Database connection lost! Application cannot function")
logger.critical("Out of memory: cannot allocate buffer")

# When to use each level:
# DEBUG → Development, verbose details
# INFO → Normal operations, audit trail
# WARNING → Potential problems, degraded performance
# ERROR → Feature failures, exceptions
# CRITICAL → System-wide failures, requires immediate attention

# In production:
# - Set level to INFO (hides DEBUG)
# - DEBUG logs would overwhelm production systems
# - ERROR and CRITICAL trigger alerts

# Example: Production logger config
production_logger = logging.getLogger("production")
production_logger.setLevel(logging.INFO)  # Ignore DEBUG

production_logger.debug("This won't show in production")
production_logger.info("This will show in production")
production_logger.error("This will trigger alert")
