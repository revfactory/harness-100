---
name: data-analysis
description: "데이터 분석 프로젝트의 탐색적 분석(EDA), 데이터 정제, 통계 분석, 시각화, 보고서 작성을 에이전트 팀이 협업하여 한 번에 수행하는 풀 분석 파이프라인. '데이터 분석해줘', 'EDA 해줘', '탐색적 분석', '통계 분석', '데이터 시각화', '분석 보고서 써줘', 'CSV 분석', '데이터 인사이트 뽑아줘', '데이터 정제', '이상치 분석' 등 데이터 분석 전반에 이 스킬을 사용한다. 단, 실시간 데이터 스트리밍, ML 모델 학습/배포, BI 대시보드 서버 구축은 이 스킬의 범위가 아니다."
---

# Data Analysis — 데이터 분석 풀 파이프라인

데이터의 탐색→정제→분석→시각화→보고서를 에이전트 팀이 협업하여 한 번에 수행한다.

## 실행 모드

**에이전트 팀** — 5명이 SendMessage로 직접 통신하며 교차 검증한다.

## 에이전트 구성

| 에이전트 | 파일 | 역할 | 타입 |
|---------|------|------|------|
| explorer | `agents/explorer.md` | 탐색적 분석, 데이터 프로파일링 | general-purpose |
| cleaner | `agents/cleaner.md` | 데이터 정제, 변환 파이프라인 | general-purpose |
| analyst | `agents/analyst.md` | 통계 분석, 인사이트 도출 | general-purpose |
| visualizer | `agents/visualizer.md` | 차트 설계, 시각화 코드 생성 | general-purpose |
| reporter | `agents/reporter.md` | 최종 보고서 작성, 품질 검증 | general-purpose |

## 워크플로우

### Phase 1: 준비 (오케스트레이터 직접 수행)

1. 사용자 입력에서 추출한다:
    - **데이터 소스**: 파일 경로, 포맷(CSV/Excel/JSON/DB), 크기
    - **분석 목적**: 비즈니스 질문, 가설, 기대 결과
    - **제약 조건** (선택): 시간, 특정 분석 기법, 보고 대상
    - **도메인 정보** (선택): 업종, 변수 의미, 비즈니스 맥락
2. `_workspace/` 디렉토리와 `_workspace/scripts/` 하위 디렉토리를 생성한다
3. 입력을 정리하여 `_workspace/00_input.md`에 저장한다
4. 데이터 파일을 `_workspace/data/`에 복사한다
5. 기존 파일이 있으면 `_workspace/`에 복사하고 해당 Phase를 건너뛴다
6. 요청 범위에 따라 **실행 모드를 결정**한다

### Phase 2: 팀 구성 및 실행

| 순서 | 작업 | 담당 | 의존 | 산출물 |
|------|------|------|------|--------|
| 1 | 탐색적 분석 | explorer | 없음 | `01_exploration_report.md` |
| 2 | 데이터 정제 | cleaner | 작업 1 | `02_cleaning_log.md`, `scripts/02_cleaning.py` |
| 3a | 통계 분석 | analyst | 작업 2 | `03_analysis_results.md`, `scripts/03_analysis.py` |
| 3b | EDA 시각화 | visualizer | 작업 1 | `04_visualizations.md` (EDA 부분) |
| 4 | 분석 결과 시각화 | visualizer | 작업 3a | `04_visualizations.md` (분석 부분), `scripts/04_viz_*.py` |
| 5 | 최종 보고서 | reporter | 작업 3a, 4 | `05_final_report.md` |

작업 3a(분석)와 3b(EDA 시각화)는 **병렬 실행**한다.

**팀원 간 소통 흐름:**
- explorer 완료 → cleaner에게 정제 권고 전달, analyst에게 분석 제안 전달, visualizer에게 분포 시각화 대상 전달
- cleaner 완료 → analyst에게 정제 데이터 위치와 변환 이력 전달
- analyst 완료 → visualizer에게 분석 결과 시각화 요청, reporter에게 인사이트 전달
- visualizer 완료 → reporter에게 시각화 목록 전달
- reporter는 모든 산출물을 교차 검증. 불일치 발견 시 해당 에이전트에 수정 요청 (최대 2회)

### Phase 3: 통합 및 최종 산출물

1. `_workspace/` 내 모든 파일을 확인한다
2. reporter의 보고서에서 필수 수정이 모두 반영되었는지 확인한다
3. 최종 요약을 사용자에게 보고한다:
    - 탐색 보고서 — `01_exploration_report.md`
    - 정제 로그 — `02_cleaning_log.md`
    - 분석 결과 — `03_analysis_results.md`
    - 시각화 — `04_visualizations.md`
    - 최종 보고서 — `05_final_report.md`
    - 재현 스크립트 — `scripts/` 디렉토리

## 작업 규모별 모드

| 사용자 요청 패턴 | 실행 모드 | 투입 에이전트 |
|----------------|----------|-------------|
| "데이터 분석해줘", "풀 분석" | **풀 파이프라인** | 5명 전원 |
| "EDA만 해줘", "데이터 탐색" | **탐색 모드** | explorer + visualizer |
| "데이터 정제해줘", "클리닝" | **정제 모드** | explorer + cleaner |
| "통계 분석만", "가설 검정" | **분석 모드** | analyst + visualizer + reporter |
| "시각화만 해줘", "차트 그려줘" | **시각화 모드** | visualizer 단독 |
| "분석 보고서 써줘" (기존 분석 있음) | **보고서 모드** | reporter 단독 |

**기존 파일 활용**: 이미 정제된 데이터가 있으면 explorer와 cleaner를 건너뛴다. 분석 결과가 있으면 analyst를 건너뛰고 시각화와 보고서만 진행한다.

## 데이터 전달 프로토콜

| 전략 | 방식 | 용도 |
|------|------|------|
| 파일 기반 | `_workspace/` 디렉토리 | 주요 산출물 및 데이터 저장 |
| 메시지 기반 | SendMessage | 핵심 정보 전달, 수정 요청 |
| 코드 기반 | `_workspace/scripts/` | 재현 가능한 분석 스크립트 |

파일명 컨벤션: `{순번}_{산출물}.{확장자}`

## 에러 핸들링

| 에러 유형 | 전략 |
|----------|------|
| 파일 읽기 실패 | 인코딩 순차 시도(UTF-8→CP949→EUC-KR→Latin-1), 구분자 자동 탐지 |
| 대용량 데이터(>1GB) | 샘플링 후 분석, chunk 처리, 전체 통계는 dask 사용 |
| 분석 가정 불충족 | 비모수 대안 자동 전환, 전환 이유를 보고서에 명시 |
| 시각화 한글 깨짐 | OS별 한글 폰트 설정 코드 자동 삽입 |
| 에이전트 실패 | 1회 재시도 후 실패 시 해당 산출물 없이 진행, 보고서에 누락 명시 |
| reporter 불일치 발견 | 해당 에이전트에 수정 요청 → 재작업 → 재검증 (최대 2회) |

## 테스트 시나리오

### 정상 흐름
**프롬프트**: "이 매출 CSV 파일을 분석해서 매출 하락 원인을 찾아줘"
**기대 결과**:
- EDA: 변수 프로파일, 결측/이상치 분석, 매출 관련 변수 식별
- 정제: 결측치 처리, 이상치 캡핑, 타입 변환 로그
- 분석: 시계열 분해, 구간별 비교(t-test/ANOVA), 상관분석
- 시각화: 매출 추이 라인차트, 요인별 비교 막대그래프, 상관 히트맵
- 보고서: 하락 원인 Top 3 + 권고 액션 + 경영진 요약

### 기존 파일 활용 흐름
**프롬프트**: "이미 정제된 데이터가 있어. 통계 분석이랑 시각화만 해줘" + 정제 데이터 파일 첨부
**기대 결과**:
- 기존 데이터를 `_workspace/data/`에 복사
- 분석 모드: explorer와 cleaner는 건너뛰고 analyst + visualizer + reporter 투입
- 정제 이력은 사용자 제공 정보 기반으로 기록

### 에러 흐름
**프롬프트**: "이 엑셀 파일 분석해줘" (결측 50% 이상 변수 다수, 이상치 대량)
**기대 결과**:
- explorer가 데이터 품질 문제를 상세히 보고
- cleaner가 변수별 처리 전략을 근거와 함께 제시, 행 30% 이상 감소 시 경고
- analyst가 데이터 충분성 한계를 명시하고 검정력 분석 수행
- reporter가 한계 섹션에 데이터 품질 이슈를 정직하게 기록


## 에이전트별 확장 스킬

| 스킬 | 경로 | 강화 대상 에이전트 | 역할 |
|------|------|-----------------|------|
| statistical-tests-selector | `skills/statistical-tests-selector/SKILL.md` | analyst | 검정 선택 트리, t-검정/ANOVA/카이제곱, 효과 크기, 검정력 |
| visualization-chooser | `skills/visualization-chooser/SKILL.md` | visualizer | 차트 유형 매트릭스, matplotlib/seaborn/plotly 패턴, 안티패턴 |
