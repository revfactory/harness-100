# Space Concept Board Harness

공간 인테리어 컨셉보드의 스타일분석→무드보드→컬러팔레트→가구·소품리스트→예산표→쇼핑가이드를 에이전트 팀이 협업하여 생성하는 하네스.

## 구조

```

├── agents/
│   ├── style-analyst.md       — 스타일 분석 (공간 파악, 스타일 진단, 레퍼런스 수집)
│   ├── moodboard-designer.md  — 무드보드 설계 (컬러팔레트, 텍스처, 소재 구성)
│   ├── item-curator.md        — 아이템 큐레이션 (가구·소품 선정, 배치 제안)
│   ├── budget-manager.md      — 예산 관리 (가격 조사, 예산표, 쇼핑가이드)
│   └── concept-reviewer.md    — 교차 검증 (스타일↔무드보드↔아이템↔예산 정합성)
├── skills/
│   ├── space-concept-board/
│   │   └── SKILL.md           — 오케스트레이터 (팀 조율, 워크플로우, 에러핸들링)
│   ├── color-harmony-engine/
│   │   └── SKILL.md           — 색채 조화 엔진 (moodboard-designer용)
│   └── spatial-layout-guide/
│       └── SKILL.md           — 공간 레이아웃 가이드 (item-curator용)
└── README.md                  — 이 파일
```

## 사용법

`/space-concept-board` 스킬을 트리거하거나, "거실 인테리어 컨셉 잡아줘" 같은 자연어로 요청한다.

## 산출물

모든 산출물은 `_workspace/` 디렉토리에 저장된다:
- `00_input.md` — 사용자 입력 정리
- `01_style_analysis.md` — 스타일 분석 보고서
- `02_moodboard.md` — 무드보드 + 컬러팔레트
- `03_item_list.md` — 가구·소품 리스트 + 배치 제안
- `04_budget_shopping.md` — 예산표 + 쇼핑가이드
- `05_review_report.md` — 리뷰 보고서
