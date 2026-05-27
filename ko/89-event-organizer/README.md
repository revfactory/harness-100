# Event Organizer Harness

이벤트 기획·운영: 컨셉→장소→프로그램→홍보→실행→사후평가까지 에이전트 팀이 협업하여 생성하는 하네스.

## 구조

```

├── agents/
│   ├── concept-planner.md        — 컨셉 기획 (테마, 목표, 타깃, 예산)
│   ├── logistics-manager.md      — 로지스틱스 (장소, 동선, 장비, 케이터링)
│   ├── program-designer.md       — 프로그램 설계 (타임테이블, 연사, 콘텐츠)
│   ├── promotion-lead.md         — 홍보 (채널전략, 콘텐츠, 등록관리)
│   └── evaluation-analyst.md     — 사후 평가 (KPI, 설문, 보고서, 교훈)
├── skills/
│   ├── event-organizer/
│   │   └── SKILL.md              — 오케스트레이터 (팀 조율, 워크플로우, 에러핸들링)
│   ├── budget-planning/
│   │   └── SKILL.md              — 이벤트 예산 계획 (concept-planner 확장)
│   └── venue-evaluation/
│       └── SKILL.md              — 장소 평가 스코어카드 (logistics-manager 확장)
└── README.md                     — 이 파일
```

## 사용법

`/event-organizer` 스킬을 트리거하거나, "이벤트 기획해줘" 같은 자연어로 요청한다.

## 산출물

모든 산출물은 `_workspace/` 디렉토리에 저장된다:
- `00_input.md` — 사용자 입력 정리
- `01_concept_plan.md` — 컨셉 기획서
- `02_logistics_plan.md` — 로지스틱스 계획서
- `03_program_design.md` — 프로그램 설계서
- `04_promotion_plan.md` — 홍보 계획서
- `05_evaluation_framework.md` — 평가 프레임워크
