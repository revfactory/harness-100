---
name: social-media-manager
description: "SNS 콘텐츠 전략 수립, 포스트 작성, 비주얼 기획, 해시태그 전략을 에이전트 팀이 협업하여 한 번에 생성하는 풀 프로덕션 파이프라인. 'SNS 콘텐츠 만들어줘', '인스타그램 포스트 써줘', '소셜미디어 전략', 'SNS 콘텐츠 달력', '해시태그 전략', '인스타 카피', '틱톡 콘텐츠', '링크드인 포스트', 'SNS 마케팅' 등 소셜미디어 콘텐츠 관리 전반에 이 스킬을 사용한다. 기존 브랜드 가이드가 있는 경우에도 포스트 작성이나 해시태그 분석을 지원한다. 단, 실제 SNS 계정 운영(게시, 답글, DM), 광고 집행, 분석 API 연동, 인플루언서 섭외는 이 스킬의 범위가 아니다."
---

# Social Media Manager — SNS 콘텐츠 풀 프로덕션 파이프라인

SNS 콘텐츠의 전략→포스트→비주얼→해시태그를 에이전트 팀이 협업하여 한 번에 생성한다.

## 실행 모드

**에이전트 팀** — 5명이 SendMessage로 직접 통신하며 교차 검증한다.

## 에이전트 구성

| 에이전트 | 파일 | 역할 | 타입 |
|---------|------|------|------|
| sns-strategist | `agents/sns-strategist.md` | 채널 분석, 콘텐츠 달력, 캠페인 설계 | general-purpose |
| copywriter | `agents/copywriter.md` | 포스트 카피, 캡션, CTA | general-purpose |
| visual-planner | `agents/visual-planner.md` | 이미지 컨셉, 카드뉴스, 릴스 기획 | general-purpose |
| hashtag-analyst | `agents/hashtag-analyst.md` | 해시태그 전략, 트렌드 분석 | general-purpose |
| performance-reviewer | `agents/performance-reviewer.md` | KPI 정렬, 품질 검증 | general-purpose |

## 워크플로우

### Phase 1: 준비 (오케스트레이터 직접 수행)

1. 사용자 입력에서 추출한다:
   - **브랜드/계정 정보**: 업종, 톤앤보이스, 타깃 고객
   - **플랫폼**: 인스타그램, 트위터/X, 틱톡, 페이스북, 링크드인
   - **기간**: 주간/월간 콘텐츠 계획
   - **목표** (선택): 브랜드 인지도, 전환, 커뮤니티 성장
   - **기존 파일** (선택): 브랜드 가이드, 기존 콘텐츠
2. `_workspace/` 디렉토리를 프로젝트 루트에 생성한다
3. 입력을 정리하여 `_workspace/00_input.md`에 저장한다
4. 기존 파일이 있으면 `_workspace/`에 복사하고 해당 Phase를 건너뛴다
5. 요청 범위에 따라 **실행 모드를 결정**한다

### Phase 2: 팀 구성 및 실행

| 순서 | 작업 | 담당 | 의존 | 산출물 |
|------|------|------|------|--------|
| 1 | SNS 전략 수립 | sns-strategist | 없음 | `_workspace/01_strategy.md` |
| 2a | 포스트 카피 | copywriter | 작업 1 | `_workspace/02_posts.md` |
| 2b | 해시태그 전략 | hashtag-analyst | 작업 1 | `_workspace/04_hashtags.md` |
| 3 | 비주얼 기획 | visual-planner | 작업 1, 2a | `_workspace/03_visuals.md` |
| 4 | 성과 검증 | performance-reviewer | 작업 2a, 2b, 3 | `_workspace/05_review_report.md` |

작업 2a(카피)와 2b(해시태그)는 **병렬 실행**한다. 비주얼 기획(3)은 카피 완료 후 시작한다.

**팀원 간 소통 흐름:**
- sns-strategist 완료 → copywriter에게 톤·달력 전달, hashtag-analyst에게 키워드·경쟁계정 전달, visual-planner에게 브랜드가이드 전달
- copywriter 완료 → visual-planner에게 텍스트 오버레이·이미지 키워드 전달, hashtag-analyst에게 포스트 주제 전달
- hashtag-analyst 완료 → visual-planner에게 트렌드 해시태그 전달
- performance-reviewer는 모든 산출물을 교차 검증. 🔴 필수 수정 발견 시 해당 에이전트에게 수정 요청 → 재작업 → 재검증 (최대 2회)

### Phase 3: 통합 및 최종 산출물

1. `_workspace/` 내 모든 파일을 확인한다
2. 리뷰 보고서의 🔴 필수 수정이 모두 반영되었는지 확인한다
3. 최종 요약을 사용자에게 보고한다:
   - 전략서/달력 — `01_strategy.md`
   - 포스트 카피 — `02_posts.md`
   - 비주얼 기획 — `03_visuals.md`
   - 해시태그 전략 — `04_hashtags.md`
   - 리뷰 보고서 — `05_review_report.md`

## 작업 규모별 모드

| 사용자 요청 패턴 | 실행 모드 | 투입 에이전트 |
|----------------|----------|-------------|
| "SNS 콘텐츠 만들어줘", "풀 관리" | **풀 파이프라인** | 5명 전원 |
| "콘텐츠 달력만 짜줘" | **전략 모드** | strategist + reviewer |
| "인스타 포스트만 써줘" | **카피 모드** | copywriter + hashtag-analyst + reviewer |
| "해시태그만 분석해줘" | **해시태그 모드** | hashtag-analyst + reviewer |
| "이 포스트 검토해줘" | **리뷰 모드** | reviewer 단독 |

**기존 파일 활용**: 사용자가 브랜드 가이드, 콘텐츠 달력 등을 제공하면, 해당 파일을 `_workspace/`의 적절한 위치에 복사하고 해당 에이전트는 건너뛴다.

## 데이터 전달 프로토콜

| 전략 | 방식 | 용도 |
|------|------|------|
| 파일 기반 | `_workspace/` 디렉토리 | 주요 산출물 저장 및 공유 |
| 메시지 기반 | SendMessage | 실시간 핵심 정보 전달, 수정 요청 |
| 태스크 기반 | TaskCreate/TaskUpdate | 진행 상황 추적, 의존 관계 관리 |

파일명 컨벤션: `{순번}_{산출물명}.{확장자}`

## 에러 핸들링

| 에러 유형 | 전략 |
|----------|------|
| 브랜드 정보 부족 | 업종 기반 표준 가이드 적용, "커스터마이징 필요" 명시 |
| 웹 검색 실패 | 일반 SNS 지식으로 작업, "트렌드 데이터 제한" 명시 |
| 에이전트 실패 | 1회 재시도 → 실패 시 해당 산출물 없이 진행, 리뷰 보고서에 누락 명시 |
| 리뷰에서 🔴 발견 | 해당 에이전트에 수정 요청 → 재작업 → 재검증 (최대 2회) |
| 이미지 생성 실패 | 텍스트 컨셉과 프롬프트만으로 진행, 사용자 재시도 가능 |

## 테스트 시나리오

### 정상 흐름
**프롬프트**: "건강식품 브랜드의 인스타그램 월간 콘텐츠를 기획해줘. 타깃은 2030 여성, 톤은 친근하고 밝게."
**기대 결과**:
- 전략: 월간 달력(주 3~4회), 콘텐츠 필러 믹스, KPI 설정
- 포스트: 12~16개 인스타 캡션 (피드+릴스+카루셀 혼합)
- 비주얼: 포스트별 이미지 컨셉, 카루셀 구성, 릴스 스토리보드
- 해시태그: 포스트별 해시태그 세트 (피라미드 전략 적용)
- 리뷰: 정합성 매트릭스 전항목 확인

### 기존 파일 활용 흐름
**프롬프트**: "이 브랜드 가이드로 이번 주 인스타 포스트 3개만 써줘" + 가이드 파일 첨부
**기대 결과**:
- 브랜드 가이드를 `_workspace/`에 복사
- 카피 모드: copywriter + hashtag-analyst + reviewer 투입
- strategist, visual-planner는 건너뜀 (또는 최소 투입)

### 에러 흐름
**프롬프트**: "SNS 해시태그만 분석해줘, 주제는 카페 창업"
**기대 결과**:
- 해시태그 모드로 전환 (hashtag-analyst + reviewer)
- 브랜드 정보 부족하므로 "카페 창업" 업종 기반 해시태그 라이브러리 생성
- 리뷰 보고서에 "전략/포스트/비주얼 미생성" 명시

## 에이전트별 확장 스킬

각 에이전트는 다음 확장 스킬의 전문 지식을 활용하여 산출물의 품질을 높인다:

| 에이전트 | 확장 스킬 | 제공 지식 |
|---------|----------|----------|
| sns-strategist, visual-planner | `/platform-algorithms` | Instagram/TikTok/LinkedIn/X 알고리즘, 골든타임, 포맷별 최적화 |
| copywriter | `/viral-copywriting` | 15가지 훅 패턴, 플랫폼별 카피 구조, 감정 트리거, CTA 설계 |
| hashtag-analyst | `/hashtag-science` | 피라미드 전략, 플랫폼별 해시태그 규칙, 리서치 프로세스, 섀도우밴 방지 |
