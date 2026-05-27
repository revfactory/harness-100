---
name: dag-orchestration-patterns
description: "Airflow DAG 설계 패턴, 의존관계 관리, 재시도 전략, 멱등성 보장, 백필 전략 등 데이터 파이프라인 오케스트레이션 가이드. 'Airflow DAG', 'DAG 설계', '의존관계', '재시도 전략', '멱등성', '백필', '파이프라인 오케스트레이션', 'Dagster', 'Prefect' 등 파이프라인 스케줄링 시 이 스킬을 사용한다. scheduler-engineer의 DAG 설계 역량을 강화한다. 단, 데이터 품질 규칙 정의나 모니터링 대시보드는 이 스킬의 범위가 아니다."
---

# DAG Orchestration Patterns — 파이프라인 오케스트레이션 패턴 가이드

Airflow 중심의 DAG 설계 패턴과 운영 전략.

## DAG 설계 패턴

### 1. Extract-Load-Transform (ELT) 패턴

```python
with DAG("elt_orders", schedule="0 2 * * *", catchup=False) as dag:
    extract = PythonOperator(task_id="extract", python_callable=extract_orders)
    load_raw = PythonOperator(task_id="load_raw", python_callable=load_to_raw)
    transform = DbtOperator(task_id="transform", select="orders")
    quality = PythonOperator(task_id="quality_check", python_callable=run_checks)
    notify = SlackOperator(task_id="notify", trigger_rule="all_done")

    extract >> load_raw >> transform >> quality >> notify
```

### 2. Fan-out/Fan-in 패턴

```python
# 다중 소스 병렬 추출 → 통합 변환
sources = ["mysql", "postgres", "api"]
extract_tasks = [
    PythonOperator(task_id=f"extract_{src}", python_callable=extract, op_args=[src])
    for src in sources
]
merge = PythonOperator(task_id="merge_all", python_callable=merge_sources)
transform = PythonOperator(task_id="transform", python_callable=transform_data)

extract_tasks >> merge >> transform
```

### 3. 센서 기반 이벤트 대기

```python
wait_for_data = S3KeySensor(
    task_id="wait_for_file",
    bucket_name="data-lake",
    bucket_key="raw/orders/{{ ds }}/data.parquet",
    timeout=3600,  # 1시간 대기
    poke_interval=60,
    mode="reschedule"  # 대기 중 워커 해제
)
```

## 멱등성 보장 패턴

### 파티션 교체 (가장 권장)

```sql
-- 날짜 파티션 전체 교체 (멱등적)
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

### 멱등성 체크리스트

- [ ] 같은 DAG를 2번 실행해도 결과가 동일한가?
- [ ] 날짜 파라미터(`{{ ds }}`)를 사용하여 범위를 제한하는가?
- [ ] INSERT 전에 기존 데이터를 정리하는가?
- [ ] 외부 API 호출에 고유 요청 ID를 사용하는가?

## 재시도 전략

```python
default_args = {
    "retries": 3,
    "retry_delay": timedelta(minutes=5),
    "retry_exponential_backoff": True,
    "max_retry_delay": timedelta(minutes=60),
    "execution_timeout": timedelta(hours=2),
}
```

### 작업별 재시도 설정

| 작업 유형 | 재시도 횟수 | 대기 시간 | 이유 |
|----------|-----------|----------|------|
| DB 추출 | 3회 | 5분 지수 백오프 | 일시적 연결 문제 |
| API 호출 | 5회 | 30초 지수 백오프 | Rate limit, 네트워크 |
| 변환 (SQL) | 1회 | 즉시 | 로직 오류는 재시도 무의미 |
| 파일 업로드 | 3회 | 1분 | 네트워크 불안정 |

## 백필 전략

```python
# 안전한 백필 설정
dag = DAG(
    "daily_orders",
    schedule="0 2 * * *",
    start_date=datetime(2024, 1, 1),
    catchup=False,  # 자동 백필 비활성
    max_active_runs=1,  # 동시 실행 방지
)

# CLI로 수동 백필
# airflow dags backfill daily_orders -s 2024-01-01 -e 2024-01-31
```

### 백필 주의사항

| 주의 | 설명 | 대응 |
|------|------|------|
| 동시 실행 | 같은 데이터 범위 중복 처리 | `max_active_runs=1` |
| API Rate Limit | 대량 과거 데이터 요청 | 배치 크기 제한, 슬립 삽입 |
| 리소스 경합 | DB/클러스터 과부하 | 병렬도 제한, 시간 분산 |
| 데이터 정합성 | 과거 데이터 구조 변경 | 스키마 진화 처리 로직 |

## 의존관계 패턴

### Cross-DAG 의존

```python
# DAG A의 완료를 대기
wait_for_upstream = ExternalTaskSensor(
    task_id="wait_for_dag_a",
    external_dag_id="dag_a",
    external_task_id="final_task",
    execution_delta=timedelta(hours=0),
    timeout=3600,
    mode="reschedule"
)
```

### Dataset 기반 의존 (Airflow 2.4+)

```python
# Producer DAG
orders_dataset = Dataset("s3://datalake/orders/")

with DAG("produce_orders", schedule="0 2 * * *") as dag:
    produce = PythonOperator(
        task_id="produce", outlets=[orders_dataset]
    )

# Consumer DAG — 자동 트리거
with DAG("consume_orders", schedule=[orders_dataset]) as dag:
    consume = PythonOperator(task_id="consume", ...)
```

## 알림 전략

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

| 이벤트 | 채널 | 대상 |
|--------|------|------|
| P0 작업 실패 | Slack + PagerDuty | 온콜 엔지니어 |
| SLA 미달 | Slack | 데이터 팀 |
| 재시도 발생 | Slack (정보) | 모니터링 채널 |
| 백필 완료 | Slack | 요청자 |
