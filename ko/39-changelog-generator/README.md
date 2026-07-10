# Changelog Generator Harness

릴리스 관리의 git이력분석→변경분류→릴리스노트생성→마이그레이션가이드→공지문작성을 에이전트 팀이 협업하여 수행하는 하네스.

## 구조

```

├── agents/
│   ├── commit-analyst.md           — 커밋 분석 (git 이력, PR, 브랜치 전략)
│   ├── change-classifier.md        — 변경 분류 (breaking/feature/fix/refactor)
│   ├── release-note-writer.md      — 릴리스 노트 작성 (사용자 관점, 기술 상세)
│   ├── migration-guide-writer.md   — 마이그레이션 가이드 (업그레이드 경로, 코드 변환)
│   └── announcement-writer.md      — 공지문 작성 (블로그, SNS, 이메일)
├── skills/
│   ├── changelog-generator/
│       └── SKILL.md                — 오케스트레이터 (팀 조율, 워크플로우, 에러핸들링)
│   ├── semver-analyzer/
│   │   └── SKILL.md                — SemVer 분석 (Breaking Change, 버전 범프)
│   └── commit-parser/
│       └── SKILL.md                — 커밋 파싱 (정규식, 비정형 분류, 영향도)
└── README.md                       — 이 파일
```

## 사용법

`/changelog-generator` 스킬을 트리거하거나, "릴리스 노트 만들어줘" 같은 자연어로 요청한다.

## 산출물

모든 산출물은 `_workspace/` 디렉토리에 저장된다:
- `00_input.md` — 사용자 입력 정리
- `01_commit_analysis.md` — 커밋 분석 보고서
- `02_change_classification.md` — 변경 분류 결과
- `03_release_notes.md` — 릴리스 노트
- `04_migration_guide.md` — 마이그레이션 가이드
- `05_announcement.md` — 공지문 (블로그/SNS/이메일)
