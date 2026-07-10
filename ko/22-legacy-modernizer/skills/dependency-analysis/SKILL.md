---
name: dependency-analysis
description: "코드베이스의 의존성 그래프를 분석하고 결합도/응집도를 정량적으로 측정하는 도구와 방법론. '의존성 분석', '결합도 측정', '순환 의존성', '모듈 결합도', '응집도 분석', '의존성 그래프', '커플링 분석' 등 코드 의존성 관련 분석에 이 스킬을 사용한다. legacy-analyzer와 refactoring-strategist의 의존성 분석 역량을 강화한다. 단, 전체 파이프라인 오케스트레이션은 이 스킬의 범위가 아니다."
---

# Dependency Analysis — 의존성 그래프 분석 도구

코드 의존성의 정량적 측정과 시각화를 위한 방법론 및 도구 가이드.

## 의존성 메트릭 체계

### 1. 결합도 메트릭 (Coupling Metrics)

| 메트릭 | 공식 | 해석 | 위험 임계값 |
|--------|------|------|-----------|
| **Ca (Afferent Coupling)** | 나를 의존하는 패키지 수 | 높으면 변경 파급 큼 | > 20 |
| **Ce (Efferent Coupling)** | 내가 의존하는 패키지 수 | 높으면 불안정 | > 20 |
| **I (Instability)** | Ce / (Ca + Ce) | 0=안정, 1=불안정 | 중간 지대(0.3~0.7) 경고 |
| **D (Distance)** | \|A + I - 1\| | 주계열에서의 거리 | > 0.3 |

**안정 의존성 원칙 (SDP) 검증:**
```
의존 방향: 불안정 → 안정 (올바름)
위반: 안정 → 불안정 (위험 — 의존성 역전 필요)
```

### 2. 응집도 메트릭

| 메트릭 | 측정 대상 | 양호 기준 |
|--------|----------|----------|
| **LCOM4** | 클래스 내 연결 컴포넌트 수 | = 1 |
| **TCC** (Tight Class Cohesion) | 직접 연결 메서드 비율 | > 0.5 |
| **H** (Henderson-Sellers) | 패키지 내부 관계 비율 | > 0.7 |

### 3. 순환 의존성 탐지 — Tarjan SCC 알고리즘

```python
def find_cycles(graph):
    """Tarjan SCC로 순환 의존성 그룹 탐지"""
    index_counter, stack, result = [0], [], []
    lowlink, index, on_stack = {}, {}, {}

    def strongconnect(v):
        index[v] = lowlink[v] = index_counter[0]
        index_counter[0] += 1
        on_stack[v] = True
        stack.append(v)
        for w in graph.get(v, []):
            if w not in index:
                strongconnect(w)
                lowlink[v] = min(lowlink[v], lowlink[w])
            elif on_stack.get(w):
                lowlink[v] = min(lowlink[v], index[w])
        if lowlink[v] == index[v]:
            component = set()
            while True:
                w = stack.pop()
                on_stack[w] = False
                component.add(w)
                if w == v: break
            if len(component) > 1:
                result.append(component)
    for v in graph:
        if v not in index: strongconnect(v)
    return result
```

### 4. 순환 해소 패턴

| 패턴 | 적용 상황 | 방법 |
|------|----------|------|
| **의존성 역전 (DIP)** | A↔B 양방향 | 인터페이스 추출, 방향 통일 |
| **이벤트 기반 분리** | A→B→A 콜백 | 이벤트 버스로 간접 통신 |
| **중재자 패턴** | A↔B↔C 복잡 순환 | Mediator 중앙 조율 |
| **공통 모듈 추출** | A↔B 공유 로직 | 공통부를 C로 추출 |

## 언어별 도구

### JavaScript/TypeScript
```bash
npx madge --image graph.svg src/        # 의존성 그래프
npx madge --circular src/               # 순환 탐지
npx depcheck                            # 미사용 의존성
```

### Python
```bash
pipdeptree --graph-output svg > deps.svg
pydeps src/mypackage --max-bacon=2
```

### Java/Kotlin
```bash
./gradlew dependencies --configuration runtimeClasspath
# ArchUnit으로 아키텍처 규칙 테스트
```

## 변경 영향도 분석 (CIA)

```
변경 파일: UserService.java
├── 직접 영향 (깊이 1): UserController, OrderService, AuthService
├── 간접 영향 (깊이 2): OrderController, PaymentService
└── 테스트 영향: UserServiceTest, OrderIntegrationTest
→ 추정 파급 범위: 파일 8개, 테스트 3개
```

## 아키텍처 피트니스 함수

```python
DEPENDENCY_RULES = {
    "domain → infrastructure 금지": {
        "from": "domain/**", "to_not": "infrastructure/**", "severity": "ERROR"
    },
    "controller → repository 직접 접근 금지": {
        "from": "controller/**", "to_not": "repository/**", "severity": "ERROR"
    },
}
```

## 보고서 템플릿

```markdown
# 의존성 분석 보고서

## 요약
- 총 모듈 수: N개 | 평균 결합도(Ce): X.X | 순환 그룹: N개

## 모듈별 메트릭
| 모듈 | Ca | Ce | I | A | D | LCOM4 | 등급 |

## 순환 의존성
- 그룹 1: [A, B, C] — 해소 전략: DIP

## 핫스팟 (높은 Ca + 높은 Ce)
- ModuleX: Ca=25, Ce=18 — 변경 파급 범위 과다

## 권고사항
1. [긴급] 순환 의존성 해소
2. [중요] 핫스팟 모듈 분리
3. [개선] 의존성 규칙 CI 자동화
```
