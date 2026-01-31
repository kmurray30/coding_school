# Generate signed URLs for temporary file access.

from fastapi import FastAPI, HTTPException
from datetime import datetime, timedelta
import hmac
import hashlib
from urllib.parse import urlencode

app = FastAPI()

# Secret key for signing (keep this secret!)
SECRET_KEY = "your-secret-key-change-in-production"

def generate_signed_url(filename: str, expires_in_seconds: int = 3600):
    """Generate a signed URL that expires"""
    # Expiration time
    expires_at = datetime.utcnow() + timedelta(seconds=expires_in_seconds)
    expires_timestamp = int(expires_at.timestamp())
    
    # Create signature
    message = f"{filename}:{expires_timestamp}"
    signature = hmac.new(
        SECRET_KEY.encode(),
        message.encode(),
        hashlib.sha256
    ).hexdigest()
    
    # Build URL with signature
    params = {
        'expires': expires_timestamp,
        'signature': signature
    }
    
    return f"/files/{filename}?{urlencode(params)}"

def verify_signed_url(filename: str, expires: int, signature: str) -> bool:
    """Verify a signed URL is valid and not expired"""
    # Check expiration
    if datetime.utcnow().timestamp() > expires:
        return False
    
    # Verify signature
    message = f"{filename}:{expires}"
    expected_signature = hmac.new(
        SECRET_KEY.encode(),
        message.encode(),
        hashlib.sha256
    ).hexdigest()
    
    return hmac.compare_digest(signature, expected_signature)

@app.get("/generate-url/{filename}")
def get_signed_url(filename: str, expires_in: int = 60):
    """Generate a signed URL for temporary access"""
    url = generate_signed_url(filename, expires_in)
    return {
        "url": url,
        "expires_in_seconds": expires_in,
        "message": "URL is valid for limited time only"
    }

@app.get("/files/{filename}")
def download_with_signature(filename: str, expires: int, signature: str):
    """Download file with signature verification"""
    # Verify signature and expiration
    if not verify_signed_url(filename, expires, signature):
        raise HTTPException(status_code=403, detail="Invalid or expired signature")
    
    # Signature valid - serve file
    from fastapi.responses import FileResponse
    from pathlib import Path
    
    file_path = Path("./uploads") / filename
    if not file_path.exists():
        raise HTTPException(status_code=404, detail="File not found")
    
    return FileResponse(file_path)

# Run with: uvicorn exercise4_signed_urls:app --reload
#
# Test flow:
# 1. GET /generate-url/document.pdf?expires_in=30
#    → {"url": "/files/document.pdf?expires=1234567890&signature=abc..."}
#
# 2. GET /files/document.pdf?expires=1234567890&signature=abc...
#    → File downloads (if within 30 seconds)
#
# 3. Wait 31 seconds, try same URL
#    → 403 Forbidden (expired)
#
# 4. Try with wrong signature
#    → 403 Forbidden (invalid signature)
#
# Use cases for signed URLs:
# - Share private files temporarily
# - Download links in emails (expire after 24 hours)
# - Video streaming (expire after viewing)
# - Secure file sharing (no permanent public URLs)
#
# S3 signed URLs work the same way (AWS handles it for you).
