# Real Estate Analyst Harness

부동산 분석 하네스. 시장조사, 입지분석, 수익성 분석, 리스크 평가, 투자 보고서까지 에이전트 팀이 협업하여 생성한다.

## 구조

```

├── agents/
│   ├── market-researcher.md      — 시장조사 (거시경제, 지역시장, 공급·수요)
│   ├── location-analyst.md       — 입지분석 (교통, 학군, 상권, 개발호재)
│   ├── profitability-analyst.md  — 수익성 분석 (임대수익률, 현금흐름, IRR)
│   ├── risk-assessor.md          — 리스크 평가 (규제, 시장, 유동성 리스크)
│   └── report-writer.md          — 투자 보고서 (종합판단, 투자의견)
├── skills/
│   ├── real-estate-analyst/
│   │   └── SKILL.md              — 오케스트레이터 (팀 조율, 워크플로우, 에러핸들링)
│   ├── cap-rate-calculator/
│   │   └── SKILL.md              — 수익률 계산기 (profitability-analyst 확장)
│   └── location-scoring/
│       └── SKILL.md              — 입지 평가 스코어카드 (location-analyst 확장)
└── README.md                     — 이 파일
```

## 사용법

`/real-estate-analyst` 스킬을 트리거하거나, "부동산 분석해줘" 같은 자연어로 요청한다.

## 산출물

모든 산출물은 `_workspace/` 디렉토리에 저장된다:
- `00_input.md` — 분석 대상 및 투자 조건 정리
- `01_market_research.md` — 시장조사 보고서
- `02_location_analysis.md` — 입지분석 보고서
- `03_profitability_analysis.md` — 수익성 분석 보고서
- `04_risk_assessment.md` — 리스크 평가 보고서
- `05_investment_report.md` — 종합 투자 보고서
