---
name: sales-enablement
description: "B2B 영업 지원 풀 파이프라인. 고객 분석, 맞춤 제안서, 프레젠테이션, 팔로업 계획을 에이전트 팀이 협업하여 생성한다. '영업 제안서 만들어줘', '고객 분석해줘', '제안서 작성', '영업 PT 만들어줘', '팔로업 계획', '세일즈 자료', '영업 전략', '고객 제안', 'B2B 제안서' 등 영업 지원 전반에 이 스킬을 사용한다. 기존 고객 분석이나 제안서가 있는 경우에도 보완·확장을 지원한다. 단, CRM 시스템 구축, 실시간 파이프라인 대시보드, 계약서 법무 검토, 실제 이메일 발송은 이 스킬의 범위가 아니다."
---

# Sales Enablement — 영업 지원 풀 파이프라인

B2B 영업의 고객분석→제안서→프레젠테이션→팔로업을 에이전트 팀이 협업하여 한 번에 생성한다.

## 실행 모드

**에이전트 팀** — 5명이 SendMessage로 직접 통신하며 교차 검증한다.

## 에이전트 구성

| 에이전트 | 파일 | 역할 | 타입 |
|---------|------|------|------|
| customer-analyst | `agents/customer-analyst.md` | 고객 프로파일링, 니즈, DMU 분석 | general-purpose |
| proposal-writer | `agents/proposal-writer.md` | 맞춤 제안서, ROI, 가격 설계 | general-purpose |
| presenter | `agents/presenter.md` | PT 스토리라인, 슬라이드 구성 | general-purpose |
| followup-manager | `agents/followup-manager.md` | 팔로업 일정, 이의 대응, 협상 | general-purpose |
| sales-reviewer | `agents/sales-reviewer.md` | 교차 검증, 정합성 확인 | general-purpose |

## 워크플로우

### Phase 1: 준비 (오케스트레이터 직접 수행)

1. 사용자 입력에서 추출한다:
    - **고객 정보**: 고객사명, 산업, 규모, 담당자
    - **자사 정보**: 제품/서비스, 강점, 가격 범위
    - **영업 상황**: 딜 스테이지, 경쟁 상황, 타임라인
    - **기존 자료** (선택): 고객 분석, 기존 제안서 등
2. `_workspace/` 디렉토리를 프로젝트 루트에 생성한다
3. 입력을 정리하여 `_workspace/00_input.md`에 저장한다
4. 기존 파일이 있으면 `_workspace/`에 복사하고 해당 Phase를 건너뛴다

### Phase 2: 팀 구성 및 실행

| 순서 | 작업 | 담당 | 의존 | 산출물 |
|------|------|------|------|--------|
| 1 | 고객 분석 | customer-analyst | 없음 | `_workspace/01_customer_analysis.md` |
| 2 | 제안서 작성 | proposal-writer | 작업 1 | `_workspace/02_proposal.md` |
| 3a | 프레젠테이션 설계 | presenter | 작업 1, 2 | `_workspace/03_presentation.md` |
| 3b | 팔로업 계획 | followup-manager | 작업 1, 2 | `_workspace/04_followup_plan.md` |
| 4 | 영업 리뷰 | sales-reviewer | 작업 1,2,3a,3b | `_workspace/05_review_report.md` |

작업 3a(PT)와 3b(팔로업)는 **병렬 실행**한다. 둘 다 작업 1(고객분석)과 2(제안서)에 의존하므로 제안서 완성 후 동시 시작한다.

**팀원 간 소통 흐름:**
- customer-analyst 완료 → proposal-writer에게 Pain Point·BANT 전달
- proposal-writer 완료 → presenter에게 가치 제안·ROI 전달, followup-manager에게 가격·이의사항 전달
- presenter 완료 → followup-manager에게 Q&A 예측 전달
- sales-reviewer는 모든 산출물을 교차 검증. 🔴 필수 수정 발견 시 해당 에이전트에게 수정 요청 → 재작업 → 재검증 (최대 2회)

### Phase 3: 통합 및 최종 산출물

1. `_workspace/` 내 모든 파일을 확인한다
2. 리뷰 보고서의 🔴 필수 수정이 모두 반영되었는지 확인한다
3. 최종 요약을 사용자에게 보고한다

## 작업 규모별 모드

| 사용자 요청 패턴 | 실행 모드 | 투입 에이전트 |
|----------------|----------|-------------|
| "영업 자료 풀세트 만들어줘" | **풀 파이프라인** | 5명 전원 |
| "제안서만 써줘" | **제안서 모드** | customer-analyst + proposal-writer + reviewer |
| "영업 PT 만들어줘" (제안서 있음) | **PT 모드** | presenter + reviewer |
| "팔로업 전략 짜줘" | **팔로업 모드** | followup-manager + reviewer |
| "이 제안서 검토해줘" | **리뷰 모드** | reviewer 단독 |

## 데이터 전달 프로토콜

| 전략 | 방식 | 용도 |
|------|------|------|
| 파일 기반 | `_workspace/` 디렉토리 | 주요 산출물 저장 및 공유 |
| 메시지 기반 | SendMessage | 실시간 핵심 정보 전달, 수정 요청 |

## 에러 핸들링

| 에러 유형 | 전략 |
|----------|------|
| 고객 정보 부족 | 산업/규모 기반 가설 프로파일 구성, "가설 기반" 태그 명시 |
| 자사 제품 정보 부족 | 일반 B2B 솔루션 프레임워크로 작성, "제품 정보 반영 필요" 태그 |
| 웹 검색 실패 | 일반 지식 기반 작업, "데이터 제한" 명시 |
| 에이전트 실패 | 1회 재시도 → 실패 시 해당 산출물 없이 진행, 리뷰 보고서에 누락 명시 |
| 리뷰에서 🔴 발견 | 해당 에이전트에 수정 요청 → 재작업 → 재검증 (최대 2회) |

## 테스트 시나리오

### 정상 흐름
**프롬프트**: "삼성SDS에 우리 클라우드 보안 솔루션을 제안하려고 해. 연간 계약 5억 규모이고, CISO가 의사결정자야. 현재 P사 솔루션을 쓰고 있어"
**기대 결과**:
- 고객 분석: 삼성SDS 공개 정보 기반 프로파일 + DMU 매핑
- 제안서: 클라우드 보안 특화 가치 제안 + P사 대비 차별점 + ROI 3단계
- PT: CISO 관점 메시지 강조, 보안 ROI 시각화
- 팔로업: 대기업 의사결정 주기 반영 (4~8주), 이의 대응 5개 이상

### 기존 파일 활용 흐름
**프롬프트**: "이 고객 분석 자료 있어. 이걸로 제안서랑 PT만 만들어줘" + 파일 첨부
**기대 결과**:
- 기존 분석을 `_workspace/01_customer_analysis.md`로 복사
- customer-analyst 건너뛰고 proposal-writer + presenter + reviewer 투입

### 에러 흐름
**프롬프트**: "영업 제안서 만들어줘, 고객은 중소기업이야"
**기대 결과**:
- 고객 정보 부족 → 산업/제품 추가 질문
- 최소 정보만 제공 시 일반 중소기업 대상 프레임워크 제안서 생성
- "고객 맞춤화 필요" 태그 명시

## 에이전트별 확장 스킬

에이전트의 도메인 전문성을 강화하는 확장 스킬:

| 스킬 | 파일 | 대상 에이전트 | 역할 |
|------|------|-------------|------|
| roi-calculator | `skills/roi-calculator/SKILL.md` | proposal-writer, presenter | ROI/TCO/Payback 공식, 가치 정량화 프레임워크, 3단계 프레젠테이션 |
| objection-handler | `skills/objection-handler/SKILL.md` | followup-manager, proposal-writer | BANT+C 이의 분류, LAER 대응 프레임워크, 심각도 판별, 협상 전략 |
