# Code Reviewer Harness

코드 리뷰 자동화의 스타일→보안→성능→아키텍처 리뷰를 에이전트 팀이 협업하여 수행하는 하네스.

## 구조

```

├── agents/
│   ├── style-inspector.md       — 코드 스타일 검사 (컨벤션, 포맷팅, 네이밍, 가독성)
│   ├── security-analyst.md      — 보안 분석 (취약점, 인젝션, 인증, 데이터 노출)
│   ├── performance-analyst.md   — 성능 분석 (복잡도, 메모리, 동시성, 쿼리)
│   ├── architecture-reviewer.md — 아키텍처 리뷰 (설계 패턴, 의존성, SOLID, 결합도)
│   └── review-synthesizer.md    — 리뷰 종합 (우선순위, 정합성, 최종 판정)
├── skills/
│   ├── code-reviewer/
│   │   └── SKILL.md              — 오케스트레이터 (팀 조율, 워크플로우, 에러핸들링)
│   ├── vulnerability-patterns/
│   │   └── SKILL.md              — 보안분석가 확장 (CWE 분류, 언어별 취약 패턴, 안전한 대안)
│   └── refactoring-catalog/
│       └── SKILL.md              — 아키텍처/성능 확장 (코드 스멜, SOLID 위반, 복잡도 측정)
└── README.md                     — 이 파일
```

## 사용법

`/code-reviewer` 스킬을 트리거하거나, "코드 리뷰해줘" 같은 자연어로 요청한다.

## 산출물

모든 산출물은 `_workspace/` 디렉토리에 저장된다:
- `00_input.md` — 사용자 입력 정리
- `01_style_review.md` — 코드 스타일 리뷰
- `02_security_review.md` — 보안 리뷰
- `03_performance_review.md` — 성능 리뷰
- `04_architecture_review.md` — 아키텍처 리뷰
- `05_review_summary.md` — 종합 리뷰 보고서
