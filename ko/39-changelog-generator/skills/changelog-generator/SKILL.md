---
name: changelog-generator
description: "릴리스 관리를 에이전트 팀이 협업하여 수행하는 풀 파이프라인. '릴리스 노트 만들어줘', 'CHANGELOG 생성', '체인지로그 작성', '버전 릴리스 준비', '마이그레이션 가이드', '릴리스 공지문', '변경사항 정리', '새 버전 발표' 등 릴리스 관리 전반에 이 스킬을 사용한다. 단, CI/CD 파이프라인 구축, 자동 배포 설정, 버전 관리 정책 수립은 이 스킬의 범위가 아니다."
---

# Changelog Generator — 릴리스 관리 파이프라인

git 이력분석→변경분류→릴리스노트→마이그레이션가이드→공지문을 에이전트 팀이 협업하여 생성한다.

## 실행 모드

**에이전트 팀** — 5명이 SendMessage로 직접 통신하며 교차 검증한다.

## 에이전트 구성

| 에이전트 | 파일 | 역할 | 타입 |
|---------|------|------|------|
| commit-analyst | `agents/commit-analyst.md` | git 이력 분석 | general-purpose |
| change-classifier | `agents/change-classifier.md` | 변경 분류, 영향도 평가 | general-purpose |
| release-note-writer | `agents/release-note-writer.md` | 릴리스 노트 작성 | general-purpose |
| migration-guide-writer | `agents/migration-guide-writer.md` | 마이그레이션 가이드 | general-purpose |
| announcement-writer | `agents/announcement-writer.md` | 공지문 작성 (블로그/SNS/이메일) | general-purpose |

## 워크플로우

### Phase 1: 준비 (오케스트레이터 직접 수행)

1. 사용자 입력에서 추출한다:
    - **버전 범위**: 이전 버전 태그 ~ 현재 커밋/태그
    - **프로젝트 정보**: 프로젝트명, 저장소 URL, 언어/프레임워크
    - **릴리스 유형**: 정규/핫픽스/프리릴리스
    - **공지 채널**: 블로그/SNS/이메일/Slack 중 필요한 채널
    - **기존 CHANGELOG** (선택): 기존 형식을 따를 CHANGELOG.md
2. `_workspace/` 디렉토리를 프로젝트 루트에 생성한다
3. 입력을 정리하여 `_workspace/00_input.md`에 저장한다
4. git 저장소를 확인하고 버전 범위를 확정한다
5. 기존 파일이 있으면 `_workspace/`에 복사하고 해당 Phase를 건너뛴다
6. 요청 범위에 따라 **실행 모드를 결정**한다

### Phase 2: 팀 구성 및 실행

| 순서 | 작업 | 담당 | 의존 | 산출물 |
|------|------|------|------|--------|
| 1 | 커밋 분석 | analyst | 없음 | `_workspace/01_commit_analysis.md` |
| 2 | 변경 분류 | classifier | 작업 1 | `_workspace/02_change_classification.md` |
| 3a | 릴리스 노트 | note-writer | 작업 2 | `_workspace/03_release_notes.md` |
| 3b | 마이그레이션 가이드 | migration-writer | 작업 2 | `_workspace/04_migration_guide.md` |
| 4 | 공지문 작성 | announcement | 작업 3a, 3b | `_workspace/05_announcement.md` |

작업 3a(릴리스 노트)와 3b(마이그레이션 가이드)는 **병렬 실행**한다.

**팀원 간 소통 흐름:**
- analyst 완료 → classifier에게 커밋 목록·diff 전달
- classifier 완료 → note-writer에게 분류 결과 전달, migration-writer에게 Breaking Changes 상세 전달
- note-writer 완료 → announcement에게 하이라이트·버전번호 전달
- migration-writer 완료 → announcement에게 마이그레이션 핵심 요약 전달, note-writer에게 가이드 링크 전달

### Phase 3: 통합 및 최종 산출물

1. 모든 산출물의 버전 번호 일관성을 확인한다
2. Breaking Change 정보가 릴리스 노트 ↔ 마이그레이션 가이드 ↔ 공지문 간에 일치하는지 검증한다
3. 기존 CHANGELOG.md가 있으면 새 버전을 맨 위에 추가한다
4. 최종 요약을 사용자에게 보고한다

## 작업 규모별 모드

| 사용자 요청 패턴 | 실행 모드 | 투입 에이전트 |
|----------------|----------|-------------|
| "릴리스 준비 전체", "체인지로그 + 공지문" | **풀 파이프라인** | 5명 전원 |
| "CHANGELOG만 만들어줘" | **노트 모드** | analyst + classifier + note-writer |
| "마이그레이션 가이드만" | **마이그레이션 모드** | analyst + classifier + migration-writer |
| "릴리스 공지문만 써줘" (노트 완료) | **공지 모드** | announcement 단독 |
| "이 커밋들 분류해줘" | **분류 모드** | analyst + classifier |

## 데이터 전달 프로토콜

| 전략 | 방식 | 용도 |
|------|------|------|
| 파일 기반 | `_workspace/` 디렉토리 | 주요 산출물 저장 및 공유 |
| 메시지 기반 | SendMessage | 실시간 핵심 정보 전달 |
| git 명령 | bash 실행 | 커밋 로그, diff, 태그 정보 추출 |

## 에러 핸들링

| 에러 유형 | 전략 |
|----------|------|
| git 저장소 없음 | 사용자에게 커밋 목록/변경 내역 직접 입력 요청 |
| 태그 없음 | 최근 N개 커밋 또는 날짜 범위로 대체 |
| Conventional Commits 미사용 | 커밋 메시지+diff 기반 LLM 분류 |
| Breaking Change 없음 | migration-writer는 "불필요" 확인 문서만 작성 |
| 에이전트 실패 | 1회 재시도 → 실패 시 해당 산출물 없이 진행 |

## 테스트 시나리오

### 정상 흐름
**프롬프트**: "v1.2.0에서 v2.0.0까지 릴리스 노트 전체를 만들어줘"
**기대 결과**:
- 커밋 분석: 두 태그 사이 모든 커밋 추출, PR/이슈 매핑
- 변경 분류: MAJOR 릴리스이므로 Breaking Changes 식별, SemVer 검증
- 릴리스 노트: Keep a Changelog 형식, 하이라이트 3~5개
- 마이그레이션: before/after 코드 예시, 단계별 절차
- 공지문: 블로그 + SNS + 이메일 형식

### 기존 파일 활용 흐름
**프롬프트**: "이 릴리스 노트가 있는데 공지문만 써줘" + 릴리스 노트 첨부
**기대 결과**:
- 기존 릴리스 노트를 `_workspace/03_release_notes.md`로 복사
- 공지 모드: announcement 단독 투입
- analyst, classifier, note-writer, migration-writer는 건너뜀

### 에러 흐름
**프롬프트**: "릴리스 노트 만들어줘" (git 저장소 없음)
**기대 결과**:
- git 저장소 부재 감지
- 사용자에게 변경사항 목록 직접 입력 요청
- 입력 받은 내용으로 분류 → 릴리스 노트 생성

## 에이전트별 확장 스킬

에이전트의 도메인 전문성을 강화하는 확장 스킬:

| 스킬 | 파일 | 대상 에이전트 | 역할 |
|------|------|-------------|------|
| semver-analyzer | `skills/semver-analyzer/SKILL.md` | change-classifier, release-note-writer | SemVer 규칙, Breaking Change 판정 매트릭스, Conventional Commits 매핑 |
| commit-parser | `skills/commit-parser/SKILL.md` | commit-analyst, change-classifier | 커밋 파싱 정규식, 비정형 커밋 분류, PR/이슈 매핑, 영향도 점수 |
