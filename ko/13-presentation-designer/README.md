# Presentation Designer Harness

프레젠테이션의 기획→스토리보드→슬라이드→발표노트를 에이전트 팀이 협업하여 제작하는 하네스.

## 구조

```

├── agents/
│   ├── storyteller.md           — 스토리 설계 (메시지 구조화, 논리 흐름, 청중 분석)
│   ├── info-architect.md        — 정보 설계 (데이터 시각화, 차트 선택, 정보 계층)
│   ├── visual-designer.md       — 비주얼 디자인 (슬라이드 레이아웃, 색상, 타이포, 이미지)
│   ├── presentation-coach.md    — 발표 코칭 (발표 노트, 타이밍, Q&A 준비, 리허설 가이드)
│   └── deck-reviewer.md         — 덱 QA (스토리↔정보↔비주얼↔발표 정합성 검증)
├── skills/
│   ├── presentation-designer/
│   │   └── SKILL.md             — 오케스트레이터 (팀 조율, 워크플로우, 에러핸들링)
│   ├── slide-layout-patterns/
│   │   └── SKILL.md             — 비주얼디자이너 확장 (20가지 레이아웃, 그리드, 디자인 토큰)
│   └── data-visualization-guide/
│       └── SKILL.md             — 정보설계자 확장 (차트 선택 매트릭스, LATCH, 색상 접근성)
└── README.md                    — 이 파일
```

## 사용법

`/presentation-designer` 스킬을 트리거하거나, "프레젠테이션 만들어줘" 같은 자연어로 요청한다.

## 산출물

모든 산출물은 `_workspace/` 디렉토리에 저장된다:
- `00_input.md` — 사용자 입력 정리
- `01_story_structure.md` — 스토리 구조·메시지 맵
- `02_info_design.md` — 정보 설계·데이터 시각화 가이드
- `03_slide_deck.md` — 슬라이드 덱 (마크다운 기반)
- `04_speaker_notes.md` — 발표 노트·타이밍·Q&A
- `05_review_report.md` — 리뷰 보고서
