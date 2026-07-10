# Travel Planner Harness

여행 계획의 목적지분석→일정→숙소→예산→현지정보를 에이전트 팀이 협업하여 생성하는 하네스.

## 구조

```

├── agents/
│   ├── destination-analyst.md  — 목적지 분석 (관광지, 계절, 비자, 안전정보)
│   ├── itinerary-designer.md   — 일정 설계 (일별 코스, 동선, 시간 배분)
│   ├── budget-manager.md       — 예산 관리 (항공, 숙소, 식비, 교통, 기타)
│   └── local-guide.md          — 현지 정보 (교통, 맛집, 문화, 긴급연락처)
├── skills/
│   ├── travel-planner/
│   │   └── SKILL.md            — 오케스트레이터 (팀 조율, 워크플로우, 에러핸들링)
│   ├── route-optimizer/
│   │   └── SKILL.md            — 동선 최적화 (itinerary-designer용)
│   └── budget-calculator/
│       └── SKILL.md            — 여행 예산 계산기 (budget-manager용)
└── README.md                   — 이 파일
```

## 사용법

`/travel-planner` 스킬을 트리거하거나, "여행 계획 짜줘" 같은 자연어로 요청한다.

## 산출물

모든 산출물은 `_workspace/` 디렉토리에 저장된다:
- `00_input.md` — 사용자 입력 정리
- `01_destination_analysis.md` — 목적지 분석 보고서
- `02_itinerary.md` — 일정표
- `03_accommodation.md` — 숙소 가이드
- `04_budget.md` — 예산 계획서
- `05_local_guide.md` — 현지 정보 가이드
