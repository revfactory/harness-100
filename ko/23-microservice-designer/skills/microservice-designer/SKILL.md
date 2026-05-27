---
name: microservice-designer
description: "마이크로서비스 아키텍처를 설계·분해·통신·모니터링하는 풀 파이프라인. 도메인 분석, 서비스 설계, 통신 패턴, 관측성을 에이전트 팀이 협업하여 수행한다. '마이크로서비스 아키텍처 설계해줘', '서비스 분해해줘', 'MSA 설계', '도메인 분석해줘', '이벤트 기반 아키텍처', '서비스 간 통신 설계', '분산 시스템 설계', 'API 게이트웨이 설계' 등 마이크로서비스 설계 전반에 이 스킬을 사용한다. 기존 모놀리스에서 MSA로 전환하는 경우에도 지원한다. 단, 실제 인프라 구축, Kubernetes 배포, 코드 구현은 이 스킬의 범위가 아니다."
---

# Microservice Designer — 마이크로서비스 아키텍처 설계 파이프라인

도메인 분석→서비스 설계→통신 설계→관측성 설계를 에이전트 팀이 협업하여 수행한다.

## 실행 모드

**에이전트 팀** — 5명이 SendMessage로 직접 통신하며 교차 검증한다.

## 에이전트 구성

| 에이전트 | 파일 | 역할 | 타입 |
|---------|------|------|------|
| domain-analyst | `agents/domain-analyst.md` | 바운디드 컨텍스트, 이벤트 스토밍 | general-purpose |
| service-architect | `agents/service-architect.md` | API 계약, 데이터 소유권, 배포 단위 | general-purpose |
| communication-designer | `agents/communication-designer.md` | 동기/비동기, 이벤트 버스, Saga | general-purpose |
| observability-engineer | `agents/observability-engineer.md` | 메트릭, 로깅, 트레이싱, 알림 | general-purpose |
| architecture-reviewer | `agents/architecture-reviewer.md` | 교차 검증, 안티패턴 검출 | general-purpose |

## 워크플로우

### Phase 1: 준비 (오케스트레이터 직접 수행)

1. 사용자 입력에서 추출한다:
    - **비즈니스 도메인**: 어떤 시스템/서비스를 설계하는가
    - **현재 상태** (선택): 모놀리스 전환인지, 신규 설계인지
    - **규모/제약** (선택): 예상 트래픽, 팀 규모, 기술 스택 제한
    - **기존 문서** (선택): ERD, 아키텍처 문서, API 문서 등
2. `_workspace/` 디렉토리를 프로젝트 루트에 생성한다
3. 입력을 정리하여 `_workspace/00_input.md`에 저장한다
4. 기존 파일이 있으면 해당 Phase를 건너뛴다

### Phase 2: 팀 구성 및 실행

| 순서 | 작업 | 담당 | 의존 | 산출물 |
|------|------|------|------|--------|
| 1 | 도메인 분석 | analyst | 없음 | `_workspace/01_domain_analysis.md` |
| 2 | 서비스 설계 | architect | 작업 1 | `_workspace/02_service_design.md` |
| 3a | 통신 설계 | comm-designer | 작업 1, 2 | `_workspace/03_communication_design.md` |
| 3b | 관측성 설계 | obs-engineer | 작업 2 | `_workspace/04_observability_design.md` |
| 4 | 아키텍처 리뷰 | reviewer | 작업 1~3b | `_workspace/05_review_report.md` |

작업 3a(통신)와 3b(관측성)는 **병렬 실행** 가능하다.

**팀원 간 소통 흐름:**
- analyst 완료 → architect에게 바운디드 컨텍스트·애그리거트 전달, comm-designer에게 도메인 이벤트 전달
- architect 완료 → comm-designer에게 서비스 카탈로그·API 계약 전달, obs-engineer에게 서비스 목록·의존성 전달
- comm-designer 완료 → obs-engineer에게 통신 매트릭스·Saga 흐름 전달
- reviewer는 모든 산출물을 교차 검증. 🔴 필수 수정 발견 시 해당 에이전트에게 수정 요청 → 재작업 → 재검증 (최대 2회)

### Phase 3: 통합 및 최종 산출물

1. `_workspace/` 내 모든 파일을 확인한다
2. 리뷰 보고서의 🔴 필수 수정이 모두 반영되었는지 확인한다
3. 최종 요약을 사용자에게 보고한다

## 작업 규모별 모드

| 사용자 요청 패턴 | 실행 모드 | 투입 에이전트 |
|----------------|----------|-------------|
| "마이크로서비스 아키텍처 설계해줘" | **풀 파이프라인** | 5명 전원 |
| "도메인 분석해줘", "이벤트 스토밍" | **도메인 모드** | analyst + reviewer |
| "서비스 분해해줘" (도메인 분석 있음) | **서비스 모드** | architect + reviewer |
| "서비스 간 통신 설계해줘" | **통신 모드** | comm-designer + reviewer |
| "모니터링/관측성 설계해줘" | **관측성 모드** | obs-engineer + reviewer |

## 데이터 전달 프로토콜

| 전략 | 방식 | 용도 |
|------|------|------|
| 파일 기반 | `_workspace/` 디렉토리 | 주요 산출물 저장 및 공유 |
| 메시지 기반 | SendMessage | 실시간 핵심 정보 전달, 수정 요청 |
| 태스크 기반 | TaskCreate/TaskUpdate | 진행 상황 추적, 의존 관계 관리 |

## 에러 핸들링

| 에러 유형 | 전략 |
|----------|------|
| 도메인 정보 부족 | 유사 도메인 참조 패턴으로 초안 작성, 사용자 검증 요청 |
| 서비스 수 과다 | 모듈형 모놀리스 → 점진적 분리 로드맵 제안 |
| 에이전트 실패 | 1회 재시도 → 실패 시 해당 산출물 없이 진행, 리뷰에 누락 명시 |
| 리뷰에서 🔴 발견 | 해당 에이전트에 수정 요청 → 재작업 → 재검증 (최대 2회) |
| 분산 모놀리스 징후 | architect에게 서비스 경계 재조정 요청 |

## 테스트 시나리오

### 정상 흐름
**프롬프트**: "이커머스 플랫폼을 마이크로서비스 아키텍처로 설계해줘. 주문, 결제, 배송, 재고, 사용자 관리가 핵심 기능이야"
**기대 결과**:
- 도메인: 5개 바운디드 컨텍스트, 컨텍스트 맵, 이벤트 스토밍 결과
- 서비스: 5~7개 서비스 카탈로그, API 계약, 데이터 소유권 매핑
- 통신: 주문-결제-배송 Saga, 이벤트 버스 토픽 설계, 서킷 브레이커 설정
- 관측성: SLI/SLO 정의, 분산 트레이싱 설계, 알림 체계
- 리뷰: 전 항목 정합성 검증, 분산 시스템 안티패턴 검사

### 기존 파일 활용 흐름
**프롬프트**: "현재 Django 모놀리스를 MSA로 전환하고 싶어. ERD와 API 문서가 있어" + 파일 첨부
**기대 결과**:
- 기존 ERD에서 바운디드 컨텍스트를 역추출
- Strangler Fig 패턴 기반 점진적 전환 로드맵 포함
- 기존 API 하위 호환성 유지 전략 포함

### 에러 흐름
**프롬프트**: "마이크로서비스로 채팅 앱 만들어줘"
**기대 결과**:
- "설계"와 "구현"을 구분하여 설계만 수행
- 실시간 통신(WebSocket/SSE) 특화 통신 설계 포함
- 구현은 이 스킬 범위 밖임을 안내


## 에이전트별 확장 스킬

| 스킬 | 경로 | 강화 대상 에이전트 | 역할 |
|------|------|-----------------|------|
| ddd-context-mapping | `skills/ddd-context-mapping/SKILL.md` | domain-analyst, service-architect | 바운디드 컨텍스트 식별, 이벤트 스토밍, 컨텍스트 맵 관계 유형, 애그리거트 설계 |
| distributed-patterns | `skills/distributed-patterns/SKILL.md` | communication-designer, service-architect | 분산 트랜잭션(Saga), CQRS, Circuit Breaker, Event Sourcing 구현 패턴 |
