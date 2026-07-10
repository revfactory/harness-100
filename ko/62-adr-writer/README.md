# ADR Writer Harness

아키텍처 결정 기록(ADR) 작성 에이전트 팀 하네스.

## 구조

```

├── agents/
│   ├── context-analyst.md
│   ├── alternative-researcher.md
│   ├── tradeoff-evaluator.md
│   ├── adr-author.md
│   └── impact-tracker.md
├── skills/
│   ├── adr-writer/
│   │   └── SKILL.md              — 오케스트레이터
│   ├── quality-attribute-analyzer/
│   │   └── SKILL.md              — 품질 속성 분석 (CAP 정리, 가중 평가, ATAM)
│   └── madr-template-engine/
│       └── SKILL.md              — MADR 포맷 (ADR 상태 관리, 번호 체계, 의존성 그래프)
└── README.md                     — 이 파일
```

## 사용법

`/adr-writer` 스킬을 트리거하거나 자연어로 요청한다.
