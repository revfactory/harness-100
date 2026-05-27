---
name: type-mapping-encyclopedia
description: "RDBMS 간 데이터 타입 매핑 테이블, RDBMS↔NoSQL 변환 패턴, 문자셋/콜레이션 변환, 특수 타입 처리 가이드. '타입 매핑', '데이터 타입 변환', 'MySQL PostgreSQL 변환', 'Oracle 마이그레이션', '문자셋 변환', '콜레이션', 'AUTO_INCREMENT 시퀀스', 'JSON 타입' 등 스키마 타입 변환 시 이 스킬을 사용한다. schema-mapper의 타입 변환 역량을 강화한다. 단, ETL 스크립트 작성이나 검증 쿼리는 이 스킬의 범위가 아니다."
---

# Type Mapping Encyclopedia — 데이터 타입 매핑 백과사전

RDBMS 간 데이터 타입 매핑, 특수 타입 변환, 문자셋 처리를 위한 종합 레퍼런스.

## MySQL → PostgreSQL 매핑

| MySQL | PostgreSQL | 주의사항 |
|-------|-----------|---------|
| TINYINT | SMALLINT | TINYINT UNSIGNED → SMALLINT |
| INT | INTEGER | |
| INT UNSIGNED | BIGINT | PostgreSQL에 UNSIGNED 없음 |
| BIGINT | BIGINT | |
| FLOAT | REAL | |
| DOUBLE | DOUBLE PRECISION | |
| DECIMAL(M,N) | NUMERIC(M,N) | 동일 |
| VARCHAR(N) | VARCHAR(N) | |
| CHAR(N) | CHAR(N) | |
| TEXT | TEXT | |
| MEDIUMTEXT | TEXT | PostgreSQL TEXT 크기 제한 없음 |
| LONGTEXT | TEXT | |
| BLOB | BYTEA | |
| LONGBLOB | BYTEA | 또는 Large Object |
| DATE | DATE | |
| DATETIME | TIMESTAMP | MySQL: UTC 아님, PG: 타임존 옵션 |
| TIMESTAMP | TIMESTAMPTZ | MySQL: UTC 변환 자동 |
| TIME | TIME | |
| YEAR | SMALLINT | |
| ENUM('a','b') | VARCHAR + CHECK | 또는 CREATE TYPE |
| SET('a','b') | VARCHAR[] | 또는 정규화 |
| JSON | JSONB | JSONB 권장 (인덱싱 가능) |
| BIT(N) | BIT(N) | |
| BOOLEAN | BOOLEAN | MySQL TINYINT(1) → BOOLEAN |
| AUTO_INCREMENT | GENERATED ALWAYS AS IDENTITY | 또는 SERIAL (레거시) |

### 특수 변환 패턴

```sql
-- MySQL ENUM → PostgreSQL
-- 방법 1: CHECK 제약
CREATE TABLE orders (
    status VARCHAR(20) CHECK (status IN ('pending', 'paid', 'shipped'))
);

-- 방법 2: 사용자 정의 타입
CREATE TYPE order_status AS ENUM ('pending', 'paid', 'shipped');
CREATE TABLE orders (status order_status);

-- MySQL AUTO_INCREMENT → PostgreSQL IDENTITY
-- MySQL:
CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY);
-- PostgreSQL:
CREATE TABLE users (id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY);

-- MySQL ON UPDATE CURRENT_TIMESTAMP → PostgreSQL 트리거
CREATE OR REPLACE FUNCTION update_modified_column()
RETURNS TRIGGER AS $$
BEGIN NEW.updated_at = CURRENT_TIMESTAMP; RETURN NEW; END;
$$ LANGUAGE plpgsql;
CREATE TRIGGER update_timestamp BEFORE UPDATE ON users
FOR EACH ROW EXECUTE FUNCTION update_modified_column();
```

## Oracle → PostgreSQL 매핑

| Oracle | PostgreSQL | 주의사항 |
|--------|-----------|---------|
| NUMBER | NUMERIC | 정밀도 지정 필요 |
| NUMBER(N,0) | INTEGER/BIGINT | 크기에 따라 선택 |
| VARCHAR2(N) | VARCHAR(N) | |
| CHAR(N) | CHAR(N) | |
| CLOB | TEXT | |
| BLOB | BYTEA | |
| DATE | TIMESTAMP | Oracle DATE는 시간 포함! |
| TIMESTAMP WITH TIME ZONE | TIMESTAMPTZ | |
| RAW | BYTEA | |
| LONG | TEXT | 사용 중단 권장 |
| NVARCHAR2 | VARCHAR | PostgreSQL UTF-8 기본 |
| ROWID | 없음 | ctid 또는 자체 키 사용 |
| SEQUENCE | SEQUENCE | 구문 유사 |
| SYSDATE | CURRENT_TIMESTAMP | |
| NVL() | COALESCE() | |
| DECODE() | CASE WHEN | |

## RDBMS → MongoDB 변환 패턴

### 정규화 해제 전략

```
관계형:                          문서형:
┌─ users ─┐  ┌─ orders ─┐      {
│ id       │  │ id       │        _id: ObjectId,
│ name     │  │ user_id  │→       name: "홍길동",
│ email    │  │ total    │        email: "hong@test.com",
└──────────┘  │ items[]  │        orders: [
              └──────────┘          { total: 50000,
                                      items: [
                                        { product: "A", qty: 2 }
                                      ]
                                    }
                                  ]
                                }
```

### 임베딩 vs 참조 결정

| 기준 | 임베딩 (내포) | 참조 (분리) |
|------|-------------|-----------|
| 관계 | 1:1, 1:Few | 1:Many, M:N |
| 읽기 패턴 | 항상 함께 조회 | 독립 조회 빈번 |
| 변경 빈도 | 부모와 동시 변경 | 독립 변경 빈번 |
| 데이터 크기 | < 16MB (문서 제한) | 크기 무관 |
| 중복 | 허용 가능 | 중복 제거 필요 |

## 문자셋/콜레이션 변환

### MySQL → PostgreSQL

```sql
-- MySQL 문자셋 확인
SHOW VARIABLES LIKE 'character_set%';
SELECT character_set_name, collation_name
FROM information_schema.columns WHERE table_name = 'users';

-- PostgreSQL 콜레이션
-- MySQL utf8mb4_general_ci → PostgreSQL ICU 콜레이션
CREATE COLLATION korean_ci (
    provider = icu, locale = 'ko-u-ks-level1', deterministic = false
);

-- 대소문자 무시 비교
-- MySQL: utf8mb4_general_ci (기본)
-- PostgreSQL: citext 확장 또는 LOWER() 인덱스
CREATE EXTENSION IF NOT EXISTS citext;
ALTER TABLE users ALTER COLUMN email TYPE citext;
```

### 인코딩 변환 주의사항

| 이슈 | 증상 | 해결 |
|------|------|------|
| MySQL utf8 (3바이트) | 이모지 깨짐 | utf8mb4로 변환 후 마이그레이션 |
| Latin1 → UTF8 | 한글 깨짐 | 바이너리 중간 단계 경유 |
| EUC-KR → UTF8 | 특수 한자 손실 | 매핑 테이블 사용 |
| CP949 → UTF8 | 확장 한글 확인 | iconv 사전 검증 |

## 비가역 변환 목록

| 변환 | 비가역 이유 | 대응 |
|------|-----------|------|
| ENUM → VARCHAR | 허용 값 제약 손실 | CHECK 제약 추가 |
| UNSIGNED INT → INT | 음수 범위 확장 | 비즈니스 규칙으로 보강 |
| DATETIME → TIMESTAMPTZ | 타임존 정보 추가 필요 | 기본 TZ 가정 명시 |
| ROWID → ctid | 물리적 위치 의존 | 논리적 키로 대체 |
| Oracle DATE → PG DATE | 시간 부분 손실 | TIMESTAMP 사용 |
| CLOB → TEXT | 동작은 동일 | — |

## 타입 매핑 검증 쿼리

```sql
-- 소스 (MySQL)
SELECT column_name, data_type, column_type,
       character_maximum_length, numeric_precision, numeric_scale,
       is_nullable, column_default, extra
FROM information_schema.columns
WHERE table_schema = 'mydb' AND table_name = 'orders'
ORDER BY ordinal_position;

-- 타깃 (PostgreSQL)
SELECT column_name, data_type, udt_name,
       character_maximum_length, numeric_precision, numeric_scale,
       is_nullable, column_default
FROM information_schema.columns
WHERE table_schema = 'public' AND table_name = 'orders'
ORDER BY ordinal_position;
```
