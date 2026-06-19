---
name: data-quality-framework
description: "A guide to designing validation rules per data quality dimension (accuracy, completeness, timeliness, consistency, etc.) and to using tools such as Great Expectations and dbt tests. Use this skill for data quality management, such as 'data quality', 'validation rules', 'Great Expectations', 'dbt test', 'data profiling', 'anomaly detection', 'data contract'. It reinforces the quality verification capability of data-quality-manager. However, pipeline scheduling and overall architecture design are out of this skill's scope."
---

# Data Quality Framework — data quality framework guide

A framework for systematically defining, measuring, and monitoring data quality.

## The 6 dimensions of data quality

| Dimension | Definition | Measurement method | Threshold example |
|------|------|----------|-----------|
| **Accuracy** | Correctly reflects reality | Source reconciliation, business rule verification | accuracy > 99.9% |
| **Completeness** | Required data exists | NULL ratio, required field satisfaction | NULL < 1% |
| **Timeliness** | Arrives within the expected time | Latency, data freshness | latency < 30 min |
| **Consistency** | Agreement across systems | Cross-validation, referential integrity | mismatches = 0 |
| **Uniqueness** | No duplicates | Duplicate row/key ratio | duplicates = 0% |
| **Validity** | Conforms to format/range | Regex, range checks | validity rate > 99% |

## Validation rule design patterns

### P0 (required — pipeline halts on failure)

```yaml
rules:
  - name: pk_uniqueness
    type: uniqueness
    column: order_id
    threshold: 0  # 0 duplicates

  - name: not_null_critical
    type: completeness
    columns: [order_id, customer_id, total_amount]
    max_null_rate: 0

  - name: row_count_sanity
    type: volume
    min_rows: 1000  # daily minimum order count
    max_deviation: 0.5  # warn on a ≥50% change vs the prior day

  - name: referential_integrity
    type: consistency
    source: orders.customer_id
    reference: customers.id
    match_rate: 1.0
```

### P1 (important — proceed after warning)

```yaml
rules:
  - name: email_format
    type: validity
    column: email
    pattern: "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$"
    threshold: 0.99

  - name: amount_range
    type: accuracy
    column: total_amount
    min: 0
    max: 100000000  # orders over 100M are suspect

  - name: freshness
    type: timeliness
    column: created_at
    max_age_hours: 24
```

## Great Expectations implementation

```python
import great_expectations as gx

# Define expectations
suite = context.add_expectation_suite("orders_quality")

# Completeness
suite.add_expectation(
    gx.expectations.ExpectColumnValuesToNotBeNull(column="order_id")
)

# Uniqueness
suite.add_expectation(
    gx.expectations.ExpectColumnValuesToBeUnique(column="order_id")
)

# Validity
suite.add_expectation(
    gx.expectations.ExpectColumnValuesToBeBetween(
        column="total_amount", min_value=0, max_value=100000000
    )
)

# Volume
suite.add_expectation(
    gx.expectations.ExpectTableRowCountToBeBetween(
        min_value=1000, max_value=1000000
    )
)
```

## dbt Tests implementation

```yaml
# schema.yml
models:
  - name: orders
    columns:
      - name: order_id
        tests:
          - unique
          - not_null
      - name: customer_id
        tests:
          - not_null
          - relationships:
              to: ref('customers')
              field: id
      - name: total_amount
        tests:
          - not_null
          - dbt_utils.accepted_range:
              min_value: 0
              max_value: 100000000
    tests:
      - dbt_utils.recency:
          datepart: hour
          field: created_at
          interval: 24
```

## Data profiling checklist

```
Per-column profile:
├── Type: actual type vs declared type
├── Cardinality: number of distinct values
├── NULL ratio: missingness pattern
├── Distribution: histogram, skewness, kurtosis
├── Outliers: IQR-based outliers
├── Pattern: regex match rate for dates, emails, phone numbers, etc.
└── Dependency: functional dependency relationships

Per-table profile:
├── Row count: expected range vs actual
├── Duplicate rate: duplicates among all rows
├── Referential integrity: count of FK violations
└── Time distribution: record creation time pattern
```

## Anomaly detection techniques

| Technique | Applies to | Formula/method |
|------|------|----------|
| Z-Score | Normally distributed data | \|x - μ\| / σ > 3 |
| IQR | Non-normal distribution | x < Q1-1.5*IQR or x > Q3+1.5*IQR |
| Moving average | Time-series volume | deviation of 2σ from the 7-day moving average |
| Day-over-day | Daily loads | \|today - yesterday\| / yesterday > 0.5 |

## Data contract (Data Contract)

```yaml
# data-contract.yml
name: orders
version: "2.0.0"
owner: order-team
description: "order data contract"

schema:
  - name: order_id
    type: string
    required: true
    unique: true
  - name: total_amount
    type: decimal(10,2)
    required: true
    min: 0

sla:
  freshness: 1h
  availability: 99.9%

quality:
  completeness: 99.9%
  accuracy: 99.99%
```
