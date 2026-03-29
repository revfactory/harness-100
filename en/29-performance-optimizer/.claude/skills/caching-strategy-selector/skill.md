---
name: caching-strategy-selector
description: "Selection matrix for caching strategies (Cache Aside, Write Through, Write Behind, etc.), Redis/Memcached usage, TTL design, and cache invalidation pattern guide. Use this skill for caching design involving 'caching strategy', 'Redis', 'cache invalidation', 'TTL', 'Cache Aside', 'Write Through', 'CDN caching', 'cache stampede', and similar topics. Enhances the caching design capabilities of the optimization-engineer. Note: full performance profiling and benchmarking are outside the scope of this skill."
---

# Caching Strategy Selector — Caching Strategy Selection Guide

Methodology for selecting the appropriate caching strategy and implementing it effectively.

## Caching Strategy Comparison

### 1. Cache Aside (Lazy Loading)

```
Read:  App → Check cache → Miss → Query DB → Store in cache → Return
Write: App → Save to DB → Invalidate cache (delete)
```

| Pros | Cons |
|------|------|
| Most general-purpose | First request always misses |
| Falls back to DB on cache failure | Read-modify-write race condition |
| Only caches needed data | Data inconsistency window exists |

### 2. Write Through

```
Write: App → Save to cache → Save to DB (synchronous)
Read:  App → Check cache → Always hits
```

| Pros | Cons |
|------|------|
| Read-write consistency | Increased write latency |
| Cache always up to date | Unused data is also cached |

### 3. Write Behind (Write Back)

```
Write: App → Save to cache → Save to DB asynchronously in batches
Read:  App → Check cache → Always hits
```

| Pros | Cons |
|------|------|
| Maximizes write performance | Data loss on cache failure |
| Smooths out DB load | Complex to implement |

### Strategy Selection Matrix

| Requirement | Cache Aside | Write Through | Write Behind |
|------------|------------|---------------|-------------|
| Read-heavy | ★★★ | ★★ | ★★ |
| Write-heavy | ★ | ★ | ★★★ |
| Consistency critical | ★★ | ★★★ | ★ |
| Performance critical | ★★ | ★ | ★★★ |
| Simple implementation | ★★★ | ★★ | ★ |
| No data loss tolerated | ★★★ | ★★★ | ★ |

## Cache Invalidation Patterns

### 1. TTL (Time-To-Live)

```python
# TTL configuration guide
CACHE_TTL = {
    "user_profile": 300,      # 5 minutes — infrequently changed
    "product_list": 60,       # 1 minute — moderately changed
    "stock_count": 10,        # 10 seconds — frequently changed
    "config": 3600,           # 1 hour — rarely changed
    "session": 86400,         # 24 hours — session lifetime
}

# Add jitter (prevents cache stampede)
import random
ttl = base_ttl + random.randint(0, base_ttl // 10)
```

### 2. Event-Based Invalidation

```python
# Event-driven invalidation
@event_handler("user.updated")
def invalidate_user_cache(event):
    cache.delete(f"user:{event.user_id}")
    cache.delete(f"user_profile:{event.user_id}")
    # Also invalidate related list caches
    cache.delete("user_list:page:*")
```

### 3. Version-Based

```python
# Invalidate all at once using a version key
version = cache.get("product_version") or 1
key = f"product_list:v{version}"
# Invalidate: just increment the version
cache.incr("product_version")
```

## Cache Problem Resolution

### Cache Stampede (Thundering Herd)

```
Problem: On cache expiry, all concurrent requests hit the DB simultaneously
Solutions:

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
   # Return stale data after TTL expiry while refreshing in the background

3. Probabilistic Early Expiry
   delta = ttl * beta * log(random())
   if now() - fetched_at > ttl + delta:
       refresh()
```

### Cache Penetration

```
Problem: Repeated requests for non-existent keys → DB hit every time
Solutions:
1. Bloom filter: Pre-check for key existence
2. Cache empty results: cache.set(key, NULL, ttl=60)
3. Request validation: Block invalid keys upfront
```

### Cache Avalanche

```
Problem: Large number of caches expire simultaneously → DB overload
Solutions:
1. TTL scatter: TTL + random jitter
2. Staggered expiry: Different TTLs by importance
3. Pre-warming (Warm-up): Pre-load cache before deployment
```

## Cache Layer Design

```
L1: Local cache (in-process)
    ├── Capacity: ~100MB
    ├── Latency: ~0.1ms
    └── Best for: config, constants, high-frequency reads

L2: Distributed cache (Redis/Memcached)
    ├── Capacity: ~10GB
    ├── Latency: ~1ms
    └── Best for: sessions, profiles, lists

L3: CDN cache (CloudFront/Cloudflare)
    ├── Capacity: unlimited
    ├── Latency: ~5ms from edge
    └── Best for: static assets, API responses

L4: Browser cache
    ├── Cache-Control: max-age, stale-while-revalidate
    └── ETag / Last-Modified
```

## Redis Data Structure Selection

| Structure | Best For | Examples |
|-----------|----------|---------|
| String | Simple key-value | Sessions, config, counters |
| Hash | Object fields | User profiles |
| List | Recent items | Recently viewed products (LPUSH + LTRIM) |
| Set | Unique collections | Online users |
| Sorted Set | Rankings | Leaderboards, trending |
| HyperLogLog | Approximate counting | UV counts |
