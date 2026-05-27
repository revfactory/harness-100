---
name: contract-analyzer
description: "계약서 분석·작성·검토·위험 평가를 에이전트 팀이 수행하는 파이프라인. '계약서 검토해줘', '계약서 분석', '계약서 작성', '계약 리스크 평가', 'contract review', '계약 조항 수정', '계약서 비교', 'NDA 검토', '용역 계약서', '임대차 계약서', '고용 계약서', '라이선스 계약' 등 계약 관리 전반에 이 스킬을 사용한다. 단, 법률 자문 제공, 소송 수행, 공증 업무, 법원 서류 작성은 이 스킬의 범위가 아니다."
---

# Contract Analyzer — 계약서 분석·작성·검토 파이프라인

계약서의 조항 분석→작성/수정→리스크 평가→비교 검토→종합 의견을 에이전트 팀이 협업하여 수행한다.

> ⚠️ 이 파이프라인은 법률 전문가의 조언을 대체하지 않습니다.

## 실행 모드

**에이전트 팀** — 5명이 SendMessage로 직접 통신하며 교차 검증한다.

## 에이전트 구성

| 에이전트 | 파일 | 역할 | 타입 |
|---------|------|------|------|
| clause-analyst | `agents/clause-analyst.md` | 조항 구조·해석·필수 조항 확인 | general-purpose |
| clause-drafter | `agents/clause-drafter.md` | 조항 작성·수정안 제시 | general-purpose |
| risk-assessor | `agents/risk-assessor.md` | 법적·사업적 리스크 평가 | general-purpose |
| comparison-reviewer | `agents/comparison-reviewer.md` | 표준/이전 버전 비교·협상 포인트 | general-purpose |
| contract-coordinator | `agents/contract-coordinator.md` | 종합 의견·정합성 검증 | general-purpose |

## 워크플로우

### Phase 1: 준비 (오케스트레이터 직접 수행)

1. 사용자 입력에서 추출한다:
    - **계약서 원문**: 분석할 계약서 (파일 또는 텍스트)
    - **계약 유형**: 매매/용역/임대/NDA/고용/라이선스 등
    - **당사자 입장**: 갑/을 중 사용자의 입장
    - **특별 관심사항** (선택): 특정 조항, 리스크, 비교 대상
    - **비교 대상** (선택): 표준 양식, 이전 버전
2. `_workspace/` 디렉토리를 프로젝트 루트에 생성한다
3. 입력을 정리하여 `_workspace/00_input.md`에 저장한다
4. 계약서 원문이 있으면 `_workspace/original_contract.md`로 복사한다
5. 요청 범위에 따라 **실행 모드를 결정**한다

### Phase 2: 팀 구성 및 실행

| 순서 | 작업 | 담당 | 의존 | 산출물 |
|------|------|------|------|--------|
| 1 | 조항 분석 | clause-analyst | 없음 | `_workspace/01_clause_analysis.md` |
| 2a | 리스크 평가 | risk-assessor | 작업 1 | `_workspace/03_risk_assessment.md` |
| 2b | 비교 검토 | comparison-reviewer | 작업 1 | `_workspace/04_comparison_report.md` |
| 3 | 조항 작성/수정 | clause-drafter | 작업 1, 2a, 2b | `_workspace/02_draft_clauses.md` |
| 4 | 종합 의견 | contract-coordinator | 작업 1, 2a, 2b, 3 | `_workspace/05_final_opinion.md` |

작업 2a(리스크)와 2b(비교)는 **병렬 실행**한다.

**팀원 간 소통 흐름:**
- clause-analyst 완료 → risk-assessor에게 위험 조항 전달, comparison-reviewer에게 구조 정보 전달
- risk-assessor + comparison-reviewer 완료 → clause-drafter에게 수정 필요 사항 전달
- clause-drafter 완료 → contract-coordinator가 전체 산출물 종합 검증
- contract-coordinator: 🔴 불일치 발견 시 해당 에이전트에게 수정 요청 → 재작업 → 재검증 (최대 2회)

### Phase 3: 통합 및 최종 산출물

1. `_workspace/` 내 모든 파일을 확인한다
2. 종합 의견의 🔴 필수 조치가 수정안에 모두 반영되었는지 확인한다
3. 최종 요약을 사용자에게 보고한다:
    - 조항 분석서 — `01_clause_analysis.md`
    - 수정안 — `02_draft_clauses.md`
    - 리스크 평가 — `03_risk_assessment.md`
    - 비교 검토 — `04_comparison_report.md`
    - 종합 의견 — `05_final_opinion.md`

## 작업 규모별 모드

| 사용자 요청 패턴 | 실행 모드 | 투입 에이전트 |
|----------------|----------|-------------|
| "계약서 검토해줘", "전체 분석" | **풀 분석** | 5명 전원 |
| "계약서 써줘", "계약서 작성" | **작성 모드** | clause-drafter + risk-assessor + contract-coordinator |
| "리스크만 평가해줘" | **리스크 모드** | clause-analyst + risk-assessor |
| "이전 버전과 비교해줘" | **비교 모드** | clause-analyst + comparison-reviewer |
| "이 조항 수정해줘" | **수정 모드** | clause-drafter 단독 |

**기존 파일 활용**: 비교 대상(표준, 이전 버전)이 제공되면 comparison-reviewer가 활용한다.

## 데이터 전달 프로토콜

| 전략 | 방식 | 용도 |
|------|------|------|
| 파일 기반 | `_workspace/` 디렉토리 | 주요 산출물 저장 및 공유 |
| 메시지 기반 | SendMessage | 실시간 핵심 정보 전달, 수정 요청 |
| 웹 탐색 | WebSearch/WebFetch | 표준 양식, 관련 법률, 판례 조사 |

## 에러 핸들링

| 에러 유형 | 전략 |
|----------|------|
| 계약서 원문 없음 | 계약 유형별 표준 템플릿 기반으로 작성 모드 전환 |
| 당사자 입장 불명 | 갑/을 양측 분석 병행, 사용자에게 입장 확인 요청 |
| 관할법 불명 | 한국법 기준 기본 분석, 타 법률 적용 가능성 명시 |
| 웹 검색 실패 | 일반 법률 지식 기반 작업, "최신 판례 미확인" 명시 |
| 에이전트 실패 | 1회 재시도 → 실패 시 해당 산출물 없이 진행, 보고에 누락 명시 |

## 테스트 시나리오

### 정상 흐름
**프롬프트**: "이 소프트웨어 개발 용역 계약서를 검토해줘. 우리는 을(수급사)이야." + 계약서 파일 제공
**기대 결과**:
- 조항 분석: 전체 구조 맵, 조항별 법적·실무적 분석, 필수 조항 체크
- 리스크 평가: 을 입장에서의 리스크, 불리 조항 식별, 완화 전략
- 비교 검토: 소프트웨어 개발 표준 계약 대비 차이
- 수정안: 불리 조항 수정 문구, 보호 조항 추가
- 종합 의견: 서명 가능 여부, 필수 수정 목록, 체크리스트

### 신규 작성 흐름
**프롬프트**: "프리랜서 디자인 용역 계약서 작성해줘. 갑 입장이야."
**기대 결과**:
- 작성 모드: clause-drafter가 표준 용역 계약서 초안 작성
- risk-assessor가 작성된 초안의 리스크 확인
- contract-coordinator가 최종 검증

### 에러 흐름
**프롬프트**: "이 계약서 괜찮은지 봐줘" + 영문 NDA 제공
**기대 결과**:
- 영문 NDA 분석, 핵심 용어 한/영 병기
- 한국법 기준으로 분석하되, 영미법 관행 차이 설명
- 관할법 확인 권고를 종합 의견에 포함

## 에이전트별 확장 스킬

| 에이전트 | 확장 스킬 | 용도 |
|---------|----------|------|
| risk-assessor, clause-analyst | `clause-risk-database` | 위험 조항 패턴 DB, 리스크 스코어링 알고리즘 |
| clause-drafter, comparison-reviewer | `negotiation-playbook` | 협상 전략 프레임워크, 수정안 문구 템플릿 |
