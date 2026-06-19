---
name: query-optimization-patterns
description: "A database performance optimization guide covering SQL/NoSQL query optimization patterns, execution plan analysis, index strategy, N+1 problem resolution, and more. Use this skill when improving database query performance such as 'query optimization', 'execution plan', 'EXPLAIN', 'index design', 'N+1 problem', 'slow query', and 'DB performance'. It strengthens the DB performance analysis capabilities of bottleneck-analyst and optimization-engineer. However, whole-system profiling and benchmark execution are out of scope for this skill."
---

# Query Optimization Patterns — query optimization pattern guide

A methodology for systematically analyzing and optimizing database query performance.

## Execution plan analysis

### Reading PostgreSQL EXPLAIN

```sql
EXPLAIN (ANALYZE, BUFFERS, FORMAT TEXT)
SELECT o.*, c.name
FROM orders o
JOIN customers c ON o.customer_id = c.id
WHERE o.created_at > '2024-01-01'
ORDER BY o.total_amount DESC
LIMIT 10;
```

### Interpreting core metrics

| Metric | Meaning | Warning sign |
|------|------|----------|
| **Seq Scan** | full table scan | when it occurs on a large table |
| **Nested Loop** | row-by-row join | when the outer table is large |
| **Hash Join** | hash-based join | uses disk when work_mem is exceeded |
| **Sort** | sorting | external sort when memory is exceeded |
| **Bitmap Heap Scan** | index → table access | performance degrades with a lossy bitmap |
| **actual time** | actual elapsed time | difference between first row vs all rows |
| **rows** | estimated vs actual difference | 10x or more difference → refresh statistics |

### Detecting risky patterns

```
❌ Seq Scan on large_table (rows=10000000)
   → index addition needed

❌ Sort Method: external merge (Disk: 256MB)
   → increase work_mem or sort by index

❌ Nested Loop (actual rows=1000000)
   → switch to Hash Join or Merge Join

❌ estimated=100 actual=100000
   → run ANALYZE to refresh statistics
```

## Index strategy

### Use by index type

| Index type | Suitable for | Unsuitable for |
|------------|-----------|-------------|
| B-Tree (default) | equality, range, sorting | arrays, JSON, full-text search |
| Hash | equality comparison only | range queries |
| GIN | arrays, JSONB, full-text search | simple equality/range |
| GiST | geospatial, range types | simple scalars |
| BRIN | physically sorted data | random distribution |

### Composite index design principles

```sql
-- Leftmost Prefix rule
CREATE INDEX idx_orders ON orders(status, created_at, customer_id);

-- Queries this index covers:
✅ WHERE status = 'PAID'
✅ WHERE status = 'PAID' AND created_at > '2024-01-01'
✅ WHERE status = 'PAID' AND created_at > '2024-01-01' AND customer_id = 123
❌ WHERE created_at > '2024-01-01'  (status missing)
❌ WHERE customer_id = 123          (status, created_at missing)

-- Criteria for deciding column order:
-- 1. equality-condition columns first (the more selective ones)
-- 2. range-condition columns next
-- 3. ORDER BY columns last
```

### Covering index

```sql
-- Complete the query from the index alone, with no table access
CREATE INDEX idx_covering ON orders(status, created_at) INCLUDE (total_amount);

SELECT total_amount FROM orders
WHERE status = 'PAID' AND created_at > '2024-01-01';
-- Index Only Scan occurs → no heap access needed
```

## N+1 problem resolution

### Diagnosing the problem

```python
# N+1 pattern (slow!)
orders = Order.objects.filter(status="PAID")  # query 1
for order in orders:
    print(order.customer.name)  # query N (one per order)
# total queries: 1 + N

# Resolve with Eager Loading
orders = Order.objects.filter(status="PAID").select_related("customer")  # query 1 (JOIN)
# or
orders = Order.objects.filter(status="PAID").prefetch_related("items")  # query 2 (IN)
```

### Resolution by ORM

| ORM | N+1 resolution | Method |
|-----|---------|------|
| Django | `select_related` / `prefetch_related` | FK JOIN / Reverse IN |
| SQLAlchemy | `joinedload` / `subqueryload` | JOIN / subquery |
| TypeORM | `relations` / `@JoinColumn` | eager/lazy configuration |
| Prisma | `include` | automatic batching |
| JPA | `@EntityGraph` / `JOIN FETCH` | JPQL/Criteria |

## Pagination optimization

| Method | SQL | Performance | Suitable for |
|------|-----|------|------|
| OFFSET | `LIMIT 20 OFFSET 10000` | O(N) — slow | small scale, early pages |
| Keyset | `WHERE id > 1000 LIMIT 20` | O(1) — fast | large scale, infinite scroll |
| Cursor | encrypted keyset | O(1) | API, client-facing |

```sql
-- OFFSET (from the 10000th → scan 10000 rows then discard them)
SELECT * FROM orders ORDER BY id LIMIT 20 OFFSET 10000;

-- Keyset (jump straight to the position)
SELECT * FROM orders WHERE id > 10000 ORDER BY id LIMIT 20;
```

## Query anti-patterns

| Anti-pattern | Problem | Resolution |
|---------|------|------|
| `SELECT *` | transfers unnecessary columns | specify only the needed columns |
| `WHERE func(column)` | cannot use the index | move the transformation to the constant side |
| `LIKE '%keyword%'` | full scan | full-text search index (GIN) |
| subquery IN (large) | slow execution | switch to a JOIN |
| implicit type conversion | invalidates the index | match the types |

## Query optimization checklist

- [ ] Run EXPLAIN ANALYZE to confirm the execution plan
- [ ] Confirm whether a Seq Scan is intentional (small data is OK)
- [ ] Check the estimated vs actual rows difference
- [ ] Whether the needed index exists
- [ ] Confirm there are no N+1 query patterns
- [ ] Confirm pagination is keyset-based
- [ ] Remove unnecessary ORDER BY / DISTINCT
- [ ] Confirm the transaction scope is minimal
