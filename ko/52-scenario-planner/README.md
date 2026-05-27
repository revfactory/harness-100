# Scenario Planner Harness

불확실한 환경에서 핵심 변수를 정의하고, 시나리오 매트릭스를 구성하여 영향 분석과 대응 전략을 수립하는 에이전트 팀 하네스.

## 구조

```

├── agents/
│   ├── variable-analyst.md       — 핵심 변수 식별 및 불확실성 평가
│   ├── scenario-designer.md      — 시나리오 매트릭스 설계 및 시나리오 서사 작성
│   ├── impact-assessor.md        — 시나리오별 영향 분석 및 정량/정성 평가
│   ├── strategy-architect.md     — 대응 전략 수립 및 의사결정 프레임워크 설계
│   └── integration-reviewer.md   — 교차 검증, 논리적 정합성 확인, 최종 문서 통합
├── skills/
│   ├── scenario-planner/
│   │   └── SKILL.md              — 오케스트레이터 (팀 조율, 워크플로우, 에러 핸들링)
│   ├── steep-framework/
│   │   └── SKILL.md              — STEEP 거시환경 분석 (6대 차원 스캐닝, 불확실성-영향력 매트릭스)
│   ├── scenario-narrative-engine/
│   │   └── SKILL.md              — 시나리오 서사 구성 (2x2 매트릭스, 타임라인, 조기 경보 신호)
│   └── decision-trigger-mapper/
│       └── SKILL.md              — 의사결정 트리거 맵 (리얼옵션, 전략 포트폴리오, 실행 로드맵)
└── README.md                     — 이 파일
```

## 사용법

`/scenario-planner` 스킬을 트리거하거나, "시나리오 분석해줘", "미래 시나리오 기획" 같은 자연어로 요청한다.

## 산출물

모든 산출물은 `_workspace/` 디렉토리에 저장된다:
- `00_input.md` — 사용자 입력 정리
- `01_variable_analysis.md` — 핵심 변수 분석서
- `02_scenario_matrix.md` — 시나리오 매트릭스 및 서사
- `03_impact_assessment.md` — 영향 분석 보고서
- `04_response_strategy.md` — 대응 전략서
- `05_decision_document.md` — 통합 의사결정 문서
- `06_review_report.md` — 리뷰 보고서
