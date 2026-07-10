---
name: content-repurposer
description: "1개 원본 콘텐츠를 블로그, SNS, 뉴스레터, 프레젠테이션, 스크립트 등 다양한 포맷으로 다중 변환하는 풀 리퍼포징 파이프라인. '이 콘텐츠 리퍼포징해줘', '블로그를 SNS로 변환', '콘텐츠 재활용', '멀티 포맷 변환', '이 글로 프레젠테이션 만들어줘', '이 보고서를 블로그로', '콘텐츠 다중 변환' 등 콘텐츠 리퍼포징 전반에 이 스킬을 사용한다. 단, 실제 이미지/영상 제작, 프레젠테이션 파일(.pptx) 생성, SNS 자동 발행은 이 스킬의 범위가 아니다."
---

# Content Repurposer — 콘텐츠 다중 변환 파이프라인

1개 원본 콘텐츠를 블로그→SNS→프레젠테이션으로 에이전트 팀이 협업하여 한 번에 변환한다.

## 실행 모드

**에이전트 팀** — 5명이 SendMessage로 직접 통신하며 교차 검증한다.

## 에이전트 구성

| 에이전트 | 파일 | 역할 | 타입 |
|---------|------|------|------|
| source-analyst | `agents/source-analyst.md` | 원본 분석, 변환 전략 수립 | general-purpose |
| blog-writer | `agents/blog-writer.md` | SEO 블로그 포스트 작성 | general-purpose |
| sns-copywriter | `agents/sns-copywriter.md` | 플랫폼별 SNS 포스트 | general-purpose |
| presentation-builder | `agents/presentation-builder.md` | 슬라이드 프레젠테이션 | general-purpose |
| quality-reviewer | `agents/quality-reviewer.md` | 메시지 일관성 교차 검증 | general-purpose |

## 워크플로우

### Phase 1: 준비 (오케스트레이터 직접 수행)

1. 사용자 입력에서 추출한다:
   - **원본 콘텐츠**: 변환할 원본 (텍스트, 파일, URL)
   - **변환 포맷** (선택): 원하는 변환 포맷 목록 (기본: 블로그+SNS+프레젠테이션)
   - **타깃 독자** (선택): 각 포맷의 타깃 독자
   - **브랜드 톤** (선택): 일관된 브랜드 보이스
   - **제약 조건** (선택): 특정 플랫폼, 길이 제한 등
2. `_workspace/` 디렉토리를 프로젝트 루트에 생성한다
3. 입력을 정리하여 `_workspace/00_input.md`에 저장한다
4. 원본 콘텐츠가 URL인 경우 WebFetch로 내용을 가져온다
5. 요청 범위에 따라 **실행 모드를 결정**한다

### Phase 2: 팀 구성 및 실행

| 순서 | 작업 | 담당 | 의존 | 산출물 |
|------|------|------|------|--------|
| 1 | 원본 분석 | source-analyst | 없음 | `_workspace/01_source_analysis.md` |
| 2a | 블로그 변환 | blog-writer | 작업 1 | `_workspace/02_blog_post.md` |
| 2b | SNS 변환 | sns-copywriter | 작업 1 | `_workspace/03_sns_package.md` |
| 2c | 프레젠테이션 변환 | presentation-builder | 작업 1 | `_workspace/04_presentation.md` |
| 3 | 품질 검증 | quality-reviewer | 작업 2a, 2b, 2c | `_workspace/05_review_report.md` |

작업 2a(블로그), 2b(SNS), 2c(프레젠테이션)는 **병렬 실행**한다. 모두 작업 1(원본 분석)에만 의존하므로 동시에 시작할 수 있다.

**팀원 간 소통 흐름:**
- source-analyst 완료 → 각 변환 에이전트에게 포맷별 전략 전달
- blog-writer 완료 → sns-copywriter에게 블로그 인용구·링크 전달
- sns-copywriter 완료 → presentation-builder에게 비주얼 일관성 정보 전달
- reviewer는 모든 산출물을 교차 검증. 🔴 필수 수정 발견 시 해당 에이전트에게 수정 요청 → 재작업 → 재검증 (최대 2회)

### Phase 3: 통합 및 최종 산출물

1. `_workspace/` 내 모든 파일을 확인한다
2. 리뷰 보고서의 🔴 필수 수정이 모두 반영되었는지 확인한다
3. 최종 요약을 사용자에게 보고한다:
   - 원본 분석 — `01_source_analysis.md`
   - 블로그 포스트 — `02_blog_post.md`
   - SNS 패키지 — `03_sns_package.md`
   - 프레젠테이션 — `04_presentation.md`
   - 리뷰 보고서 — `05_review_report.md`

## 작업 규모별 모드

| 사용자 요청 패턴 | 실행 모드 | 투입 에이전트 |
|----------------|----------|-------------|
| "이 콘텐츠 리퍼포징해줘", "풀 변환" | **풀 파이프라인** | 5명 전원 |
| "블로그로 변환해줘" | **블로그 모드** | source-analyst + blog-writer + quality-reviewer |
| "SNS 포스트로 만들어줘" | **SNS 모드** | source-analyst + sns-copywriter + quality-reviewer |
| "프레젠테이션으로 바꿔줘" | **프레젠테이션 모드** | source-analyst + presentation-builder + quality-reviewer |
| "이 변환 결과 검토해줘" | **리뷰 모드** | quality-reviewer 단독 |

**기존 파일 활용**: 사용자가 이미 변환된 콘텐츠를 제공하면, 해당 파일을 `_workspace/`에 복사하고 해당 변환 에이전트는 건너뛴다.

## 데이터 전달 프로토콜

| 전략 | 방식 | 용도 |
|------|------|------|
| 파일 기반 | `_workspace/` 디렉토리 | 주요 산출물 저장 및 공유 |
| 메시지 기반 | SendMessage | 실시간 핵심 정보 전달, 수정 요청 |
| 태스크 기반 | TaskCreate/TaskUpdate | 진행 상황 추적, 의존 관계 관리 |

파일명 컨벤션: `{순번}_{산출물}.{확장자}`

## 에러 핸들링

| 에러 유형 | 전략 |
|----------|------|
| 원본 URL 접근 실패 | 사용자에게 텍스트 직접 입력 요청, 또는 캐시된 내용으로 작업 |
| 원본이 너무 짧음 (500단어 미만) | 웹 검색으로 관련 자료 보충, "원본 보강" 명시 |
| 에이전트 실패 | 1회 재시도 → 실패 시 해당 포맷 없이 진행, 리뷰 보고서에 누락 명시 |
| 리뷰에서 🔴 발견 | 해당 에이전트에 수정 요청 → 재작업 → 재검증 (최대 2회) |

## 테스트 시나리오

### 정상 흐름
**프롬프트**: "이 블로그 글을 SNS, 프레젠테이션으로 리퍼포징해줘" + 2,000단어 블로그 글 첨부
**기대 결과**:
- 원본 분석: 구조 맵, 핵심 메시지 3개, 포맷별 변환 전략
- 블로그: SEO 최적화 재작성 (원본이 블로그인 경우 개선 버전)
- SNS: Twitter 스레드 8개, Instagram 캐러셀 8슬라이드, LinkedIn 포스트
- 프레젠테이션: 15슬라이드, 발표 노트 포함
- 리뷰: 메시지 일관성 매트릭스 전항목 확인

### 기존 파일 활용 흐름
**프롬프트**: "이 보고서를 프레젠테이션으로만 변환해줘" + PDF 파일 첨부
**기대 결과**:
- 프레젠테이션 모드: source-analyst + presentation-builder + quality-reviewer 투입
- blog-writer, sns-copywriter는 건너뜀

### 에러 흐름
**프롬프트**: "이 URL의 글을 리퍼포징해줘" + 접근 불가 URL
**기대 결과**:
- URL 접근 실패 → 사용자에게 텍스트 직접 입력 요청
- 사용자가 텍스트 제공 시 정상 파이프라인 진행
- 리뷰 보고서에 "원본 URL 접근 불가, 사용자 제공 텍스트 기반" 명시

## 에이전트별 확장 스킬

각 에이전트는 다음 확장 스킬의 전문 지식을 활용하여 산출물의 품질을 높인다:

| 에이전트 | 확장 스킬 | 제공 지식 |
|---------|----------|----------|
| sns-copywriter, blog-writer | `/platform-adaptation` | 플랫폼별 DNA, 변환 매트릭스, 메시지 일관성 체크 |
| source-analyst, presentation-builder | `/content-atomization` | MINE 분석 프레임워크, 원자 분류 체계, 슬라이드 변환 공식 |
