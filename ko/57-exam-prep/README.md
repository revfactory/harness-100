# Exam Prep Harness

시험 준비의 출제경향→약점진단→맞춤학습→모의고사→오답분석 에이전트 팀 하네스.

## 구조

```

├── agents/
│   ├── trend-analyst.md
│   ├── diagnostician.md
│   ├── learning-designer.md
│   ├── examiner.md
│   └── error-analyst.md
├── skills/
│   ├── exam-prep/
│   │   └── SKILL.md              — 오케스트레이터
│   ├── bloom-taxonomy-engine/
│   │   └── SKILL.md              — Bloom 분류학 (인지 수준별 문항, 학습 활동 매핑)
│   └── error-pattern-analyzer/
│       └── SKILL.md              — 오답 패턴 분석 (5-Type 분류, 개념 결손 추적)
└── README.md                     — 이 파일
```

## 사용법

`/exam-prep` 스킬을 트리거하거나 자연어로 요청한다.
