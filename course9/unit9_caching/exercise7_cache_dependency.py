# FastAPI dependency for Redis client.

from fastapi import FastAPI, Depends
import redis
from typing import Generator

app = FastAPI()

# Redis connection pool (create once, reuse)
redis_pool = redis.ConnectionPool(
    host='localhost',
    port=6379,
    decode_responses=True,
    max_connections=10
)

def get_redis() -> Generator[redis.Redis, None, None]:
    """Dependency that provides Redis client"""
    client = redis.Redis(connection_pool=redis_pool)
    try:
        yield client
    finally:
        # Connection returns to pool automatically
        pass

@app.get("/cache-test")
def cache_test(cache: redis.Redis = Depends(get_redis)):
    # Use cache in your endpoint
    cache.set('test_key', 'test_value', ex=10)
    value = cache.get('test_key')
    return {"cached_value": value}

@app.get("/counter")
def increment_counter(cache: redis.Redis = Depends(get_redis)):
    # Increment a counter
    count = cache.incr('api_calls')
    return {"total_calls": count}

@app.get("/cache-stats")
def cache_stats(cache: redis.Redis = Depends(get_redis)):
    # Get cache statistics
    info = cache.info('stats')
    return {
        "total_commands": info.get('total_commands_processed'),
        "total_connections": info.get('total_connections_received'),
        "keyspace_hits": info.get('keyspace_hits', 0),
        "keyspace_misses": info.get('keyspace_misses', 0)
    }

# Example with caching expensive operation
import time

@app.get("/expensive/{item_id}")
def get_expensive_data(item_id: int, cache: redis.Redis = Depends(get_redis)):
    cache_key = f"expensive:{item_id}"
    
    # Try cache first
    cached = cache.get(cache_key)
    if cached:
        return {"source": "cache", "data": cached, "fast": True}
    
    # Simulate expensive operation
    time.sleep(2)  # 2 seconds of processing
    result = f"Expensive result for item {item_id}"
    
    # Cache for 1 minute
    cache.set(cache_key, result, ex=60)
    
    return {"source": "computed", "data": result, "fast": False}

# Run with: uvicorn exercise7_cache_dependency:app --reload
#
# Test:
# GET /expensive/1 → slow (2s), source: computed
# GET /expensive/1 → fast (<1ms), source: cache
# GET /counter → increments each time
# GET /cache-stats → shows Redis stats
