---
name: sop-writer
description: "표준운영절차(SOP)를 에이전트 팀이 협업하여 프로세스분석→절차서→체크리스트→교육자료→버전관리까지 한 번에 생성하는 풀 파이프라인. 'SOP 만들어줘', '표준운영절차서 작성', '업무 절차서', '작업 매뉴얼', '운영 절차', '절차서 작성해줘', '체크리스트 만들어줘', '업무 프로세스 문서화' 등 SOP 작성 전반에 이 스킬을 사용한다. 기존 프로세스 문서가 있으면 절차서·체크리스트·교육자료 작성을 지원한다. 단, 실제 BPM 시스템 구축, 워크플로우 자동화 엔진 개발, ISO 인증 심사 대행은 이 스킬의 범위가 아니다."
---

# SOP Writer — 표준운영절차 풀 파이프라인

표준운영절차(SOP)의 프로세스분석→절차서→체크리스트→교육자료→버전관리를 에이전트 팀이 협업하여 한 번에 생성한다.

## 실행 모드

**에이전트 팀** — 5명이 SendMessage로 직접 통신하며 교차 검증한다.

## 에이전트 구성

| 에이전트 | 파일 | 역할 | 타입 |
|---------|------|------|------|
| process-analyst | `agents/process-analyst.md` | 현행 업무 흐름 분석, SIPOC, RACI | general-purpose |
| procedure-writer | `agents/procedure-writer.md` | 단계별 절차서 작성, 의사결정 분기 | general-purpose |
| checklist-designer | `agents/checklist-designer.md` | 실행 점검표, 품질 게이트 설계 | general-purpose |
| training-developer | `agents/training-developer.md` | 교육 가이드, 시나리오 연습, 평가 문항 | general-purpose |
| version-controller | `agents/version-controller.md` | 버전 관리, 교차 검증 | general-purpose |

## 워크플로우

### Phase 1: 준비 (오케스트레이터 직접 수행)

1. 사용자 입력에서 추출한다:
    - **대상 프로세스**: 어떤 업무/절차에 대한 SOP인가
    - **적용 범위**: 대상 부서/팀/조직
    - **규제 요건** (선택): 관련 법규, 인증(ISO, HACCP 등)
    - **기존 문서** (선택): 현행 매뉴얼, 업무 기술서, 규정집
2. `_workspace/` 디렉토리를 프로젝트 루트에 생성한다
3. 입력을 정리하여 `_workspace/00_input.md`에 저장한다
4. 기존 파일이 있으면 `_workspace/`에 복사하고 해당 Phase를 건너뛴다
5. 요청 범위에 따라 **실행 모드를 결정**한다

### Phase 2: 팀 구성 및 실행

| 순서 | 작업 | 담당 | 의존 | 산출물 |
|------|------|------|------|--------|
| 1 | 프로세스 분석 | analyst | 없음 | `_workspace/01_process_analysis.md` |
| 2 | 절차서 작성 | writer | 작업 1 | `_workspace/02_procedure_document.md` |
| 3a | 체크리스트 설계 | designer | 작업 2 | `_workspace/03_checklists.md` |
| 3b | 교육자료 제작 | developer | 작업 2 | `_workspace/04_training_materials.md` |
| 4 | 버전 관리 및 검증 | controller | 작업 3a, 3b | `_workspace/05_version_control.md` |

작업 3a(체크리스트)와 3b(교육자료)는 **병렬 실행**한다. 둘 다 작업 2(절차서)에만 의존한다.

**팀원 간 소통 흐름:**
- analyst 완료 → writer에게 프로세스 흐름도+RACI+예외경로 전달, designer에게 품질 게이트 지점 전달
- writer 완료 → designer에게 검증 기준 전달, developer에게 난이도 높은 단계+실수 사례 전달
- designer 완료 → developer에게 체크리스트 사용법 전달
- controller는 모든 산출물을 교차 검증. 🔴 필수 수정 발견 시 해당 에이전트에게 수정 요청 → 재작업 → 재검증 (최대 2회)

### Phase 3: 통합 및 최종 산출물

1. `_workspace/` 내 모든 파일을 확인한다
2. 검증 보고서의 🔴 필수 수정이 모두 반영되었는지 확인한다
3. 최종 요약을 사용자에게 보고한다:
    - 프로세스 분석 — `01_process_analysis.md`
    - 표준 절차서 — `02_procedure_document.md`
    - 체크리스트 세트 — `03_checklists.md`
    - 교육자료 — `04_training_materials.md`
    - 버전 관리 및 검증 — `05_version_control.md`

## 작업 규모별 모드

| 사용자 요청 패턴 | 실행 모드 | 투입 에이전트 |
|----------------|----------|-------------|
| "SOP 만들어줘", "절차서 전체" | **풀 파이프라인** | 5명 전원 |
| "이 프로세스 절차서만 써줘" | **절차서 모드** | analyst + writer + controller |
| "체크리스트만 만들어줘" (절차서 제공) | **체크리스트 모드** | designer + controller |
| "교육자료 만들어줘" (절차서 제공) | **교육 모드** | developer + controller |
| "이 절차서 검토해줘" | **검토 모드** | controller 단독 |

**기존 파일 활용**: 사용자가 기존 절차서, 매뉴얼 등을 제공하면 해당 단계를 건너뛴다.

## 데이터 전달 프로토콜

| 전략 | 방식 | 용도 |
|------|------|------|
| 파일 기반 | `_workspace/` 디렉토리 | 주요 산출물 저장 및 공유 |
| 메시지 기반 | SendMessage | 실시간 핵심 정보 전달, 수정 요청 |

파일명 컨벤션: `{순번}_{에이전트}_{산출물}.{확장자}`

## 에러 핸들링

| 에러 유형 | 전략 |
|----------|------|
| 기존 문서 없음 | 사용자 인터뷰(채팅) 기반 프로세스 재구성, 산업 표준 참조 |
| 규제 요건 불명확 | 해당 산업의 일반 규제 프레임워크를 웹 검색으로 조사 |
| 에이전트 실패 | 1회 재시도 → 실패 시 해당 산출물 없이 진행, 검증 보고서에 누락 명시 |
| 검증에서 🔴 발견 | 해당 에이전트에 수정 요청 → 재작업 → 재검증 (최대 2회) |
| 프로세스가 너무 복잡 | 하위 프로세스로 분리하여 각각 SOP 생성 |

## 테스트 시나리오

### 정상 흐름
**프롬프트**: "신규 직원 입사 처리 프로세스 SOP를 만들어줘. 인사팀 대상이고 50인 규모 회사야."
**기대 결과**:
- 프로세스 분석: 채용확정→입사서류→시스템등록→장비지급→교육→OJT 흐름도
- 절차서: 단계별 상세 절차 + RACI + 의사결정 분기
- 체크리스트: 입사 전/당일/1주일/1개월 점검표
- 교육자료: 인사담당자 교육 가이드 + 시나리오 연습 + 평가 문항
- 검증: 정합성 매트릭스 전항목 확인

### 기존 문서 활용 흐름
**프롬프트**: "이 업무 매뉴얼로 체크리스트랑 교육자료 만들어줘" + 매뉴얼 파일 제공
**기대 결과**:
- 프로세스 분석과 절차서 작성 건너뜀
- 제공된 매뉴얼을 `_workspace/02_procedure_document.md`로 정리
- designer + developer + controller 투입

### 에러 흐름
**프롬프트**: "우리 팀 업무 SOP 만들어줘, 관련 문서는 없어"
**기대 결과**:
- 분석가가 업무 내용에 대해 사용자에게 질문
- 답변 기반으로 프로세스 재구성
- 검증 보고서에 "사용자 인터뷰 기반 작성 — 현장 검증 필요" 명시

## 에이전트별 확장 스킬

| 확장 스킬 | 경로 | 대상 에이전트 | 역할 |
|----------|------|-------------|------|
| process-mapping | `skills/process-mapping/SKILL.md` | process-analyst | SIPOC, VSM, RACI, Swim Lane 매핑 방법론 |
| checklist-design | `skills/checklist-design/SKILL.md` | checklist-designer | 체크리스트 유형, 7원칙, 품질 게이트 설계 |
