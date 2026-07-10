---
name: commit-parser
description: "git 커밋 메시지를 파싱하여 구조화된 변경 정보를 추출하는 방법론. '커밋 파싱', '커밋 메시지 분석', 'Conventional Commits 파싱', 'git 이력 구조화' 등 커밋 분석 시 사용한다. 단, git hook 설정, 커밋 린트 도구 설치는 이 스킬의 범위가 아니다."
---

# Commit Parser — 커밋 메시지 파싱 + 구조화 방법론

commit-analyst의 커밋 분석 역량을 강화하는 스킬.

## 대상 에이전트

- **commit-analyst** — git 이력에서 의미 있는 변경 정보를 추출한다
- **change-classifier** — 파싱된 결과로 변경을 분류한다

## Conventional Commits 파싱 규칙

### 정규식 패턴

```
^(?<type>feat|fix|docs|style|refactor|perf|test|ci|chore|build|revert)
(?:\((?<scope>[^)]+)\))?
(?<breaking>!)?
:\s*
(?<subject>.+)$

Body: BREAKING CHANGE: <description>
Footer: Refs: #123, Closes #456
```

### 파싱 결과 구조

```python
ParsedCommit = {
    "hash": "abc1234",
    "type": "feat",           # 변경 유형
    "scope": "auth",          # 영향 범위 (선택)
    "breaking": True/False,   # Breaking Change
    "subject": "add OAuth2",  # 제목
    "body": "...",            # 본문
    "footer": {
        "refs": ["#123"],     # 참조 이슈
        "closes": ["#456"],   # 종료 이슈
        "breaking_change": "" # BREAKING CHANGE 설명
    },
    "author": "name <email>",
    "date": "2025-01-15",
    "files_changed": ["src/auth.py"],
    "insertions": 50,
    "deletions": 10
}
```

## 비정형 커밋 분류 전략

Conventional Commits를 사용하지 않는 프로젝트용:

### 키워드 기반 분류

```python
classification_rules = {
    "feat": ["add", "new", "implement", "introduce", "support",
             "추가", "신규", "구현", "도입"],
    "fix": ["fix", "bug", "patch", "resolve", "correct", "hotfix",
            "수정", "버그", "해결", "오류"],
    "refactor": ["refactor", "restructure", "reorganize", "clean",
                 "리팩토링", "리팩터", "정리"],
    "perf": ["performance", "optimize", "speed", "faster", "cache",
             "성능", "최적화", "캐시"],
    "docs": ["doc", "readme", "comment", "문서", "주석"],
    "test": ["test", "spec", "coverage", "테스트"],
    "ci": ["ci", "pipeline", "workflow", "deploy", "배포"],
    "style": ["format", "lint", "whitespace", "포맷"],
    "chore": ["bump", "update dep", "upgrade", "의존성"]
}
```

### diff 기반 분류 (키워드 실패 시)

```
1. 변경 파일 확장자 분석:
   - .md/.rst → docs
   - test_*.py / *.test.js → test
   - .yml/.yaml (CI 경로) → ci

2. 변경 패턴 분석:
   - 새 파일 추가 + export → feat
   - 기존 파일 수정 + error/exception → fix
   - import 추가 없이 코드 이동 → refactor

3. 변경 규모 분석:
   - +500줄 이상 → feat 가능성 높음
   - ±10줄 이내 → fix/style 가능성 높음
```

## PR/이슈 매핑 전략

```python
# 커밋에서 이슈 번호 추출
issue_patterns = [
    r'#(\d+)',                    # #123
    r'(?:close|fix|resolve)s?\s+#(\d+)',  # closes #123
    r'([A-Z]+-\d+)',              # JIRA-123
    r'GH-(\d+)',                  # GH-123
]

# PR에서 연관 이슈 추출 (Merge commit)
merge_pattern = r'Merge pull request #(\d+)'

# Squash merge에서 PR 번호 추출
squash_pattern = r'\(#(\d+)\)$'
```

## 변경 영향도 점수 계산

```python
def impact_score(commit):
    score = 0

    # 파일 수 기반
    score += min(len(commit.files), 10) * 2  # 최대 20

    # 변경 줄 수 기반
    changes = commit.insertions + commit.deletions
    if changes > 500: score += 30
    elif changes > 100: score += 20
    elif changes > 30: score += 10
    else: score += 5

    # Breaking Change
    if commit.breaking: score += 50

    # 공개 API 변경
    if any('api' in f or 'public' in f for f in commit.files):
        score += 15

    # 데이터베이스 마이그레이션
    if any('migration' in f for f in commit.files):
        score += 20

    return min(score, 100)

# 점수 해석:
# 80-100: Critical — 릴리스 노트 하이라이트
# 50-79: High — 릴리스 노트 포함
# 20-49: Medium — 변경 목록 포함
# 0-19: Low — 상세 목록에만 포함
```

## git 명령어 레시피

```bash
# 두 태그 사이 커밋 목록
git log v1.2.0..v2.0.0 --oneline --no-merges

# 변경 파일 포함
git log v1.2.0..v2.0.0 --name-only --pretty=format:"%H|%s|%an|%ai"

# diff 통계
git diff v1.2.0..v2.0.0 --stat

# 기여자 목록
git log v1.2.0..v2.0.0 --format="%aN" | sort -u

# Breaking Change 커밋만
git log v1.2.0..v2.0.0 --grep="BREAKING" --grep="!" --all-match
```
