# Cache-aside pattern: Check cache first, then database.

import redis
import time

cache = redis.Redis(host='localhost', port=6379, decode_responses=True)

# Simulate database
fake_database = {
    "user:1": {"name": "Alice", "email": "alice@example.com"},
    "user:2": {"name": "Bob", "email": "bob@example.com"},
}

def get_user(user_id: int):
    """
    Cache-aside pattern:
    1. Check cache
    2. If hit: return from cache
    3. If miss: query database, store in cache, return
    """
    cache_key = f"user:{user_id}"
    
    # Try cache first
    cached = cache.get(cache_key)
    if cached:
        print(f"Cache HIT for {cache_key}")
        return cached
    
    print(f"Cache MISS for {cache_key}")
    
    # Not in cache, query database
    db_result = fake_database.get(cache_key)
    if not db_result:
        return None
    
    # Store in cache for next time (TTL: 60 seconds)
    import json
    cache.set(cache_key, json.dumps(db_result), ex=60)
    print(f"Stored in cache: {cache_key}")
    
    return db_result

# First request: Cache miss
print("Request 1:")
user = get_user(1)
print(f"Result: {user}\n")

# Second request: Cache hit
print("Request 2:")
user = get_user(1)
print(f"Result: {user}\n")

# Different user: Cache miss
print("Request 3:")
user = get_user(2)
print(f"Result: {user}\n")

# Same user again: Cache hit
print("Request 4:")
user = get_user(2)
print(f"Result: {user}\n")

# Clean up
cache.delete("user:1", "user:2")

# Expected output:
# Request 1:
# Cache MISS for user:1
# Stored in cache: user:1
# Result: {'name': 'Alice', 'email': 'alice@example.com'}
#
# Request 2:
# Cache HIT for user:1
# Result: {"name": "Alice", "email": "alice@example.com"}
#
# Request 3:
# Cache MISS for user:2
# Stored in cache: user:2
# Result: {'name': 'Bob', 'email': 'bob@example.com'}
#
# Request 4:
# Cache HIT for user:2
# Result: {"name": "Bob", "email": "bob@example.com"}
#
# Cache-aside (lazy loading):
# - Application checks cache
# - Application loads from DB on miss
# - Application populates cache
# Most common caching pattern.
