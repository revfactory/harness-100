# Comic Creator Harness

4컷/장편 만화 제작의 콘티→대사→이미지생성→편집을 에이전트 팀이 협업하여 생성하는 하네스.

## 구조

```

├── agents/
│   ├── storyboarder.md       — 스토리보더 (시놉시스, 콘티, 장면구성, 패널레이아웃)
│   ├── dialogue-writer.md    — 대사 작가 (캐릭터 대사, 효과음, 나레이션)
│   ├── image-generator.md    — 이미지 생성자 (Gemini 기반 패널 이미지 생성)
│   ├── comic-editor.md       — 만화 편집자 (말풍선 배치, 페이지 편집, 최종 구성)
│   └── quality-reviewer.md   — 품질 검증자 (스토리-대사-이미지 정합성, 연속성 검증)
├── skills/
│   ├── comic-creator/
│   │   └── SKILL.md          — 오케스트레이터 (팀 조율, 워크플로우, 에러핸들링)
│   ├── panel-composition/
│   │   └── SKILL.md          — storyboarder+image-generator 확장 (앵글, 시선유도, 리듬)
│   ├── visual-narrative/
│   │   └── SKILL.md          — dialogue-writer+comic-editor 확장 (말풍선, 효과음, SDT)
│   └── character-design-system/
│       └── SKILL.md          — storyboarder+image-generator 확장 (캐릭터 시트, AI 일관성)
└── README.md                 — 이 파일
```

## 사용법

`/comic-creator` 스킬을 트리거하거나, "만화 만들어줘", "4컷 만화 그려줘" 같은 자연어로 요청한다.

## 산출물

모든 산출물은 `_workspace/` 디렉토리에 저장된다:
- `00_input.md` — 사용자 입력 정리
- `01_storyboard.md` — 콘티/스토리보드
- `02_dialogue.md` — 대사 스크립트
- `03_image_prompts.md` — 이미지 생성 프롬프트 및 결과
- `04_layout.md` — 페이지 레이아웃/편집 지시서
- `05_review_report.md` — 리뷰 보고서
- `panels/` — 생성된 패널 이미지
