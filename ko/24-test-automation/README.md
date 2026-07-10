# Test Automation Harness

테스트 자동화 전략 수립부터 테스트 작성, CI 통합, 커버리지 분석까지 에이전트 팀이 협업하는 하네스.

## 구조

```

├── agents/
│   ├── test-strategist.md      — 테스트 전략 (피라미드, 범위, 도구 선정)
│   ├── unit-tester.md          — 단위 테스트 (모킹, 어서션, 경계값)
│   ├── integration-tester.md   — 통합 테스트 (API, DB, 외부 서비스)
│   ├── coverage-analyst.md     — 커버리지 분석 (갭 식별, 리스크 기반 우선순위)
│   └── qa-reviewer.md          — 교차 검증 (전략↔테스트↔커버리지 정합성)
├── skills/
│   ├── test-automation/
│   │   └── SKILL.md              — 오케스트레이터 (팀 조율, 워크플로우, 에러핸들링)
│   ├── test-design-patterns/
│   │   └── SKILL.md              — 체계적 테스트 설계 패턴 가이드
│   └── mocking-strategy/
│       └── SKILL.md              — 테스트 더블 선택 및 모킹 전략 가이드
└── README.md                   — 이 파일
```

## 사용법

`/test-automation` 스킬을 트리거하거나, "테스트 자동화해줘" 같은 자연어로 요청한다.

## 산출물

모든 산출물은 `_workspace/` 디렉토리에 저장된다:
- `00_input.md` — 사용자 입력 정리
- `01_test_strategy.md` — 테스트 전략서
- `02_unit_tests.md` — 단위 테스트 코드 및 가이드
- `03_integration_tests.md` — 통합 테스트 코드 및 가이드
- `04_coverage_report.md` — 커버리지 분석 보고서
- `05_review_report.md` — 최종 리뷰 보고서
