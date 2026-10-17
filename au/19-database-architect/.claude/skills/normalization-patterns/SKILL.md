---
name: normalization-patterns
description: "Database normalization/denormalization pattern library. An extension skill for data-modeler that provides 1NF-BCNF criteria, functional dependency analysis, step-by-step normalisation procedures, strategic denormalization patterns, and common domain ERD templates. Use when data modelling involves 'normalisation', 'denormalization', 'ERD patterns', 'functional dependencies', 'table splitting', 'relationship design', etc. Note: DDL generation and query optimisation are outside the scope of this skill."
---

# Normalisation Patterns — Normalization/Denormalization Pattern Library

Normalisation rules, denormalization strategies, and domain-specific ERD patterns used by the data-modeler agent during data modelling.

## Target Agent

`data-modeler` — Directly applies the normalisation rules and ERD patterns from this skill to data model designs.

## Normalisation Stage Identification & Transformation

### 1NF (First Normal Form)
**Rule**: Every column must contain atomic (indivisible) values.

| Violation Pattern | Problem | Solution |
|------------------|---------|----------|
| Multi-value column | `tags = "java,python,go"` | Separate table (M:N) |
| Repeating groups | `phone1, phone2, phone3` | Separate table (1:N) |
| Composite values | `address = "123 Main St, City, State"` | Split into street/city/state columns |

### 2NF (Second Normal Form)
**Prerequisite**: Satisfies 1NF
**Rule**: Remove partial functional dependencies — separate columns that depend on only part of a composite primary key.

| Violation Example | Dependency | Solution |
|------------------|------------|----------|
| `order_details(order_id, product_id, product_name, quantity)` | product_name depends only on product_id | Separate into products table |

### 3NF (Third Normal Form)
**Prerequisite**: Satisfies 2NF
**Rule**: Remove transitive functional dependencies — a non-key column must not determine another non-key column.

| Violation Example | Dependency | Solution |
|------------------|------------|----------|
| `employees(id, dept_id, dept_name, dept_head)` | dept_name, dept_head transitively depend on dept_id | Separate into departments table |

### BCNF (Boyce-Codd Normal Form)
**Rule**: Every determinant must be a candidate key.

| Violation Example | Problem | Solution |
|------------------|---------|----------|
| `enrollment(student, course, professor)` where professor -> course | Professor is a determinant but not a candidate key | Separate into professor-course table |

## Normalisation Decision Flowchart

```
Data Analysis
  ├─ Atomic value violation? -> 1NF transformation
  ├─ Composite key & partial dependency? -> 2NF transformation
  ├─ Transitive dependency? -> 3NF transformation
  ├─ Non-candidate-key determinant? -> BCNF transformation
  └─ Performance requirements -> Review strategic denormalization
```

## Strategic Denormalization Patterns

### When to Denormalize?
- When the read-to-write ratio is very high
- Frequent queries requiring 5+ JOINs
- When real-time aggregation/statistics are needed
- Dashboard/report-specific data

### Denormalization Pattern Catalog

| Pattern | Description | Suitable For | Trade-offs |
|---------|-------------|-------------|------------|
| **Derived column** | Store computed values (`total_price`) | Frequent sum lookups | Requires sync on update |
| **Duplicated column** | Copy frequently used FK target columns | Avoiding JOINs | Data inconsistency risk |
| **Pre-joined table** | Materialize join results as physical table | Reports/dashboards | Storage space, update complexity |
| **History snapshot** | Preserve point-in-time data (`order_address`) | Storing address at time of order | Storage space |
| **Counter column** | `likes_count`, `comments_count` | Real-time count display | Concurrency handling |
| **JSON/JSONB** | Unstructured extension data | Settings, metadata | Indexing limitations |

## Common Domain ERD Patterns

### E-Commerce
```
users ──1:N──> orders ──1:N──> order_items
  │                                 │
  └──1:N──> addresses          products
  └──1:N──> reviews ──N:1──────┘
                               │
products ──N:M──> categories (via product_categories)
products ──1:N──> product_images
products ──1:N──> product_variants
```

Core tables:
- `users` (id, email, name, password_hash, created_at)
- `products` (id, name, description, base_price, status)
- `orders` (id, user_id, status, total, shipping_address_snapshot)
- `order_items` (id, order_id, product_id, variant_id, quantity, unit_price)

### SaaS Multi-Tenant
```
tenants ──1:N──> users ──N:M──> roles (via user_roles)
   │                              │
   └──1:N──> subscriptions    permissions ──N:M──> roles
   └──1:N──> [domain tables] (tenant_id FK)
```

Key point: Include `tenant_id` in all business tables; apply RLS (Row Level Security)

### Social Network
```
users ──N:M──> users (via follows: follower_id, following_id)
  │
  └──1:N──> posts ──1:N──> comments
  │              └──N:M──> tags (via post_tags)
  │              └──1:N──> likes (user_id + post_id UNIQUE)
  └──1:N──> messages (sender_id, receiver_id)
```

### CMS/Blog
```
users ──1:N──> posts ──N:M──> tags (via post_tags)
                 │
                 └──1:N──> comments (self-referencing: parent_id)
                 └──1:N──> media
                 └──1:1──> post_meta (SEO, OG tags, etc.)
```

## Relationship Patterns

### 1:1 Relationship
- Large table splitting (frequently used columns vs rarely used columns)
- Optional extension (`user` + `user_profile`)
- Implementation: FK + UNIQUE constraint

### 1:N Relationship
- Most common relationship type
- Self-referencing: category trees, comment threads (`parent_id`)
- Implementation: FK on the child table

### M:N Relationship
- Junction table required
- Junction table may include additional attributes (`created_at`, `role`, `quantity`)
- Naming: `{table1}_{table2}` or a meaningful name (`enrollments`)

## Common Column Patterns

### Default Timestamps
Include in all tables:
- `id` — UUID or BIGINT AUTO_INCREMENT
- `created_at` — TIMESTAMPTZ DEFAULT NOW()
- `updated_at` — TIMESTAMPTZ, auto-updated via trigger

### Soft Delete
- `deleted_at` — TIMESTAMPTZ NULL (NULL means not deleted)
- All queries include `WHERE deleted_at IS NULL` condition
- Enables restoration and serves as audit trail

### Status Management
- `status` — ENUM or VARCHAR
- State transition rules must be documented (which states can transition to which)
- If history is needed, use a separate `status_history` table

### Internationalization
- Strategy 1: Column extension (`name_ko`, `name_en`, `name_ja`)
- Strategy 2: Translation table (`product_translations`: product_id, locale, name, description)
- Strategy 2 recommended (no schema changes needed when adding languages)
