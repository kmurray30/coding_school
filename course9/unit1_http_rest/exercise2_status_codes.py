# HTTP status codes tell clients what happened. Run and test each endpoint.

from fastapi import FastAPI, Response

app = FastAPI()

@app.get("/success")
def success():
    # 200 OK - request succeeded
    return {"status": "all good"}

@app.get("/not-found")
def not_found(response: Response):
    # 404 Not Found - resource doesn't exist
    response.status_code = 404
    return {"error": "nothing here"}

@app.post("/created")
def created(response: Response):
    # 201 Created - new resource created successfully
    response.status_code = 201
    return {"id": 123, "message": "resource created"}

# Run with: uvicorn exercise2_status_codes:app --reload
# Visit /docs to test each endpoint and see the status codes
# 
# Expected:
# GET /success → 200 OK
# GET /not-found → 404 Not Found  
# POST /created → 201 Created
