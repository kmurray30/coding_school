# Decode and validate a JWT token. Handle expiration and invalid signatures.

from jose import jwt, JWTError
from datetime import datetime, timedelta

SECRET_KEY = "your-secret-key-keep-this-safe"
ALGORITHM = "HS256"

# Create a valid token
def create_token(user_id: int, expires_minutes: int = 30):
    data = {
        "user_id": user_id,
        "exp": datetime.utcnow() + timedelta(minutes=expires_minutes)
    }
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

# Verify and decode a token
def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError as e:
        return {"error": str(e)}

# Test with valid token
valid_token = create_token(123)
print("Valid token:", verify_token(valid_token))

# Test with expired token (expires in -1 minutes = already expired)
expired_token = create_token(456, expires_minutes=-1)
print("Expired token:", verify_token(expired_token))

# Test with tampered token (change one character)
tampered = valid_token[:-5] + "XXXXX"
print("Tampered token:", verify_token(tampered))

# Test with wrong secret
try:
    wrong_secret = jwt.decode(valid_token, "wrong-secret", algorithms=[ALGORITHM])
except JWTError:
    print("Wrong secret: verification failed")

# Expected output:
# Valid token: {'user_id': 123, 'exp': ...}
# Expired token: {'error': 'Signature has expired'}
# Tampered token: {'error': 'Signature verification failed'}
# Wrong secret: verification failed
