---
name: madr-template-engine
description: "MADR(Markdown Any Decision Record) 표준 포맷으로 ADR을 구조화하고 상태 관리를 체계화하는 전문 스킬. adr-author와 impact-tracker가 표준 포맷의 ADR 문서를 작성하고 결정 이력을 추적할 때 활용한다. 'MADR 포맷', 'ADR 템플릿', '결정 상태', 'ADR 번호 체계', '결정 이력' 등의 맥락에서 자동 적용한다. 단, Git 커밋 훅 설정이나 CI/CD 파이프라인 구축은 이 스킬의 범위가 아니다."
---

# MADR Template Engine — ADR 표준 포맷 도구

adr-author, impact-tracker 에이전트의 ADR 문서화 역량을 강화하는 전문 스킬.

## 적용 대상 에이전트

- **adr-author** — MADR 포맷 ADR 문서 작성
- **impact-tracker** — ADR 간 의존관계 추적, 상태 관리

## MADR 표준 템플릿

```markdown
# ADR-{NNN}: {결정 제목}

## 상태

{Proposed | Accepted | Deprecated | Superseded by ADR-XXX}

## 날짜

{YYYY-MM-DD}

## 컨텍스트

{이 결정을 하게 된 배경, 문제 상황, 제약 조건}

## 의사결정 드라이버

* {드라이버 1: 예) 응답 시간 200ms 이내 필요}
* {드라이버 2: 예) 팀 규모 5명의 학습 곡선}
* {드라이버 3: 예) 예산 제약 월 100만원}

## 고려한 대안

### 대안 1: {대안명}

{설명}

* 장점: {좋은 점, 왜냐하면 ...}
* 장점: {좋은 점, 왜냐하면 ...}
* 단점: {나쁜 점, 왜냐하면 ...}

### 대안 2: {대안명}

{설명}

* 장점: {좋은 점, 왜냐하면 ...}
* 단점: {나쁜 점, 왜냐하면 ...}
* 단점: {나쁜 점, 왜냐하면 ...}

### 대안 3: {대안명}

{설명 - 최소 3개 대안 비교}

## 결정

대안 {N}: {대안명}을 선택한다.

### 선택 근거

{왜 이 대안을 선택했는지 구체적으로}

### 기각 근거

* 대안 {X}를 기각한 이유: {이유}
* 대안 {Y}를 기각한 이유: {이유}

## 결과

### 긍정적 영향

* {예상되는 긍정적 결과}

### 부정적 영향

* {감수해야 할 트레이드오프}

### 후속 조치

* [ ] {필요한 후속 작업 1}
* [ ] {필요한 후속 작업 2}

## 관련 ADR

* ADR-{XXX}: {관련 결정}
* ADR-{YYY}: {이 결정에 영향받는 결정}
```

## ADR 상태 관리

### 상태 전이도

```
[Proposed] → [Accepted] → [Deprecated]
                    ↓
              [Superseded by ADR-XXX]
```

| 상태 | 의미 | 조건 |
|------|------|------|
| Proposed | 검토 중 | 작성 직후 |
| Accepted | 채택됨 | 이해관계자 합의 |
| Deprecated | 더 이상 유효하지 않음 | 전제 변경 |
| Superseded | 새 ADR로 대체됨 | 대안 재평가 |

## ADR 번호 체계

### 번호 부여 규칙

```
ADR-{순번}: {카테고리 코드}-{결정 제목}

카테고리 코드:
  ARCH - 아키텍처 패턴
  DATA - 데이터 저장/처리
  INFRA - 인프라/배포
  SEC - 보안
  API - API 설계
  UI - 프론트엔드
  PROC - 프로세스/방법론
```

### ADR 디렉토리 구조

```
docs/adr/
├── 0001-arch-monolith-vs-microservice.md
├── 0002-data-postgresql-selection.md
├── 0003-infra-kubernetes-adoption.md
├── 0004-api-rest-vs-graphql.md
├── index.md  ← ADR 목록 및 상태 대시보드
└── template.md
```

## ADR 작성 품질 체크리스트

### 필수 요소

- [ ] 컨텍스트가 배경을 충분히 설명하는가?
- [ ] 의사결정 드라이버가 명확한가?
- [ ] 3개 이상 대안을 비교했는가?
- [ ] 각 대안의 장단점이 구체적인가?
- [ ] 선택 근거가 논리적인가?
- [ ] 기각 근거가 명시되어 있는가?
- [ ] 트레이드오프가 솔직하게 기술되었는가?
- [ ] 후속 조치가 구체적인가?

### 흔한 실수

| 실수 | 개선 방법 |
|------|----------|
| 결정만 있고 맥락 없음 | "왜 이 결정이 필요했는가" 먼저 작성 |
| 대안 1개만 기술 | 기각된 대안도 반드시 기록 |
| 장점만 기술 | 단점과 트레이드오프 솔직히 기록 |
| 너무 길거나 짧음 | 1-3페이지 권장 |
| 업데이트 안 됨 | 상태 전이 시 반드시 업데이트 |

## ADR 의존성 그래프 (impact-tracker용)

```markdown
### ADR 의존성 맵

ADR-001 (마이크로서비스)
  ├── ADR-002 (서비스 간 통신: gRPC)
  ├── ADR-003 (서비스 디스커버리: Consul)
  ├── ADR-004 (분산 추적: Jaeger)
  └── ADR-005 (API Gateway: Kong)
       └── ADR-006 (인증: OAuth2 + JWT)

영향 분석:
ADR-001이 Deprecated 되면 → ADR-002~006 모두 재검토 필요
```
