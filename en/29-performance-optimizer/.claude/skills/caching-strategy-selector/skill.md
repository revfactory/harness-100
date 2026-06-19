---
name: caching-strategy-selector
description: "A guide to caching strategies (Cache Aside, Write Through, Write Behind, etc.) with a selection matrix, Redis/Memcached usage, TTL design, and cache invalidation patterns. Use this skill when designing caching such as 'caching strategy', 'Redis', 'cache invalidation', 'TTL', 'Cache Aside', 'Write Through', 'CDN caching', and 'cache stampede'. It strengthens optimization-engineer's caching design capability. However, whole-system performance profiling and benchmarking are out of scope for this skill."
---

# Caching Strategy Selector — caching strategy selection guide

A methodology for selecting an appropriate caching strategy and implementing it effectively.

## Comparing caching strategies

### 1. Cache Aside (Lazy Loading)

```
Read: App → check Cache → miss → query DB → store in Cache → return
Write: App → store in DB → invalidate (delete) Cache
```

| Pros | Cons |
|------|------|
| most general-purpose | the first request is always a miss |
| DB fallback when the cache fails | read-modify-write race condition |
| caches only the needed data | data inconsistency window exists |

### 2. Write Through

```
Write: App → store in Cache → store in DB (synchronous)
Read: App → check Cache → always a hit
```

| Pros | Cons |
|------|------|
| read-write consistency | increased write latency |
| cache always fresh | caches even unused data |

### 3. Write Behind (Write Back)

```
Write: App → store in Cache → store in DB via asynchronous batch
Read: App → check Cache → always a hit
```

| Pros | Cons |
|------|------|
| maximizes write performance | data loss when the cache fails |
| flattens DB load | complex to implement |

### Strategy selection matrix

| Requirement | Cache Aside | Write Through | Write Behind |
|---------|------------|---------------|-------------|
| read-heavy | ★★★ | ★★ | ★★ |
| write-heavy | ★ | ★ | ★★★ |
| consistency critical | ★★ | ★★★ | ★ |
| performance critical | ★★ | ★ | ★★★ |
| simple to implement | ★★★ | ★★ | ★ |
| data loss unacceptable | ★★★ | ★★★ | ★ |

## Cache invalidation patterns

### 1. TTL (Time-To-Live)

```python
# TTL configuration guide
CACHE_TTL = {
    "user_profile": 300,      # 5 min — does not change often
    "product_list": 60,       # 1 min — moderate change frequency
    "stock_count": 10,        # 10 sec — changes often
    "config": 3600,           # 1 hour — almost never changes
    "session": 86400,         # 24 hours — session lifetime
}

# Add Jitter (prevent cache stampede)
import random
ttl = base_ttl + random.randint(0, base_ttl // 10)
```

### 2. Event-Based Invalidation

```python
# event-based invalidation
@event_handler("user.updated")
def invalidate_user_cache(event):
    cache.delete(f"user:{event.user_id}")
    cache.delete(f"user_profile:{event.user_id}")
    # also invalidate related list caches
    cache.delete("user_list:page:*")
```

### 3. Version-Based

```python
# invalidate all at once via a version key
version = cache.get("product_version") or 1
key = f"product_list:v{version}"
# invalidation: just increment the version
cache.incr("product_version")
```

## Cache problem resolution

### Cache Stampede (Thundering Herd)

```
Problem: when the cache expires, concurrent requests all hit the DB
Resolution:

1. Mutex Lock
   if cache.miss(key):
       if cache.lock(key + ":lock", timeout=5):
           result = db.query()
           cache.set(key, result, ttl)
           cache.unlock(key + ":lock")
       else:
           wait_and_retry()

2. Stale-While-Revalidate
   cache.set(key, data, ttl=300, stale_ttl=600)
   # return stale data even after the TTL expires while refreshing in the background

3. Probabilistic Early Expiry
   delta = ttl * beta * log(random())
   if now() - fetched_at > ttl + delta:
       refresh()
```

### Cache Penetration

```
Problem: repeated requests for a nonexistent key → hits the DB every time
Resolution:
1. Bloom filter: check the possibility of existence in advance
2. cache empty results: cache.set(key, NULL, ttl=60)
3. request validation: block invalid keys in advance
```

### Cache Avalanche

```
Problem: a large number of caches expire at the same time → DB overload
Resolution:
1. TTL spreading: TTL + random jitter
2. staggered expiry: different TTLs by importance
3. Warm-up: preload the cache at deploy time
```

## Cache layer design

```
L1: local cache (in-process)
    ├── capacity: ~100MB
    ├── speed: ~0.1ms
    └── suitable: config, constants, frequent reads

L2: distributed cache (Redis/Memcached)
    ├── capacity: ~10GB
    ├── speed: ~1ms
    └── suitable: sessions, profiles, lists

L3: CDN cache (CloudFront/Cloudflare)
    ├── capacity: unlimited
    ├── speed: ~5ms from the edge
    └── suitable: static assets, API responses

L4: browser cache
    ├── Cache-Control: max-age, stale-while-revalidate
    └── ETag / Last-Modified
```

## Choosing Redis data structures

| Structure | Suitable for | Example |
|------|------|------|
| String | simple key-value | sessions, config, counters |
| Hash | object fields | user profile |
| List | recent lists | recently viewed products (LPUSH + LTRIM) |
| Set | unique sets | online users |
| Sorted Set | rankings | leaderboard, trending |
| HyperLogLog | approximate counting | UV count |
