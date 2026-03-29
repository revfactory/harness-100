---
name: query-optimization-patterns
description: "Guide for SQL/NoSQL query optimization patterns, execution plan analysis, index strategies, N+1 problem resolution, and other database performance optimizations. Use this skill for database query performance improvements involving 'query optimization', 'execution plan', 'EXPLAIN', 'index design', 'N+1 problem', 'slow query', 'DB performance', and similar topics. Enhances the DB performance analysis capabilities of bottleneck-analyst and optimization-engineer. Note: full system profiling and benchmark execution are outside the scope of this skill."
---

# Query Optimization Patterns — Query Optimization Pattern Guide

Methodology for systematically analyzing and optimizing database query performance.

## Execution Plan Analysis

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

### Key Metric Interpretation

| Metric | Meaning | Warning Signal |
|--------|---------|---------------|
| **Seq Scan** | Full table scan | Occurs on large tables |
| **Nested Loop** | Row-by-row join | When outer table is large |
| **Hash Join** | Hash-based join | Uses disk when work_mem exceeded |
| **Sort** | Sorting | External sort when memory exceeded |
| **Bitmap Heap Scan** | Index → table access | Performance degrades with lossy bitmap |
| **actual time** | Actual elapsed time | Difference between first row vs. all rows |
| **rows** | estimated vs actual difference | >10x difference → update statistics |

### Risk Pattern Detection

```
❌ Seq Scan on large_table (rows=10000000)
   → Index addition required

❌ Sort Method: external merge (Disk: 256MB)
   → Increase work_mem or add a sorted index

❌ Nested Loop (actual rows=1000000)
   → Switch to Hash Join or Merge Join

❌ estimated=100 actual=100000
   → Run ANALYZE to refresh statistics
```

## Index Strategy

### Index Type Usage

| Index Type | Suitable For | Not Suitable For |
|-----------|-------------|-----------------|
| B-Tree (default) | Equality, range, sorting | Arrays, JSON, full-text search |
| Hash | Equality comparisons only | Range queries |
| GIN | Arrays, JSONB, full-text search | Simple equality/range |
| GiST | Geospatial, range types | Simple scalars |
| BRIN | Physically sorted data | Random distribution |

### Composite Index Design Principles

```sql
-- Leftmost Prefix Rule
CREATE INDEX idx_orders ON orders(status, created_at, customer_id);

-- Queries covered by this index:
✅ WHERE status = 'PAID'
✅ WHERE status = 'PAID' AND created_at > '2024-01-01'
✅ WHERE status = 'PAID' AND created_at > '2024-01-01' AND customer_id = 123
❌ WHERE created_at > '2024-01-01'  (status missing)
❌ WHERE customer_id = 123          (status, created_at missing)

-- Column ordering criteria:
-- 1. Equality condition columns first (higher selectivity)
-- 2. Range condition columns next
-- 3. ORDER BY columns last
```

### Covering Index

```sql
-- Complete the query using only the index, without accessing the table
CREATE INDEX idx_covering ON orders(status, created_at) INCLUDE (total_amount);

SELECT total_amount FROM orders
WHERE status = 'PAID' AND created_at > '2024-01-01';
-- Index Only Scan → heap access not required
```

## N+1 Problem Resolution

### Problem Diagnosis

```python
# N+1 pattern (slow!)
orders = Order.objects.filter(status="PAID")  # Query 1
for order in orders:
    print(order.customer.name)  # Query N (once per order)
# Total queries: 1 + N

# Resolve with Eager Loading
orders = Order.objects.filter(status="PAID").select_related("customer")  # Query 1 (JOIN)
# or
orders = Order.objects.filter(status="PAID").prefetch_related("items")  # Query 2 (IN)
```

### ORM-Specific Solutions

| ORM | N+1 Solution | Method |
|-----|-------------|--------|
| Django | `select_related` / `prefetch_related` | FK JOIN / Reverse IN |
| SQLAlchemy | `joinedload` / `subqueryload` | JOIN / Subquery |
| TypeORM | `relations` / `@JoinColumn` | eager/lazy configuration |
| Prisma | `include` | Automatic batching |
| JPA | `@EntityGraph` / `JOIN FETCH` | JPQL/Criteria |

## Pagination Optimization

| Method | SQL | Performance | Best For |
|--------|-----|-------------|---------|
| OFFSET | `LIMIT 20 OFFSET 10000` | O(N) — slow | Small datasets, early pages |
| Keyset | `WHERE id > 1000 LIMIT 20` | O(1) — fast | Large datasets, infinite scroll |
| Cursor | Encrypted keyset | O(1) | APIs, client-facing |

```sql
-- OFFSET (starting from row 10000 → scans 10000 rows then discards)
SELECT * FROM orders ORDER BY id LIMIT 20 OFFSET 10000;

-- Keyset (jumps directly to the target position)
SELECT * FROM orders WHERE id > 10000 ORDER BY id LIMIT 20;
```

## Query Anti-Patterns

| Anti-Pattern | Problem | Solution |
|-------------|---------|---------|
| `SELECT *` | Transmits unnecessary columns | Specify only required columns |
| `WHERE func(column)` | Cannot use index | Move the transformation to the constant side |
| `LIKE '%keyword%'` | Full scan | Full-text search index (GIN) |
| Subquery IN (large set) | Slow execution | Switch to JOIN |
| Implicit type conversion | Invalidates index | Match types explicitly |

## Query Optimization Checklist

- [ ] Run EXPLAIN ANALYZE to review the execution plan
- [ ] Confirm whether Seq Scan is intentional (acceptable for small data)
- [ ] Check estimated vs actual rows difference
- [ ] Verify that necessary indexes exist
- [ ] Confirm absence of N+1 query patterns
- [ ] Confirm that pagination uses keyset-based approach
- [ ] Remove unnecessary ORDER BY / DISTINCT
- [ ] Confirm that transaction scope is minimal
