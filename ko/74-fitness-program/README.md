# Fitness Program Harness

운동 프로그램의 목표별설계→주간스케줄→운동가이드→식단연계→진행기록을 에이전트 팀이 협업하여 생성하는 하네스.

## 구조

```

├── agents/
│   ├── program-architect.md    — 프로그램 설계 (목표분석, 주기화, 볼륨·강도 설정)
│   ├── exercise-guide.md       — 운동 가이드 (동작설명, 폼가이드, 대체운동)
│   ├── nutrition-linker.md     — 영양 연계 (운동별 영양전략, 보충제, 타이밍)
│   └── template-builder.md    — 템플릿 빌더 (기록지, 진행추적, 측정항목)
├── skills/
│   ├── fitness-program/
│   │   └── SKILL.md           — 오케스트레이터 (팀 조율, 워크플로우, 에러핸들링)
│   ├── exercise-biomechanics/
│   │   └── SKILL.md           — 운동 생체역학 가이드 (exercise-guide용)
│   └── periodization-engine/
│       └── SKILL.md           — 주기화 설계 엔진 (program-architect용)
└── README.md                  — 이 파일
```

## 사용법

`/fitness-program` 스킬을 트리거하거나, "운동 프로그램 짜줘" 같은 자연어로 요청한다.

## 산출물

모든 산출물은 `_workspace/` 디렉토리에 저장된다:
- `00_input.md` — 사용자 입력 정리
- `01_program_design.md` — 프로그램 설계서
- `02_weekly_schedule.md` — 주간 운동 스케줄
- `03_exercise_guide.md` — 운동 가이드 문서
- `04_nutrition_plan.md` — 식단 연계표
- `05_tracking_template.md` — 진행 기록 템플릿
