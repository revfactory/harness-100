---
name: strategy-framework
description: "조직의 전략 프레임워크를 OKR 설계, BSC 매핑, SWOT 분석, 비전·미션 선언문, 전략 실행 로드맵으로 체계화하는 풀 파이프라인. '전략 프레임워크 만들어줘', 'OKR 설계해줘', 'BSC 분석', 'SWOT 분석', '비전 미션 작성', '전략 로드맵', '전략 수립', '중장기 전략', '경영전략 프레임워크', '전략 체계 설계' 등 조직 전략 수립 전반에 이 스킬을 사용한다. 기존 OKR이나 SWOT이 있는 경우에도 보완·검증을 지원한다. 단, 재무제표 작성, ERP 시스템 구축, 인사평가 실행, 실시간 KPI 대시보드 개발은 이 스킬의 범위가 아니다."
---

# Strategy Framework — 전략 프레임워크 풀 파이프라인

조직의 전략을 OKR→BSC→SWOT→비전·미션→실행 로드맵으로 체계화한다.

## 실행 모드

**에이전트 팀** — 5명이 SendMessage로 직접 통신하며 교차 검증한다.

## 에이전트 구성

| 에이전트 | 파일 | 역할 | 타입 |
|---------|------|------|------|
| okr-designer | `agents/okr-designer.md` | OKR 목표·핵심결과 설계, 정렬 | general-purpose |
| bsc-analyst | `agents/bsc-analyst.md` | BSC 4대 관점 매핑, KPI 체계 | general-purpose |
| swot-specialist | `agents/swot-specialist.md` | SWOT 분석, TOWS 전략 도출 | general-purpose |
| strategy-writer | `agents/strategy-writer.md` | 비전·미션, 전략 실행 로드맵 | general-purpose |
| strategy-reviewer | `agents/strategy-reviewer.md` | 교차 검증, 정합성 확인 | general-purpose |

## 워크플로우

### Phase 1: 준비 (오케스트레이터 직접 수행)

1. 사용자 입력에서 추출한다:
    - **조직 정보**: 조직명, 산업, 규모, 현재 상황
    - **전략 기간**: 연간/3개년/5개년
    - **기존 전략 자산** (선택): 기존 OKR, 비전·미션, 분석 자료
    - **특별 요구사항** (선택): 특정 프레임워크 강조, 특정 관점 집중
2. `_workspace/` 디렉토리를 프로젝트 루트에 생성한다
3. 입력을 정리하여 `_workspace/00_input.md`에 저장한다
4. 기존 파일이 있으면 `_workspace/`에 복사하고 해당 Phase를 건너뛴다
5. 요청 범위에 따라 **실행 모드를 결정**한다

### Phase 2: 팀 구성 및 실행

| 순서 | 작업 | 담당 | 의존 | 산출물 |
|------|------|------|------|--------|
| 1 | OKR 설계 | okr-designer | 없음 | `_workspace/01_okr_design.md` |
| 2a | BSC 매핑 | bsc-analyst | 작업 1 | `_workspace/02_bsc_mapping.md` |
| 2b | SWOT 분석 | swot-specialist | 작업 1 | `_workspace/03_swot_analysis.md` |
| 3 | 비전·미션+로드맵 | strategy-writer | 작업 1,2a,2b | `_workspace/04_vision_mission.md`, `_workspace/05_strategy_roadmap.md` |
| 4 | 전략 리뷰 | strategy-reviewer | 작업 1,2a,2b,3 | `_workspace/06_review_report.md` |

작업 2a(BSC)와 2b(SWOT)는 **병렬 실행**한다. 둘 다 작업 1(OKR)에만 의존하므로 동시에 시작할 수 있다.

**팀원 간 소통 흐름:**
- okr-designer 완료 → bsc-analyst에게 OKR 체계 전달, swot-specialist에게 전략적 가정 전달
- bsc-analyst 완료 → swot-specialist에게 전략적 사각지대 전달, strategy-writer에게 KPI 체계 전달
- swot-specialist 완료 → strategy-writer에게 TOWS 전략 우선순위 전달
- strategy-writer 완료 → strategy-reviewer에게 모든 문서 전달
- strategy-reviewer는 모든 산출물을 교차 검증. 🔴 필수 수정 발견 시 해당 에이전트에게 수정 요청 → 재작업 → 재검증 (최대 2회)

### Phase 3: 통합 및 최종 산출물

1. `_workspace/` 내 모든 파일을 확인한다
2. 리뷰 보고서의 🔴 필수 수정이 모두 반영되었는지 확인한다
3. 최종 요약을 사용자에게 보고한다:
    - OKR 설계서 — `01_okr_design.md`
    - BSC 매핑표 — `02_bsc_mapping.md`
    - SWOT 분석서 — `03_swot_analysis.md`
    - 비전·미션 선언문 — `04_vision_mission.md`
    - 전략 실행 로드맵 — `05_strategy_roadmap.md`
    - 리뷰 보고서 — `06_review_report.md`

## 작업 규모별 모드

| 사용자 요청 패턴 | 실행 모드 | 투입 에이전트 |
|----------------|----------|-------------|
| "전략 프레임워크 만들어줘", "풀 전략 체계" | **풀 파이프라인** | 5명 전원 |
| "OKR만 설계해줘" | **OKR 모드** | okr-designer + reviewer |
| "SWOT 분석해줘" | **SWOT 모드** | swot-specialist + reviewer |
| "비전 미션 써줘" (기존 분석 있음) | **문서 모드** | strategy-writer + reviewer |
| "이 OKR 검토해줘" | **리뷰 모드** | reviewer 단독 |
| "OKR이랑 BSC 만들어줘" | **분석 모드** | okr-designer + bsc-analyst + reviewer |

**기존 파일 활용**: 사용자가 OKR, SWOT 등 기존 파일을 제공하면, 해당 파일을 `_workspace/`의 적절한 번호 위치에 복사하고 해당 단계의 에이전트는 건너뛴다.

## 데이터 전달 프로토콜

| 전략 | 방식 | 용도 |
|------|------|------|
| 파일 기반 | `_workspace/` 디렉토리 | 주요 산출물 저장 및 공유 |
| 메시지 기반 | SendMessage | 실시간 핵심 정보 전달, 수정 요청 |

파일명 컨벤션: `{순번}_{산출물명}.md`

## 에러 핸들링

| 에러 유형 | 전략 |
|----------|------|
| 조직 정보 부족 | 산업 벤치마크 기반 가설 OKR 설계, "가설 기반" 태그 명시 |
| 웹 검색 실패 | 일반 지식 기반 작업, "데이터 제한" 명시 |
| 에이전트 실패 | 1회 재시도 → 실패 시 해당 산출물 없이 진행, 리뷰 보고서에 누락 명시 |
| 리뷰에서 🔴 발견 | 해당 에이전트에 수정 요청 → 재작업 → 재검증 (최대 2회) |
| OKR↔SWOT 모순 | 모순 지점을 명시하고 okr-designer·swot-specialist 간 조정 협의 |

## 테스트 시나리오

### 정상 흐름
**프롬프트**: "시리즈B 단계 SaaS 스타트업(직원 50명)의 2025년 전략 프레임워크를 만들어줘. B2B HR테크 분야이고, ARR 50억에서 100억으로 성장하려고 해"
**기대 결과**:
- OKR: 회사 레벨 3~5개 Objective + 부서별 캐스케이딩
- BSC: 4대 관점 KPI 매핑 + 전략맵, SaaS 핵심 메트릭(ARR, NRR, CAC, LTV) 반영
- SWOT: HR테크 산업 동향 반영, TOWS 전략 5개 이상
- 비전·미션: SaaS 기업에 적합한 선언문
- 로드맵: 분기별 마일스톤 + ARR 성장 경로

### 기존 파일 활용 흐름
**프롬프트**: "이미 SWOT 분석은 했어. 이걸 기반으로 OKR이랑 BSC, 로드맵까지 만들어줘" + SWOT 파일 첨부
**기대 결과**:
- SWOT 파일을 `_workspace/03_swot_analysis.md`로 복사
- swot-specialist 건너뛰고 okr-designer + bsc-analyst + strategy-writer + reviewer 투입
- 기존 SWOT의 TOWS 전략을 OKR과 로드맵에 반영

### 에러 흐름
**프롬프트**: "우리 회사 전략 프레임워크 만들어줘"
**기대 결과**:
- 조직 정보 부족 → 산업/규모/현황 추가 질문
- 최소 정보(산업명)만 제공 시 벤치마크 기반 가설 프레임워크 생성
- 모든 문서에 "가설 기반 — 실제 데이터로 검증 필요" 태그 명시

## 에이전트별 확장 스킬

에이전트의 도메인 전문성을 강화하는 확장 스킬:

| 스킬 | 파일 | 대상 에이전트 | 역할 |
|------|------|-------------|------|
| okr-quality-checker | `skills/okr-quality-checker/SKILL.md` | okr-designer, strategy-reviewer | QSIM/SMART-V 기준, OKR 구조 검증, 채점 시스템, 안티패턴 |
| tows-matrix-builder | `skills/tows-matrix-builder/SKILL.md` | swot-specialist, strategy-writer | TOWS 매트릭스 구조, SO/WO/ST/WT 전략 도출 가이드, 우선순위 평가 |
