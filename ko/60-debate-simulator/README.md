# Debate Simulator Harness

토론 시뮬레이션 에이전트 팀 하네스.

## 구조

```

├── agents/
│   ├── topic-analyst.md
│   ├── pro-debater.md
│   ├── con-debater.md
│   ├── judge.md
│   └── rapporteur.md
├── skills/
│   ├── debate-simulator/
│   │   └── SKILL.md              — 오케스트레이터
│   ├── argumentation-framework/
│   │   └── SKILL.md              — 논증 구축 (Toulmin 모델, 증거 피라미드, 반박 5-Type)
│   └── logical-fallacy-detector/
│       └── SKILL.md              — 논리적 오류 검출 (4대 분류, 감점 기준, 루브릭)
└── README.md                     — 이 파일
```

## 사용법

`/debate-simulator` 스킬을 트리거하거나 자연어로 요청한다.
