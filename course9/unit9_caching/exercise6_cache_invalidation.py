# Cache invalidation: Delete cache when data changes.

import redis
import json

cache = redis.Redis(host='localhost', port=6379, decode_responses=True)

# Simulate database
users_db = {
    1: {"name": "Alice", "email": "alice@example.com", "bio": "Developer"}
}

def get_user(user_id: int):
    """Get user (with caching)"""
    cache_key = f"user:{user_id}"
    
    # Check cache
    cached = cache.get(cache_key)
    if cached:
        print(f"✓ Cache hit")
        return json.loads(cached)
    
    # Cache miss - load from DB
    print(f"✗ Cache miss - loading from DB")
    user = users_db.get(user_id)
    if user:
        cache.set(cache_key, json.dumps(user), ex=300)  # Cache for 5 minutes
    return user

def update_user(user_id: int, updates: dict):
    """Update user and invalidate cache"""
    cache_key = f"user:{user_id}"
    
    # Update database
    if user_id in users_db:
        users_db[user_id].update(updates)
        print(f"Updated user {user_id} in database")
        
        # Invalidate cache - delete the cached entry
        cache.delete(cache_key)
        print(f"Invalidated cache for {cache_key}")
        return True
    return False

# Test the flow
print("1. First fetch (cache miss):")
user = get_user(1)
print(f"User: {user}\n")

print("2. Second fetch (cache hit):")
user = get_user(1)
print(f"User: {user}\n")

print("3. Update user:")
update_user(1, {"bio": "Senior Developer"})
print()

print("4. Fetch after update (cache miss - was invalidated):")
user = get_user(1)
print(f"User: {user}\n")

print("5. Fetch again (cache hit with new data):")
user = get_user(1)
print(f"User: {user}\n")

# Clean up
cache.delete("user:1")

# Expected output:
# 1. First fetch (cache miss):
# ✗ Cache miss - loading from DB
# User: {'name': 'Alice', 'email': 'alice@example.com', 'bio': 'Developer'}
#
# 2. Second fetch (cache hit):
# ✓ Cache hit
# User: {'name': 'Alice', 'email': 'alice@example.com', 'bio': 'Developer'}
#
# 3. Update user:
# Updated user 1 in database
# Invalidated cache for user:1
#
# 4. Fetch after update (cache miss - was invalidated):
# ✗ Cache miss - loading from DB
# User: {'name': 'Alice', 'email': 'alice@example.com', 'bio': 'Senior Developer'}
#
# 5. Fetch again (cache hit with new data):
# ✓ Cache hit
# User: {'name': 'Alice', 'email': 'alice@example.com', 'bio': 'Senior Developer'}
#
# Invalidation strategies:
# 1. Time-based (TTL) - let cache expire naturally
# 2. Event-based (shown above) - delete on write
# 3. Pattern-based - delete multiple related keys
