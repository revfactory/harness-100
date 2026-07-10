---
name: code-reviewer
description: "코드 리뷰 자동화 풀 파이프라인. 스타일→보안→성능→아키텍처 4개 영역을 에이전트 팀이 협업하여 체계적으로 리뷰한다. '코드 리뷰해줘', '이 코드 봐줘', '코드 검토', 'PR 리뷰', '코드 품질 분석', '보안 리뷰', '성능 리뷰', '아키텍처 리뷰', '코드 스타일 검사' 등 코드 리뷰 전반에 이 스킬을 사용한다. 특정 영역만 요청하는 경우에도 지원한다. 단, 실제 CI/CD 통합, 자동 수정(auto-fix), Git 커밋/머지 작업은 이 스킬의 범위가 아니다."
---

# Code Reviewer — 코드 리뷰 자동화 파이프라인

코드의 스타일→보안→성능→아키텍처를 에이전트 팀이 체계적으로 리뷰한다.

## 실행 모드

**에이전트 팀** — 5명이 SendMessage로 직접 통신하며 교차 검증한다.

## 에이전트 구성

| 에이전트 | 파일 | 역할 | 타입 |
|---------|------|------|------|
| style-inspector | `agents/style-inspector.md` | 컨벤션, 포맷팅, 네이밍, 가독성 | general-purpose |
| security-analyst | `agents/security-analyst.md` | 취약점, 인젝션, 인증, 데이터 노출 | general-purpose |
| performance-analyst | `agents/performance-analyst.md` | 복잡도, 메모리, 동시성, 쿼리 | general-purpose |
| architecture-reviewer | `agents/architecture-reviewer.md` | 설계 패턴, SOLID, 의존성, 결합도 | general-purpose |
| review-synthesizer | `agents/review-synthesizer.md` | 우선순위 종합, 충돌 해결, 최종 판정 | general-purpose |

## 워크플로우

### Phase 1: 준비 (오케스트레이터 직접 수행)

1. 사용자 입력에서 추출한다:
   - **대상 코드**: 파일 경로, PR 번호, diff, 디렉토리
   - **언어/프레임워크**: 자동 감지 또는 사용자 지정
   - **리뷰 범위** (선택): 특정 영역만 요청한 경우
   - **컨텍스트** (선택): PR 설명, 관련 이슈, 변경 이유
   - **스타일 가이드** (선택): 팀 고유 컨벤션
2. `_workspace/` 디렉토리를 프로젝트 루트에 생성한다
3. 입력을 정리하여 `_workspace/00_input.md`에 저장한다
4. 대상 코드를 식별하고 리뷰 범위를 결정한다
5. 기존 파일이 있으면 `_workspace/`에 복사하고 해당 Phase를 건너뛴다
6. 요청 범위에 따라 **실행 모드를 결정**한다

### Phase 2: 팀 구성 및 실행

| 순서 | 작업 | 담당 | 의존 | 산출물 |
|------|------|------|------|--------|
| 1a | 스타일 리뷰 | style-inspector | 없음 | `_workspace/01_style_review.md` |
| 1b | 보안 리뷰 | security-analyst | 없음 | `_workspace/02_security_review.md` |
| 1c | 성능 리뷰 | performance-analyst | 없음 | `_workspace/03_performance_review.md` |
| 1d | 아키텍처 리뷰 | architecture-reviewer | 없음 | `_workspace/04_architecture_review.md` |
| 2 | 종합 리뷰 | review-synthesizer | 작업 1a~1d | `_workspace/05_review_summary.md` |

작업 1a~1d(4개 영역 리뷰)는 **모두 병렬 실행**한다.

**팀원 간 소통 흐름:**
- style-inspector → security-analyst에게 주석 내 민감 정보 전달, performance-analyst에게 복잡 함수 목록 전달
- security-analyst → performance-analyst에게 보안 조치 성능 영향 전달, architecture-reviewer에게 인증 아키텍처 전달
- performance-analyst → architecture-reviewer에게 구조적 병목 전달
- review-synthesizer는 모든 리뷰를 통합. 영역 간 충돌 발견 시 해당 분석가에게 추가 분석 요청

### Phase 3: 통합 및 최종 산출물

종합 보고서를 기반으로 최종 산출물을 정리한다:

1. `_workspace/` 내 모든 리뷰를 확인한다
2. 최종 판정(Approve/Request Changes/Reject)을 결정한다
3. 최종 요약을 사용자에게 보고한다

## 작업 규모별 모드

| 사용자 요청 패턴 | 실행 모드 | 투입 에이전트 |
|----------------|----------|-------------|
| "코드 리뷰해줘", "전체 리뷰" | **풀 리뷰** | 5명 전원 |
| "보안 리뷰만 해줘" | **보안 모드** | security-analyst + review-synthesizer |
| "성능 분석해줘" | **성능 모드** | performance-analyst + review-synthesizer |
| "아키텍처 리뷰해줘" | **아키텍처 모드** | architecture-reviewer + review-synthesizer |
| "코드 스타일만 봐줘" | **스타일 모드** | style-inspector + review-synthesizer |

**PR 리뷰**: PR 번호가 제공되면 diff를 추출하여 변경된 코드만 리뷰한다. 전체 파일 컨텍스트도 참조하지만 리뷰 대상은 diff에 집중한다.

## 데이터 전달 프로토콜

| 전략 | 방식 | 용도 |
|------|------|------|
| 파일 기반 | `_workspace/` 디렉토리 | 주요 산출물 저장 및 공유 |
| 메시지 기반 | SendMessage | 실시간 핵심 정보 전달, 추가 분석 요청 |
| 태스크 기반 | TaskCreate/TaskUpdate | 진행 상황 추적, 의존 관계 관리 |

파일명 컨벤션: `{순번}_{에이전트}_{산출물}.{확장자}`

## 에러 핸들링

| 에러 유형 | 전략 |
|----------|------|
| 언어 미식별 | 파일 확장자 + 코드 패턴에서 자동 감지 |
| 대용량 코드 | 변경된 파일 또는 핵심 파일에 집중, 범위를 리뷰 보고서에 명시 |
| 에이전트 실패 | 1회 재시도 → 실패 시 해당 영역 없이 진행, 종합 보고서에 누락 명시 |
| 영역 간 충돌 | review-synthesizer가 트레이드오프 분석 후 판정 |
| 컨텍스트 부족 | PR 설명이나 이슈 번호가 없으면 코드만으로 리뷰, 제한 사항 명시 |

## 테스트 시나리오

### 정상 흐름
**프롬프트**: "이 Python Flask 프로젝트를 전체 코드 리뷰해줘" + 코드 파일/디렉토리
**기대 결과**:
- 스타일: PEP 8 기준, 네이밍/포맷팅/가독성 검사, Black/flake8 설정 제안
- 보안: SQL 인젝션, XSS, 하드코딩 시크릿, 의존성 CVE 검사
- 성능: 쿼리 최적화, N+1, 메모리 사용, 캐싱 기회
- 아키텍처: MVC 패턴 준수, SOLID, 의존성 분석
- 종합: 통합 우선순위, 최종 판정, 액션 아이템

### 기존 파일 활용 흐름
**프롬프트**: "이 PR의 보안만 리뷰해줘" + PR diff
**기대 결과**:
- 보안 모드: security-analyst + review-synthesizer 투입
- diff 중심 리뷰, 전체 파일 컨텍스트 참조
- style-inspector, performance-analyst, architecture-reviewer 건너뜀

### 에러 흐름
**프롬프트**: "이 코드 봐줘" + 단일 파일 (100줄 미만)
**기대 결과**:
- 소규모 코드 → 아키텍처 리뷰는 함수 분리/모듈 설계 관점으로 축소
- 풀 리뷰 모드로 실행하되, 각 영역이 코드 규모에 맞게 조정
- 종합 보고서에 "단일 파일 리뷰, 아키텍처 평가 제한적" 명시

## 에이전트별 확장 스킬

개별 에이전트의 도메인 전문성을 강화하는 확장 스킬:

| 스킬 | 대상 에이전트 | 역할 |
|------|-------------|------|
| `vulnerability-patterns` | security-analyst | CWE 분류, 언어별 취약 코드 패턴, 안전한 대안 |
| `refactoring-catalog` | architecture-reviewer, performance-analyst | 코드 스멜→리팩토링 매핑, SOLID 위반, 복잡도 측정 |
