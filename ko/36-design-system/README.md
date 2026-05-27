# Design System Harness

UI 디자인 시스템 구축: 디자인토큰→컴포넌트라이브러리→스토리북→접근성검증→문서를 에이전트 팀이 협업하여 수행하는 하네스.

## 구조

```

├── agents/
│   ├── token-designer.md       — 디자인 토큰 (색상, 타이포, 간격, 그림자, 모션)
│   ├── component-developer.md  — 컴포넌트 개발 (React/Vue, 변형, 합성, 상태)
│   ├── a11y-auditor.md         — 접근성 검증 (WCAG 2.1, ARIA, 키보드, 스크린리더)
│   ├── storybook-builder.md    — 스토리북 (스토리, 인터랙션 테스트, 문서화)
│   └── doc-writer.md           — 문서 작성 (설계 원칙, 사용 가이드, 기여 가이드)
├── skills/
│   ├── design-system/
│       └── SKILL.md            — 오케스트레이터 (팀 조율, 워크플로우, 에러핸들링)
│   ├── wcag-checker/
│   │   └── SKILL.md            — 접근성 검증 (WCAG 체크리스트, 대비비, ARIA)
│   └── token-generator/
│       └── SKILL.md            — 디자인 토큰 생성 (색상 스케일, 타이포, 간격)
└── README.md                   — 이 파일
```

## 사용법

`/design-system` 스킬을 트리거하거나, "디자인 시스템 만들어줘" 같은 자연어로 요청한다.

## 산출물

모든 산출물은 `_workspace/` 디렉토리에 저장된다:
- `00_input.md` — 사용자 입력 및 브랜드 정보
- `01_design_tokens/` — 디자인 토큰 정의 파일
- `02_components/` — 컴포넌트 라이브러리 코드
- `03_storybook/` — 스토리북 스토리 및 설정
- `04_a11y_report.md` — 접근성 검증 보고서
- `05_docs/` — 디자인 시스템 문서
