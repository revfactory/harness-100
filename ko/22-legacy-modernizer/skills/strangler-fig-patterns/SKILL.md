---
name: strangler-fig-patterns
description: "레거시 시스템을 점진적으로 교체하는 Strangler Fig 패턴과 관련 마이그레이션 패턴의 상세 구현 가이드. 'strangler fig', '점진적 마이그레이션', '리팩토링 패턴', 'branch by abstraction', 'parallel run', '점진적 교체', '마이그레이션 패턴 선택' 등 레거시 전환 패턴 적용 시 이 스킬을 사용한다. refactoring-strategist와 migration-engineer의 패턴 선택·구현을 강화한다. 단, 전체 팀 오케스트레이션이나 프로젝트 관리는 이 스킬의 범위가 아니다."
---

# Strangler Fig Patterns — 점진적 마이그레이션 패턴 가이드

레거시 시스템 교체를 위한 검증된 패턴들의 상세 구현 방법론.

## 패턴 카탈로그

### 1. Strangler Fig Pattern

**적용 조건**: 모놀리스에서 새 시스템으로 점진적 전환이 필요할 때

```
┌─────────────────────────────────────────────┐
│                 라우터/프록시                  │
│  ┌──────────┐    ┌──────────────────────┐   │
│  │ 레거시    │ ←→ │ 새 시스템            │   │
│  │ (축소 중) │    │ (확장 중)            │   │
│  └──────────┘    └──────────────────────┘   │
└─────────────────────────────────────────────┘
```

**구현 단계:**

| 단계 | 작업 | 검증 기준 | 롤백 방법 |
|------|------|----------|----------|
| 1. 인터셉터 삽입 | 라우터/프록시 계층 추가 | 기존 트래픽 100% 레거시 경유 확인 | 인터셉터 제거 |
| 2. 기능 단위 추출 | 가장 독립적인 기능부터 새 서비스로 | 동일 입출력 검증 (Shadow Test) | 라우팅 복원 |
| 3. 트래픽 전환 | 카나리 → 점진적 비율 증가 | 에러율, 지연시간, 비즈니스 메트릭 | 비율 0% 복귀 |
| 4. 레거시 제거 | 이관 완료된 코드 삭제 | 전환 완료 100% 확인 | N/A |

**추출 우선순위 매트릭스:**

```
높은 비즈니스 가치
       │
  ③ Quick │ ① 최우선
    Wins  │  추출 대상
  ────────┼──────────→ 낮은 결합도
  ④ 후순위 │ ② 점진적
    보류   │  분리 후 추출
       │
낮은 비즈니스 가치
```

### 2. Branch by Abstraction

**적용 조건**: 내부 컴포넌트를 교체할 때 (같은 코드베이스 내)

```python
# Step 1: 추상화 계층 삽입
class PaymentGateway(ABC):
    @abstractmethod
    def process(self, amount: Decimal) -> PaymentResult: ...

# Step 2: 레거시 구현 래핑
class LegacyPayment(PaymentGateway):
    def process(self, amount):
        return self.old_system.charge(amount)

# Step 3: 신규 구현
class ModernPayment(PaymentGateway):
    def process(self, amount):
        return self.stripe_client.create_charge(amount)

# Step 4: 피처 플래그로 전환
gateway = ModernPayment() if feature_flag('new_payment') else LegacyPayment()
```

### 3. Parallel Run (Scientist 패턴)

**적용 조건**: 교체 전에 신규 시스템의 정확성을 검증할 때

```python
class Experiment:
    def run(self, input_data):
        control_result = self.legacy.execute(input_data)
        try:
            candidate_result = self.modern.execute(input_data)
            if not self.compare(control_result, candidate_result):
                self.report_mismatch(input_data, control_result, candidate_result)
        except Exception as e:
            self.report_error(input_data, e)
        return control_result  # 항상 레거시 결과 반환
```

**비교 전략:**

| 비교 수준 | 방법 | 허용 범위 |
|----------|------|----------|
| 정확 일치 | `==` | 0% 차이 |
| 구조적 일치 | 스키마 비교 | 필드 존재/타입 일치 |
| 의미적 일치 | 비즈니스 규칙 기반 | 도메인별 허용 오차 |
| 통계적 일치 | 집계/분포 비교 | 99.9% 일치율 이상 |

### 4. Anti-Corruption Layer (ACL)

**적용 조건**: 레거시와 신규 시스템이 공존해야 할 때 도메인 오염 방지

**ACL 구성요소:**

| 구성요소 | 역할 | 구현 |
|---------|------|------|
| Translator | 도메인 모델 변환 | DTO ↔ Domain Object 매핑 |
| Adapter | 인터페이스 변환 | 레거시 API → 현대 인터페이스 |
| Facade | 복잡성 은닉 | 레거시 다중 호출 → 단일 메서드 |

### 5. Feature Toggle 전략

```yaml
toggles:
  # Phase 1: 개발 팀만
  new_user_service: { type: permission, users: ["dev-team"] }
  # Phase 2: 카나리 (10%)
  new_user_service: { type: gradual-rollout, percentage: 10, sticky: true }
  # Phase 3: 전면 전환
  new_user_service: { type: release, enabled: true }
  # Phase 4: 토글 제거 (레거시 코드 삭제)
```

## 패턴 선택 의사결정 트리

```
레거시 교체가 필요한가?
├── 외부 시스템/서비스 교체 → Strangler Fig
├── 내부 컴포넌트 교체
│   ├── 교체 전 검증 필요 → Parallel Run + Branch by Abstraction
│   └── 교체 확신 있음 → Branch by Abstraction
├── 레거시-신규 공존 장기화 → Anti-Corruption Layer
└── 모든 경우 → Feature Toggle 병용 권장
```

## 위험 신호와 대응

| 위험 신호 | 의미 | 대응 |
|----------|------|------|
| 추출할 모듈이 10개 이상 의존 | 결합도 과다 | ACL 삽입 후 점진적 의존성 정리 |
| Parallel Run 불일치율 > 5% | 동작 차이 과다 | 비즈니스 규칙 재검증, 엣지 케이스 수집 |
| 토글 수 > 20개 동시 활성 | 토글 부채 | 정기 토글 청소 스프린트 도입 |
| 마이그레이션 6개월 이상 지속 | 병렬 운영 비용 증가 | 범위 축소 또는 부분 Big Bang 검토 |
