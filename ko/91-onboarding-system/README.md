# Onboarding System Harness

신규입사자 온보딩: 체크리스트→교육→멘토배정→30-60-90일 계획까지 에이전트 팀이 협업하여 생성하는 하네스.

## 구조

```

├── agents/
│   ├── onboarding-architect.md   — 온보딩 설계 (체크리스트, 일정, 마일스톤)
│   ├── training-builder.md       — 교육 콘텐츠 (커리큘럼, 자료, 퀴즈)
│   ├── mentor-matcher.md         — 멘토·버디 배정 (기준, 매칭, 가이드)
│   ├── milestone-tracker.md      — 30-60-90일 (목표, 평가, 피드백)
│   └── experience-reviewer.md    — 경험 검증 (정합성, 개선, 보고서)
├── skills/
│   ├── onboarding-system/
│   │   └── SKILL.md              — 오케스트레이터 (팀 조율, 워크플로우, 에러핸들링)
│   ├── learning-path-design/
│   │   └── SKILL.md              — 학습 경로 설계 (training-builder 확장)
│   └── buddy-program-guide/
│       └── SKILL.md              — 버디 프로그램 가이드 (mentor-matcher 확장)
└── README.md                     — 이 파일
```

## 사용법

`/onboarding-system` 스킬을 트리거하거나, "온보딩 프로그램 만들어줘" 같은 자연어로 요청한다.

## 산출물

모든 산출물은 `_workspace/` 디렉토리에 저장된다:
- `00_input.md` — 사용자 입력 정리
- `01_onboarding_checklist.md` — 온보딩 체크리스트 및 일정
- `02_training_program.md` — 교육 프로그램
- `03_mentor_guide.md` — 멘토·버디 배정 가이드
- `04_30_60_90_plan.md` — 30-60-90일 계획
- `05_review_report.md` — 온보딩 경험 검증 보고서
