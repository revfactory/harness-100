# Personal Finance Harness

개인 재무관리의 수입지출분석→예산설계→투자전략→절세방안→은퇴설계를 에이전트 팀이 협업하여 생성하는 하네스.

## 구조

```

├── agents/
│   ├── financial-analyst.md   — 재무 분석 (수입지출 파악, 재무건전성 진단)
│   ├── budget-planner.md      — 예산 설계 (카테고리별 예산, 저축 목표)
│   ├── investment-advisor.md  — 투자 전략 (자산배분, 포트폴리오 설계)
│   ├── tax-strategist.md      — 절세 전략 (세금 최적화, 공제 활용)
│   └── finance-reviewer.md   — 교차 검증 (분석↔예산↔투자↔절세 정합성)
├── skills/
│   ├── personal-finance/
│   │   └── SKILL.md           — 오케스트레이터 (팀 조율, 워크플로우, 에러핸들링)
│   ├── compound-interest-simulator/
│   │   └── SKILL.md           — 복리 시뮬레이터 (investment-advisor용)
│   └── financial-ratio-analyzer/
│       └── SKILL.md           — 재무 비율 분석기 (financial-analyst용)
└── README.md                  — 이 파일
```

## 사용법

`/personal-finance` 스킬을 트리거하거나, "재무 관리 도와줘" 같은 자연어로 요청한다.

## 산출물

모든 산출물은 `_workspace/` 디렉토리에 저장된다:
- `00_input.md` — 사용자 입력 정리
- `01_financial_analysis.md` — 수입지출 분석 + 재무건전성 진단
- `02_budget_plan.md` — 예산 설계 + 저축 계획
- `03_investment_strategy.md` — 투자 전략 + 포트폴리오
- `04_tax_strategy.md` — 절세 방안 + 은퇴 설계
- `05_review_report.md` — 리뷰 보고서
