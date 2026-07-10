---
name: newsletter-engine
description: "뉴스레터 큐레이션, 작성, A/B테스트, 발송 최적화를 에이전트 팀이 협업하여 한 번에 생성하는 풀 프로덕션 파이프라인. '뉴스레터 작성해줘', '뉴스레터 기획', '이메일 뉴스레터', '뉴스레터 큐레이션', '뉴스레터 A/B테스트', '구독자 이메일', '위클리 뉴스레터', '뉴스레터 발송 최적화' 등 뉴스레터 제작 전반에 이 스킬을 사용한다. 기존 콘텐츠가 있는 경우에도 편집·최적화를 지원한다. 단, 이메일 발송 시스템(Mailchimp, Stibee) API 연동, 구독자 DB 관리, 실제 A/B테스트 실행은 이 스킬의 범위가 아니다."
---

# Newsletter Engine — 뉴스레터 풀 프로덕션 파이프라인

뉴스레터의 큐레이션→작성→A/B테스트→편집→발행을 에이전트 팀이 협업하여 한 번에 생성한다.

## 실행 모드

**에이전트 팀** — 5명이 SendMessage로 직접 통신하며 교차 검증한다.

## 에이전트 구성

| 에이전트 | 파일 | 역할 | 타입 |
|---------|------|------|------|
| curator | `agents/curator.md` | 소스 수집, 트렌드 분석, 콘텐츠 선별 | general-purpose |
| copywriter | `agents/copywriter.md` | 헤드라인, 본문, CTA 작성 | general-purpose |
| analyst | `agents/analyst.md` | A/B테스트 설계, 발송 최적화 | general-purpose |
| editor-in-chief | `agents/editor-in-chief.md` | 톤 일관성, 최종 편집 | general-purpose |
| quality-reviewer | `agents/quality-reviewer.md` | 교차 검증, 정합성 확인 | general-purpose |

## 워크플로우

### Phase 1: 준비 (오케스트레이터 직접 수행)

1. 사용자 입력에서 추출한다:
   - **주제/테마**: 뉴스레터가 다룰 주제
   - **뉴스레터 정보** (선택): 브랜드 톤, 구독자 규모, 발행 주기
   - **타깃 독자** (선택): 구독자 특성, 관심사
   - **제약 조건** (선택): 길이, 특정 섹션 구성
   - **기존 파일** (선택): 사용자가 제공한 콘텐츠, 이전 호 등
2. `_workspace/` 디렉토리를 프로젝트 루트에 생성한다
3. 입력을 정리하여 `_workspace/00_input.md`에 저장한다
4. 기존 파일이 있으면 `_workspace/`에 복사하고 해당 Phase를 건너뛴다
5. 요청 범위에 따라 **실행 모드를 결정**한다

### Phase 2: 팀 구성 및 실행

| 순서 | 작업 | 담당 | 의존 | 산출물 |
|------|------|------|------|--------|
| 1 | 콘텐츠 큐레이션 | curator | 없음 | `_workspace/01_curation_brief.md` |
| 2 | 뉴스레터 작성 | copywriter | 작업 1 | `_workspace/02_newsletter_draft.md` |
| 3 | A/B테스트 설계 | analyst | 작업 1, 2 | `_workspace/03_ab_test_plan.md` |
| 4 | 최종 편집 | editor-in-chief | 작업 2, 3 | `_workspace/04_editorial_final.md` |
| 5 | 품질 검증 | quality-reviewer | 작업 2, 3, 4 | `_workspace/05_review_report.md` |

**팀원 간 소통 흐름:**
- curator 완료 → copywriter에게 앵글·콘텐츠 전달, analyst에게 트렌드 키워드 전달
- copywriter 완료 → analyst에게 A/B 변형 소재 전달, editor-in-chief에게 초안 전달
- analyst 완료 → editor-in-chief에게 발송 최적화·A/B 권장 전달
- editor-in-chief 완료 → quality-reviewer에게 최종본 전달
- reviewer는 모든 산출물을 교차 검증. 🔴 필수 수정 발견 시 해당 에이전트에게 수정 요청 → 재작업 → 재검증 (최대 2회)

### Phase 3: 통합 및 최종 산출물

1. `_workspace/` 내 모든 파일을 확인한다
2. 리뷰 보고서의 🔴 필수 수정이 모두 반영되었는지 확인한다
3. 최종 요약을 사용자에게 보고한다:
   - 큐레이션 브리프 — `01_curation_brief.md`
   - 뉴스레터 초안 — `02_newsletter_draft.md`
   - A/B테스트 설계 — `03_ab_test_plan.md`
   - 편집장 최종본 — `04_editorial_final.md`
   - 리뷰 보고서 — `05_review_report.md`

## 작업 규모별 모드

| 사용자 요청 패턴 | 실행 모드 | 투입 에이전트 |
|----------------|----------|-------------|
| "뉴스레터 기획해줘", "풀 프로덕션" | **풀 파이프라인** | 5명 전원 |
| "뉴스레터 본문만 써줘" | **카피 모드** | curator + copywriter + quality-reviewer |
| "이 콘텐츠로 뉴스레터 만들어줘" (기존 파일) | **편집 모드** | copywriter + editor-in-chief + quality-reviewer |
| "A/B테스트 설계해줘" (기존 뉴스레터 있음) | **분석 모드** | analyst + quality-reviewer |
| "이 뉴스레터 검토해줘" | **리뷰 모드** | quality-reviewer 단독 |

**기존 파일 활용**: 사용자가 콘텐츠나 이전 뉴스레터를 제공하면, 해당 파일을 `_workspace/`의 적절한 위치에 복사하고 해당 단계를 건너뛴다.

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
| 웹 검색 실패 | 큐레이터가 사용자 제공 자료 기반으로 작업, "실시간 데이터 미반영" 명시 |
| 브랜드 톤 불명확 | 기본 톤(전문적+친근) 적용, 편집장이 첫 호 발행 후 톤 조정 권장 |
| 에이전트 실패 | 1회 재시도 → 실패 시 해당 산출물 없이 진행, 리뷰 보고서에 누락 명시 |
| 리뷰에서 🔴 발견 | 해당 에이전트에 수정 요청 → 재작업 → 재검증 (최대 2회) |

## 테스트 시나리오

### 정상 흐름
**프롬프트**: "AI 산업 동향을 다루는 주간 뉴스레터를 만들어줘. 개발자 대상, 전문적이면서 위트 있는 톤"
**기대 결과**:
- 큐레이션: AI 관련 최신 기사 5건 이상, 트렌드 분석, 추천 리소스
- 카피: 제목(A/B 2안), 프리헤더, 인트로+메인 스토리+서브+추천+클로징
- 분석: A/B테스트 2종(제목, CTA), 발송 시간 권장, 성과 예측
- 편집: 톤 검수, 법적 체크, 최종본
- 리뷰: 정합성 매트릭스 전항목 확인

### 기존 파일 활용 흐름
**프롬프트**: "이 기사 모음으로 뉴스레터 만들어줘" + 콘텐츠 파일 첨부
**기대 결과**:
- 기존 콘텐츠를 `_workspace/01_curation_brief.md`로 정리
- 편집 모드: copywriter + editor-in-chief + quality-reviewer 투입
- curator는 건너뜀

### 에러 흐름
**프롬프트**: "뉴스레터 제목만 A/B테스트 설계해줘"
**기대 결과**:
- 분석 모드로 전환 (analyst + quality-reviewer)
- 뉴스레터 본문이 없으므로 분석가가 제목 패턴 기반 A/B안 제시
- 리뷰 보고서에 "본문/큐레이션 미생성" 명시

## 에이전트별 확장 스킬

각 에이전트는 다음 확장 스킬의 전문 지식을 활용하여 산출물의 품질을 높인다:

| 에이전트 | 확장 스킬 | 제공 지식 |
|---------|----------|----------|
| copywriter | `/email-copywriting` | CURVE 제목줄 프레임워크, CTA 설계, F-패턴 본문 구조 |
| analyst, curator | `/audience-segmentation` | BEAR 세그멘테이션 모델, 발송 시간 최적화, 웰컴 시리즈 |
| editor-in-chief, analyst | `/deliverability-optimization` | 스팸 필터 회피, Gmail 프로모션탭 대응, 법적 컴플라이언스 |
