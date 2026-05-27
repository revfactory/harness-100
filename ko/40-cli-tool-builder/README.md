# CLI Tool Builder Harness

CLI 도구 개발의 명령설계→파서→핸들러→테스트→문서→배포설정을 에이전트 팀이 협업하여 수행하는 하네스.

## 구조

```

├── agents/
│   ├── command-designer.md    — 명령 체계 설계 (서브커맨드, 옵션, 인자 구조)
│   ├── core-developer.md      — 코어 개발 (파서, 핸들러, 비즈니스 로직)
│   ├── test-engineer.md       — 테스트 (단위/통합/E2E, 커버리지)
│   ├── docs-writer.md         — 문서 작성 (man page, --help, README, 예제)
│   └── release-engineer.md    — 릴리스 (빌드, 패키징, 배포, CI/CD)
├── skills/
│   ├── cli-tool-builder/
│       └── SKILL.md           — 오케스트레이터 (팀 조율, 워크플로우, 에러핸들링)
│   ├── arg-parser-generator/
│   │   └── SKILL.md           — 인자 파서 생성 (서브커맨드, 언어별 보일러플레이트)
│   └── ux-linter/
│       └── SKILL.md           — CLI UX 검증 (12원칙, 에러 메시지, 출력 포맷)
└── README.md                  — 이 파일
```

## 사용법

`/cli-tool-builder` 스킬을 트리거하거나, "CLI 도구 만들어줘" 같은 자연어로 요청한다.

## 산출물

모든 산출물은 `_workspace/` 디렉토리에 저장된다:
- `00_input.md` — 사용자 입력 정리
- `01_command_design.md` — 명령 체계 설계서
- `02_core_implementation.md` — 코어 구현 문서
- `03_test_suite.md` — 테스트 스위트
- `04_documentation.md` — 사용자 문서
- `05_release_config.md` — 릴리스 설정
- `src/` — CLI 소스코드
