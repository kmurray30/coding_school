# TTL (Time To Live): Automatic cache expiration.

import redis
import time

cache = redis.Redis(host='localhost', port=6379, decode_responses=True)

# Set value with TTL
cache.set('user_session', 'session_abc123', ex=30)  # Expires in 30 seconds

# Check TTL (time remaining)
ttl = cache.ttl('user_session')
print(f"TTL for user_session: {ttl} seconds")

# Wait a bit
time.sleep(5)

# Check TTL again
ttl = cache.ttl('user_session')
print(f"TTL after 5 seconds: {ttl} seconds")

# Set TTL on existing key
cache.set('product_cache', 'product_data')
cache.expire('product_cache', 60)  # Expire in 60 seconds
print(f"Product cache TTL: {cache.ttl('product_cache')} seconds")

# Persist: Remove TTL (make key permanent)
cache.persist('product_cache')
print(f"After persist: {cache.ttl('product_cache')}")  # -1 means no expiry

# Different TTL for different data
cache.set('homepage_html', '<html>...</html>', ex=60)      # 1 minute (changes rarely)
cache.set('stock_price', '150.25', ex=5)                    # 5 seconds (changes often)
cache.set('user_preferences', '{"theme": "dark"}', ex=3600) # 1 hour (changes rarely)

print("\nTTLs:")
print(f"Homepage: {cache.ttl('homepage_html')}s")
print(f"Stock: {cache.ttl('stock_price')}s")
print(f"Preferences: {cache.ttl('user_preferences')}s")

# Clean up
cache.delete('user_session', 'product_cache', 'homepage_html', 'stock_price', 'user_preferences')

# Expected output:
# TTL for user_session: 30 seconds
# TTL after 5 seconds: 25 seconds
# Product cache TTL: 60 seconds
# After persist: -1
# 
# TTLs:
# Homepage: 60s
# Stock: 5s
# Preferences: 3600s
#
# Choose TTL based on:
# - How often data changes
# - How stale you can tolerate
# - How expensive to regenerate
