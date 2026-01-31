# Build a personal library API. Track books, authors, and reading status.
# Combine everything: routes, methods, path/query params, models, status codes.

from fastapi import FastAPI

app = FastAPI(title="Personal Library API")

# Your library should track:
# - Books (title, author, year published, reading status: "to-read", "reading", "finished")
# - Each book gets a unique ID

# Build these features:
# - Add a book to your library
# - List all books (with optional filter by status: ?status=reading)
# - Get details for a specific book
# - Update a book's reading status
# - Delete a book from your library
# - Get stats (how many books total, how many finished, etc.)

# Choose your own:
# - URL patterns
# - Pydantic models
# - Response structures
# - Status codes

# Make it work like a real API. Test it in /docs.

...

# Run with: uvicorn exercise10_simple_api:app --reload
#
# Example flow (yours will vary):
# POST /books → {"title": "Dune", "author": "Frank Herbert", "year": 1965, "status": "to-read"}
#   Response: {"id": 1, "title": "Dune", ...}
# 
# GET /books → list all books
# GET /books?status=to-read → filter by status
# GET /books/1 → get Dune
# PUT /books/1 → change status to "reading"
# GET /stats → {"total": 1, "to_read": 0, "reading": 1, "finished": 0}
# DELETE /books/1 → remove book
