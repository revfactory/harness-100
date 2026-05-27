---
name: adr-writer
description: "아키텍처 결정 기록(ADR)을 에이전트 팀이 체계적으로 작성하는 파이프라인. 'ADR 작성해줘', '아키텍처 결정 기록', '기술 의사결정 문서화', 'architecture decision record', '아키텍처 선택 근거 정리', '기술 스택 결정', '대안 비교 분석', '트레이드오프 분석', '아키텍처 결정 이력' 등 아키텍처 의사결정 문서화 전반에 이 스킬을 사용한다. 단, 실제 코드 마이그레이션 수행, 인프라 프로비저닝, 성능 테스트 실행은 이 스킬의 범위가 아니다."
---

# ADR Writer — 아키텍처 결정 기록 파이프라인

아키텍처 결정의 컨텍스트 분석→대안 비교→트레이드오프 평가→결정 문서화→영향 추적을 에이전트 팀이 협업하여 수행한다.

## 실행 모드

**에이전트 팀** — 5명이 SendMessage로 직접 통신하며 교차 검증한다.

## 에이전트 구성

| 에이전트 | 파일 | 역할 | 타입 |
|---------|------|------|------|
| context-analyst | `agents/context-analyst.md` | 현재 아키텍처·문제·제약 조건 분석 | general-purpose |
| alternative-researcher | `agents/alternative-researcher.md` | 기술 대안 탐색·벤치마크 수집 | general-purpose |
| tradeoff-evaluator | `agents/tradeoff-evaluator.md` | 가중 평가·리스크-보상 분석 | general-purpose |
| adr-author | `agents/adr-author.md` | ADR 표준 포맷 문서 작성 | general-purpose |
| impact-tracker | `agents/impact-tracker.md` | 영향 분석·마이그레이션 로드맵 | general-purpose |

## 워크플로우

### Phase 1: 준비 (오케스트레이터 직접 수행)

1. 사용자 입력에서 추출한다:
    - **결정 주제**: 어떤 아키텍처 결정인가
    - **프로젝트 컨텍스트** (선택): 기술 스택, 팀 규모, 프로젝트 단계
    - **제약 조건** (선택): 예산, 일정, 기술적 제약
    - **기존 ADR** (선택): 이미 작성된 ADR 목록이나 코드베이스
2. `_workspace/` 디렉토리를 프로젝트 루트에 생성한다
3. 입력을 정리하여 `_workspace/00_input.md`에 저장한다
4. 코드베이스가 있으면 컨텍스트 분석가에게 탐색을 지시한다
5. 요청 범위에 따라 **실행 모드를 결정**한다 (아래 "작업 규모별 모드" 참조)

### Phase 2: 팀 구성 및 실행

| 순서 | 작업 | 담당 | 의존 | 산출물 |
|------|------|------|------|--------|
| 1 | 기술 컨텍스트 분석 | context-analyst | 없음 | `_workspace/01_context_analysis.md` |
| 2 | 대안 조사 | alternative-researcher | 작업 1 | `_workspace/02_alternatives_report.md` |
| 3 | 트레이드오프 평가 | tradeoff-evaluator | 작업 1, 2 | `_workspace/03_tradeoff_matrix.md` |
| 4a | ADR 문서 작성 | adr-author | 작업 1, 2, 3 | `_workspace/04_adr_document.md` |
| 4b | 영향 평가 | impact-tracker | 작업 1, 2, 3 | `_workspace/05_impact_assessment.md` |

작업 4a(ADR 문서)와 4b(영향 평가)는 **병렬 실행**한다. 둘 다 작업 1~3에만 의존하므로 동시에 시작할 수 있다.

**팀원 간 소통 흐름:**
- context-analyst 완료 → alternative-researcher에게 제약 조건·기술 스택 전달, tradeoff-evaluator에게 품질 속성 우선순위 전달
- alternative-researcher 완료 → tradeoff-evaluator에게 대안 목록·데이터 전달
- tradeoff-evaluator 완료 → adr-author에게 권고안 전달, impact-tracker에게 리스크 목록 전달
- adr-author ↔ impact-tracker: ADR 문서와 영향 평가 간 정합성 교차 확인

### Phase 3: 통합 및 최종 산출물

1. `_workspace/` 내 모든 파일을 확인한다
2. ADR 문서와 영향 평가 간 정합성을 검증한다
3. 최종 요약을 사용자에게 보고한다:
    - 기술 컨텍스트 — `01_context_analysis.md`
    - 대안 조사 — `02_alternatives_report.md`
    - 트레이드오프 평가 — `03_tradeoff_matrix.md`
    - ADR 문서 — `04_adr_document.md`
    - 영향 평가 — `05_impact_assessment.md`

## 작업 규모별 모드

| 사용자 요청 패턴 | 실행 모드 | 투입 에이전트 |
|----------------|----------|-------------|
| "ADR 작성해줘", "아키텍처 결정 기록" | **풀 파이프라인** | 5명 전원 |
| "대안 비교만 해줘" | **대안 분석 모드** | context-analyst + alternative-researcher + tradeoff-evaluator |
| "이 결정 문서화해줘" (결정 완료 상태) | **문서화 모드** | adr-author + impact-tracker |
| "이 ADR 영향 분석해줘" (기존 ADR 있음) | **영향 분석 모드** | impact-tracker 단독 |
| "기술 컨텍스트 정리해줘" | **컨텍스트 모드** | context-analyst 단독 |

**기존 파일 활용**: 사용자가 이미 분석 자료를 제공하면, 해당 파일을 `_workspace/`에 복사하고 해당 단계의 에이전트는 건너뛴다.

## 데이터 전달 프로토콜

| 전략 | 방식 | 용도 |
|------|------|------|
| 파일 기반 | `_workspace/` 디렉토리 | 주요 산출물 저장 및 공유 |
| 메시지 기반 | SendMessage | 실시간 핵심 정보 전달, 수정 요청 |
| 코드 탐색 | Read/Grep/Glob | 코드베이스에서 아키텍처 정보 추출 |

## 에러 핸들링

| 에러 유형 | 전략 |
|----------|------|
| 코드베이스 없음 | 사용자 설명 기반으로 컨텍스트 분석, "추론 기반" 명시 |
| 웹 검색 실패 | 일반 기술 지식 기반으로 대안 조사, "최신 데이터 미확인" 명시 |
| 정량 데이터 부족 | 정성 평가로 대체, 트레이드오프 매트릭스에 "추정치" 표시 |
| 에이전트 실패 | 1회 재시도 → 실패 시 해당 산출물 없이 진행, 최종 보고에 누락 명시 |
| 결정 보류 | ADR 상태를 "제안(Proposed)"으로 설정, 추가 필요 정보 명시 |

## 테스트 시나리오

### 정상 흐름
**프롬프트**: "모놀리스에서 마이크로서비스로의 전환 여부를 ADR로 작성해줘. 현재 Java Spring Boot 기반이고 팀은 5명이야."
**기대 결과**:
- 컨텍스트 분석: 모놀리스 현황, 전환 트리거, 팀 규모 제약
- 대안: 마이크로서비스, 모듈러 모놀리스, 현상 유지 최소 3개
- 트레이드오프: 가중 평가 매트릭스, 5명 팀 역량 고려
- ADR: MADR 포맷, 결정 근거와 기각 사유 모두 포함
- 영향 평가: 단계별 마이그레이션 로드맵, 롤백 전략

### 기존 자료 활용 흐름
**프롬프트**: "이미 Redis vs Memcached 비교는 했는데, ADR 문서로 정리해줘" + 비교 자료 제공
**기대 결과**:
- 제공된 비교 자료를 `_workspace/`에 복사
- context-analyst, alternative-researcher는 건너뛰거나 보완만 수행
- adr-author + impact-tracker 중심으로 문서화

### 에러 흐름
**프롬프트**: "데이터베이스 선택 ADR 써줘"
**기대 결과**:
- 컨텍스트가 부족하므로 context-analyst가 요구사항(데이터 유형, 규모, 접근 패턴) 질문 제안
- 일반적 시나리오 가정 하에 작업 진행, 가정 사항을 ADR에 명시
- 영향 평가에 "가정 검증 필요" 항목 추가

## 에이전트별 확장 스킬

에이전트의 도메인 전문성을 강화하는 확장 스킬:

| 에이전트 | 확장 스킬 | 역할 |
|---------|----------|------|
| tradeoff-evaluator | `quality-attribute-analyzer` | 품질 속성 사전, CAP 정리, 가중 평가 매트릭스, ATAM 간소화 |
| adr-author, impact-tracker | `madr-template-engine` | MADR 표준 포맷, ADR 상태 관리, 번호 체계, 의존성 그래프 |
