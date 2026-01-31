# Redis data structures: hashes, lists, sets.

import redis

cache = redis.Redis(host='localhost', port=6379, decode_responses=True)

# HASH: Store objects/dictionaries
print("=== HASHES ===")
cache.hset('user:100', 'name', 'Charlie')
cache.hset('user:100', 'email', 'charlie@example.com')
cache.hset('user:100', 'age', '25')

# Get single field
name = cache.hget('user:100', 'name')
print(f"Name: {name}")

# Get all fields
user = cache.hgetall('user:100')
print(f"Full user: {user}")

# SET: Unordered collection (no duplicates)
print("\n=== SETS ===")
cache.sadd('tags:post:1', 'python', 'fastapi', 'tutorial')
cache.sadd('tags:post:1', 'python')  # Duplicate ignored

tags = cache.smembers('tags:post:1')
print(f"Tags: {tags}")

# Check if member exists
is_python = cache.sismember('tags:post:1', 'python')
print(f"Has python tag: {is_python}")

# LIST: Ordered collection (allows duplicates)
print("\n=== LISTS ===")
cache.rpush('recent_searches', 'fastapi', 'redis', 'sqlalchemy')
cache.rpush('recent_searches', 'fastapi')  # Duplicate allowed

# Get all items
searches = cache.lrange('recent_searches', 0, -1)
print(f"Recent searches: {searches}")

# Get last 2 items
last_two = cache.lrange('recent_searches', -2, -1)
print(f"Last 2 searches: {last_two}")

# Pop from list
first = cache.lpop('recent_searches')
print(f"Popped: {first}")
print(f"Remaining: {cache.lrange('recent_searches', 0, -1)}")

# Clean up
cache.delete('user:100', 'tags:post:1', 'recent_searches')

# When to use each type:
# String: Simple values (counters, flags, cached HTML)
# Hash: Objects/entities (user profiles, product details)
# Set: Unique collections (tags, followers, permissions)
# List: Ordered sequences (activity feeds, queues, recent items)
