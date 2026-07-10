---
name: mocking-strategy
description: "테스트 더블(Mock, Stub, Spy, Fake) 선택과 효과적인 모킹 전략 가이드. '모킹', 'Mock', 'Stub', 'Spy', 'Fake', '테스트 더블', '의존성 격리', '외부 서비스 모킹', 'DB 모킹' 등 테스트 격리 전략 수립 시 이 스킬을 사용한다. unit-tester와 integration-tester의 모킹 설계 역량을 강화한다. 단, 테스트 전략 전체 수립이나 CI 연동은 이 스킬의 범위가 아니다."
---

# Mocking Strategy — 테스트 더블 선택 및 모킹 전략 가이드

의존성을 효과적으로 격리하여 안정적인 테스트를 만드는 방법론.

## 테스트 더블 유형 비교

| 유형 | 목적 | 동작 | 검증 대상 |
|------|------|------|----------|
| **Dummy** | 파라미터 채움 | 아무것도 안 함 | 사용되지 않음 |
| **Stub** | 고정 응답 제공 | 미리 정의된 값 반환 | 상태(결과값) |
| **Spy** | 호출 기록 | 실제 동작 + 기록 | 상호작용(호출 횟수/인자) |
| **Mock** | 기대 동작 정의 | 기대에 맞으면 통과 | 상호작용(호출 순서/인자) |
| **Fake** | 경량 구현 | 동작하는 간소화 구현 | 상태(통합 수준) |

## 선택 의사결정 트리

```
외부 의존성을 격리해야 한다
├── 응답값만 필요 → Stub
├── 호출 여부/횟수 확인 필요 → Mock 또는 Spy
│   ├── 실제 동작도 필요 → Spy
│   └── 실제 동작 불필요 → Mock
├── 동작하는 경량 구현 필요 → Fake
│   └── 예: InMemoryRepository, FakeEmailSender
└── 그냥 타입만 맞추면 됨 → Dummy
```

## 계층별 모킹 전략

### Repository/DB 계층
```python
# Stub: 고정 데이터 반환
stub_repo = Mock(spec=UserRepository)
stub_repo.find_by_id.return_value = User(id=1, name="테스트")

# Fake: 인메모리 구현
class FakeUserRepository(UserRepository):
    def __init__(self):
        self._store = {}
    def save(self, user):
        self._store[user.id] = user
    def find_by_id(self, id):
        return self._store.get(id)
```

### 외부 API 계층
```python
# HTTP 모킹 (responses / httpx_mock)
@responses.activate
def test_payment_api():
    responses.add(
        responses.POST, "https://api.pg.com/charge",
        json={"status": "success", "tx_id": "TX123"},
        status=200
    )
    result = payment_service.charge(10000)
    assert result.tx_id == "TX123"

# 타임아웃 / 에러 시뮬레이션
responses.add(
    responses.POST, "https://api.pg.com/charge",
    body=ConnectionError("timeout")
)
```

### 메시지 큐 계층
```python
class FakeMessageBroker(MessageBroker):
    def __init__(self):
        self.published = []
    def publish(self, topic, message):
        self.published.append((topic, message))
    def assert_published(self, topic, expected_count=1):
        actual = [m for t, m in self.published if t == topic]
        assert len(actual) == expected_count
```

### 시간/날짜 계층
```python
# 시간 의존성 주입
class OrderService:
    def __init__(self, clock=datetime.now):
        self.clock = clock

# 테스트에서 고정 시간
fixed_time = lambda: datetime(2024, 1, 1, 12, 0, 0)
service = OrderService(clock=fixed_time)
```

## 모킹 안티패턴과 해결

| 안티패턴 | 문제 | 해결 |
|---------|------|------|
| **과도한 모킹** | 구현 상세에 테스트가 결합 | 동작 기반 테스트로 전환 |
| **모킹 사슬** | `mock.a.b.c.d()` 깊은 모킹 | 디미터 법칙 위반 — 코드 리팩토링 |
| **모킹 지옥** | 모든 것을 Mock | Fake로 대체, 통합 테스트 추가 |
| **반복 설정** | 모든 테스트에서 같은 Mock 설정 | Fixture/Builder 패턴 도입 |
| **Mock 검증 과다** | `verify(mock, times(1)).method()` 남용 | 필수 상호작용만 검증 |

## 프레임워크별 모킹 도구

### Python
```python
# unittest.mock
from unittest.mock import Mock, patch, MagicMock
# pytest-mock
def test_something(mocker):
    mocker.patch('module.Class.method', return_value=42)
# responses (HTTP)
# freezegun (시간)
```

### JavaScript/TypeScript
```typescript
// Jest
jest.mock('./userService');
jest.spyOn(service, 'findUser').mockResolvedValue(mockUser);
// MSW (HTTP — 서비스 워커)
server.use(rest.get('/api/users', (req, res, ctx) => res(ctx.json([]))));
// Sinon (범용)
sinon.stub(db, 'query').resolves([]);
```

### Java/Kotlin
```java
// Mockito
@Mock UserRepository repo;
when(repo.findById(1L)).thenReturn(Optional.of(user));
verify(repo, times(1)).save(any(User.class));
// WireMock (HTTP)
// Testcontainers (실제 DB/Redis)
```

## Testcontainers 활용 (Fake 대안)

```python
# 실제 DB를 도커로 격리 — Fake보다 현실적
@pytest.fixture
def postgres():
    with PostgresContainer("postgres:16") as pg:
        engine = create_engine(pg.get_connection_url())
        yield engine

def test_user_crud(postgres):
    # 실제 PostgreSQL에서 테스트
    repo = UserRepository(postgres)
    repo.save(User(name="test"))
    assert repo.find_by_name("test") is not None
```

## 모킹 수준 결정 매트릭스

| 테스트 유형 | DB | 외부 API | 메시지 큐 | 파일 시스템 |
|------------|-----|---------|----------|-----------|
| 단위 테스트 | Stub/Mock | Stub | Mock | Stub |
| 통합 테스트 | Fake/Container | WireMock | Fake | tmpdir |
| E2E 테스트 | 실제 DB | Sandbox API | 실제 큐 | 실제 FS |
