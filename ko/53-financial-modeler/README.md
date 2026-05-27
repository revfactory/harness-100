# Financial Modeler Harness

수익 모델, 비용 구조, 시나리오 분석, 밸류에이션까지 재무 모델링 전 과정을 에이전트 팀이 협업하여 생성하는 하네스.

## 구조

```

├── agents/
│   ├── revenue-modeler.md        — 수익 모델 설계
│   ├── cost-analyst.md           — 비용 구조 분석
│   ├── scenario-planner.md       — 시나리오 분석
│   ├── valuation-expert.md       — 밸류에이션
│   └── model-reviewer.md         — 교차 검증
├── skills/
│   ├── financial-modeler/
│   │   └── SKILL.md              — 오케스트레이터
│   ├── dcf-valuation/
│   │   └── SKILL.md              — DCF 밸류에이션 (WACC, FCFF, 터미널 밸류)
│   ├── sensitivity-analysis/
│   │   └── SKILL.md              — 민감도 분석 (토네이도, 시나리오 테이블, 브레이크이븐)
│   └── unit-economics/
│       └── SKILL.md              — 단위 경제학 (LTV/CAC, 공헌이익, 코호트 분석)
└── README.md                     — 이 파일
```

## 사용법

`/financial-modeler` 스킬을 트리거하거나 자연어로 요청한다.
