---
name: query-optimization-catalog
description: "SQL query optimisation catalog. An extension skill for performance-analyst that provides index strategies (B-Tree/Hash/GIN/GiST), execution plan analysis, N+1 problem resolution, partitioning strategies, and per-pattern optimisation techniques for slow queries. Use when performing DB performance analysis involving 'query optimisation', 'index design', 'execution plans', 'N+1 problems', 'partitioning', 'slow queries', etc. Note: data modelling and security configuration are outside the scope of this skill."
---

# Query Optimisation Catalog — SQL Query Optimisation Catalog

A reference of index strategies, execution plan analysis, and query anti-pattern resolution used by the performance-analyst agent during performance optimisation.

## Target Agent

`performance-analyst` — Directly applies the optimisation techniques from this skill to performance analysis and index design.

## Index Strategies

### Index Type Selection Guide

| Index Type | Suitable Queries | DBMS | Characteristics |
|-----------|-----------------|------|-----------------|
| **B-Tree** | `=`, `<`, `>`, `BETWEEN`, `ORDER BY` | All | General purpose, default |
| **Hash** | `=` equality only | PostgreSQL, MySQL | No range searches |
| **GIN** | Arrays, JSONB, full-text search | PostgreSQL | Multi-value indexing |
| **GiST** | Spatial (geometry), ranges | PostgreSQL | PostGIS, range types |
| **BRIN** | Time-series, naturally sorted data | PostgreSQL | Very small size |
| **Fulltext** | Full-text search | MySQL, PostgreSQL | Replaces LIKE '%word%' |

### Composite Index Design Principles

#### Leftmost Prefix Rule
```sql
INDEX idx_abc ON table(a, b, c)

-- Usable:
WHERE a = 1                          -- O (a only)
WHERE a = 1 AND b = 2               -- O (a, b)
WHERE a = 1 AND b = 2 AND c = 3     -- O (all columns)
WHERE a = 1 AND c = 3               -- Partial (a only, c skipped)

-- Not usable:
WHERE b = 2                          -- X (a missing)
WHERE c = 3                          -- X (a, b missing)
```

#### Column Order Decision Rules
1. **WHERE equality (=) condition** columns first
2. **Sort (ORDER BY)** columns next
3. **Range (<, >, BETWEEN)** columns last
4. **Higher cardinality** first (but rules 1-3 take priority)

### Covering Indexes
Return query results using only the index (no table access needed).

```sql
-- Covering index
CREATE INDEX idx_covering ON orders(user_id, status, created_at);

-- This query responds from the index only (Index Only Scan)
SELECT status, created_at FROM orders WHERE user_id = 123;
```

### Index Add/Remove Decision Guide

| Scenario | Add Index? | Reason |
|----------|-----------|--------|
| Column frequently used in WHERE clause | Yes | Improves search speed |
| FK column in JOIN ON clause | Yes | JOIN performance |
| Column frequently used in ORDER BY | Yes | Avoids sorting |
| Very low cardinality (boolean, etc.) | No | Minimal benefit |
| Frequently UPDATEd column | Carefully | Write performance degradation |
| Small table (under 10K rows) | No | Full scan is faster |

## Slow Query Anti-Patterns & Solutions

### 1. N+1 Problem
```sql
-- Anti-pattern: Individual queries in a loop
SELECT * FROM users;
-- For each user:
SELECT * FROM orders WHERE user_id = ?;  -- Repeated N times!

-- Solution: JOIN or IN
SELECT u.*, o.* FROM users u
LEFT JOIN orders o ON u.id = o.user_id;

-- Or batch loading
SELECT * FROM orders WHERE user_id IN (1, 2, 3, ...);
```

### 2. SELECT *
```sql
-- Anti-pattern
SELECT * FROM products WHERE category = 'electronics';

-- Solution: Only needed columns
SELECT id, name, price FROM products WHERE category = 'electronics';
-- Enables covering index usage
```

### 3. Function Invalidating Index
```sql
-- Anti-pattern: Applying function to indexed column
WHERE YEAR(created_at) = 2025

-- Solution: Convert to range condition
WHERE created_at >= '2025-01-01' AND created_at < '2026-01-01'
```

### 4. OR Condition Invalidating Index
```sql
-- Anti-pattern
WHERE status = 'active' OR category = 'books'

-- Solution: UNION ALL
SELECT * FROM products WHERE status = 'active'
UNION ALL
SELECT * FROM products WHERE category = 'books' AND status != 'active'
```

### 5. Subquery vs JOIN
```sql
-- Anti-pattern: Correlated subquery
SELECT * FROM orders o
WHERE o.total > (SELECT AVG(total) FROM orders WHERE user_id = o.user_id);

-- Solution: JOIN + aggregate
SELECT o.* FROM orders o
JOIN (SELECT user_id, AVG(total) as avg_total FROM orders GROUP BY user_id) a
ON o.user_id = a.user_id
WHERE o.total > a.avg_total;
```

### 6. OFFSET Pagination
```sql
-- Anti-pattern: Deep OFFSET
SELECT * FROM products ORDER BY id LIMIT 20 OFFSET 100000;

-- Solution: Cursor-based (Keyset)
SELECT * FROM products WHERE id > 100000 ORDER BY id LIMIT 20;
```

### 7. Large IN Clause
```sql
-- Anti-pattern: Thousands of IDs
WHERE id IN (1, 2, 3, ..., 10000)

-- Solution: Temporary table or JOIN
-- PostgreSQL: VALUES or ANY(ARRAY[...])
-- General: Batch processing (500 at a time)
```

## EXPLAIN Analysis Guide (PostgreSQL)

### Reading Execution Plans
```sql
EXPLAIN (ANALYZE, BUFFERS, FORMAT TEXT)
SELECT * FROM orders WHERE user_id = 123 AND status = 'completed';
```

### Key Node Types

| Node | Meaning | Performance |
|------|---------|-------------|
| Seq Scan | Full table scan | Slow (large data) |
| Index Scan | Index + table access | Moderate |
| Index Only Scan | Response from index only | Fast |
| Bitmap Index Scan | Bitmap-based index scan | Moderate |
| Nested Loop | Nested loop join | Suitable for small datasets |
| Hash Join | Hash table join | Large equality joins |
| Merge Join | Sort-merge join | Large sorted data |
| Sort | Sort operation | Watch memory/disk |

### Warning Signs
- `Seq Scan` on a large table -> Index needed
- `Sort` with `external merge Disk` -> Insufficient work_mem
- `actual rows` >> `estimated rows` -> Stale statistics (ANALYSE needed)
- `Nested Loop` with a large table -> Encourage Hash Join

## Partitioning Strategy

### Signs Partitioning Is Needed
- Table size > hundreds of millions of rows
- Time-series data (logs, events, metrics)
- Periodic deletion/archiving of old data
- Most queries target specific time ranges

### Partitioning Types

| Type | Split Criterion | Suitable For | Example |
|------|----------------|-------------|---------|
| **Range** | Value range | Time-series | Monthly/yearly partitions |
| **List** | Value list | Categories | By region, by status |
| **Hash** | Hash value | Even distribution | user_id % N |

### Range Partitioning Example (PostgreSQL)
```sql
CREATE TABLE events (
  id BIGINT,
  event_time TIMESTAMPTZ,
  data JSONB
) PARTITION BY RANGE (event_time);

CREATE TABLE events_2025_q1 PARTITION OF events
  FOR VALUES FROM ('2025-01-01') TO ('2025-04-01');
```

## Caching Strategy

| Level | Tool | Suitable Data | TTL |
|-------|------|--------------|-----|
| **Query cache** | Redis/Memcached | Frequently read query results | 30s-5min |
| **ORM cache** | Prisma/TypeORM cache | Entity-level | 1-5min |
| **Aggregation cache** | Materialized View | Statistics/dashboards | 1hr+ |
| **CDN cache** | CloudFront/CloudFlare | Static API responses | 5-60min |

### Cache Invalidation Strategies
- **TTL-based**: Auto-refresh after expiration time
- **Event-based**: Immediate deletion on data change
- **Write-Through**: Update cache on writes
- **Cache-Aside**: On read miss, query DB and store in cache
