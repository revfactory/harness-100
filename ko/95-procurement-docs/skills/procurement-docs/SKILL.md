---
name: procurement-docs
description: "구매 문서세트 생성 파이프라인. 요구사항 정의부터 벤더 비교, 평가 기준, 계약 조건, 검수 기준까지 에이전트 팀이 협업 생성한다. '구매 문서 만들어줘', '벤더 비교표 작성', '구매 사양서', '평가 기준표', '검수 기준서', '조달 문서', '입찰 평가', 'RFP 작성', '벤더 선정' 등 구매·조달 문서 전반에 이 스킬을 사용한다. 실제 발주·계약 체결, 대금 지급 처리, 자산 등록은 이 스킬의 범위가 아니다."
---

# Procurement Docs — 구매 문서세트 생성 파이프라인

구매 요구사항 정의부터 벤더 비교, 평가 기준, 계약 조건 검토, 검수 기준서까지 에이전트 팀이 협업 생성한다.

## 실행 모드

**에이전트 팀** — 5명이 SendMessage로 직접 통신하며 교차 검증한다.

## 에이전트 구성

| 에이전트 | 파일 | 역할 | 타입 |
|---------|------|------|------|
| requirements-definer | `agents/requirements-definer.md` | 사양서, 수량, 납기, 예산 | general-purpose |
| vendor-comparator | `agents/vendor-comparator.md` | 후보 조사, 비교표, SWOT | general-purpose |
| evaluation-designer | `agents/evaluation-designer.md` | 배점, 가중치, 평가 프로세스 | general-purpose |
| contract-reviewer | `agents/contract-reviewer.md` | 약관, 리스크, SLA, 협상 | general-purpose |
| acceptance-builder | `agents/acceptance-builder.md` | 검수항목, 테스트, 합격기준 | general-purpose |

## 워크플로우

### Phase 1: 준비 (오케스트레이터 직접 수행)

1. 사용자 입력에서 추출한다:
    - **구매 대상**: 물품, 소프트웨어, 서비스, 공사 등
    - **구매 배경**: 신규 도입, 교체, 증설 등 구매 사유
    - **예산**: 예산 범위 또는 한도
    - **일정**: 희망 납기, 프로젝트 일정
    - **벤더 후보** (선택): 이미 검토 중인 벤더
    - **기존 문서** (선택): 기존 사양서, 계약서 초안
2. `_workspace/` 디렉토리를 프로젝트 루트에 생성한다
3. 입력을 정리하여 `_workspace/00_input.md`에 저장한다
4. 요청 범위에 따라 **실행 모드를 결정**한다

### Phase 2: 팀 구성 및 실행

| 순서 | 작업 | 담당 | 의존 | 산출물 |
|------|------|------|------|--------|
| 1 | 요구사항 정의 | definer | 없음 | `_workspace/01_requirements_spec.md` |
| 2 | 벤더 비교 분석 | comparator | 작업 1 | `_workspace/02_vendor_comparison.md` |
| 3a | 평가 기준표 | evaluator | 작업 1, 2 | `_workspace/03_evaluation_criteria.md` |
| 3b | 계약 조건 검토 | contract | 작업 1, 2 | `_workspace/04_contract_review.md` |
| 4 | 검수 기준서 | acceptance | 작업 1, 3b | `_workspace/05_acceptance_criteria.md` |

작업 3a(평가 기준)와 3b(계약 검토)는 **병렬 실행**한다.

**팀원 간 소통 흐름:**
- definer 완료 → comparator에게 요구사항·예산 전달, evaluator에게 우선순위·측정 기준 전달, contract에게 납품·지원 조건 전달, acceptance에게 필수 요구사항·측정 기준 전달
- comparator 완료 → evaluator에게 벤더 정보·비교 항목 전달, contract에게 라이선스·약관 특이사항 전달
- contract 완료 → acceptance에게 검수 조건·하자보증 전달
- 오케스트레이터가 전체 문서 간 정합성을 최종 검증

### Phase 3: 통합 및 최종 산출물

1. `_workspace/` 내 모든 파일을 확인한다
2. 교차 검증:
    - [ ] 요구사항의 모든 필수 항목이 검수 기준에 반영되었는가
    - [ ] 평가 기준의 가중치 합계가 100%인가
    - [ ] 계약 조건이 요구사항/검수 기준과 일치하는가
    - [ ] 벤더 비교표의 항목이 요구사항과 매핑되는가
3. `_workspace/06_procurement_summary.md`에 구매 종합 보고서 생성
4. 최종 요약을 사용자에게 보고한다

## 작업 규모별 모드

| 사용자 요청 패턴 | 실행 모드 | 투입 에이전트 |
|----------------|----------|-------------|
| "구매 문서 전체 만들어줘" | **풀 파이프라인** | 5명 전원 |
| "요구사항 사양서만 써줘" | **사양서 모드** | definer 단독 |
| "벤더 비교만 해줘" | **비교 모드** | definer + comparator |
| "평가 기준표만 만들어줘" | **평가 모드** | definer + evaluator |
| "이 계약서 검토해줘" | **검토 모드** | contract 단독 |
| "검수 기준서만 만들어줘" | **검수 모드** | definer + acceptance |

## 데이터 전달 프로토콜

| 전략 | 방식 | 용도 |
|------|------|------|
| 파일 기반 | `_workspace/` 디렉토리 | 주요 산출물 저장 및 공유 |
| 메시지 기반 | SendMessage | 실시간 핵심 정보 전달, 수정 요청 |
| 태스크 기반 | TaskCreate/TaskUpdate | 진행 상황 추적, 의존 관계 관리 |

## 에러 핸들링

| 에러 유형 | 전략 |
|----------|------|
| 구매 대상 불명확 | definer가 구체화 질문 목록 제시, 답변 기반 작업 |
| 벤더 정보 부족 | comparator가 웹 검색 실패 시 RFI 템플릿 제공, 사용자 직접 입력 요청 |
| 예산 미정 | 시장 가격 기반 예산 범위를 추정하여 제시, 사용자 확인 후 진행 |
| 법률 검토 필요 | contract가 "[법무 확인 필요]" 태그 부여, 법률 자문 대체 불가 경고 |
| 에이전트 실패 | 1회 재시도 → 실패 시 해당 산출물 없이 진행, 보고서에 명시 |

## 테스트 시나리오

### 정상 흐름
**프롬프트**: "클라우드 서버 호스팅 서비스 구매를 위한 문서세트를 만들어줘. 예산은 연 5천만원이고 AWS, Azure, GCP를 비교하고 싶어"
**기대 결과**:
- 사양서: 컴퓨팅·스토리지·네트워크 요구사항, SLA 요건
- 비교표: 3사 기능·가격·지원 비교, TCO 분석, SWOT
- 평가표: 기술 40% / 가격 30% / 지원 20% / 안정성 10% 배점
- 계약서: SLA 조항, 데이터 주권, 해지 조건, 협상 포인트
- 검수서: 인프라 구축 검수, 성능 테스트, SLA 충족 확인

### 기존 파일 활용 흐름
**프롬프트**: "이미 사양서가 있어. 벤더 비교랑 평가 기준표만 만들어줘" + 사양서 파일
**기대 결과**:
- 기존 사양서를 `_workspace/01_requirements_spec.md`로 복사
- 비교 모드 + 평가 모드: comparator + evaluator 투입
- 사양서 기반 벤더 비교 및 평가 기준표 생성

### 에러 흐름
**프롬프트**: "뭔가 사야 하는데 뭘 사야 할지 모르겠어, 업무용 노트북?"
**기대 결과**:
- definer가 구체화 질문 제시 (사용 목적, 사용자 수, 성능 요구 등)
- 사용자 답변 기반으로 요구사항 도출
- 예산 미정 시 시장 가격 범위 제시
- 보고서에 "요구사항 확정 필요" 명시

## 에이전트별 확장 스킬

| 확장 스킬 | 경로 | 대상 에이전트 | 역할 |
|----------|------|-------------|------|
| vendor-scoring | `skills/vendor-scoring/SKILL.md` | vendor-comparator, evaluation-designer | 벤더 평가 스코어카드, 가격 공식, 레퍼런스 체크 |
| contract-checklist | `skills/contract-checklist/SKILL.md` | contract-reviewer, acceptance-builder | 계약 10대 조항, SLA 설계, 검수 기준서 |
