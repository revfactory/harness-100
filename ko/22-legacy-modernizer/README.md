# Legacy Modernizer Harness

레거시 코드베이스를 현대적 아키텍처로 전환하는 에이전트 팀 하네스. 분석→리팩토링전략→마이그레이션→검증 파이프라인을 자동화한다.

## 구조

```

├── agents/
│   ├── legacy-analyzer.md        — 레거시 분석 (기술부채 식별, 의존성 매핑, 복잡도 측정)
│   ├── refactoring-strategist.md — 리팩토링 전략 (패턴 선정, 우선순위, 로드맵)
│   ├── migration-engineer.md     — 마이그레이션 실행 (코드 변환, API 현대화, 프레임워크 전환)
│   ├── regression-tester.md      — 회귀 테스트 (동작 보존 검증, 성능 비교, 호환성 확인)
│   └── modernization-reviewer.md — 교차 검증 (분석↔전략↔마이그레이션↔테스트 정합성)
├── skills/
│   ├── legacy-modernizer/
│   │   └── SKILL.md              — 오케스트레이터 (팀 조율, 워크플로우, 에러핸들링)
│   ├── strangler-fig-patterns/
│   │   └── SKILL.md              — 점진적 마이그레이션 패턴 가이드
│   └── dependency-analysis/
│       └── SKILL.md              — 의존성 그래프 분석 도구
└── README.md                     — 이 파일
```

## 사용법

`/legacy-modernizer` 스킬을 트리거하거나, "레거시 코드 현대화해줘" 같은 자연어로 요청한다.

## 산출물

모든 산출물은 `_workspace/` 디렉토리에 저장된다:
- `00_input.md` — 사용자 입력 정리
- `01_legacy_analysis.md` — 레거시 분석 보고서
- `02_refactoring_strategy.md` — 리팩토링 전략서
- `03_migration_plan.md` — 마이그레이션 실행 계획 및 코드
- `04_test_report.md` — 회귀 테스트 보고서
- `05_review_report.md` — 최종 리뷰 보고서
