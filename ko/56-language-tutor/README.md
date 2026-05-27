# Language Tutor Harness

외국어 학습을 위한 레벨 테스트, 커리큘럼, 레슨, 퀴즈, 복습 관리 에이전트 팀 하네스.

## 구조

```

├── agents/
│   ├── level-assessor.md
│   ├── curriculum-designer.md
│   ├── lesson-tutor.md
│   ├── quiz-master.md
│   └── review-coach.md
├── skills/
│   ├── language-tutor/
│   │   └── SKILL.md              — 오케스트레이터
│   ├── spaced-repetition/
│   │   └── SKILL.md              — 간격 반복 알고리즘 (SM-2, 에빙하우스, 복습 설계)
│   └── cefr-assessment/
│       └── SKILL.md              — CEFR 레벨 평가 (6단계 기술자, 적응형 진단, 시험 매핑)
└── README.md                     — 이 파일
```

## 사용법

`/language-tutor` 스킬을 트리거하거나 자연어로 요청한다.
