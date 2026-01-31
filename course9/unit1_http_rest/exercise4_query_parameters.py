# Query parameters come after ? in URLs. Use them for filtering and options.

from fastapi import FastAPI

app = FastAPI()

@app.get("/items")
def list_items(category: str = "all", limit: int = 10):
    # category and limit come from query params like: /items?category=books&limit=5
    return {
        "category": category,
        "limit": limit,
        "items": [f"Item {i} in {category}" for i in range(1, limit + 1)]
    }

# Add an endpoint that accepts 'search' and 'page' query parameters
# search should default to empty string, page should default to 1

@app.get("/search")
def search(...):
    ...

# Run with: uvicorn exercise4_query_parameters:app --reload
#
# Expected:
# GET /items → default category "all", limit 10
# GET /items?category=books&limit=3 → 3 items in books category
# GET /search?search=fastapi&page=2 → {"query": "fastapi", "page": 2, "results": [...]}
