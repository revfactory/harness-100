# Visual Storytelling Harness

비주얼 스토리텔링의 스토리설계→텍스트집필→AI이미지생성→HTML레이아웃→통합편집을 에이전트 팀이 협업하여 제작하는 하네스.

## 구조

```

├── agents/
│   ├── story-architect.md       — 스토리 설계 (내러티브 구조, 장면 구성, 시각-텍스트 밸런스)
│   ├── essay-writer.md          — 에세이 작가 (본문 집필, 캡션, 인용구, 감정적 문체)
│   ├── image-prompter.md        — 이미지 프롬프터 (Gemini 프롬프트 설계, 스타일 일관성)
│   ├── layout-builder.md        — 레이아웃 빌더 (HTML/CSS 제작, 반응형, 타이포그래피)
│   └── editorial-reviewer.md    — 편집 리뷰어 (스토리↔텍스트↔이미지↔레이아웃 정합성)
├── skills/
│   ├── visual-storytelling/
│   │   └── SKILL.md             — 오케스트레이터 (팀 조율, 워크플로우, 에러핸들링)
│   ├── image-prompt-engineering/
│   │   └── SKILL.md             — 이미지프롬프터 확장 (5-Layer 프롬프트, 스타일 키워드, 일관성 기법)
│   └── narrative-structure-patterns/
│       └── SKILL.md             — 스토리설계자 확장 (3막/5막/영웅여정, 감정 곡선, 비주얼 리듬)
└── README.md                    — 이 파일
```

## 사용법

`/visual-storytelling` 스킬을 트리거하거나, "비주얼 스토리 만들어줘" 같은 자연어로 요청한다.

## 산출물

모든 산출물은 `_workspace/` 디렉토리에 저장된다:
- `00_input.md` — 사용자 입력 정리
- `01_story_blueprint.md` — 스토리 블루프린트
- `02_essay_text.md` — 에세이 본문
- `03_image_prompts.md` — 이미지 프롬프트 시트
- `04_layout.html` — HTML 레이아웃
- `05_review_report.md` — 편집 리뷰 보고서
- `images/` — 생성된 이미지 디렉토리
