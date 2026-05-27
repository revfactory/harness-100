---
name: semver-analyzer
description: "시맨틱 버저닝(SemVer) 규칙에 따라 변경사항을 분석하고 적절한 버전 번호를 결정하는 방법론. 'SemVer 분석', '버전 번호 결정', 'Breaking Change 판정', '버전 범프 결정' 등 버전 관리 시 사용한다. 단, git 태그 자동 생성, CI/CD 릴리스 실행은 이 스킬의 범위가 아니다."
---

# SemVer Analyzer — 시맨틱 버저닝 분석 방법론

change-classifier와 release-note-writer의 버전 결정 역량을 강화하는 스킬.

## 대상 에이전트

- **change-classifier** — 변경사항의 SemVer 영향도를 판정한다
- **release-note-writer** — 버전 번호와 하이라이트를 결정한다

## SemVer 2.0.0 핵심 규칙

```
MAJOR.MINOR.PATCH[-prerelease][+build]

MAJOR: 호환되지 않는 API 변경 (Breaking Change)
MINOR: 하위 호환 기능 추가
PATCH: 하위 호환 버그 수정
```

## Breaking Change 판정 매트릭스

### API/라이브러리

| 변경 유형 | Breaking? | 예시 |
|----------|-----------|------|
| 공개 함수 삭제 | YES | `remove_user()` 삭제 |
| 공개 함수 시그니처 변경 | YES | 필수 매개변수 추가/제거 |
| 반환 타입 변경 | YES | `dict` → `list` |
| 예외 타입 변경 | YES | `ValueError` → `TypeError` |
| 기본값 변경 | MAYBE | 동작 변경 여부에 따라 |
| 새 선택 매개변수 추가 | NO | `def func(x, new=None)` |
| 새 공개 함수 추가 | NO | 기존 코드 영향 없음 |
| 내부 함수 변경 | NO | `_private_func()` |
| 성능 개선 | NO | 동작 동일 |

### 웹 API (REST/GraphQL)

| 변경 유형 | Breaking? |
|----------|-----------|
| 엔드포인트 삭제/이동 | YES |
| 필수 필드 추가 (요청) | YES |
| 응답 필드 삭제 | YES |
| 응답 구조 변경 | YES |
| 인증 방식 변경 | YES |
| 새 선택 필드 추가 (요청) | NO |
| 새 응답 필드 추가 | NO |
| 새 엔드포인트 추가 | NO |

### 데이터베이스

| 변경 유형 | Breaking? |
|----------|-----------|
| 테이블/컬럼 삭제 | YES |
| NOT NULL 제약 추가 | YES |
| 컬럼 타입 변경 | YES |
| 새 nullable 컬럼 추가 | NO |
| 새 인덱스 추가 | NO |

## 버전 범프 결정 알고리즘

```
입력: 변경사항 목록

1. Breaking Change 있음? → MAJOR 범프
2. 새 기능 있음? → MINOR 범프
3. 버그 수정만? → PATCH 범프

특수 규칙:
- MAJOR = 0 (개발 중): Breaking Change도 MINOR로 허용
- pre-release 붙은 경우: 0.x.y-alpha.1 → 정식 릴리스 시 MAJOR
- 여러 유형 혼합 시: 가장 높은 수준 적용
```

## Conventional Commits 매핑

| 접두사 | SemVer 영향 | 릴리스 노트 섹션 |
|--------|-----------|----------------|
| `feat:` | MINOR | Added (추가) |
| `fix:` | PATCH | Fixed (수정) |
| `feat!:` / `BREAKING CHANGE:` | MAJOR | Breaking Changes |
| `perf:` | PATCH | Performance (성능) |
| `refactor:` | - | Changed (변경) |
| `docs:` | - | Documentation |
| `test:` | - | - (노트 제외 가능) |
| `chore:` | - | - (노트 제외 가능) |
| `ci:` | - | - (노트 제외 가능) |
| `style:` | - | - (노트 제외 가능) |
| `deps:` | PATCH~MAJOR | Dependencies |

## Keep a Changelog 형식

```markdown
# Changelog

## [Unreleased]

## [2.0.0] - 2025-01-15

### Breaking Changes
- `createUser()` API가 `registerUser()`로 이름 변경 (#123)

### Added
- 팀 관리 기능 추가 (#456)
- 다크모드 지원 (#789)

### Changed
- 로그인 화면 UI 개선 (#234)

### Deprecated
- `v1` API 엔드포인트 (v3.0에서 제거 예정)

### Fixed
- 비밀번호 재설정 이메일 미발송 문제 (#567)

### Security
- XSS 취약점 패치 (#890)
```

## 프리릴리스 버전 체계

```
1.0.0-alpha.1 → 초기 알파
1.0.0-alpha.2 → 알파 수정
1.0.0-beta.1  → 베타 진입
1.0.0-beta.2  → 베타 수정
1.0.0-rc.1    → 릴리스 후보
1.0.0         → 정식 릴리스

우선순위: alpha < beta < rc < release
```
