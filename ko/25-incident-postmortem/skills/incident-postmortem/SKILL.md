---
name: incident-postmortem
description: "장애 사후분석(포스트모텀) 보고서를 에이전트 팀이 협업하여 생성하는 풀 파이프라인. 타임라인 재구성, 근본원인 분석, 영향범위 산정, 재발방지 대책을 체계적으로 수행한다. '장애 포스트모텀 작성해줘', '사후분석 보고서', '장애 보고서 만들어줘', 'incident report', '근본원인 분석해줘', 'RCA 보고서', '장애 타임라인 정리해줘', '재발방지 대책 세워줘' 등 장애 분석 전반에 이 스킬을 사용한다. 단, 실시간 장애 대응(온콜), 모니터링 시스템 구축, 알림 설정은 이 스킬의 범위가 아니다."
---

# Incident Postmortem — 장애 사후분석 파이프라인

타임라인재구성→근본원인분석→영향범위산정→재발방지대책→보고서생성을 에이전트 팀이 협업하여 수행한다.

## 실행 모드

**에이전트 팀** — 5명이 SendMessage로 직접 통신하며 교차 검증한다.

## 에이전트 구성

| 에이전트 | 파일 | 역할 | 타입 |
|---------|------|------|------|
| timeline-reconstructor | `agents/timeline-reconstructor.md` | 이벤트 수집, 시간순 정렬, 갭 식별 | general-purpose |
| root-cause-investigator | `agents/root-cause-investigator.md` | 5 Whys, 피시본, Fault Tree | general-purpose |
| impact-assessor | `agents/impact-assessor.md` | 사용자/매출/SLA/평판 영향 산정 | general-purpose |
| remediation-planner | `agents/remediation-planner.md` | 단기/중기/장기 대책, 액션 아이템 | general-purpose |
| postmortem-reviewer | `agents/postmortem-reviewer.md` | 교차 검증, 비난 없는 문화 확인 | general-purpose |

## 워크플로우

### Phase 1: 준비 (오케스트레이터 직접 수행)

1. 사용자 입력에서 추출한다:
    - **장애 설명**: 무엇이 언제 발생했는가
    - **증거 자료** (선택): 로그, 메트릭 스크린샷, 채팅 기록, 알림 기록
    - **영향 정보** (선택): 영향받은 사용자 수, 서비스, 기간
    - **조치 내역** (선택): 이미 수행한 긴급 조치
2. `_workspace/` 디렉토리를 프로젝트 루트에 생성한다
3. 입력을 정리하여 `_workspace/00_input.md`에 저장한다
4. 기존 파일이 있으면 `_workspace/`에 복사하고 해당 Phase를 건너뛴다
5. 요청 범위에 따라 **실행 모드를 결정**한다 (아래 "작업 규모별 모드" 참조)

### Phase 2: 팀 구성 및 실행

| 순서 | 작업 | 담당 | 의존 | 산출물 |
|------|------|------|------|--------|
| 1 | 타임라인 재구성 | reconstructor | 없음 | `_workspace/01_timeline.md` |
| 2a | 근본원인 분석 | investigator | 작업 1 | `_workspace/02_root_cause.md` |
| 2b | 영향범위 산정 | assessor | 작업 1 | `_workspace/03_impact_assessment.md` |
| 3 | 재발방지 대책 | planner | 작업 2a, 2b | `_workspace/04_remediation_plan.md` |
| 4 | 최종 리뷰 | reviewer | 작업 1~3 | `_workspace/05_review_report.md` |

작업 2a(근본원인)와 2b(영향범위)는 **병렬 실행** 가능하다.

**팀원 간 소통 흐름:**
- reconstructor 완료 → investigator에게 타임라인·트리거 후보 전달, assessor에게 장애 기간·지표 전달
- investigator 완료 → planner에게 근본 원인·기여 요인 전달
- assessor 완료 → planner에게 영향 규모·SLA 위반 현황 전달
- planner 완료 → reviewer에게 대책 전문 전달
- reviewer는 모든 산출물을 교차 검증. 🔴 필수 수정 시 해당 에이전트에게 수정 요청 (최대 2회)

### Phase 3: 통합 보고서 생성

1. 모든 산출물을 통합한 `_workspace/postmortem_report.md`를 생성한다
2. 보고서 구조: 요약 → 타임라인 → 근본원인 → 영향 → 대책 → 잘한 점 → 교훈
3. 최종 보고서를 사용자에게 제공한다

## 작업 규모별 모드

| 사용자 요청 패턴 | 실행 모드 | 투입 에이전트 |
|----------------|----------|-------------|
| "포스트모텀 보고서 작성해줘" | **풀 파이프라인** | 5명 전원 |
| "장애 타임라인 정리해줘" | **타임라인 모드** | reconstructor + reviewer |
| "근본원인 분석해줘" | **RCA 모드** | reconstructor + investigator + reviewer |
| "재발방지 대책만 세워줘" (원인 분석 있음) | **대책 모드** | planner + reviewer |
| "이 포스트모텀 리뷰해줘" | **리뷰 모드** | reviewer 단독 |

**기존 파일 활용**: 사용자가 기존 타임라인, 원인 분석서 등을 제공하면, 해당 파일을 `_workspace/`의 적절한 위치에 복사하고 해당 단계의 에이전트는 건너뛴다.

## 데이터 전달 프로토콜

| 전략 | 방식 | 용도 |
|------|------|------|
| 파일 기반 | `_workspace/` 디렉토리 | 주요 산출물 저장 및 공유 |
| 메시지 기반 | SendMessage | 실시간 핵심 정보 전달, 수정 요청 |
| 태스크 기반 | TaskCreate/TaskUpdate | 진행 상황 추적, 의존 관계 관리 |

## 에러 핸들링

| 에러 유형 | 전략 |
|----------|------|
| 장애 정보 부족 | 사용자에게 추가 질문 후 진행, 불확실한 부분 "[미확인]" 태그 |
| 로그/메트릭 접근 불가 | 구술 기반 재구성, "[구술 기반]" 태그 부착 |
| 에이전트 실패 | 1회 재시도 → 실패 시 해당 산출물 없이 진행, 리뷰에 누락 명시 |
| 리뷰에서 🔴 발견 | 해당 에이전트에 수정 요청 → 재작업 → 재검증 (최대 2회) |
| 비난적 표현 발견 | reviewer가 즉시 수정 요청 — 비난 없는 문화 절대 원칙 |

## 테스트 시나리오

### 정상 흐름
**프롬프트**: "어제 오후 2시에 결제 서비스가 30분간 다운됐어. 배포 직후에 발생했고, 롤백으로 복구했어. 포스트모텀 보고서 만들어줘"
**기대 결과**:
- 타임라인: 배포→장애 발생→감지→대응→롤백→복구 시간순 정리
- 근본원인: 배포된 코드의 구체적 결함, 카나리 배포 미적용 등 기여 요인
- 영향: 사용자 수, 매출 손실, SLA 영향 추정
- 대책: 카나리 배포 도입, 자동 롤백, 알림 개선 등 SMART 액션 아이템
- 통합 보고서: 경영진 보고 가능한 완성된 포스트모텀

### 기존 파일 활용 흐름
**프롬프트**: "이 포스트모텀 보고서 검토해줘" + 보고서 첨부
**기대 결과**:
- 기존 보고서를 `_workspace/`에 복사
- 리뷰 모드로 실행
- 정합성, 완전성, 비난 없는 문화 준수 검증
- 개선 제안 제공

### 에러 흐름
**프롬프트**: "API 서버가 오늘 아침에 느려졌었어. 원인 분석해줘"
**기대 결과**:
- 추가 질문으로 장애 세부 정보 수집 (시각, 영향, 조치 등)
- 수집된 정보로 RCA 모드 실행
- 불확실한 부분 명시


## 에이전트별 확장 스킬

| 스킬 | 경로 | 강화 대상 에이전트 | 역할 |
|------|------|-----------------|------|
| rca-methodology | `skills/rca-methodology/SKILL.md` | root-cause-investigator | 5 Whys, 피시본, Fault Tree, 변경점 분석, 인지 편향 방지 |
| sla-impact-calculator | `skills/sla-impact-calculator/SKILL.md` | impact-assessor | SLA/SLO/SLI 체계, 에러 버짓, 매출 손실 추정, 심각도 등급 |
