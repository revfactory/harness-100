---
name: feature-engineering-cookbook
description: "피처 엔지니어링 기법 카탈로그: 수치형/범주형/시계열/텍스트 변환, 피처 선택, 피처 스토어 설계. '피처 엔지니어링', '특성 공학', '변수 변환', '인코딩', '스케일링', '피처 선택', '피처 스토어', '피처 중요도' 등 데이터 전처리 및 피처 설계 시 이 스킬을 사용한다. data-engineer의 피처 엔지니어링 역량을 강화한다. 단, 모델 설계나 학습 관리는 이 스킬의 범위가 아니다."
---

# Feature Engineering Cookbook — 피처 엔지니어링 기법 카탈로그

데이터 타입별 변환 기법, 피처 선택 방법, 피처 스토어 설계 가이드.

## 수치형 변환

### 스케일링

| 방법 | 공식 | 적합 | 부적합 |
|------|------|------|--------|
| StandardScaler | (x - μ) / σ | 정규분포, SVM, 로지스틱 회귀 | 이상치 민감 |
| MinMaxScaler | (x - min) / (max - min) | [0,1] 필요, 신경망 | 이상치 민감 |
| RobustScaler | (x - Q2) / (Q3 - Q1) | 이상치 존재 | — |
| PowerTransformer | Box-Cox / Yeo-Johnson | 왜도 큰 분포 | 음수값(Box-Cox) |
| QuantileTransformer | 분위수 기반 | 균일/정규 분포 변환 | 순서 관계 파괴 |

### 이산화 (Binning)

```python
# 등간격 (Equal Width)
pd.cut(df['age'], bins=5)

# 등빈도 (Equal Frequency)
pd.qcut(df['income'], q=5)

# 도메인 기반
bins = [0, 18, 30, 50, 65, 100]
labels = ['미성년', '청년', '중년', '장년', '노년']
pd.cut(df['age'], bins=bins, labels=labels)
```

### 수학적 변환

```python
# 로그 변환 (오른쪽 꼬리 분포)
df['log_income'] = np.log1p(df['income'])

# 제곱근 (카운트 데이터)
df['sqrt_count'] = np.sqrt(df['count'])

# 역수 (반비례 관계)
df['inv_distance'] = 1 / (df['distance'] + 1)
```

## 범주형 인코딩

| 방법 | 카디널리티 | 순서 | 트리 모델 | 선형 모델 |
|------|-----------|------|----------|----------|
| Label Encoding | 무관 | 있음 | ✅ | ❌ |
| One-Hot Encoding | 낮음(<20) | 없음 | ✅ | ✅ |
| Target Encoding | 높음 | N/A | ✅ | ✅ |
| Frequency Encoding | 높음 | N/A | ✅ | ✅ |
| Binary Encoding | 중간 | N/A | ✅ | ✅ |
| Ordinal Encoding | 무관 | 있음 | ✅ | ✅ |

### Target Encoding (과적합 방지)

```python
from sklearn.model_selection import KFold

def target_encode_cv(train, col, target, n_folds=5):
    """K-Fold 기반 타깃 인코딩 — 데이터 누수 방지"""
    global_mean = train[target].mean()
    encoded = pd.Series(index=train.index, dtype=float)

    kf = KFold(n_splits=n_folds, shuffle=True, random_state=42)
    for train_idx, val_idx in kf.split(train):
        means = train.iloc[train_idx].groupby(col)[target].mean()
        encoded.iloc[val_idx] = train.iloc[val_idx][col].map(means)

    encoded.fillna(global_mean, inplace=True)
    return encoded
```

## 시계열 피처

```python
# 날짜 분해
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df['dayofweek'] = df['date'].dt.dayofweek
df['is_weekend'] = df['dayofweek'].isin([5, 6]).astype(int)
df['hour'] = df['date'].dt.hour
df['is_business_hour'] = df['hour'].between(9, 18).astype(int)

# 순환 인코딩 (월, 시간 등 주기적 변수)
df['month_sin'] = np.sin(2 * np.pi * df['month'] / 12)
df['month_cos'] = np.cos(2 * np.pi * df['month'] / 12)

# Lag 피처
df['sales_lag_1'] = df['sales'].shift(1)
df['sales_lag_7'] = df['sales'].shift(7)

# Rolling 통계
df['sales_ma_7'] = df['sales'].rolling(7).mean()
df['sales_std_7'] = df['sales'].rolling(7).std()
```

## 피처 선택 방법

### 필터 방법

| 방법 | 수치→수치 | 범주→수치 | 수치→범주 |
|------|----------|----------|----------|
| 상관계수 (Pearson) | ✅ | — | — |
| 상호정보량 (MI) | ✅ | ✅ | ✅ |
| 카이제곱 | — | — | ✅ |
| ANOVA F-test | — | — | ✅ |
| 분산 기반 | ✅ (분산=0 제거) | — | — |

### 래퍼/임베디드 방법

```python
# 트리 기반 피처 중요도
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier().fit(X, y)
importances = pd.Series(model.feature_importances_, index=X.columns)
top_features = importances.nlargest(20).index

# Permutation Importance (모델 무관)
from sklearn.inspection import permutation_importance
result = permutation_importance(model, X_test, y_test, n_repeats=10)

# SHAP (해석 가능한 피처 중요도)
import shap
explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X_test)
shap.summary_plot(shap_values, X_test)
```

## 결측치 처리 의사결정

```
결측 비율 확인
├── < 5%: 제거 또는 단순 대체(평균/중앙값/최빈값)
├── 5~30%: 모델 기반 대체 (KNN, MICE, 트리 기반)
├── 30~50%: 결측 자체를 피처로 + 대체
│           df['col_missing'] = df['col'].isna().astype(int)
└── > 50%: 컬럼 제거 고려 (비즈니스 중요도 확인)
```

## 데이터 누수 방지 체크리스트

- [ ] 타깃 변수에서 파생된 피처가 없는가?
- [ ] 미래 정보를 사용하는 피처가 없는가?
- [ ] train/test 분할 전에 인코딩/스케일링을 하지 않았는가?
- [ ] Target Encoding에 CV를 적용했는가?
- [ ] 시계열 데이터에서 미래 데이터를 참조하지 않는가?
