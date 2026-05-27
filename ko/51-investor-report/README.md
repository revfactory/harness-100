# Investor Report Harness

투자자 보고서 생성: 재무실적분석→KPI대시보드→시장동향→전략업데이트→리스크공시를 에이전트 팀이 협업하여 생성하는 하네스.

## 구조

```

├── agents/
│   ├── financial-analyst.md     — 재무 분석 (P&L, 현금흐름, 핵심 재무지표)
│   ├── kpi-designer.md          — KPI 대시보드 (핵심 메트릭, 트렌드, 벤치마크)
│   ├── market-analyst.md        — 시장 동향 (산업 트렌드, 경쟁, 규제)
│   ├── strategy-updater.md      — 전략 업데이트 (진행 상황, 로드맵, 리스크 공시)
│   └── ir-reviewer.md           — 교차 검증 (재무↔KPI↔시장↔전략 정합성)
├── skills/
│   ├── investor-report/
│   │   └── SKILL.md             — 오케스트레이터 (팀 조율, 워크플로우, 에러핸들링)
│   ├── financial-ratio-analyzer/
│   │   └── SKILL.md             — 재무비율 심층 분석 (DuPont, SaaS 메트릭, 5대 비율)
│   ├── kpi-benchmark-engine/
│   │   └── SKILL.md             — KPI 벤치마크 (산업별 벤치마크, SMART-R, 피라미드)
│   └── ir-narrative-builder/
│       └── SKILL.md             — IR 서사 구성 (Equity Story, 투자자별 톤, EBITDA Bridge)
└── README.md                    — 이 파일
```

## 사용법

`/investor-report` 스킬을 트리거하거나, "투자자 보고서 만들어줘" 같은 자연어로 요청한다.

## 산출물

모든 산출물은 `_workspace/` 디렉토리에 저장된다:
- `00_input.md` — 사용자 입력 정리
- `01_financial_analysis.md` — 재무 실적 분석서
- `02_kpi_dashboard.md` — KPI 대시보드
- `03_market_trends.md` — 시장 동향 보고서
- `04_strategy_update.md` — 전략 업데이트 및 리스크 공시
- `05_review_report.md` — 리뷰 보고서
- `06_investor_report_final.md` — 최종 통합 보고서
