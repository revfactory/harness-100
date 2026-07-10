# Meeting Strategist Harness

회의 전략 문서의 안건구조설계→배경자료조사→의사결정프레임워크→회의록템플릿→팔로업플랜을 에이전트 팀이 협업하여 생성하는 하네스.

## 구조

```

├── agents/
│   ├── agenda-architect.md        — 안건 설계 (회의 목적, 구조, 시간 배분)
│   ├── background-researcher.md   — 배경 조사 (관련 데이터, 이해관계자 분석)
│   ├── framework-designer.md      — 의사결정 프레임워크 (판단 기준, 옵션 평가)
│   ├── template-builder.md        — 문서 템플릿 (회의록, 보고 양식)
│   └── followup-planner.md        — 팔로업 플랜 및 교차 검증 (실행 추적, QA)
├── skills/
│   ├── meeting-strategist/
│   │   └── SKILL.md               — 오케스트레이터 (팀 조율, 워크플로우, 에러핸들링)
│   ├── decision-frameworks/
│   │   └── SKILL.md               — 의사결정 프레임워크 라이브러리 (framework-designer 확장)
│   └── facilitation-techniques/
│       └── SKILL.md               — 퍼실리테이션 기법 (agenda-architect 확장)
└── README.md                      — 이 파일
```

## 사용법

`/meeting-strategist` 스킬을 트리거하거나, "회의 준비 자료 만들어줘" 같은 자연어로 요청한다.

## 산출물

모든 산출물은 `_workspace/` 디렉토리에 저장된다:
- `00_input.md` — 사용자 입력 정리
- `01_agenda_design.md` — 안건 구조 설계서
- `02_background_brief.md` — 배경 자료 브리프
- `03_decision_framework.md` — 의사결정 프레임워크
- `04_meeting_templates.md` — 회의록 및 보고 템플릿
- `05_followup_plan.md` — 팔로업 플랜 및 검증 보고서
