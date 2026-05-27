---
name: model-selection-guide
description: "ML 문제 유형별 모델 선택 매트릭스, 하이퍼파라미터 튜닝 전략, 앙상블 방법론 가이드. '모델 선택', '알고리즘 비교', '하이퍼파라미터 튜닝', 'Optuna', '앙상블', 'XGBoost vs LightGBM', '모델 비교', '교차 검증' 등 ML 모델 선택 및 설계 시 이 스킬을 사용한다. model-designer와 evaluation-analyst의 모델 설계 역량을 강화한다. 단, 데이터 전처리나 학습 인프라 관리는 이 스킬의 범위가 아니다."
---

# Model Selection Guide — ML 모델 선택 매트릭스 가이드

문제 유형, 데이터 특성, 제약 조건에 따른 최적 모델 선택과 튜닝 전략.

## 문제 유형별 모델 추천

### 정형 데이터 (Tabular)

| 문제 유형 | 베이스라인 | 최적 후보 | 비고 |
|----------|----------|----------|------|
| 이진 분류 | LogisticRegression | XGBoost, LightGBM | 트리 기반 대부분 최적 |
| 다중 분류 | LogisticRegression(OVR) | LightGBM, CatBoost | CatBoost: 범주형 다수 |
| 회귀 | LinearRegression | XGBoost, LightGBM | 랜덤포레스트: 과적합 방지 |
| 순위 | — | LambdaMART (LightGBM) | 검색/추천 |
| 이상 탐지 | IsolationForest | AutoEncoder, LOF | 비지도/준지도 |
| 시계열 | ARIMA | Prophet, LightGBM | 피처 기반 시계열은 트리 |

### 비정형 데이터

| 데이터 | 모델 | 프레임워크 |
|--------|------|-----------|
| 이미지 | ResNet, EfficientNet, ViT | PyTorch, timm |
| 텍스트 | BERT, RoBERTa | HuggingFace Transformers |
| 음성 | Whisper, Wav2Vec | HuggingFace |
| 그래프 | GCN, GAT | PyG, DGL |

## XGBoost vs LightGBM vs CatBoost

| 기준 | XGBoost | LightGBM | CatBoost |
|------|---------|----------|----------|
| 속도 | 중간 | 빠름 | 느림 |
| 메모리 | 많음 | 적음 | 중간 |
| 범주형 처리 | 인코딩 필요 | 내장 지원 | 최고 성능 |
| 결측치 처리 | 내장 | 내장 | 내장 |
| 과적합 방지 | regularization | GOSS, EFB | Ordered Boosting |
| GPU 지원 | ✅ | ✅ | ✅ |
| 기본 추천 | 범용 | 대용량, 속도 중시 | 범주형 다수 |

## 하이퍼파라미터 튜닝

### Optuna 기본 구조

```python
import optuna

def objective(trial):
    params = {
        'n_estimators': trial.suggest_int('n_estimators', 100, 1000),
        'max_depth': trial.suggest_int('max_depth', 3, 10),
        'learning_rate': trial.suggest_float('learning_rate', 0.01, 0.3, log=True),
        'subsample': trial.suggest_float('subsample', 0.6, 1.0),
        'colsample_bytree': trial.suggest_float('colsample_bytree', 0.6, 1.0),
        'reg_alpha': trial.suggest_float('reg_alpha', 1e-8, 10.0, log=True),
        'reg_lambda': trial.suggest_float('reg_lambda', 1e-8, 10.0, log=True),
    }
    model = XGBClassifier(**params)
    score = cross_val_score(model, X, y, cv=5, scoring='f1').mean()
    return score

study = optuna.create_study(direction='maximize')
study.optimize(objective, n_trials=100)
```

### 튜닝 우선순위

```
LightGBM 튜닝 순서:
1단계 (영향 大): learning_rate, n_estimators, num_leaves
2단계 (영향 中): max_depth, min_child_samples, subsample
3단계 (영향 小): reg_alpha, reg_lambda, colsample_bytree
4단계 (미세 조정): min_split_gain, path_smooth
```

## 교차 검증 전략

| 전략 | 적합 | 코드 |
|------|------|------|
| K-Fold | 범용 (충분한 데이터) | `KFold(n_splits=5)` |
| Stratified K-Fold | 불균형 분류 | `StratifiedKFold(n_splits=5)` |
| Time Series Split | 시계열 | `TimeSeriesSplit(n_splits=5)` |
| Group K-Fold | 그룹 데이터 누수 방지 | `GroupKFold(n_splits=5)` |
| Repeated K-Fold | 더 안정적 추정 | `RepeatedKFold(n_splits=5, n_repeats=3)` |

## 앙상블 방법

### Stacking

```python
from sklearn.ensemble import StackingClassifier

estimators = [
    ('xgb', XGBClassifier()),
    ('lgbm', LGBMClassifier()),
    ('cat', CatBoostClassifier(verbose=0)),
]
stack = StackingClassifier(
    estimators=estimators,
    final_estimator=LogisticRegression(),
    cv=5
)
```

### Blending 가중치

```python
# 최적 가중치 탐색
from scipy.optimize import minimize

def objective(weights):
    pred = sum(w * p for w, p in zip(weights, predictions))
    return -f1_score(y_true, pred > 0.5)

result = minimize(objective, x0=[1/3]*3, constraints={'type': 'eq', 'fun': lambda w: sum(w)-1})
```

## 모델 선택 의사결정 트리

```
데이터 유형?
├── 정형 (테이블)
│   ├── 행 수 < 1000 → 로지스틱 회귀 / SVM
│   ├── 1000 < 행 수 < 100만 → XGBoost / LightGBM
│   └── 행 수 > 100만 → LightGBM (속도 우선)
├── 이미지 → CNN (EfficientNet, ViT)
├── 텍스트 → Transformer (BERT)
└── 시계열
    ├── 단변량 → Prophet / ARIMA
    └── 다변량 → LightGBM (피처 기반) / LSTM
```
