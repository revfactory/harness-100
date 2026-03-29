---
name: data-quality-framework
description: "A guide to designing validation rules per data quality dimension (accuracy, completeness, timeliness, consistency, etc.) and using tools such as Great Expectations and dbt tests. Use this skill when working with 'data quality', 'validation rules', 'Great Expectations', 'dbt test', 'data profiling', 'anomaly detection', or 'data contracts'. Augments the quality validation capability of the data-quality-manager. Note: pipeline scheduling and overall architecture design are outside this skill's scope."
---

# Data Quality Framework — Data Quality Framework Guide

A framework for systematically defining, measuring, and monitoring data quality.

## 6 Dimensions of Data Quality

| Dimension | Definition | Measurement Method | Threshold Example |
|-----------|-----------|-------------------|------------------|
| **Accuracy** | Correctly reflects reality | Source reconciliation, business rule validation | Accuracy > 99.9% |
| **Completeness** | Required data is present | NULL rate, mandatory field coverage | NULL < 1% |
| **Timeliness** | Arrives within the expected window | Latency, data freshness | Delay < 30 minutes |
| **Consistency** | Agrees across systems | Cross-validation, referential integrity | Mismatches = 0 |
| **Uniqueness** | No duplicates | Duplicate row / key rate | Duplicates = 0% |
| **Validity** | Conforms to format and range | Regex, range checks | Validity rate > 99% |

## Validation Rule Design Patterns

### P0 (Critical — pipeline halts on failure)

```yaml
rules:
  - name: pk_uniqueness
    type: uniqueness
    column: order_id
    threshold: 0  # zero duplicates allowed

  - name: not_null_critical
    type: completeness
    columns: [order_id, customer_id, total_amount]
    max_null_rate: 0

  - name: row_count_sanity
    type: volume
    min_rows: 1000  # minimum daily order count
    max_deviation: 0.5  # alert if deviation exceeds 50% vs. prior day

  - name: referential_integrity
    type: consistency
    source: orders.customer_id
    reference: customers.id
    match_rate: 1.0
```

### P1 (Important — warn and continue)

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
    max: 100000000  # orders above 100M are suspicious

  - name: freshness
    type: timeliness
    column: created_at
    max_age_hours: 24
```

## Great Expectations Implementation

```python
import great_expectations as gx

# Define the expectation suite
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

## dbt Tests Implementation

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

## Data Profiling Checklist

```
Per-column profile:
├── Type: actual type vs. declared type
├── Cardinality: number of distinct values
├── NULL rate: missing data patterns
├── Distribution: histogram, skewness, kurtosis
├── Outliers: IQR-based outlier detection
├── Patterns: regex match rate for dates, emails, phone numbers, etc.
└── Dependencies: functional dependency relationships

Per-table profile:
├── Row count: expected range vs. actual
├── Duplicate rate: duplicate rows out of total
├── Referential integrity: number of FK violations
└── Time distribution: record creation time patterns
```

## Anomaly Detection Techniques

| Technique | Application | Formula / Method |
|-----------|------------|-----------------|
| Z-Score | Normally distributed data | \|x - μ\| / σ > 3 |
| IQR | Non-normal distributions | x < Q1 - 1.5×IQR or x > Q3 + 1.5×IQR |
| Moving average | Time-series volume | Deviation of more than 2σ from the 7-day moving average |
| Day-over-day | Daily loads | \|today - yesterday\| / yesterday > 0.5 |

## Data Contract

```yaml
# data-contract.yml
name: orders
version: "2.0.0"
owner: order-team
description: "Order data contract"

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
