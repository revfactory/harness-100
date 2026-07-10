---
name: ux-linter
description: "CLI 도구의 사용자 경험을 검증하는 체크리스트와 모범 사례. 'CLI UX 검증', '사용성 체크', '출력 형식 검증', '에러 메시지 검토', '인터랙션 패턴 검사' 등 CLI UX 품질 확인 시 사용한다. 단, GUI 사용성 테스트, 접근성 인증은 이 스킬의 범위가 아니다."
---

# UX Linter — CLI 사용자 경험 검증 체크리스트

test-engineer와 docs-writer의 UX 품질 검증을 강화하는 스킬.

## 대상 에이전트

- **test-engineer** — CLI 사용성 테스트를 체계적으로 수행한다
- **docs-writer** — 사용자 관점의 문서를 작성한다

## CLI UX 12원칙 체크리스트

### 1. 발견 가능성 (Discoverability)
```
[ ] --help가 유용한 정보를 제공하는가?
[ ] 서브커맨드 목록이 설명과 함께 표시되는가?
[ ] 잘못된 명령 시 "Did you mean...?" 제안이 있는가?
[ ] 예시(Examples) 섹션이 있는가?
```

### 2. 피드백 (Feedback)
```
[ ] 작업 진행 중 프로그레스 표시가 있는가? (bar/spinner)
[ ] 성공/실패가 명확히 구분되는가?
[ ] 장시간 작업에 예상 시간이 표시되는가?
[ ] 결과 요약이 제공되는가?
```

### 3. 에러 처리 (Error Handling)
```
[ ] 에러 메시지가 구체적인가? (무엇이 잘못됐고 어떻게 고치는지)
[ ] 에러와 경고가 구분되는가?
[ ] stderr로 에러가 출력되는가? (stdout 오염 방지)
[ ] 종료 코드가 적절한가? (0: 성공, 비0: 실패)
```

### 4. 파이프 친화 (Pipe-friendly)
```
[ ] stdout이 구조화된 데이터를 출력하는가?
[ ] 인간용/기계용 출력 전환이 가능한가? (--json, --quiet)
[ ] stdin에서 입력을 읽을 수 있는가? (파이프)
[ ] 색상이 파이프 시 자동 비활성화되는가? (isatty 체크)
```

### 5. 설정 (Configuration)
```
[ ] 설정 파일 경로를 표시하는가?
[ ] 환경변수 + 설정파일 + CLI 옵션 우선순위가 명확한가?
[ ] 기본값이 합리적인가?
[ ] 현재 설정을 확인하는 명령이 있는가?
```

## 에러 메시지 포맷 표준

### BAD (피해야 할 패턴)
```
Error: invalid input
Error: operation failed
Exception: NullPointerException at line 42
```

### GOOD (권장 패턴)
```
Error: 입력 파일을 찾을 수 없습니다: data.json
  경로를 확인하거나 --input 옵션으로 지정하세요.
  예: mytool convert --input /path/to/data.json

Error: JSON 파싱 실패 (line 15, column 8)
  닫히지 않은 중괄호가 있습니다.
  힌트: jsonlint data.json 으로 문법을 확인해보세요.
```

### 에러 메시지 구성 요소

```
1. [무엇이 일어났는가] — 문제 설명
2. [왜 일어났는가] — 원인 (가능한 경우)
3. [어떻게 해결하는가] — 해결 방법
4. [추가 정보] — 문서 링크, 관련 명령어
```

## 출력 포맷 가이드

### 테이블 출력

```
NAME        STATUS    SIZE     MODIFIED
config.yml  active    2.4 KB   2025-01-15
data.json   pending   156 KB   2025-01-14
```

### JSON 출력 (--json)

```json
[
  {"name": "config.yml", "status": "active", "size": 2400},
  {"name": "data.json", "status": "pending", "size": 156000}
]
```

### 진행 상태 표시

```
TTY (터미널):
  Processing... [████████░░░░░░░░] 50% (15/30 files)

Non-TTY (파이프/리다이렉트):
  Processing 15/30 files...
  Processing 30/30 files... done.
```

## 색상 사용 가이드

| 의미 | 색상 | ANSI |
|------|------|------|
| 성공 | 초록 | `\033[32m` |
| 경고 | 노랑 | `\033[33m` |
| 오류 | 빨강 | `\033[31m` |
| 정보 | 파랑 | `\033[34m` |
| 강조 | 굵게 | `\033[1m` |
| 보조 | 회색 | `\033[90m` |

```
규칙:
1. NO_COLOR 환경변수 존재 시 색상 비활성화
2. 파이프/리다이렉트 시 자동 비활성화
3. --no-color 옵션 제공
4. 색상 없이도 의미 전달 가능해야 함
```

## 인터랙티브 패턴

```
확인 프롬프트 (위험 작업):
  정말 삭제하시겠습니까? [y/N]: _
  → 대문자가 기본값 (N = 기본 No)
  → --force / --yes 로 건너뛰기

선택 프롬프트:
  출력 형식을 선택하세요:
  > json
    yaml
    toml
  → 화살표 키로 선택 (TTY 전용)

드라이런:
  --dry-run 옵션으로 실제 변경 없이 미리보기
```

## UX 검증 보고서 템플릿

```markdown
## CLI UX 검증 보고서

### 12원칙 통과 현황
| 원칙 | 상태 | 비고 |
|------|------|------|

### 에러 메시지 품질
| 시나리오 | 현재 메시지 | 개선안 |

### 출력 형식 검증
| 명령 | 터미널 출력 | 파이프 출력 | JSON |
```
