# Build a complete authentication system from scratch.
# Features: registration, login, protected routes, user profile.

from fastapi import FastAPI

app = FastAPI(title="Complete Auth System")

# Build:
# 1. POST /register - create new user with username, password, email
#    - Hash password before storing
#    - Return success message
#    - Store in memory for this exercise (use a dict)
#
# 2. POST /login - accept username/password, return JWT if valid
#    - Verify password hash
#    - Return access token
#
# 3. GET /me - return current user's profile
#    - Requires valid JWT
#    - Extract user from token
#    - Return user info (no password!)
#
# 4. GET /protected/dashboard - requires authentication
#    - Show personalized message with username
#
# 5. PUT /me/password - change password
#    - Requires authentication
#    - Accept old_password and new_password
#    - Verify old password before changing

# You choose:
# - Pydantic models
# - Data structures
# - Error handling
# - Response formats

# Requirements:
# - Never store plaintext passwords
# - Return proper status codes (201 for registration, 401 for bad auth, etc.)
# - JWT tokens should expire in 30 minutes
# - Protected routes should use dependency injection

...

# Run with: uvicorn exercise10_auth_system:app --reload
#
# Test flow:
# 1. POST /register {"username": "alice", "password": "secret123", "email": "alice@example.com"}
# 2. POST /login {"username": "alice", "password": "secret123"} → get token
# 3. GET /me (with Authorization: Bearer <token>) → see profile
# 4. GET /protected/dashboard (with token) → personalized message
# 5. PUT /me/password (with token) {"old_password": "secret123", "new_password": "newsecret"}
# 6. POST /login with old password → should fail
# 7. POST /login with new password → should work
