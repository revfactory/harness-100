# Advertising Campaign Harness

광고 캠페인의 타깃분석→카피→크리에이티브→미디어플랜을 에이전트 팀이 협업하여 설계하는 하네스.

## 구조

```

├── agents/
│   ├── market-analyst.md        — 시장·타깃 분석 (오디언스 세분화, 경쟁 광고 분석, 인사이트 도출)
│   ├── copywriter.md            — 광고 카피 작성 (헤드라인, 바디카피, CTA, 톤앤보이스)
│   ├── creative-director.md     — 크리에이티브 설계 (비주얼 컨셉, 스토리보드, 이미지 생성)
│   ├── media-planner.md         — 미디어 플래닝 (채널 선정, 예산 배분, 일정 수립)
│   └── campaign-reviewer.md     — 캠페인 QA (전략↔카피↔크리에이티브↔미디어 정합성 검증)
├── skills/
│   ├── advertising-campaign/
│   │   └── SKILL.md             — 오케스트레이터 (팀 조율, 워크플로우, 에러핸들링)
│   ├── ad-copywriting-formulas/
│   │   └── SKILL.md             — 카피라이터 확장 (AIDA/PAS/BAB 설득 공식, 심리 트리거, 채널별 글자수)
│   └── media-mix-calculator/
│       └── SKILL.md             — 미디어플래너 확장 (GRP/CPM/ROAS 계산, 예산 배분 모델, 벤치마크)
└── README.md                    — 이 파일
```

## 사용법

`/advertising-campaign` 스킬을 트리거하거나, "광고 캠페인 기획해줘" 같은 자연어로 요청한다.

## 산출물

모든 산출물은 `_workspace/` 디렉토리에 저장된다:
- `00_input.md` — 사용자 입력 정리
- `01_market_analysis.md` — 시장·타깃 분석 보고서
- `02_ad_copy.md` — 광고 카피 세트
- `03_creative_concept.md` — 크리에이티브 컨셉·스토리보드
- `04_media_plan.md` — 미디어 플랜
- `05_review_report.md` — 리뷰 보고서
