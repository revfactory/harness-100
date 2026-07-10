# Technical Writer Harness

기술 문서 작성의 구조설계→집필→다이어그램→리뷰→버전관리를 에이전트 팀이 협업하여 생성하는 하네스.

## 구조

```

├── agents/
│   ├── info-architect.md      — 정보 설계 (구조 설계, 목차, 독자 분석)
│   ├── doc-writer.md          — 집필자 (본문 작성, 코드 예제, 튜토리얼)
│   ├── diagram-maker.md       — 다이어그램 작성 (Mermaid, 시각 자료)
│   ├── tech-reviewer.md       — 기술 리뷰어 (정확성, 완전성, 일관성 검증)
│   └── version-controller.md  — 버전 관리 (변경 이력, 메타데이터, 배포)
├── skills/
│   ├── technical-writer/
│   │   └── SKILL.md           — 오케스트레이터 (팀 조율, 워크플로우, 에러핸들링)
│   ├── diagram-patterns/
│   │   └── SKILL.md           — Mermaid 다이어그램 패턴 라이브러리 (diagram-maker 확장)
│   ├── api-doc-standards/
│   │   └── SKILL.md           — API 문서 작성 표준 (doc-writer 확장)
│   └── code-example-patterns/
│       └── SKILL.md           — 코드 예제 패턴 라이브러리 (doc-writer 확장)
└── README.md                  — 이 파일
```

## 사용법

`/technical-writer` 스킬을 트리거하거나, "기술 문서 작성해줘" 같은 자연어로 요청한다.

## 산출물

모든 산출물은 `_workspace/` 디렉토리에 저장된다:
- `00_input.md` — 사용자 입력 정리
- `01_doc_structure.md` — 문서 구조 설계서
- `02_doc_draft.md` — 문서 본문 초안
- `03_diagrams.md` — 다이어그램 모음
- `04_review_report.md` — 기술 리뷰 보고서
- `05_version_meta.md` — 버전 관리 메타데이터
