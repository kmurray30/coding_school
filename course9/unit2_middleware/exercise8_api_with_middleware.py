# Build an API with multiple middleware layers working together.
# Add: CORS, request logging, timing, custom headers, error formatting.

from fastapi import FastAPI

app = FastAPI(title="Multi-Middleware API")

# Add CORS middleware (allow requests from any origin)

# Add logging middleware (log method, path, status code)

# Add timing middleware (measure request duration)

# Add custom headers middleware (request ID, server version)

# Add at least 3 endpoints to test your middleware stack
# Each endpoint should show the middleware working:
# - Check console for logs and timing
# - Check response headers for custom headers
# - Test CORS from browser console

...

# Run with: uvicorn exercise8_api_with_middleware:app --reload
#
# Expected behavior:
# Every request logs to console with timing
# Every response includes X-Request-ID and X-Server-Version headers
# Browser can call API from any origin (CORS)
# Middleware runs in order: CORS → logging → timing → custom headers → handler
