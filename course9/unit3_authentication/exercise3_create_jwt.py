# Create a JWT token with user data and expiration.

from jose import jwt
from datetime import datetime, timedelta

SECRET_KEY = "your-secret-key-keep-this-safe"
ALGORITHM = "HS256"

# Create a token with user data
user_data = {
    "user_id": 123,
    "username": "alice",
    "exp": ...  # Expiration time: current time + 30 minutes
}

token = jwt.encode(user_data, SECRET_KEY, algorithm=ALGORITHM)

print(f"JWT Token: {token}")
print(f"Token parts: header.payload.signature (3 parts separated by dots)")

# Create another token for a different user that expires in 1 hour
...

# Expected output:
# JWT Token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9... (long string)
# Token parts: header.payload.signature (3 parts separated by dots)
# 
# The token contains the user data but is signed so it can't be tampered with.
# Anyone can READ the token (it's base64, not encrypted) but can't MODIFY it.
