---
name: experiment-tracking-setup
description: "MLflow, Weights & Biases 등 실험 추적 도구 설정, 재현성 보장, 모델 레지스트리, 실험 비교 방법론 가이드. '실험 추적', 'MLflow', 'W&B', 'Weights and Biases', '재현성', '모델 레지스트리', '실험 비교', '하이퍼파라미터 로깅' 등 ML 실험 관리 시 이 스킬을 사용한다. training-manager의 실험 관리 역량을 강화한다. 단, 모델 아키텍처 설계나 피처 엔지니어링은 이 스킬의 범위가 아니다."
---

# Experiment Tracking Setup — 실험 추적 및 재현성 가이드

ML 실험의 추적, 재현성 보장, 모델 버전 관리를 위한 실전 가이드.

## MLflow 설정

### 기본 구조

```python
import mlflow

mlflow.set_tracking_uri("http://localhost:5000")
mlflow.set_experiment("order-prediction")

with mlflow.start_run(run_name="xgboost-v2"):
    # 파라미터 로깅
    mlflow.log_params({
        "model": "XGBClassifier",
        "n_estimators": 500,
        "max_depth": 6,
        "learning_rate": 0.1,
    })

    # 학습
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    # 메트릭 로깅
    mlflow.log_metrics({
        "accuracy": accuracy_score(y_test, predictions),
        "f1": f1_score(y_test, predictions),
        "precision": precision_score(y_test, predictions),
        "recall": recall_score(y_test, predictions),
    })

    # 모델 저장
    mlflow.sklearn.log_model(model, "model")

    # 아티팩트 저장
    mlflow.log_artifact("confusion_matrix.png")
    mlflow.log_artifact("feature_importance.csv")
```

### 자동 로깅

```python
# 프레임워크별 자동 로깅
mlflow.sklearn.autolog()     # scikit-learn
mlflow.xgboost.autolog()     # XGBoost
mlflow.lightgbm.autolog()    # LightGBM
mlflow.pytorch.autolog()     # PyTorch
mlflow.tensorflow.autolog()  # TensorFlow
```

## 재현성 보장 체크리스트

### 필수 기록 항목

```python
import platform, sys

reproducibility_info = {
    # 환경
    "python_version": sys.version,
    "os": platform.platform(),
    "gpu": torch.cuda.get_device_name(0) if torch.cuda.is_available() else "N/A",

    # 시드
    "random_seed": 42,
    "numpy_seed": 42,
    "torch_seed": 42,

    # 데이터
    "data_version": "v2.1",
    "data_hash": hashlib.md5(open('data.csv','rb').read()).hexdigest(),
    "train_size": len(X_train),
    "test_size": len(X_test),
    "split_method": "StratifiedKFold(5)",

    # 코드
    "git_commit": subprocess.check_output(['git', 'rev-parse', 'HEAD']).decode().strip(),
    "git_branch": subprocess.check_output(['git', 'branch', '--show-current']).decode().strip(),
}
mlflow.log_params(reproducibility_info)
```

### 시드 고정

```python
import random, numpy as np, torch

def set_seed(seed=42):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False
    os.environ['PYTHONHASHSEED'] = str(seed)
```

### 의존성 고정

```bash
# requirements.txt 정확한 버전
pip freeze > requirements.txt

# pip-compile (권장)
pip-compile requirements.in --generate-hashes

# conda
conda env export --no-builds > environment.yml
```

## 모델 레지스트리

### MLflow Model Registry 워크플로우

```
실험(Experiment)
└── 실행(Run)
    └── 모델 아티팩트
        └── 모델 등록 (Model Registry)
            ├── Stage: Staging → 검증
            ├── Stage: Production → 배포
            └── Stage: Archived → 보관
```

```python
# 모델 등록
mlflow.register_model(
    model_uri=f"runs:/{run_id}/model",
    name="order-prediction-model"
)

# 스테이지 전환
client = mlflow.tracking.MlflowClient()
client.transition_model_version_stage(
    name="order-prediction-model",
    version=3,
    stage="Production"
)

# Production 모델 로드
model = mlflow.pyfunc.load_model("models:/order-prediction-model/Production")
```

## 실험 비교 프레임워크

### 통계적 검증

```python
from scipy import stats

# 5-fold CV 결과 비교
model_a_scores = [0.85, 0.87, 0.84, 0.86, 0.88]
model_b_scores = [0.82, 0.84, 0.83, 0.81, 0.85]

# 대응 t-검정 (Paired t-test)
t_stat, p_value = stats.ttest_rel(model_a_scores, model_b_scores)
print(f"p-value: {p_value:.4f}")
if p_value < 0.05:
    print("통계적으로 유의미한 차이 있음")
```

### 실험 비교 테이블

```markdown
| 실험 | 모델 | F1 | Precision | Recall | 학습 시간 | 추론 시간 |
|------|------|-----|-----------|--------|----------|----------|
| exp-001 | LogReg (baseline) | 0.78 | 0.80 | 0.76 | 2s | 0.1ms |
| exp-002 | XGBoost | 0.85 | 0.87 | 0.83 | 45s | 0.5ms |
| exp-003 | LightGBM | 0.86 | 0.88 | 0.84 | 20s | 0.3ms |
| exp-004 | LightGBM + Optuna | 0.88 | 0.89 | 0.87 | 2h | 0.3ms |
| exp-005 | Stacking (top3) | 0.89 | 0.90 | 0.88 | 3h | 1.2ms |
```

## 프로젝트 구조 템플릿

```
ml-project/
├── data/
│   ├── raw/              # 원본 데이터 (수정 금지)
│   ├── processed/        # 전처리 완료
│   └── external/         # 외부 데이터
├── notebooks/            # 탐색적 분석
├── src/
│   ├── data/             # 데이터 로딩/전처리
│   ├── features/         # 피처 엔지니어링
│   ├── models/           # 모델 정의
│   └── evaluation/       # 평가 로직
├── configs/              # 하이퍼파라미터 YAML
├── models/               # 학습된 모델
├── reports/              # 분석 보고서
├── requirements.txt
└── Makefile              # 재현 가능한 실행
```
