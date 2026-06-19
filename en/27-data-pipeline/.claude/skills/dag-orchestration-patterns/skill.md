---
name: dag-orchestration-patterns
description: "A data pipeline orchestration guide covering Airflow DAG design patterns, dependency management, retry strategies, idempotency guarantees, backfill strategies, and more. Use this skill for pipeline scheduling, such as 'Airflow DAG', 'DAG design', 'dependencies', 'retry strategy', 'idempotency', 'backfill', 'pipeline orchestration', 'Dagster', 'Prefect'. It reinforces the DAG design capability of scheduler-engineer. However, defining data quality rules and monitoring dashboards are out of this skill's scope."
---

# DAG Orchestration Patterns — pipeline orchestration pattern guide

Airflow-centric DAG design patterns and operational strategies.

## DAG design patterns

### 1. Extract-Load-Transform (ELT) pattern

```python
with DAG("elt_orders", schedule="0 2 * * *", catchup=False) as dag:
    extract = PythonOperator(task_id="extract", python_callable=extract_orders)
    load_raw = PythonOperator(task_id="load_raw", python_callable=load_to_raw)
    transform = DbtOperator(task_id="transform", select="orders")
    quality = PythonOperator(task_id="quality_check", python_callable=run_checks)
    notify = SlackOperator(task_id="notify", trigger_rule="all_done")

    extract >> load_raw >> transform >> quality >> notify
```

### 2. Fan-out/Fan-in pattern

```python
# Parallel extraction from multiple sources → unified transformation
sources = ["mysql", "postgres", "api"]
extract_tasks = [
    PythonOperator(task_id=f"extract_{src}", python_callable=extract, op_args=[src])
    for src in sources
]
merge = PythonOperator(task_id="merge_all", python_callable=merge_sources)
transform = PythonOperator(task_id="transform", python_callable=transform_data)

extract_tasks >> merge >> transform
```

### 3. Sensor-based event waiting

```python
wait_for_data = S3KeySensor(
    task_id="wait_for_file",
    bucket_name="data-lake",
    bucket_key="raw/orders/{{ ds }}/data.parquet",
    timeout=3600,  # wait 1 hour
    poke_interval=60,
    mode="reschedule"  # release the worker while waiting
)
```

## Idempotency guarantee patterns

### Partition replacement (most recommended)

```sql
-- Full replacement of the date partition (idempotent)
DELETE FROM analytics.orders WHERE date_partition = '{{ ds }}';
INSERT INTO analytics.orders
SELECT * FROM staging.orders WHERE date_partition = '{{ ds }}';
```

### MERGE/UPSERT

```sql
MERGE INTO target AS t
USING source AS s ON t.id = s.id
WHEN MATCHED THEN UPDATE SET t.amount = s.amount, t.updated_at = CURRENT_TIMESTAMP
WHEN NOT MATCHED THEN INSERT (id, amount, created_at) VALUES (s.id, s.amount, CURRENT_TIMESTAMP);
```

### Idempotency checklist

- [ ] Does running the same DAG twice produce the same result?
- [ ] Does it limit the range using the date parameter (`{{ ds }}`)?
- [ ] Does it clean up existing data before the INSERT?
- [ ] Does it use a unique request ID for external API calls?

## Retry strategy

```python
default_args = {
    "retries": 3,
    "retry_delay": timedelta(minutes=5),
    "retry_exponential_backoff": True,
    "max_retry_delay": timedelta(minutes=60),
    "execution_timeout": timedelta(hours=2),
}
```

### Per-job retry configuration

| Job type | Retry count | Wait time | Reason |
|----------|-----------|----------|------|
| DB extraction | 3 | 5 min exponential backoff | Transient connection issues |
| API call | 5 | 30 sec exponential backoff | Rate limit, network |
| Transformation (SQL) | 1 | Immediate | Retrying logic errors is pointless |
| File upload | 3 | 1 min | Network instability |

## Backfill strategy

```python
# Safe backfill configuration
dag = DAG(
    "daily_orders",
    schedule="0 2 * * *",
    start_date=datetime(2024, 1, 1),
    catchup=False,  # automatic backfill disabled
    max_active_runs=1,  # prevent concurrent runs
)

# Manual backfill via CLI
# airflow dags backfill daily_orders -s 2024-01-01 -e 2024-01-31
```

### Backfill cautions

| Caution | Description | Mitigation |
|------|------|------|
| Concurrent runs | Duplicate processing of the same data range | `max_active_runs=1` |
| API Rate Limit | Bulk requests for historical data | Limit batch size, insert sleeps |
| Resource contention | DB/cluster overload | Limit parallelism, spread over time |
| Data consistency | Structural changes in historical data | Schema evolution handling logic |

## Dependency patterns

### Cross-DAG dependency

```python
# Wait for the completion of DAG A
wait_for_upstream = ExternalTaskSensor(
    task_id="wait_for_dag_a",
    external_dag_id="dag_a",
    external_task_id="final_task",
    execution_delta=timedelta(hours=0),
    timeout=3600,
    mode="reschedule"
)
```

### Dataset-based dependency (Airflow 2.4+)

```python
# Producer DAG
orders_dataset = Dataset("s3://datalake/orders/")

with DAG("produce_orders", schedule="0 2 * * *") as dag:
    produce = PythonOperator(
        task_id="produce", outlets=[orders_dataset]
    )

# Consumer DAG — triggered automatically
with DAG("consume_orders", schedule=[orders_dataset]) as dag:
    consume = PythonOperator(task_id="consume", ...)
```

## Alert strategy

```python
def failure_callback(context):
    task = context["task_instance"]
    dag_id = context["dag"].dag_id
    execution_date = context["execution_date"]
    message = f"FAILED: {dag_id}/{task.task_id} at {execution_date}"
    send_slack(message)

default_args = {
    "on_failure_callback": failure_callback,
    "on_retry_callback": retry_callback,
}
```

| Event | Channel | Target |
|--------|------|------|
| P0 job failure | Slack + PagerDuty | On-call engineer |
| SLA breach | Slack | Data team |
| Retry occurred | Slack (info) | Monitoring channel |
| Backfill complete | Slack | Requester |
