# Redis basics: set, get, delete. Simple key-value storage.

import redis

# Connect to Redis (make sure Redis is running: brew services start redis)
cache = redis.Redis(host='localhost', port=6379, decode_responses=True)

# SET: Store a value
cache.set('name', 'Alice')
cache.set('age', '30')
cache.set('city', 'San Francisco')

# GET: Retrieve a value
name = cache.get('name')
age = cache.get('age')
city = cache.get('city')

print(f"Name: {name}")
print(f"Age: {age}")
print(f"City: {city}")

# GET non-existent key
missing = cache.get('country')
print(f"Missing key: {missing}")  # None

# DELETE: Remove a key
cache.delete('city')
print(f"After delete: {cache.get('city')}")  # None

# SET with expiration (TTL in seconds)
cache.set('session_token', 'abc123', ex=10)  # Expires after 10 seconds
print(f"Token: {cache.get('session_token')}")
print("Waiting 11 seconds...")
import time
time.sleep(11)
print(f"Token after expiry: {cache.get('session_token')}")  # None

# SETEX: Set with expiration (alternative syntax)
cache.setex('temp_data', 5, 'temporary')
print(f"Temp: {cache.get('temp_data')}")

# EXISTS: Check if key exists
if cache.exists('name'):
    print("Name exists in cache")

# KEYS: List all keys (don't use in production! Slow on large datasets)
all_keys = cache.keys('*')
print(f"All keys: {all_keys}")

# Expected output:
# Name: Alice
# Age: 30
# City: San Francisco
# Missing key: None
# After delete: None
# Token: abc123
# Waiting 11 seconds...
# Token after expiry: None
# Temp: temporary
# Name exists in cache
# All keys: [...]
#
# Redis is just a super-fast key-value store in memory.
