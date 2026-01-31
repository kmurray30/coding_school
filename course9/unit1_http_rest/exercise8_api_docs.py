# FastAPI generates automatic interactive API documentation. Free.
# Run with: uvicorn exercise8_api_docs:app --reload
# Visit http://localhost:8000/...

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="My API",
    description="A sample API to demonstrate automatic docs",
    version="1.0.0"
)

class Item(BaseModel):
    name: str
    price: float
    description: str = ""

@app.get("/", tags=["root"])
def read_root():
    """Root endpoint returns a welcome message."""
    return {"message": "Welcome to the API"}

@app.post("/items", tags=["items"], response_model=Item)
def create_item(item: Item):
    """Create a new item with name, price, and optional description."""
    return item

@app.get("/items/{item_id}", tags=["items"])
def get_item(item_id: int):
    """Get an item by ID."""
    return {"id": item_id, "name": "Sample Item", "price": 9.99}

# Visit these URLs:
# - http://localhost:8000/docs (Swagger UI - interactive docs)
# - http://localhost:8000/redoc (ReDoc - alternative doc format)
#
# Notice:
# - All endpoints are listed
# - Request/response schemas are shown
# - You can test endpoints directly in /docs
# - Tags organize endpoints into groups
# - Docstrings become descriptions
#
# This is automatic. You wrote no extra code for this.
