---
name: hiring-pipeline
description: "채용 프로세스의 JD작성, 소싱, 스크리닝, 면접 설계, 평가, 오퍼까지 에이전트 팀이 협업하여 한 번에 생성하는 풀 파이프라인. '채용', '인재 채용', 'JD 작성', '직무기술서', '채용공고', '면접 질문', '면접 설계', '채용 프로세스', '소싱 전략', '스크리닝', '오퍼레터', '채용 파이프라인', 'hiring', '인재 확보' 등 채용 전반에 이 스킬을 사용한다. 단, 실제 채용 플랫폼(ATS) 연동, 급여 시스템 등록, 채용 계약서의 법적 효력 보장, 레퍼런스 체크 실행은 이 스킬의 범위가 아니다."
---

# Hiring Pipeline — 채용 프로세스 풀 파이프라인

채용의 JD작성→소싱→스크리닝→면접→평가→오퍼를 에이전트 팀이 협업하여 한 번에 생성한다.

## 실행 모드

**에이전트 팀** — 5명이 SendMessage로 직접 통신하며 교차 검증한다.

## 에이전트 구성

| 에이전트 | 파일 | 역할 | 타입 |
|---------|------|------|------|
| jd-writer | `agents/jd-writer.md` | 직무기술서, 채용공고 | general-purpose |
| sourcing-specialist | `agents/sourcing-specialist.md` | 채널전략, 아웃리치 | general-purpose |
| screening-expert | `agents/screening-expert.md` | 서류평가, 과제, 스크리닝 | general-purpose |
| interview-designer | `agents/interview-designer.md` | 구조화면접, 질문, 평가표 | general-purpose |
| offer-coordinator | `agents/offer-coordinator.md` | 최종평가, 보상, 오퍼 | general-purpose |

## 워크플로우

### Phase 1: 준비 (오케스트레이터 직접 수행)

1. 사용자 입력에서 추출한다:
    - **포지션**: 채용할 직무, 직급
    - **조직 정보**: 회사명, 팀 구성, 문화
    - **채용 조건**: 고용 형태, 근무 형태, 급여 범위
    - **긴급도**: 채용 기한, 채용 인원
    - **기존 자료** (선택): 기존 JD, 지원자 현황
2. `_workspace/` 디렉토리를 프로젝트 루트에 생성한다
3. 입력을 정리하여 `_workspace/00_input.md`에 저장한다
4. 기존 자료가 있으면 `_workspace/`에 복사하고 해당 Phase를 조정한다
5. 요청 범위에 따라 **실행 모드를 결정**한다

### Phase 2: 팀 구성 및 실행

| 순서 | 작업 | 담당 | 의존 | 산출물 |
|------|------|------|------|--------|
| 1 | JD 작성 | writer | 없음 | `_workspace/01_job_description.md` |
| 2 | 소싱 전략 | sourcing | 작업 1 | `_workspace/02_sourcing_strategy.md` |
| 3 | 스크리닝 설계 | screening | 작업 1 | `_workspace/03_screening_framework.md` |
| 4 | 면접 설계 | interview | 작업 1, 3 | `_workspace/04_interview_design.md` |
| 5 | 평가·오퍼 | offer | 작업 1, 2, 3, 4 | `_workspace/05_evaluation_offer.md` |

작업 2(소싱)와 3(스크리닝)은 **병렬 실행**한다. 둘 다 작업 1(JD)에만 의존한다.

**팀원 간 소통 흐름:**
- writer 완료 → sourcing에게 타깃 프로필·EVP, screening에게 역량·평가기준 전달
- sourcing 완료 → offer에게 시장 보상 수준 전달
- screening 완료 → interview에게 심층 확인 필요 역량 전달
- interview 완료 → offer에게 평가표 구조·채용 추천 기준 전달
- offer는 전체 파이프라인을 교차 검증, 불일치 발견 시 수정 요청 (최대 2회)

### Phase 3: 통합 및 최종 산출물

1. `_workspace/` 내 모든 파일을 확인한다
2. offer의 정합성 검증 결과를 반영한다
3. 최종 요약을 사용자에게 보고한다

## 작업 규모별 모드

| 사용자 요청 패턴 | 실행 모드 | 투입 에이전트 |
|----------------|----------|-------------|
| "채용 프로세스 전체 설계해줘" | **풀 파이프라인** | 5명 전원 |
| "JD만 써줘" | **JD 모드** | writer 단독 |
| "면접 질문 만들어줘" | **면접 모드** | writer + interview |
| "이 JD로 소싱 전략 짜줘" (기존 JD) | **소싱 모드** | sourcing 단독 |
| "채용 스크리닝 기준 만들어줘" | **스크리닝 모드** | writer + screening |

## 데이터 전달 프로토콜

| 전략 | 방식 | 용도 |
|------|------|------|
| 파일 기반 | `_workspace/` 디렉토리 | 주요 산출물 저장 및 공유 |
| 메시지 기반 | SendMessage | 실시간 핵심 정보 전달, 수정 요청 |
| 태스크 기반 | TaskCreate/TaskUpdate | 진행 상황 추적, 의존 관계 관리 |

파일명 컨벤션: `{순번}_{에이전트}_{산출물}.{확장자}`

## 에러 핸들링

| 에러 유형 | 전략 |
|----------|------|
| 직무 정보 부족 | writer가 표준 JD 템플릿 + 맞춤화 가이드 제공 |
| 급여 정보 없음 | sourcing이 시장 벤치마크 조사, 3단계 범위 제안 |
| 웹 검색 실패 | 일반 지식 기반 JD/소싱 전략, "[시장 데이터 미반영]" 명시 |
| 에이전트 실패 | 1회 재시도 → 실패 시 해당 산출물 없이 진행 |
| 정합성 불일치 | offer가 수정 요청 → 재작업 (최대 2회) |

## 테스트 시나리오

### 정상 흐름
**프롬프트**: "시니어 백엔드 개발자 1명을 채용하려고 해. 연봉 8천~1억, 원격근무 가능, 한 달 안에 채용하고 싶어."
**기대 결과**:
- JD: 시니어 백엔드 역량 5개, 매력적인 채용공고, 평가 기준
- 소싱: LinkedIn Boolean 쿼리, 아웃리치 템플릿 3종, 채널별 전략
- 스크리닝: 코딩 테스트 + 시스템 설계 과제, 전화 스크리닝 5문항
- 면접: 기술 면접(라이브코딩) + 문화 면접, STAR 질문 10개+
- 오퍼: 시장 벤치마크 대비 보상, 오퍼레터, 협상 가이드

### 부분 요청 흐름
**프롬프트**: "이 JD로 면접 질문만 만들어줘" + JD 파일
**기대 결과**:
- 면접 모드 (writer + interview)
- 기존 JD 기반 역량 추출 후 구조화 면접 질문 설계
- writer는 역량 기준 초안만 보강

### 에러 흐름
**프롬프트**: "채용해야 하는데 어떤 직무인지 잘 모르겠어"
**기대 결과**:
- writer가 업무 내용/목표 질문으로 직무 분석 시작
- 유사 직무 3개 벤치마킹 제안
- 최소한의 정보로 초안 JD 작성 후 사용자 확인 요청

## 에이전트별 확장 스킬

| 확장 스킬 | 경로 | 대상 에이전트 | 역할 |
|----------|------|-------------|------|
| competency-model | `skills/competency-model/SKILL.md` | jd-writer, screening-expert | 역량 정의, 수준 체계, 스크리닝 매트릭스 |
| interview-scorecard | `skills/interview-scorecard/SKILL.md` | interview-designer | 구조화 면접, BEI 질문 뱅크, 편향 방지 |
