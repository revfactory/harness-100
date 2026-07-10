# API Designer Harness

REST/GraphQL API의 설계·문서화·목업·테스트를 에이전트 팀이 협업하여 수행하는 하네스.

## 구조

```

├── agents/
│   ├── api-architect.md      — API 설계 (리소스 모델링, 엔드포인트, 버전관리)
│   ├── schema-validator.md   — 스키마 검증 (OpenAPI/GraphQL 스키마, 타입 안전성)
│   ├── doc-writer.md         — API 문서 작성 (개발자 가이드, 예제, 에러 레퍼런스)
│   ├── mock-tester.md        — 목업 서버 및 테스트 (Mock API, 통합 테스트, 부하 시나리오)
│   └── review-auditor.md     — API 리뷰 (보안, 일관성, 성능, 베스트 프랙티스 준수)
├── skills/
│   ├── api-designer/
│   │   └── SKILL.md           — 오케스트레이터 (팀 조율, 워크플로우, 에러핸들링)
│   ├── rest-api-conventions/
│   │   └── SKILL.md           — API설계자 확장 (URL 네이밍, 상태 코드, 페이지네이션, 버전관리)
│   └── api-error-design/
│       └── SKILL.md           — 문서작성자/테스터 확장 (에러 코드 체계, 에러 응답, retry 전략)
└── README.md                  — 이 파일
```

## 사용법

`/api-designer` 스킬을 트리거하거나, "API 설계해줘" 같은 자연어로 요청한다.

## 산출물

모든 산출물은 `_workspace/` 디렉토리에 저장된다:
- `00_input.md` — 사용자 입력 정리
- `01_api_design.md` — API 설계 문서
- `02_schema.yaml` — OpenAPI/GraphQL 스키마 파일
- `03_api_docs.md` — API 개발자 문서
- `04_mock_tests.md` — 목업 서버 설정 및 테스트 결과
- `05_review_report.md` — API 리뷰 보고서
