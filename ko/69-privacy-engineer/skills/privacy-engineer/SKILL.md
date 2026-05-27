---
name: privacy-engineer
description: "개인정보보호 엔지니어링 풀 파이프라인. GDPR/PIPA 분석→PIA→동의서→프로세스설계를 에이전트 팀이 협업하여 한 번에 수행한다. '개인정보보호 설계', 'GDPR 대응', '개인정보 영향평가', 'PIA 수행', '동의서 작성', '개인정보 처리방침', '프라이버시 설계', '개인정보보호법 준수', 'PIPA 대응', '데이터 보호 체계' 등 개인정보보호 전반에 이 스킬을 사용한다. 단, 실제 개인정보보호위원회 신고/접수, 법적 소송 대리, ISMS-P 인증 심사, 실제 시스템 보안 구축은 이 스킬의 범위가 아니다."
---

# Privacy Engineer — 개인정보보호 엔지니어링 파이프라인

서비스의 개인정보보호 체계를 법률 분석부터 프로세스 설계까지 체계적으로 구축한다.

## 실행 모드

**에이전트 팀** — 4명이 SendMessage로 직접 통신하며 교차 검증한다.

## 에이전트 구성

| 에이전트 | 파일 | 역할 | 타입 |
|---------|------|------|------|
| privacy-law-analyst | `agents/privacy-law-analyst.md` | GDPR/PIPA 분석, 적용 범위 판단 | general-purpose |
| pia-assessor | `agents/pia-assessor.md` | 개인정보 영향평가, 위험도 산정 | general-purpose |
| consent-designer | `agents/consent-designer.md` | 동의서 설계, 고지사항, 처리방침 | general-purpose |
| process-architect | `agents/process-architect.md` | 처리 프로세스, 기술적 보호조치 | general-purpose |

## 워크플로우

### Phase 1: 준비 (오케스트레이터 직접 수행)

1. 사용자 입력에서 추출한다:
    - **서비스명/유형**: 웹, 앱, SaaS, 이커머스 등
    - **처리 데이터**: 수집하는 개인정보 항목
    - **이용자 지역**: 국내, EU, 미국 등
    - **서비스 규모**: 이용자 수, 데이터 규모
    - **기존 자료** (선택): 현행 처리방침, 동의서, 시스템 구성도
2. `_workspace/` 디렉토리를 프로젝트 루트에 생성한다
3. 입력을 정리하여 `_workspace/00_input.md`에 저장한다
4. 요청 범위에 따라 **실행 모드를 결정**한다

### Phase 2: 팀 구성 및 실행

| 순서 | 작업 | 담당 | 의존 | 산출물 |
|------|------|------|------|--------|
| 1 | 법률 분석 | privacy-law-analyst | 없음 | `_workspace/01_privacy_law_analysis.md` |
| 2 | PIA 수행 | pia-assessor | 작업 1 | `_workspace/02_pia_report.md` |
| 3a | 동의서 작성 | consent-designer | 작업 1, 2 | `_workspace/03_consent_documents.md` |
| 3b | 프로세스 설계 | process-architect | 작업 1, 2 | `_workspace/04_process_design.md` |

작업 3a(동의서)와 3b(프로세스)는 **병렬 실행**한다. 둘 다 법률 분석과 PIA에 의존하므로 작업 2 완료 후 동시 시작 가능하다.

**팀원 간 소통 흐름:**
- privacy-law-analyst 완료 → pia-assessor에게 처리 활동 목록·위험 요소 전달
- pia-assessor 완료 → consent-designer에게 고지 요건 전달, process-architect에게 보호 조치 권고 전달
- consent-designer → process-architect에게 동의 수집 시점·관리 요구사항 전달
- process-architect는 최종 설계 시 전체 산출물의 논리적 일관성을 교차 검증한다

### Phase 3: 통합 및 최종 산출물

1. `_workspace/` 내 모든 파일을 확인한다
2. 법률 분석→PIA→동의서→프로세스 간 일관성을 확인한다
3. 최종 요약을 사용자에게 보고한다:
    - 법률 분석 보고서 — `01_privacy_law_analysis.md`
    - PIA 보고서 — `02_pia_report.md`
    - 동의서·고지사항 세트 — `03_consent_documents.md`
    - 프로세스 설계서 — `04_process_design.md`

## 작업 규모별 모드

| 사용자 요청 패턴 | 실행 모드 | 투입 에이전트 |
|----------------|----------|-------------|
| "개인정보보호 체계 전체 설계", "프라이버시 풀 설계" | **풀 파이프라인** | 4명 전원 |
| "GDPR 적용 여부 분석해줘" | **법률 분석 모드** | privacy-law-analyst 단독 |
| "PIA만 수행해줘" (법률 분석 있음) | **PIA 모드** | pia-assessor |
| "동의서만 작성해줘" | **동의서 모드** | consent-designer |
| "개인정보 처리 프로세스만 설계해줘" | **프로세스 모드** | process-architect |

## 데이터 전달 프로토콜

| 전략 | 방식 | 용도 |
|------|------|------|
| 파일 기반 | `_workspace/` 디렉토리 | 주요 산출물 저장 및 공유 |
| 메시지 기반 | SendMessage | 실시간 핵심 정보 전달, 수정 요청 |

파일명 컨벤션: `{순번}_{에이전트}_{산출물}.{확장자}`

## 에러 핸들링

| 에러 유형 | 전략 |
|----------|------|
| 웹 검색 실패 | 법률 분석가가 일반 지식 기반으로 작업, "최신 가이드라인 미확인" 명시 |
| 서비스 정보 부족 | 일반적 웹 서비스 기준으로 가정, "가정 기반" 명시 |
| GDPR 적용 판단 불확실 | 적용 가정으로 작업, 별도 확인 권고 |
| 에이전트 실패 | 1회 재시도 → 실패 시 해당 산출물 없이 진행, 최종 보고서에 누락 명시 |
| PIA와 법률 분석 간 불일치 | process-architect가 불일치 식별, 보수적 판단 적용 |

## 테스트 시나리오

### 정상 흐름
**프롬프트**: "EU 사용자도 포함된 SaaS 서비스의 개인정보보호 체계를 설계해줘. 회원가입, 결제, 마케팅 데이터를 처리해."
**기대 결과**:
- 법률 분석: GDPR + PIPA 동시 적용, 처리 활동 10건 이상 매핑
- PIA: 위험 평가 15건 이상, 보호 조치 권고
- 동의서: 필수/선택 분리, GDPR 유효 동의 요건 반영, 국외 이전 동의
- 프로세스: 전체 라이프사이클, 기술적 보호조치, 사고 대응 체계

### 부분 흐름
**프롬프트**: "우리 앱에 넣을 개인정보 수집 동의서만 작성해줘"
**기대 결과**:
- 동의서 모드로 전환 (consent-designer 단독)
- 표준 동의서 템플릿 기반으로 작성, 세부 항목 확인 필요 명시

### 에러 흐름
**프롬프트**: "개인정보보호 체계 설계해줘, 스타트업인데 뭘 해야 할지 모르겠어"
**기대 결과**:
- 풀 파이프라인 실행, 서비스 정보 부족으로 추가 질문
- 일반적 스타트업 기준으로 가정 작업, "서비스 상세 확인 후 보완 필요" 명시
- 최소한의 법적 의무(처리방침 공개, 동의 확보)부터 우선 조치 제시

## 에이전트별 확장 스킬

| 에이전트 | 확장 스킬 | 용도 |
|---------|----------|------|
| pia-assessor, process-architect | `data-flow-mapper` | 데이터 플로우 매핑, 위험 지점 식별 |
| privacy-law-analyst, consent-designer | `gdpr-pipa-cross-reference` | GDPR·PIPA 조문 매핑, 통합 준수 가이드 |
