---
name: chatbot-builder
description: "챗봇 시스템을 에이전트 팀이 협업하여 구축하는 풀 파이프라인. '챗봇 만들어줘', '대화형 봇 개발', '고객 응대 봇', 'FAQ 챗봇', '카카오톡 챗봇', 'Slack 봇', '자동 응답 시스템', '대화 AI', '챗봇 설계' 등 챗봇 구축 전반에 이 스킬을 사용한다. 대화 설계만 필요한 경우에도 설계 모드로 지원한다. 단, 음성 비서(Alexa/Google Home), 실시간 음성 통화 봇, 영상 챗봇은 이 스킬의 범위가 아니다."
---

# Chatbot Builder — 챗봇 구축 파이프라인

챗봇의 페르소나→대화설계→NLU→통합→테스트를 에이전트 팀이 협업하여 구축한다.

## 실행 모드

**에이전트 팀** — 5명이 SendMessage로 직접 통신하며 교차 검증한다.

## 에이전트 구성

| 에이전트 | 파일 | 역할 | 타입 |
|---------|------|------|------|
| persona-architect | `agents/persona-architect.md` | 봇 페르소나 설계 | general-purpose |
| conversation-designer | `agents/conversation-designer.md` | 대화 시나리오 설계 | general-purpose |
| nlu-developer | `agents/nlu-developer.md` | NLU 파이프라인 구현 | general-purpose |
| integration-engineer | `agents/integration-engineer.md` | 채널 연동, 배포 | general-purpose |
| dialog-tester | `agents/dialog-tester.md` | 품질 검증, 테스트 | general-purpose |

## 워크플로우

### Phase 1: 준비 (오케스트레이터 직접 수행)

1. 사용자 입력에서 추출한다:
    - **챗봇 목적**: 고객 응대/FAQ/예약/주문/상담 등
    - **타깃 사용자**: 연령, 디지털 리터러시, 기대 수준
    - **연동 채널**: Slack/카카오톡/텔레그램/웹/다중 채널
    - **도메인 지식**: 비즈니스 규칙, FAQ 목록, 상품 정보 등
    - **제약 조건** (선택): 기술 스택, 응답 시간 요구사항
2. `_workspace/` 디렉토리를 프로젝트 루트에 생성한다
3. 입력을 정리하여 `_workspace/00_input.md`에 저장한다
4. `_workspace/src/` 디렉토리를 생성한다
5. 기존 파일이 있으면 `_workspace/`에 복사하고 해당 Phase를 건너뛴다
6. 요청 범위에 따라 **실행 모드를 결정**한다 (아래 "작업 규모별 모드" 참조)

### Phase 2: 팀 구성 및 실행

| 순서 | 작업 | 담당 | 의존 | 산출물 |
|------|------|------|------|--------|
| 1 | 페르소나 설계 | persona | 없음 | `_workspace/01_persona_spec.md` |
| 2 | 대화 설계 | designer | 작업 1 | `_workspace/02_conversation_design.md` |
| 3a | NLU 구현 | nlu-dev | 작업 2 | `_workspace/03_nlu_config.md` + `src/` |
| 3b | 통합 설계 | integrator | 작업 2 | `_workspace/04_integration_spec.md` + `src/` |
| 4 | 테스트 | tester | 작업 3a, 3b | `_workspace/05_test_report.md` |

작업 3a(NLU)와 3b(통합)는 **병렬 실행**한다.

**팀원 간 소통 흐름:**
- persona 완료 → designer에게 톤앤매너 가이드 전달, nlu-dev에게 도메인 키워드 전달
- designer 완료 → nlu-dev에게 의도/엔티티 카탈로그 전달, integrator에게 외부 연동 플로우 전달
- nlu-dev 완료 → integrator에게 NLU 인터페이스 전달, tester에게 테스트 데이터 전달
- integrator 완료 → tester에게 테스트 환경 정보 전달
- tester는 모든 산출물을 교차 검증. CRITICAL 발견 시 해당 에이전트에게 수정 요청 → 재작업 → 재검증 (최대 2회)

### Phase 3: 통합 및 최종 산출물

테스터의 보고서를 기반으로 최종 산출물을 정리한다:

1. `_workspace/` 내 모든 파일과 `src/` 코드를 확인한다
2. CRITICAL 발견 사항이 모두 해결되었는지 확인한다
3. 최종 요약을 사용자에게 보고한다

## 작업 규모별 모드

| 사용자 요청 패턴 | 실행 모드 | 투입 에이전트 |
|----------------|----------|-------------|
| "챗봇 만들어줘", "풀 구축" | **풀 파이프라인** | 5명 전원 |
| "대화 설계만 해줘", "시나리오 작성" | **설계 모드** | persona + designer |
| "NLU만 개발해줘" (설계 완료) | **NLU 모드** | nlu-dev + tester |
| "카카오톡에 챗봇 연동해줘" (구현 완료) | **통합 모드** | integrator + tester |
| "챗봇 테스트해줘" (구현 완료) | **테스트 모드** | tester 단독 |

**기존 파일 활용**: 사용자가 기존 대화 설계서나 NLU 설정을 제공하면, 해당 파일을 `_workspace/`에 복사하고 해당 단계를 건너뛴다.

## 데이터 전달 프로토콜

| 전략 | 방식 | 용도 |
|------|------|------|
| 파일 기반 | `_workspace/` 디렉토리 | 설계 문서 및 설정 공유 |
| 메시지 기반 | SendMessage | 실시간 핵심 정보 전달, 수정 요청 |
| 코드 기반 | `_workspace/src/` | 실행 가능한 소스코드 |

## 에러 핸들링

| 에러 유형 | 전략 |
|----------|------|
| 도메인 지식 부족 | FAQ 목록/사업 정보를 사용자에게 추가 요청, 웹 검색으로 보완 |
| 채널 API 변경 | 최신 API 문서를 WebFetch로 확인 후 연동 코드 업데이트 |
| NLU 정확도 미달 | 학습 데이터 증강 → 프롬프트 재설계 → 폴백 강화 순으로 대응 |
| 에이전트 실패 | 1회 재시도 → 실패 시 해당 산출물 없이 진행, 보고서에 명시 |

## 테스트 시나리오

### 정상 흐름
**프롬프트**: "카페 주문 접수용 카카오톡 챗봇을 만들어줘. 메뉴 조회, 주문, 결제 안내가 가능해야 해"
**기대 결과**:
- 페르소나: 밝고 친근한 카페 직원 캐릭터, 높임말, 이모지 적극 사용
- 대화 설계: 메뉴조회/주문/결제안내/운영시간 의도, 슬롯(메뉴명/수량/옵션)
- NLU: LLM 프롬프트 기반 의도분류, 메뉴명 엔티티 사전 구축
- 통합: 카카오톡 챗봇 API 연동, 카드형 메시지로 메뉴 표시
- 테스트: 주문 플로우 해피패스, 메뉴 없는 경우 폴백, 멀티턴 주문

### 기존 파일 활용 흐름
**프롬프트**: "이 대화 설계서가 있는데 NLU 구현하고 카카오톡에 연동해줘" + 설계서 첨부
**기대 결과**:
- 기존 설계서를 `_workspace/02_conversation_design.md`로 복사
- persona와 designer는 건너뛰고 nlu-dev + integrator + tester 투입
- 기존 의도/엔티티 카탈로그 기반 NLU 구현

### 에러 흐름
**프롬프트**: "챗봇 만들어줘" (목적, 채널 불명확)
**기대 결과**:
- persona가 범용 페르소나 제안 후 사용자에게 목적 확인 요청
- 목적 확인 후 나머지 파이프라인 진행
- 보고서에 "채널 미정 — 웹 위젯 기본 적용" 명시

## 에이전트별 확장 스킬

에이전트의 도메인 전문성을 강화하는 확장 스킬:

| 스킬 | 파일 | 대상 에이전트 | 역할 |
|------|------|-------------|------|
| intent-taxonomy-builder | `skills/intent-taxonomy-builder/SKILL.md` | nlu-developer, conversation-designer | 의도 분류 체계 설계, 엔티티-슬롯 매핑, 학습 데이터 생성, 혼동 매트릭스 |
| conversation-flow-validator | `skills/conversation-flow-validator/SKILL.md` | dialog-tester, conversation-designer | 대화 흐름 결함 탐지, Happy/Sad/Edge 테스트, 폴백 계층, 품질 메트릭 |
