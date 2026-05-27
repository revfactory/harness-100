# Microservice Designer Harness

마이크로서비스 아키텍처를 설계·분해·통신·모니터링하는 에이전트 팀 하네스. 도메인 분석부터 관측성 설계까지 풀 파이프라인을 자동화한다.

## 구조

```

├── agents/
│   ├── domain-analyst.md        — 도메인 분석 (바운디드 컨텍스트, 이벤트 스토밍, 애그리거트 식별)
│   ├── service-architect.md     — 서비스 설계 (API 계약, 데이터 소유권, 배포 단위)
│   ├── communication-designer.md — 통신 설계 (동기/비동기, 이벤트 버스, API 게이트웨이)
│   ├── observability-engineer.md — 관측성 설계 (메트릭, 로깅, 트레이싱, 알림)
│   └── architecture-reviewer.md  — 교차 검증 (도메인↔서비스↔통신↔관측성 정합성)
├── skills/
│   ├── microservice-designer/
│   │   └── SKILL.md              — 오케스트레이터 (팀 조율, 워크플로우, 에러핸들링)
│   ├── ddd-context-mapping/
│   │   └── SKILL.md              — 바운디드 컨텍스트·이벤트 스토밍·컨텍스트 맵 가이드
│   └── distributed-patterns/
│       └── SKILL.md              — 분산 시스템 패턴(Saga, CQRS, Circuit Breaker) 가이드
└── README.md                     — 이 파일
```

## 사용법

`/microservice-designer` 스킬을 트리거하거나, "마이크로서비스 아키텍처 설계해줘" 같은 자연어로 요청한다.

## 산출물

모든 산출물은 `_workspace/` 디렉토리에 저장된다:
- `00_input.md` — 사용자 입력 정리
- `01_domain_analysis.md` — 도메인 분석 보고서
- `02_service_design.md` — 서비스 설계서
- `03_communication_design.md` — 통신 설계서
- `04_observability_design.md` — 관측성 설계서
- `05_review_report.md` — 최종 리뷰 보고서
