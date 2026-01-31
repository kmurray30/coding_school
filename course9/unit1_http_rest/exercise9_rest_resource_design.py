# Design a RESTful API for a blog. Resources: posts, comments.
# REST conventions: collections at /resource, single items at /resource/{id}
# Run with: uvicorn exercise9_rest_resource_design:app --reload
# Visit http://localhost:8000/...

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Design URL patterns and methods for:
# - List all posts
# - Get a specific post
# - Create a new post
# - Update a post
# - Delete a post
# - List comments for a post
# - Add a comment to a post

# Pydantic models to get you started:

class Post(BaseModel):
    id: int
    title: str
    content: str
    author: str

class Comment(BaseModel):
    id: int
    post_id: int
    text: str
    author: str

# In-memory storage
posts = {}
comments = {}
post_counter = 1
comment_counter = 1

# Implement the endpoints following REST conventions.
# Use appropriate HTTP methods (GET, POST, PUT, DELETE)
# Structure URLs logically (/posts, /posts/{id}, /posts/{id}/comments)

...

# Your API should support this flow:
# POST /posts → create post with id 1
# GET /posts → list all posts (just the one)
# GET /posts/1 → get specific post
# PUT /posts/1 → update the post
# POST /posts/1/comments → add a comment to post 1
# GET /posts/1/comments → list comments for post 1
# DELETE /posts/1 → delete the post
