# Use Pydantic models to validate request bodies. Type-safe JSON parsing.

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    username: str
    email: str
    age: int

# Create a POST endpoint that accepts a User in the request body
# Validate the data automatically with Pydantic
# Return a confirmation message with the user info

# Create another model for a Book with title, author, and year
# Make an endpoint that accepts a Book and returns it with an assigned ID

...

# Run with: uvicorn exercise6_request_bodies:app --reload
#
# Expected:
# POST /users with {"username": "bob", "email": "bob@example.com", "age": 25}
#   → {"message": "user created", "username": "bob", "email": "bob@example.com"}
# 
# POST with bad data (missing field, wrong type) → automatic 422 validation error
# POST /books with {"title": "FastAPI Guide", "author": "Someone", "year": 2024}
#   → {"id": 1, "title": "FastAPI Guide", "author": "Someone", "year": 2024}
