# Never store passwords in plaintext. Hash them with bcrypt.

from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Hash a password
password = "supersecret123"
hashed = pwd_context.hash(password)

print(f"Original: {password}")
print(f"Hashed: {hashed}")

# Verify password
is_correct = pwd_context.verify("supersecret123", hashed)
is_wrong = pwd_context.verify("wrongpassword", hashed)

print(f"Correct password: {is_correct}")
print(f"Wrong password: {is_wrong}")

# Hash the same password again
another_hash = pwd_context.hash(password)
print(f"Same password, different hash: {another_hash != hashed}")

# Expected output:
# Original: supersecret123
# Hashed: $2b$12$... (long random string)
# Correct password: True
# Wrong password: False
# Same password, different hash: True
#
# Bcrypt adds random salt, so same password → different hash every time.
# Can't reverse a hash to get the password. That's the point.
