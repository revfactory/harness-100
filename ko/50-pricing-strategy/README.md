# Pricing Strategy Harness

가격 전략 수립: 원가분석→경쟁가격→가치기반→시뮬레이션을 에이전트 팀이 협업하여 생성하는 하네스.

## 구조

```

├── agents/
│   ├── cost-analyst.md          — 원가 분석 (직접비·간접비, BEP, 마진 구조)
│   ├── competitive-analyst.md   — 경쟁 가격 분석 (시장 포지셔닝, 가격 벤치마크)
│   ├── value-assessor.md        — 가치 기반 가격 (WTP, 가치 드라이버, 세그먼트)
│   ├── pricing-simulator.md     — 가격 시뮬레이션 (시나리오, 탄력성, P&L 영향)
│   └── pricing-reviewer.md      — 교차 검증 (원가↔경쟁↔가치↔시뮬레이션 정합성)
├── skills/
│   ├── pricing-strategy/
│       └── SKILL.md             — 오케스트레이터 (팀 조율, 워크플로우, 에러핸들링)
│   ├── psm-analyzer/
│   │   └── SKILL.md             — PSM 분석 (Van Westendorp, 최적 가격, 세그먼트)
│   └── price-elasticity-calculator/
│       └── SKILL.md             — 가격 탄력성 (PED/XED, 최적 가격, 시뮬레이션)
└── README.md                    — 이 파일
```

## 사용법

`/pricing-strategy` 스킬을 트리거하거나, "가격 전략 세워줘" 같은 자연어로 요청한다.

## 산출물

모든 산출물은 `_workspace/` 디렉토리에 저장된다:
- `00_input.md` — 사용자 입력 정리
- `01_cost_analysis.md` — 원가 분석서
- `02_competitive_pricing.md` — 경쟁 가격 분석서
- `03_value_pricing.md` — 가치 기반 가격 분석서
- `04_pricing_simulation.md` — 가격 시뮬레이션 보고서
- `05_review_report.md` — 리뷰 보고서
