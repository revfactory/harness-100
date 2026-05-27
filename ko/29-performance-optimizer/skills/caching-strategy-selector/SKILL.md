---
name: caching-strategy-selector
description: "캐싱 전략(Cache Aside, Write Through, Write Behind 등) 선택 매트릭스와 Redis/Memcached 활용, TTL 설계, 캐시 무효화 패턴 가이드. '캐싱 전략', 'Redis', '캐시 무효화', 'TTL', 'Cache Aside', 'Write Through', 'CDN 캐싱', '캐시 스탬피드' 등 캐싱 설계 시 이 스킬을 사용한다. optimization-engineer의 캐싱 설계 역량을 강화한다. 단, 전체 성능 프로파일링이나 벤치마크는 이 스킬의 범위가 아니다."
---

# Caching Strategy Selector — 캐싱 전략 선택 가이드

적절한 캐싱 전략을 선택하고 효과적으로 구현하는 방법론.

## 캐싱 전략 비교

### 1. Cache Aside (Lazy Loading)

```
읽기: App → Cache 확인 → 미스 → DB 조회 → Cache 저장 → 반환
쓰기: App → DB 저장 → Cache 무효화(삭제)
```

| 장점 | 단점 |
|------|------|
| 가장 범용적 | 첫 요청은 항상 미스 |
| 캐시 장애 시 DB 폴백 | 읽기-수정-쓰기 경쟁 조건 |
| 필요한 데이터만 캐시 | 데이터 불일치 윈도우 존재 |

### 2. Write Through

```
쓰기: App → Cache 저장 → DB 저장 (동기)
읽기: App → Cache 확인 → 항상 히트
```

| 장점 | 단점 |
|------|------|
| 읽기-쓰기 일관성 | 쓰기 지연 증가 |
| 캐시 항상 최신 | 사용하지 않는 데이터도 캐시 |

### 3. Write Behind (Write Back)

```
쓰기: App → Cache 저장 → 비동기 배치로 DB 저장
읽기: App → Cache 확인 → 항상 히트
```

| 장점 | 단점 |
|------|------|
| 쓰기 성능 극대화 | 캐시 장애 시 데이터 유실 |
| DB 부하 평탄화 | 구현 복잡 |

### 전략 선택 매트릭스

| 요구사항 | Cache Aside | Write Through | Write Behind |
|---------|------------|---------------|-------------|
| 읽기 집중 | ★★★ | ★★ | ★★ |
| 쓰기 집중 | ★ | ★ | ★★★ |
| 일관성 중요 | ★★ | ★★★ | ★ |
| 성능 중요 | ★★ | ★ | ★★★ |
| 구현 단순 | ★★★ | ★★ | ★ |
| 데이터 유실 불가 | ★★★ | ★★★ | ★ |

## 캐시 무효화 패턴

### 1. TTL (Time-To-Live)

```python
# TTL 설정 가이드
CACHE_TTL = {
    "user_profile": 300,      # 5분 — 자주 변경되지 않음
    "product_list": 60,       # 1분 — 중간 변경 빈도
    "stock_count": 10,        # 10초 — 자주 변경
    "config": 3600,           # 1시간 — 거의 변경 안 됨
    "session": 86400,         # 24시간 — 세션 수명
}

# Jitter 추가 (캐시 스탬피드 방지)
import random
ttl = base_ttl + random.randint(0, base_ttl // 10)
```

### 2. Event-Based Invalidation

```python
# 이벤트 기반 무효화
@event_handler("user.updated")
def invalidate_user_cache(event):
    cache.delete(f"user:{event.user_id}")
    cache.delete(f"user_profile:{event.user_id}")
    # 관련 목록 캐시도 무효화
    cache.delete("user_list:page:*")
```

### 3. Version-Based

```python
# 버전 키로 한꺼번에 무효화
version = cache.get("product_version") or 1
key = f"product_list:v{version}"
# 무효화: 버전만 증가
cache.incr("product_version")
```

## 캐시 문제 해결

### Cache Stampede (Thundering Herd)

```
문제: 캐시 만료 시 동시 요청이 모두 DB에 접근
해결:

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
   # TTL 만료 후에도 stale 데이터 반환하면서 백그라운드 갱신

3. Probabilistic Early Expiry
   delta = ttl * beta * log(random())
   if now() - fetched_at > ttl + delta:
       refresh()
```

### Cache Penetration

```
문제: 존재하지 않는 키 반복 요청 → 매번 DB 접근
해결:
1. 블룸 필터: 존재 가능성 사전 체크
2. 빈 결과 캐싱: cache.set(key, NULL, ttl=60)
3. 요청 검증: 유효하지 않은 키 사전 차단
```

### Cache Avalanche

```
문제: 대량 캐시가 동시 만료 → DB 과부하
해결:
1. TTL 분산: TTL + random jitter
2. 단계적 만료: 중요도별 다른 TTL
3. 예열(Warm-up): 배포 시 캐시 사전 적재
```

## 캐시 계층 설계

```
L1: 로컬 캐시 (인프로세스)
    ├── 용량: ~100MB
    ├── 속도: ~0.1ms
    └── 적합: 설정, 상수, 빈번한 읽기

L2: 분산 캐시 (Redis/Memcached)
    ├── 용량: ~10GB
    ├── 속도: ~1ms
    └── 적합: 세션, 프로필, 목록

L3: CDN 캐시 (CloudFront/Cloudflare)
    ├── 용량: 무제한
    ├── 속도: 엣지에서 ~5ms
    └── 적합: 정적 자산, API 응답

L4: 브라우저 캐시
    ├── Cache-Control: max-age, stale-while-revalidate
    └── ETag / Last-Modified
```

## Redis 데이터 구조 선택

| 구조 | 적합 | 예시 |
|------|------|------|
| String | 단순 키-값 | 세션, 설정, 카운터 |
| Hash | 객체 필드 | 사용자 프로필 |
| List | 최근 목록 | 최근 본 상품 (LPUSH + LTRIM) |
| Set | 고유 집합 | 온라인 사용자 |
| Sorted Set | 랭킹 | 리더보드, 트렌딩 |
| HyperLogLog | 근사 카운팅 | UV 카운트 |
