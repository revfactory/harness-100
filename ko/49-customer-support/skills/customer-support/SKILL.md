---
name: customer-support
description: "고객지원 시스템을 FAQ, 응대 매뉴얼, 에스컬레이션 정책, CS 분석 프레임워크로 체계화하는 풀 파이프라인. '고객지원 시스템 만들어줘', 'FAQ 작성해줘', '응대 매뉴얼', 'CS 매뉴얼', '에스컬레이션 정책', '고객응대 스크립트', '컴플레인 대응', '고객 불만 처리', 'CS 운영 체계', '고객서비스 프로세스' 등 고객지원 체계 구축 전반에 이 스킬을 사용한다. 기존 FAQ나 매뉴얼이 있는 경우에도 보완·개선을 지원한다. 단, CRM/헬프데스크 소프트웨어 개발, 콜센터 인프라 구축, 실시간 챗봇 개발, 상담원 채용은 이 스킬의 범위가 아니다."
---

# Customer Support — 고객지원 시스템 구축 파이프라인

고객지원의 FAQ→응대매뉴얼→에스컬레이션→분석을 에이전트 팀이 협업하여 한 번에 생성한다.

## 실행 모드

**에이전트 팀** — 5명이 SendMessage로 직접 통신하며 교차 검증한다.

## 에이전트 구성

| 에이전트 | 파일 | 역할 | 타입 |
|---------|------|------|------|
| faq-builder | `agents/faq-builder.md` | FAQ 구축, 검색 최적화 | general-purpose |
| response-specialist | `agents/response-specialist.md` | 응대 스크립트, 톤앤매너 | general-purpose |
| escalation-manager | `agents/escalation-manager.md` | 에스컬레이션 단계, SLA | general-purpose |
| cs-analyst | `agents/cs-analyst.md` | 메트릭, VOC, 개선 제안 | general-purpose |
| cs-reviewer | `agents/cs-reviewer.md` | 교차 검증, 고객여정 시뮬레이션 | general-purpose |

## 워크플로우

### Phase 1: 준비 (오케스트레이터 직접 수행)

1. 사용자 입력에서 추출한다:
    - **서비스 정보**: 제품/서비스명, 유형, 고객 규모
    - **지원 채널**: 전화/채팅/이메일/SNS 중 운영 채널
    - **현재 상태**: 기존 CS 체계 유무, 팀 규모
    - **기존 자료** (선택): 기존 FAQ, 매뉴얼, 데이터
2. `_workspace/` 디렉토리를 프로젝트 루트에 생성한다
3. 입력을 정리하여 `_workspace/00_input.md`에 저장한다
4. 기존 파일이 있으면 `_workspace/`에 복사하고 해당 Phase를 건너뛴다

### Phase 2: 팀 구성 및 실행

| 순서 | 작업 | 담당 | 의존 | 산출물 |
|------|------|------|------|--------|
| 1a | FAQ 구축 | faq-builder | 없음 | `_workspace/01_faq.md` |
| 1b | 응대 매뉴얼 | response-specialist | 없음 | `_workspace/02_response_manual.md` |
| 2 | 에스컬레이션 정책 | escalation-manager | 작업 1a, 1b | `_workspace/03_escalation_policy.md` |
| 3 | CS 분석 프레임워크 | cs-analyst | 작업 1a, 1b, 2 | `_workspace/04_cs_analytics.md` |
| 4 | CS 리뷰 | cs-reviewer | 작업 1a,1b,2,3 | `_workspace/05_review_report.md` |

작업 1a(FAQ)와 1b(매뉴얼)는 **병렬 실행**한다. 둘 다 초기 의존 관계가 없으므로 동시에 시작할 수 있다.

**팀원 간 소통 흐름:**
- faq-builder 완료 → response-specialist에게 FAQ 범위 밖 시나리오 전달, escalation-manager에게 셀프서비스 한계선 전달
- response-specialist 완료 → escalation-manager에게 에스컬레이션 트리거 조건 전달
- escalation-manager 완료 → cs-analyst에게 SLA 메트릭 전달
- cs-analyst 완료 → cs-reviewer에게 모든 문서 전달
- cs-reviewer는 모든 산출물을 교차 검증. 🔴 필수 수정 발견 시 해당 에이전트에게 수정 요청 → 재작업 → 재검증 (최대 2회)

### Phase 3: 통합 및 최종 산출물

1. `_workspace/` 내 모든 파일을 확인한다
2. 리뷰 보고서의 🔴 필수 수정이 모두 반영되었는지 확인한다
3. 최종 요약을 사용자에게 보고한다

## 작업 규모별 모드

| 사용자 요청 패턴 | 실행 모드 | 투입 에이전트 |
|----------------|----------|-------------|
| "고객지원 시스템 만들어줘", "CS 풀세트" | **풀 파이프라인** | 5명 전원 |
| "FAQ만 만들어줘" | **FAQ 모드** | faq-builder + reviewer |
| "응대 매뉴얼 작성해줘" | **매뉴얼 모드** | response-specialist + reviewer |
| "에스컬레이션 정책 만들어줘" | **에스컬레이션 모드** | escalation-manager + reviewer |
| "CS 메트릭 설계해줘" | **분석 모드** | cs-analyst + reviewer |
| "이 FAQ 검토해줘" | **리뷰 모드** | reviewer 단독 |

## 데이터 전달 프로토콜

| 전략 | 방식 | 용도 |
|------|------|------|
| 파일 기반 | `_workspace/` 디렉토리 | 주요 산출물 저장 및 공유 |
| 메시지 기반 | SendMessage | 실시간 핵심 정보 전달, 수정 요청 |

## 에러 핸들링

| 에러 유형 | 전략 |
|----------|------|
| 서비스 정보 부족 | 산업 유형 기반 일반 CS 체계 구축, "서비스 맞춤화 필요" 태그 명시 |
| 기존 CS 데이터 없음 | 산업 벤치마크 기반 목표 설정, 초기 측정 방법 제안 |
| 웹 검색 실패 | 일반 CS 베스트 프랙티스 기반 작업, "데이터 제한" 명시 |
| 에이전트 실패 | 1회 재시도 → 실패 시 해당 산출물 없이 진행, 리뷰 보고서에 누락 명시 |
| 리뷰에서 🔴 발견 | 해당 에이전트에 수정 요청 → 재작업 → 재검증 (최대 2회) |

## 테스트 시나리오

### 정상 흐름
**프롬프트**: "B2C SaaS 프로젝트 관리 도구의 고객지원 시스템을 구축해줘. 월 활성 사용자 1만 명이고, 채팅과 이메일 채널을 운영해. CS 팀은 5명이야"
**기대 결과**:
- FAQ: 가입/결제/기능/연동 카테고리, 30개 이상 Q&A
- 매뉴얼: 5개 이상 시나리오 스크립트, 채팅+이메일 채널별 가이드
- 에스컬레이션: L1~L3 단계, SLA 매트릭스, 위기 대응 프로토콜
- 분석: CSAT/NPS/FCR/AHT 메트릭 + 주간/월간 보고 템플릿
- 리뷰: 3개 고객 여정 시뮬레이션 포함

### 기존 파일 활용 흐름
**프롬프트**: "이 FAQ 있는데, 응대 매뉴얼이랑 에스컬레이션 정책 만들어줘" + FAQ 파일 첨부
**기대 결과**:
- 기존 FAQ를 `_workspace/01_faq.md`로 복사
- faq-builder 건너뛰고 response-specialist + escalation-manager + cs-analyst + reviewer 투입

### 에러 흐름
**프롬프트**: "고객지원 FAQ 만들어줘"
**기대 결과**:
- FAQ 모드로 전환 (faq-builder + reviewer)
- 서비스 정보 부족 시 산업/제품 유형 추가 질문
- 최소 정보만 제공 시 일반 SaaS FAQ 템플릿 생성

## 에이전트별 확장 스킬

에이전트의 도메인 전문성을 강화하는 확장 스킬:

| 스킬 | 파일 | 대상 에이전트 | 역할 |
|------|------|-------------|------|
| csat-analyzer | `skills/csat-analyzer/SKILL.md` | cs-analyst, cs-reviewer | CSAT/NPS/CES 설계, 운영 메트릭, VOC 분석, CS 대시보드 설계 |
| escalation-flowchart | `skills/escalation-flowchart/SKILL.md` | escalation-manager, response-specialist | L1/L2/L3 구조, 심각도 분류, 트리거 조건, SLA 매트릭스, 위기 대응 |
