# Game Narrative Harness

게임 스토리·퀘스트·대사·분기 시나리오를 에이전트 팀이 협업하여 설계하는 하네스.

## 구조

```

├── agents/
│   ├── worldbuilder.md        — 세계관 설계자 (배경, 세력, 역사, 규칙)
│   ├── quest-designer.md      — 퀘스트 디자이너 (메인/사이드 퀘스트, 보상 체계)
│   ├── dialogue-writer.md     — 대사 작가 (NPC 대사, 선택지, 감정 연출)
│   ├── branch-architect.md    — 분기 설계자 (분기 구조, 결말, 플래그 시스템)
│   └── narrative-reviewer.md  — 내러티브 검증자 (정합성, 밸런스, 품질 검증)
├── skills/
│   ├── game-narrative/
│   │   └── SKILL.md           — 오케스트레이터 (팀 조율, 워크플로우, 에러핸들링)
│   ├── quest-design-patterns/
│   │   └── SKILL.md           — quest-designer 확장 (12 아키타입, DRIP 보상, 난이도 곡선)
│   ├── dialogue-systems/
│   │   └── SKILL.md           — dialogue-writer 확장 (VOICE 보이스, 선택지 심리학, 바크)
│   └── branching-logic/
│       └── SKILL.md           — branch-architect 확장 (6가지 분기 패턴, 플래그, 엔딩)
└── README.md                  — 이 파일
```

## 사용법

`/game-narrative` 스킬을 트리거하거나, "게임 시나리오 만들어줘" 같은 자연어로 요청한다.

## 산출물

모든 산출물은 `_workspace/` 디렉토리에 저장된다:
- `00_input.md` — 사용자 입력 정리
- `01_worldbuilding.md` — 세계관 설정 문서
- `02_quest_design.md` — 퀘스트 설계 문서
- `03_dialogue_script.md` — 대사 스크립트
- `04_branch_map.md` — 분기 구조도
- `05_review_report.md` — 리뷰 보고서
