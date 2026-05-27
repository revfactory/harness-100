---
name: sustainability-audit
description: "ESG/지속가능성 감사의 환경, 사회, 거버넌스 평가와 통합 보고서, 개선 계획을 에이전트 팀이 협업하여 한 번에 생성하는 풀 감사 파이프라인. 'ESG 감사 해줘', '지속가능성 보고서 작성', 'ESG 평가', '탄소배출량 산정', 'ESG 등급 진단', '거버넌스 점검', '사회적 책임 평가', 'GRI 보고서', 'TCFD 공시', 'ESG 개선 계획' 등 ESG/지속가능성 관련 전반에 이 스킬을 사용한다. 특정 영역(E/S/G)만의 평가나 기존 보고서 개선도 지원한다. 단, 실제 현장 감사 수행, 제3자 검증 인증서 발급, ESG 평가기관 등급 변경, 탄소 크레딧 거래는 이 스킬의 범위가 아니다."
---

# Sustainability Audit — ESG/지속가능성 감사 풀 파이프라인

ESG의 환경→사회→거버넌스 평가와 통합 보고서→개선 계획을 에이전트 팀이 협업하여 한 번에 생성한다.

## 실행 모드

**에이전트 팀** — 5명이 SendMessage로 직접 통신하며 교차 검증한다.

## 에이전트 구성

| 에이전트 | 파일 | 역할 | 타입 |
|---------|------|------|------|
| environmental-analyst | `agents/environmental-analyst.md` | 탄소배출, 에너지, 폐기물, 수자원 | general-purpose |
| social-assessor | `agents/social-assessor.md` | 노동, 인권, DEI, 공급망 | general-purpose |
| governance-reviewer | `agents/governance-reviewer.md` | 이사회, 윤리, 컴플라이언스 | general-purpose |
| esg-reporter | `agents/esg-reporter.md` | GRI/SASB/TCFD 보고서 작성 | general-purpose |
| improvement-planner | `agents/improvement-planner.md` | 개선 로드맵, KPI, 투자 계획 | general-purpose |

## 워크플로우

### Phase 1: 준비 (오케스트레이터 직접 수행)

1. 사용자 입력에서 추출한다:
    - **기업 정보**: 기업명, 산업, 규모(매출/직원수), 상장 여부
    - **감사 범위** (선택): E/S/G 전체 또는 특정 영역
    - **기존 자료** (선택): 사업보고서, 기존 ESG 보고서, 배출량 데이터
    - **목표** (선택): ESG 등급 목표, 규제 대응, 투자자 요구
    - **제약 조건** (선택): 일정, 예산, 보고 프레임워크 지정
2. `_workspace/` 디렉토리를 프로젝트 루트에 생성한다
3. 입력을 정리하여 `_workspace/00_input.md`에 저장한다
4. 기존 파일이 있으면 `_workspace/`에 복사하고 참조 자료로 활용한다
5. 요청 범위에 따라 **실행 모드를 결정**한다

### Phase 2: 팀 구성 및 실행

| 순서 | 작업 | 담당 | 의존 | 산출물 |
|------|------|------|------|--------|
| 1a | 환경 평가 | environmental | 없음 | `_workspace/01_environmental_assessment.md` |
| 1b | 사회 평가 | social | 없음 | `_workspace/02_social_assessment.md` |
| 1c | 거버넌스 평가 | governance | 없음 | `_workspace/03_governance_assessment.md` |
| 2 | 통합 보고서 | reporter | 작업 1a, 1b, 1c | `_workspace/04_esg_report.md` |
| 3 | 개선 계획 | planner | 작업 1a, 1b, 1c, 2 | `_workspace/05_improvement_plan.md` |
| 4 | 교차 검증 | 오케스트레이터 | 전체 | `_workspace/06_review_report.md` |

작업 1a, 1b, 1c(E/S/G 평가)는 **병렬 실행**한다. 세 영역은 독립적으로 평가 가능하다.

**팀원 간 소통 흐름:**
- E/S/G 분석가 상호: 영역 간 연관 이슈를 교차 공유 (환경→사회 영향, 거버넌스→환경 정책)
- E/S/G 완료 → reporter에게 각 영역 데이터·등급 전달
- E/S/G 완료 → planner에게 취약점·리스크·개선기회 전달
- reporter 완료 → planner에게 보고서 내 목표/약속 전달
- 오케스트레이터가 전체 정합성을 교차 검증

### Phase 3: 통합 및 최종 산출물

1. `_workspace/` 내 모든 파일의 정합성을 확인한다
2. E/S/G 평가↔보고서↔개선계획 간 불일치를 검출한다
3. 교차 검증 보고서를 생성한다
4. 최종 요약을 사용자에게 보고한다

## 작업 규모별 모드

| 사용자 요청 패턴 | 실행 모드 | 투입 에이전트 |
|----------------|----------|-------------|
| "ESG 감사 해줘", "지속가능성 보고서" | **풀 감사** | 5명 전원 |
| "탄소배출량만 산정해줘" | **환경 단독** | environmental 단독 |
| "거버넌스만 점검해줘" | **거버넌스 단독** | governance 단독 |
| "ESG 개선 계획 세워줘" + 기존 보고서 | **개선 모드** | planner 단독 |
| "이 보고서 GRI 형식으로 변환해줘" | **보고서 모드** | reporter 단독 |
| "환경이랑 사회만 봐줘" | **부분 감사** | 해당 영역 + reporter |

**기존 파일 활용**: 사용자가 기존 ESG 보고서, 사업보고서 등을 제공하면 참조 자료로 활용하여 정확도를 높인다.

## 데이터 전달 프로토콜

| 전략 | 방식 | 용도 |
|------|------|------|
| 파일 기반 | `_workspace/` 디렉토리 | 주요 산출물 저장 및 공유 |
| 메시지 기반 | SendMessage | 영역 간 연관 이슈 공유, 수정 요청 |
| 태스크 기반 | TaskCreate/TaskUpdate | 진행 상황 추적, 의존 관계 관리 |

파일명 컨벤션: `{순번}_{산출물}.{확장자}`

## 에러 핸들링

| 에러 유형 | 전략 |
|----------|------|
| 기업 데이터 부재 | 산업 평균치로 추정, "추정치" 라벨 부착 |
| 웹 검색 실패 | 일반적 ESG 기준으로 작업, "데이터 제한" 명시 |
| 산업별 기준 미확인 | SASB 산업 분류 기준으로 웹 검색, 없으면 범용 기준 적용 |
| 에이전트 실패 | 1회 재시도 → 실패 시 해당 영역 누락으로 진행 |
| E/S/G 간 불일치 | 교차 검증에서 발견 → 해당 에이전트에 수정 요청 (최대 2회) |

## 테스트 시나리오

### 정상 흐름
**프롬프트**: "우리 회사(제조업, 직원 500명, 매출 1,000억)의 ESG 감사를 해줘. GRI 기준으로 보고서도 작성해줘"
**기대 결과**:
- 환경: 제조업 특화 Scope 1/2 배출 추정, 폐기물/수질 평가
- 사회: 중대재해처벌법 대응, 산재율, DEI 지표
- 거버넌스: 이사회 구조, 컴플라이언스, 내부통제
- 보고서: GRI Standards 기반 통합 보고서, 중대성 평가
- 개선: 우선순위화된 3개년 로드맵

### 부분 감사 흐름
**프롬프트**: "우리 회사 탄소배출량 산정하고 감축 로드맵 만들어줘"
**기대 결과**:
- environmental + planner 투입
- Scope 1/2/3 배출량 산정
- 감축 목표 설정(SBTi 기반) + 감축 로드맵

### 에러 흐름
**프롬프트**: "ESG 보고서 써줘, 근데 데이터는 없어"
**기대 결과**:
- 산업 평균 데이터로 "추정 기반 ESG 보고서" 작성
- 모든 데이터에 "추정치" 라벨 부착
- 실제 데이터 수집을 위한 데이터 요청 목록 별도 제공

## 에이전트별 확장 스킬

| 확장 스킬 | 경로 | 대상 에이전트 | 역할 |
|----------|------|-------------|------|
| ghg-protocol | `skills/ghg-protocol/SKILL.md` | environmental-analyst | Scope 1/2/3 배출 산출, 배출계수, SBTi 목표 |
| materiality-assessment | `skills/materiality-assessment/SKILL.md` | esg-reporter, improvement-planner | 이중 중대성, 매트릭스, 업종별 이슈, KPI |
