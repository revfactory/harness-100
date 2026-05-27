# Product Manager Harness

PM 업무의 로드맵→PRD→유저스토리→스프린트→회고를 에이전트 팀이 협업하여 생성하는 하네스.

## 구조

```

├── agents/
│   ├── strategist.md          — 전략가 (비전, 로드맵, 우선순위 프레임워크)
│   ├── prd-writer.md          — PRD 작성자 (제품 요구사항 정의서)
│   ├── story-writer.md        — 유저스토리 작성자 (AC, 스토리맵, 포인트)
│   ├── sprint-planner.md      — 스프린트 플래너 (계획, 용량, 리스크)
│   └── pm-reviewer.md         — PM 검증자 (정합성, 실행 가능성 검토)
├── skills/
│   ├── product-manager/
│       └── SKILL.md           — 오케스트레이터 (팀 조율, 워크플로우, 에러핸들링)
│   ├── rice-prioritizer/
│   │   └── SKILL.md           — RICE 우선순위 (스코어 공식, ICE/MoSCoW 보완)
│   └── story-point-estimator/
│       └── SKILL.md           — 스토리 포인트 (피보나치, 벨로시티, 분해 기준)
└── README.md                  — 이 파일
```

## 사용법

`/product-manager` 스킬을 트리거하거나, "PRD 작성해줘" 같은 자연어로 요청한다.

## 산출물

모든 산출물은 `_workspace/` 디렉토리에 저장된다:
- `00_input.md` — 사용자 입력 정리
- `01_product_roadmap.md` — 제품 로드맵
- `02_prd.md` — 제품 요구사항 정의서
- `03_user_stories.md` — 유저스토리 목록
- `04_sprint_plan.md` — 스프린트 계획
- `05_review_report.md` — PM 검증 보고서
