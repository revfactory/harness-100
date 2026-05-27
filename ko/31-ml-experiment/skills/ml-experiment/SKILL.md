---
name: ml-experiment
description: "ML 실험의 데이터 준비, 모델 설계, 학습, 평가, 배포 준비를 에이전트 팀이 협업하여 수행하는 풀 ML 파이프라인. 'ML 실험 설계해줘', '모델 학습해줘', '머신러닝 프로젝트', '딥러닝 모델 만들어줘', '분류 모델', '회귀 모델', '데이터 전처리', '모델 평가', '하이퍼파라미터 튜닝', 'MLOps 설정', 'XGBoost 모델', 'PyTorch 모델' 등 ML 실험 전반에 이 스킬을 사용한다. 데이터 전처리만 필요하거나 모델 평가만 필요한 경우에도 지원한다. 단, 모델 서빙 인프라(SageMaker/Vertex AI) 직접 배포, 대규모 분산 학습 클러스터 관리, 실시간 추론 서비스 운영은 이 스킬의 범위가 아니다."
---

# ML Experiment — ML 실험 관리 풀 파이프라인

ML 실험의 데이터준비→모델설계→학습→평가→배포준비를 에이전트 팀이 협업하여 한 번에 수행한다.

## 실행 모드

**에이전트 팀** — 5명이 SendMessage로 직접 통신하며 교차 검증한다.

## 에이전트 구성

| 에이전트 | 파일 | 역할 | 타입 |
|---------|------|------|------|
| data-engineer | `agents/data-engineer.md` | 수집, 전처리, 피처엔지니어링 | general-purpose |
| model-designer | `agents/model-designer.md` | 아키텍처, 하이퍼파라미터, 손실함수 | general-purpose |
| training-manager | `agents/training-manager.md` | 실험추적, 체크포인트, 재현성 | general-purpose |
| evaluation-analyst | `agents/evaluation-analyst.md` | 메트릭, 편향검증, 해석가능성 | general-purpose |
| experiment-reviewer | `agents/experiment-reviewer.md` | 교차검증, 재현성, 최종보고서 | general-purpose |

## 워크플로우

### Phase 1: 준비 (오케스트레이터 직접 수행)

1. 사용자 입력에서 추출한다:
    - **문제 정의**: 분류/회귀/생성/추천/시계열 등
    - **데이터**: 데이터 소스, 파일, 형식, 규모
    - **목표 메트릭**: 정확도, F1, RMSE 등 구체적 목표
    - **제약 조건** (선택): 프레임워크, GPU, 추론 속도, 모델 크기
    - **기존 코드** (선택): 기존 모델, 전처리 코드, 실험 결과
2. `_workspace/` 디렉토리를 프로젝트 루트에 생성한다
3. 입력을 정리하여 `_workspace/00_input.md`에 저장한다
4. 기존 파일이 있으면 `_workspace/`에 복사하고 해당 Phase를 건너뛴다
5. 요청 범위에 따라 **실행 모드를 결정**한다

### Phase 2: 팀 구성 및 실행

| 순서 | 작업 | 담당 | 의존 | 산출물 |
|------|------|------|------|--------|
| 1 | 데이터 준비 | data-engineer | 없음 | `_workspace/01_data_preparation.md` |
| 2 | 모델 설계 | model-designer | 작업 1 | `_workspace/02_model_design.md` |
| 3 | 학습 설정 | training-manager | 작업 1, 2 | `_workspace/03_training_config.md` |
| 4 | 평가 분석 | evaluation-analyst | 작업 1, 2, 3 | `_workspace/04_evaluation_report.md` |
| 5 | 실험 리뷰 | experiment-reviewer | 작업 1~4 | `_workspace/05_review_report.md` |

**팀원 간 소통 흐름:**
- data-engineer 완료 → model-designer에게 피처·형상·데이터 특성 전달, training에게 데이터 로더 전달, evaluation에게 클래스 분포 전달
- model-designer 완료 → training에게 모델 코드·하이퍼파라미터 공간 전달, evaluation에게 모델 구조·평가 메트릭 전달
- training 완료 → evaluation에게 학습 곡선·최적 모델·실험 로그 전달
- evaluation 완료 → reviewer에게 평가 보고서 전달
- reviewer는 모든 산출물을 교차 검증. 🔴 필수 수정 발견 시 해당 에이전트에게 수정 요청 → 재작업 → 재검증 (최대 2회)

### Phase 3: 통합 및 최종 산출물

1. `_workspace/` 내 모든 파일을 확인한다
2. 리뷰 보고서의 🔴 필수 수정이 모두 반영되었는지 확인한다
3. 최종 요약을 사용자에게 보고한다:
    - 데이터 준비 — `01_data_preparation.md`
    - 모델 설계 — `02_model_design.md`
    - 학습 설정 — `03_training_config.md`
    - 평가 보고서 — `04_evaluation_report.md`
    - 리뷰 보고서 — `05_review_report.md`
    - 실험 코드 — `experiment_code/`

## 작업 규모별 모드

| 사용자 요청 패턴 | 실행 모드 | 투입 에이전트 |
|----------------|----------|-------------|
| "ML 실험 전체 설계해줘" | **풀 파이프라인** | 5명 전원 |
| "데이터 전처리해줘" | **데이터 모드** | data-engineer + reviewer |
| "모델 아키텍처 설계해줘" | **모델 모드** | model-designer + reviewer |
| "이 모델 평가해줘" (기존 결과) | **평가 모드** | evaluation-analyst + reviewer |
| "이 실험 리뷰해줘" | **리뷰 모드** | reviewer 단독 |

**기존 파일 활용**: 사용자가 전처리 코드, 학습된 모델 등을 제공하면, 해당 단계를 건너뛴다.

## 데이터 전달 프로토콜

| 전략 | 방식 | 용도 |
|------|------|------|
| 파일 기반 | `_workspace/` 디렉토리 | 주요 산출물 저장 및 공유 |
| 코드 기반 | `_workspace/experiment_code/` | 실행 가능한 코드 |
| 메시지 기반 | SendMessage | 실시간 핵심 정보 전달, 수정 요청 |

파일명 컨벤션: `{순번}_{에이전트}_{산출물}.{확장자}`

## 에러 핸들링

| 에러 유형 | 전략 |
|----------|------|
| 데이터 미제공 | 공개 데이터셋 추천 + 합성 데이터 생성 코드 제공 |
| GPU 부재 | CPU 최적화 설정 + 경량 모델 우선 제안 |
| 문제 유형 불명확 | 데이터 특성에서 추론 + 사용자 확인 요청 |
| 학습 발산 | LR 감소, Gradient Clipping, 배치 사이즈 조정 방안 제시 |
| 에이전트 실패 | 1회 재시도 → 실패 시 해당 산출물 없이 진행, 리뷰 보고서에 누락 명시 |
| 리뷰에서 🔴 발견 | 해당 에이전트에 수정 요청 → 재작업 → 재검증 (최대 2회) |

## 테스트 시나리오

### 정상 흐름
**프롬프트**: "Kaggle 타이타닉 데이터로 생존 예측 분류 모델을 만들어줘. F1 스코어 0.85 이상 목표."
**기대 결과**:
- 데이터: EDA(결측치, 분포, 상관관계), 전처리 파이프라인(Imputer+Scaler+Encoder), 층화 분할
- 모델: 베이스라인(LogisticRegression) + XGBoost + RandomForest 설계
- 학습: Optuna 하이퍼파라미터 튜닝, MLflow 실험 추적
- 평가: Confusion Matrix, SHAP 분석, 모델 비교, 통계적 검증
- 리뷰: 데이터 누수 없음 확인, 재현성 확인, 결론 타당성 검증

### 기존 파일 활용 흐름
**프롬프트**: "이 학습된 모델을 평가하고 개선 방향 제안해줘" + 모델 파일 첨부
**기대 결과**:
- 기존 모델을 `_workspace/`에 복사
- 평가 모드: evaluation-analyst + reviewer 투입
- 성능 분석, 오류 분석, 개선 권고 제공

### 에러 흐름
**프롬프트**: "머신러닝 모델 만들어줘, 데이터는 아직 없어"
**기대 결과**:
- 문제 유형 확인 요청
- 공개 데이터셋(UCI/Kaggle/HuggingFace) 3~5개 추천
- 합성 데이터 생성 코드 제공
- "데이터 확보 후 전체 파이프라인 실행 가능" 명시


## 에이전트별 확장 스킬

| 스킬 | 경로 | 강화 대상 에이전트 | 역할 |
|------|------|-----------------|------|
| feature-engineering-cookbook | `skills/feature-engineering-cookbook/SKILL.md` | data-engineer | 수치/범주/시계열 변환, 피처 선택, 데이터 누수 방지 |
| model-selection-guide | `skills/model-selection-guide/SKILL.md` | model-designer, evaluation-analyst | 문제별 모델 추천, 하이퍼파라미터 튜닝, 앙상블 |
| experiment-tracking-setup | `skills/experiment-tracking-setup/SKILL.md` | training-manager | MLflow 설정, 재현성 보장, 모델 레지스트리, 실험 비교 |
