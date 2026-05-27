# Side Project Launcher Harness

사이드프로젝트 기획의 아이디어검증→기술스택선정→MVP스펙→개발로드맵→런칭체크리스트를 에이전트 팀이 협업하여 생성하는 하네스.

## 구조

```

├── agents/
│   ├── idea-validator.md      — 아이디어 검증 (시장 분석, 경쟁 조사, 차별화)
│   ├── techstack-analyst.md   — 기술스택 분석 (선정 기준, 비교, 추천)
│   ├── mvp-designer.md        — MVP 설계 (핵심 기능, 와이어프레임, 스펙)
│   ├── roadmap-builder.md     — 로드맵 작성 (개발 일정, 마일스톤, 런칭 전략)
│   └── launch-reviewer.md    — 교차 검증 (아이디어↔기술↔MVP↔로드맵 정합성)
├── skills/
│   ├── side-project-launcher/
│   │   └── SKILL.md           — 오케스트레이터 (팀 조율, 워크플로우, 에러핸들링)
│   ├── market-sizing-calculator/
│   │   └── SKILL.md           — 시장 규모 계산기 (idea-validator용)
│   └── techstack-decision-matrix/
│       └── SKILL.md           — 기술스택 의사결정 매트릭스 (techstack-analyst용)
└── README.md                  — 이 파일
```

## 사용법

`/side-project-launcher` 스킬을 트리거하거나, "사이드프로젝트 기획 도와줘" 같은 자연어로 요청한다.

## 산출물

모든 산출물은 `_workspace/` 디렉토리에 저장된다:
- `00_input.md` — 사용자 입력 정리
- `01_idea_validation.md` — 아이디어 검증 보고서
- `02_techstack_recommendation.md` — 기술스택 추천서
- `03_mvp_spec.md` — MVP 스펙 문서
- `04_roadmap_launch.md` — 개발 로드맵 + 런칭 체크리스트
- `05_review_report.md` — 리뷰 보고서
