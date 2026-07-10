---
name: market-research
description: "시장 조사의 산업분석, 경쟁분석, 소비자조사, 트렌드 분석, 종합 보고서를 에이전트 팀이 협업하여 한 번에 생성하는 풀 리서치 파이프라인. '시장 조사해줘', '경쟁 분석', '산업 분석', '소비자 분석', '트렌드 분석', '시장 리서치', '시장 규모 알려줘', '경쟁사 분석해줘', 'PESTLE 분석', 'Porter 5 Forces', '시장 진입 전략', '타깃 고객 분석' 등 시장 조사 전반에 이 스킬을 사용한다. 기존 분석 자료가 있는 경우에도 추가 분석이나 통합 보고서 작성을 지원한다. 단, 실제 설문조사 실행, 인터뷰 진행, 통계 소프트웨어 분석, 시장조사 리포트 구매는 이 스킬의 범위가 아니다."
---

# Market Research — 시장 조사 풀 리서치 파이프라인

산업분석→경쟁분석→소비자조사→트렌드→종합 보고서를 에이전트 팀이 협업하여 한 번에 생성한다.

## 실행 모드

**에이전트 팀** — 5명이 SendMessage로 직접 통신하며 교차 검증한다.

## 에이전트 구성

| 에이전트 | 파일 | 역할 | 타입 |
|---------|------|------|------|
| industry-analyst | `agents/industry-analyst.md` | 시장 규모, 산업 구조, 밸류체인 | general-purpose |
| competitor-analyst | `agents/competitor-analyst.md` | 경쟁사 매핑, SWOT, 포지셔닝 | general-purpose |
| consumer-analyst | `agents/consumer-analyst.md` | 세그먼테이션, 구매 여정, 니즈 | general-purpose |
| trend-analyst | `agents/trend-analyst.md` | PESTLE, 기술/소비자 트렌드 | general-purpose |
| research-reviewer | `agents/research-reviewer.md` | 교차 검증, 인사이트 통합 | general-purpose |

## 워크플로우

### Phase 1: 준비 (오케스트레이터 직접 수행)

1. 사용자 입력에서 추출한다:
    - **조사 대상**: 산업/제품/서비스 카테고리
    - **조사 목적**: 신규 진입/확장/투자 판단/전략 수립 등
    - **지리 범위**: 국내/해외/특정 지역
    - **중점 분석**: 특히 깊이 있게 다뤄야 할 영역
    - **기존 자료** (선택): 이미 보유 중인 분석 결과
2. `_workspace/` 디렉토리를 프로젝트 루트에 생성한다
3. 입력을 정리하여 `_workspace/00_input.md`에 저장한다
4. 기존 파일이 있으면 해당 단계를 건너뛴다
5. 요청 범위에 따라 **실행 모드를 결정**한다

### Phase 2: 팀 구성 및 실행

| 순서 | 작업 | 담당 | 의존 | 산출물 |
|------|------|------|------|--------|
| 1 | 산업 분석 | industry-analyst | 없음 | `_workspace/01_industry_analysis.md` |
| 2a | 경쟁 분석 | competitor-analyst | 작업 1 | `_workspace/02_competitor_analysis.md` |
| 2b | 소비자 분석 | consumer-analyst | 작업 1 | `_workspace/03_consumer_analysis.md` |
| 3 | 트렌드 분석 | trend-analyst | 작업 1, 2a, 2b | `_workspace/04_trend_analysis.md` |
| 4 | 종합 검증 | research-reviewer | 작업 1~3 | `_workspace/05_review_report.md` |

작업 2a(경쟁)와 2b(소비자)는 **병렬 실행**한다. 둘 다 작업 1(산업)에만 의존하므로 동시에 시작할 수 있다.

**팀원 간 소통 흐름:**
- industry-analyst 완료 → competitor-analyst에게 산업 구조·핵심 플레이어 전달, consumer-analyst에게 시장 세그먼트·소비자 접점 전달
- competitor-analyst 완료 → consumer-analyst에게 경쟁사별 고객 평판 전달, trend-analyst에게 전략 변화 방향 전달
- consumer-analyst 완료 → trend-analyst에게 소비자 행동 변화 시그널 전달
- research-reviewer는 모든 산출물 교차 검증. 🔴 필수 수정 발견 시 수정 요청 → 재작업 (최대 2회)

### Phase 3: 통합 및 최종 산출물

1. `_workspace/` 내 모든 파일을 확인한다
2. 검증 보고서의 🔴 필수 수정이 모두 반영되었는지 확인한다
3. 최종 요약을 사용자에게 보고한다

## 작업 규모별 모드

| 사용자 요청 패턴 | 실행 모드 | 투입 에이전트 |
|----------------|----------|-------------|
| "시장 조사해줘", "풀 리서치" | **풀 파이프라인** | 5명 전원 |
| "산업 분석만 해줘" | **산업 모드** | industry-analyst + reviewer |
| "경쟁사 분석해줘" | **경쟁 모드** | industry-analyst + competitor-analyst + reviewer |
| "소비자 조사해줘" | **소비자 모드** | consumer-analyst + reviewer |
| "트렌드 분석해줘" | **트렌드 모드** | trend-analyst + reviewer |
| "이 보고서 검토해줘" | **리뷰 모드** | reviewer 단독 |

## 데이터 전달 프로토콜

| 전략 | 방식 | 용도 |
|------|------|------|
| 파일 기반 | `_workspace/` 디렉토리 | 주요 산출물 저장 및 공유 |
| 메시지 기반 | SendMessage | 실시간 핵심 정보 전달, 수정 요청 |
| 태스크 기반 | TaskCreate/TaskUpdate | 진행 상황 추적, 의존 관계 관리 |

## 에러 핸들링

| 에러 유형 | 전략 |
|----------|------|
| 웹 검색 실패 | 일반 산업 지식 기반으로 분석, "데이터 제한" 명시 |
| 시장 데이터 미확보 | 인접 산업/해외 시장 데이터로 유추, 추정 근거 명시 |
| 에이전트 실패 | 1회 재시도 → 실패 시 해당 산출물 없이 진행, 보고서에 누락 명시 |
| 검증에서 🔴 발견 | 해당 에이전트에 수정 요청 → 재작업 → 재검증 (최대 2회) |

## 테스트 시나리오

### 정상 흐름
**프롬프트**: "국내 반려동물 사료 시장을 조사해줘. 프리미엄 사료 시장에 진입하려고 해"
**기대 결과**:
- 산업: 반려동물 시장 규모, 사료 세그먼트, 밸류체인, 규제
- 경쟁: 주요 사료 브랜드 10개 이상, SWOT, 포지셔닝 맵
- 소비자: 반려인 세그먼트, 사료 구매 여정, 프리미엄 지불 의사
- 트렌드: 휴먼그레이드, 맞춤형 사료, 구독 서비스 트렌드
- 종합: 프리미엄 시장 진입 전략 권고

### 기존 파일 활용 흐름
**프롬프트**: "이 산업 분석 결과로 경쟁사 분석과 소비자 분석 해줘" + 파일 첨부
**기대 결과**:
- 기존 분석을 `01_industry_analysis.md`로 복사
- 경쟁+소비자 모드 병합 투입, 산업 분석 건너뜀

### 에러 흐름
**프롬프트**: "새로운 시장 조사해줘, 뭐가 좋을지 모르겠어"
**기대 결과**:
- 조사 대상 불명확 → 최근 성장 산업 3개 제안 후 선택 유도
- 선택 후 풀 파이프라인 진행

## 에이전트별 확장 스킬

에이전트의 도메인 전문성을 강화하는 확장 스킬:

| 스킬 | 파일 | 대상 에이전트 | 역할 |
|------|------|-------------|------|
| tam-sam-som-calculator | `skills/tam-sam-som-calculator/SKILL.md` | industry-analyst, research-reviewer | 상향식/하향식/가치 기반 산출, 데이터 소스 가이드, 검증 체크리스트 |
| porter-five-forces | `skills/porter-five-forces/SKILL.md` | industry-analyst, competitor-analyst | 5 Forces 평가 항목, 점수 체계, 산업 매력도 산출, 전략 시사점 |
