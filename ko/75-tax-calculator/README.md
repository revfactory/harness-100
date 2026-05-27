# Tax Calculator Harness

세금 계산·절세 전략의 소득분석→공제항목최적화→세액계산→절세시뮬레이션→신고자료준비를 에이전트 팀이 협업하여 생성하는 하네스.

## 구조

```

├── agents/
│   ├── income-analyst.md       — 소득 분석 (소득유형분류, 과세표준산출, 세율적용)
│   ├── deduction-optimizer.md  — 공제 최적화 (소득공제, 세액공제, 감면항목 극대화)
│   ├── tax-engine.md           — 세액 계산 (산출세액, 결정세액, 납부/환급 산출)
│   └── strategy-advisor.md    — 절세 전략 (시뮬레이션, 절세방안, 신고자료 준비)
├── skills/
│   ├── tax-calculator/
│   │   └── SKILL.md           — 오케스트레이터 (팀 조율, 워크플로우, 에러핸들링)
│   ├── deduction-optimizer-engine/
│   │   └── SKILL.md           — 공제 최적화 엔진 (deduction-optimizer용)
│   └── tax-bracket-simulator/
│       └── SKILL.md           — 세율 구간 시뮬레이터 (tax-engine, strategy-advisor용)
└── README.md                  — 이 파일
```

## 사용법

`/tax-calculator` 스킬을 트리거하거나, "세금 계산해줘" 같은 자연어로 요청한다.

## 산출물

모든 산출물은 `_workspace/` 디렉토리에 저장된다:
- `00_input.md` — 사용자 입력 정리
- `01_income_analysis.md` — 소득 분석 보고서
- `02_deduction_optimization.md` — 공제 최적화 보고서
- `03_tax_calculation.md` — 세액 계산서
- `04_tax_strategy.md` — 절세 전략 및 시뮬레이션
- `05_filing_preparation.md` — 신고 자료 준비 가이드
