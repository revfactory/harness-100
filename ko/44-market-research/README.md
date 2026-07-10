# Market Research Harness

시장 조사의 산업분석→경쟁분석→소비자조사→트렌드→보고서를 에이전트 팀이 협업하여 생성하는 하네스.

## 구조

```

├── agents/
│   ├── industry-analyst.md    — 산업 분석가 (시장 규모, 성장률, 밸류체인, 규제)
│   ├── competitor-analyst.md  — 경쟁 분석가 (경쟁사 매핑, 포지셔닝, SWOT)
│   ├── consumer-analyst.md    — 소비자 분석가 (세그먼테이션, 구매여정, 니즈)
│   ├── trend-analyst.md       — 트렌드 분석가 (거시/미시 트렌드, 시나리오)
│   └── research-reviewer.md   — 리서치 검증자 (교차 검증, 인사이트 통합)
├── skills/
│   ├── market-research/
│       └── SKILL.md           — 오케스트레이터 (팀 조율, 워크플로우, 에러핸들링)
│   ├── tam-sam-som-calculator/
│   │   └── SKILL.md           — TAM/SAM/SOM 산출 (상향식/하향식, 데이터 소스)
│   └── porter-five-forces/
│       └── SKILL.md           — Porter 5 Forces (산업 매력도, 전략 시사점)
└── README.md                  — 이 파일
```

## 사용법

`/market-research` 스킬을 트리거하거나, "시장 조사해줘" 같은 자연어로 요청한다.

## 산출물

모든 산출물은 `_workspace/` 디렉토리에 저장된다:
- `00_input.md` — 사용자 입력 정리
- `01_industry_analysis.md` — 산업 분석 보고서
- `02_competitor_analysis.md` — 경쟁 분석 보고서
- `03_consumer_analysis.md` — 소비자 분석 보고서
- `04_trend_analysis.md` — 트렌드 분석 보고서
- `05_review_report.md` — 종합 리서치 보고서
