# API Client Generator Harness

API 클라이언트 SDK 생성: 스펙파싱→타입생성→클라이언트코드→테스트→사용문서를 에이전트 팀이 협업하여 수행하는 하네스.

## 구조

```

├── agents/
│   ├── spec-parser.md       — 스펙 파서 (OpenAPI/GraphQL/gRPC 스펙 분석, 엔드포인트 추출)
│   ├── type-generator.md    — 타입 생성 (요청/응답 모델, Enum, 유니온, 제네릭 타입)
│   ├── sdk-developer.md     — SDK 개발 (HTTP 클라이언트, 인증, 페이지네이션, 재시도)
│   ├── test-engineer.md     — 테스트 엔지니어 (단위/통합 테스트, 모킹, 스냅샷)
│   └── doc-writer.md        — 문서 작성 (README, API 레퍼런스, 사용 예제, 변경 로그)
├── skills/
│   ├── api-client-generator/
│   │   └── SKILL.md              — 오케스트레이터 (팀 조율, 워크플로우, 에러핸들링)
│   ├── openapi-spec-patterns/
│   │   └── SKILL.md              — API 스펙 분석 패턴 가이드
│   └── sdk-design-patterns/
│       └── SKILL.md              — SDK 설계 패턴 가이드
└── README.md                — 이 파일
```

## 사용법

`/api-client-generator` 스킬을 트리거하거나, "API 클라이언트 SDK 만들어줘" 같은 자연어로 요청한다.

## 산출물

모든 산출물은 `_workspace/` 디렉토리에 저장된다:
- `00_input.md` — 사용자 입력 및 API 스펙 정보
- `01_spec_analysis.md` — API 스펙 분석 결과
- `02_types/` — 생성된 타입 정의 파일
- `03_client/` — SDK 클라이언트 코드
- `04_tests/` — 테스트 코드
- `05_docs/` — 사용 문서
