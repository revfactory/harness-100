---
name: security-audit
description: "보안 감사의 취약점 스캔, 코드 보안 분석, 침투 테스트 시나리오 작성, 개선 권고를 에이전트 팀이 협업하여 수행하는 풀 보안 감사 파이프라인. '보안 감사해줘', '취약점 점검', '보안 진단', '코드 보안 분석', '침투 테스트 보고서', '보안 취약점 스캔', 'OWASP 점검', '시큐어 코딩 검토', '보안 개선 방안', '인프라 보안 점검' 등 보안 감사 전반에 이 스킬을 사용한다. 코드 분석만 필요하거나 개선 권고만 필요한 경우에도 지원한다. 단, 실제 네트워크 침투 실행, 악성코드 분석, SOC 운영, 실시간 보안 모니터링은 이 스킬의 범위가 아니다."
---

# Security Audit — 보안 감사 풀 파이프라인

보안 감사의 취약점스캔→코드분석→침투테스트보고→개선권고를 에이전트 팀이 협업하여 한 번에 수행한다.

## 실행 모드

**에이전트 팀** — 5명이 SendMessage로 직접 통신하며 교차 검증한다.

## 에이전트 구성

| 에이전트 | 파일 | 역할 | 타입 |
|---------|------|------|------|
| vulnerability-scanner | `agents/vulnerability-scanner.md` | CVE, 의존성, 설정오류 스캔 | general-purpose |
| code-analyst | `agents/code-analyst.md` | SAST, 시큐어코딩, 패턴탐지 | general-purpose |
| pentest-reporter | `agents/pentest-reporter.md` | 공격시나리오, PoC, 영향분석 | general-purpose |
| security-consultant | `agents/security-consultant.md` | 개선권고, 로드맵, 프레임워크매핑 | general-purpose |
| audit-reviewer | `agents/audit-reviewer.md` | 교차검증, 위험등급조정, 최종보고서 | general-purpose |

## 워크플로우

### Phase 1: 준비 (오케스트레이터 직접 수행)

1. 사용자 입력에서 추출한다:
    - **감사 대상**: 코드 저장소, 인프라, 애플리케이션 URL
    - **감사 범위**: 전체/부분, 포함/제외 항목
    - **기술 스택**: 언어, 프레임워크, 클라우드, DB
    - **규제 요구사항** (선택): GDPR, 개인정보보호법, 전자금융감독규정
    - **기존 보고서** (선택): 이전 감사 보고서, 취약점 목록
2. `_workspace/` 디렉토리를 프로젝트 루트에 생성한다
3. 입력을 정리하여 `_workspace/00_input.md`에 저장한다
4. 감사 대상 코드가 있으면 분석 범위를 확정한다
5. 기존 파일이 있으면 `_workspace/`에 복사하고 해당 Phase를 건너뛴다
6. 요청 범위에 따라 **실행 모드를 결정**한다

### Phase 2: 팀 구성 및 실행

팀을 구성하고 작업을 할당한다. 작업 간 의존 관계는 다음과 같다:

| 순서 | 작업 | 담당 | 의존 | 산출물 |
|------|------|------|------|--------|
| 1a | 취약점 스캔 | scanner | 없음 | `_workspace/01_vulnerability_scan.md` |
| 1b | 코드 보안 분석 | analyst | 없음 | `_workspace/02_code_analysis.md` |
| 2 | 침투 테스트 보고 | pentest | 작업 1a, 1b | `_workspace/03_pentest_report.md` |
| 3 | 개선 권고 | consultant | 작업 1a, 1b, 2 | `_workspace/04_remediation_plan.md` |
| 4 | 감사 리뷰 | reviewer | 작업 1a, 1b, 2, 3 | `_workspace/05_audit_report.md` |

작업 1a(스캔)와 1b(코드분석)는 **병렬 실행**한다. 둘 다 초기 의존이 없으므로 동시에 시작할 수 있다.

**팀원 간 소통 흐름:**
- scanner 완료 → analyst에게 CWE 매핑 전달, pentest에게 공격 가능한 취약점 전달
- analyst 완료 → pentest에게 데이터 흐름·공격 벡터 전달
- pentest 완료 → consultant에게 비즈니스 영향·긴급도 전달
- consultant 완료 → reviewer에게 전체 개선 계획 전달
- reviewer는 모든 산출물을 교차 검증. 🔴 필수 수정 발견 시 해당 에이전트에게 수정 요청 → 재작업 → 재검증 (최대 2회)

### Phase 3: 통합 및 최종 산출물

리뷰어의 보고서를 기반으로 최종 산출물을 정리한다:

1. `_workspace/` 내 모든 파일을 확인한다
2. 리뷰 보고서의 🔴 필수 수정이 모두 반영되었는지 확인한다
3. 최종 요약을 사용자에게 보고한다:
    - 취약점 스캔 — `01_vulnerability_scan.md`
    - 코드 분석 — `02_code_analysis.md`
    - 침투 테스트 — `03_pentest_report.md`
    - 개선 권고 — `04_remediation_plan.md`
    - 최종 감사 보고서 — `05_audit_report.md`

## 작업 규모별 모드

| 사용자 요청 패턴 | 실행 모드 | 투입 에이전트 |
|----------------|----------|-------------|
| "보안 감사 전체 수행해줘" | **풀 감사** | 5명 전원 |
| "이 코드 보안 분석해줘" | **코드 분석 모드** | analyst + reviewer |
| "취약점 스캔해줘" | **스캔 모드** | scanner + reviewer |
| "보안 개선 방안 만들어줘" (기존 보고서) | **컨설팅 모드** | consultant + reviewer |
| "이 보안 보고서 검토해줘" | **리뷰 모드** | reviewer 단독 |

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
| 코드 미제공 | 사용자에게 코드 경로 요청, 일반 보안 체크리스트 선제공 |
| CVE DB 접근 불가 | 로컬 지식 기반 분석, "오프라인 스캔" 표기 |
| 기술 스택 불명 | 코드 확장자/import 문에서 자동 감지 시도 |
| 에이전트 실패 | 1회 재시도 → 실패 시 해당 산출물 없이 진행, 리뷰 보고서에 누락 명시 |
| 리뷰에서 🔴 발견 | 해당 에이전트에 수정 요청 → 재작업 → 재검증 (최대 2회) |

## 테스트 시나리오

### 정상 흐름
**프롬프트**: "이 Node.js Express 웹앱 코드베이스에 대해 전체 보안 감사를 수행해줘"
**기대 결과**:
- 스캔: npm 의존성 CVE 목록, 시크릿 탐지, 설정 점검
- 코드분석: OWASP Top 10 기준 취약점(XSS, SQL Injection, CSRF 등), 수정 코드 포함
- 침투테스트: 3~5개 공격 시나리오, MITRE ATT&CK 매핑, PoC 절차
- 개선권고: NIST CSF 갭 분석, 단기·중기·장기 로드맵
- 리뷰: 정합성 매트릭스 전항목 확인

### 기존 파일 활용 흐름
**프롬프트**: "이전 감사 보고서를 기반으로 개선 진행 상황 점검하고 추가 권고해줘" + 이전 보고서 첨부
**기대 결과**:
- 이전 보고서를 `_workspace/`에 복사
- 컨설팅 모드: consultant + reviewer 투입
- 이전 취약점 해결 여부 추적 + 신규 권고

### 에러 흐름
**프롬프트**: "보안 점검해줘, 코드는 나중에 줄게"
**기대 결과**:
- 코드 부재 시 일반적 보안 감사 체크리스트와 프레임워크 매핑 선제공
- "코드 제공 후 상세 분석 가능" 명시
- 인프라/설정 수준 점검 항목 안내


## 에이전트별 확장 스킬

| 스킬 | 경로 | 강화 대상 에이전트 | 역할 |
|------|------|-----------------|------|
| owasp-testing-guide | `skills/owasp-testing-guide/SKILL.md` | code-analyst, pentest-reporter | OWASP Top 10 취약점별 테스트 방법, 수정 가이드 |
| cve-analysis | `skills/cve-analysis/SKILL.md` | vulnerability-scanner | CVSS 점수 해석, 의존성 스캔 도구, 시크릿 탐지 |
| threat-modeling | `skills/threat-modeling/SKILL.md` | security-consultant, pentest-reporter | STRIDE, DREAD, Attack Tree, 공격 표면 분석 |
