---
name: statistical-tests-selector
description: "통계 검정 선택 의사결정 트리, 검정별 가정/공식/해석 가이드, 효과 크기와 검정력 분석. '통계 검정', 't-검정', 'ANOVA', '카이제곱', '상관분석', 'p-value', '가설 검정', '정규성 검정', '비모수 검정', '효과 크기' 등 통계 분석 방법 선택 시 이 스킬을 사용한다. analyst의 통계 분석 역량을 강화한다. 단, 데이터 정제나 시각화는 이 스킬의 범위가 아니다."
---

# Statistical Tests Selector — 통계 검정 선택 가이드

데이터 유형과 분석 목적에 따라 적절한 통계 검정을 선택하고 해석하는 가이드.

## 검정 선택 의사결정 트리

```
비교할 것이 무엇인가?
├── 두 그룹의 평균 차이
│   ├── 독립 표본 → 정규 분포? → Yes: 독립 t-검정
│   │                          → No: Mann-Whitney U
│   └── 대응 표본 → 정규 분포? → Yes: 대응 t-검정
│                              → No: Wilcoxon 부호순위
├── 세 그룹 이상 평균 차이
│   ├── 독립 → 정규 분포? → Yes: One-way ANOVA → 사후: Tukey HSD
│   │                     → No: Kruskal-Wallis → 사후: Dunn
│   └── 반복 측정 → Repeated Measures ANOVA / Friedman
├── 두 변수의 관계
│   ├── 연속 × 연속 → 선형? → Yes: Pearson 상관
│   │                       → No: Spearman 순위 상관
│   └── 범주 × 범주 → 카이제곱 독립성 검정
├── 비율 차이
│   ├── 두 그룹 → Z-검정 (비율)
│   └── 세 그룹 이상 → 카이제곱 동질성 검정
└── 분포 검정
    ├── 정규성 → Shapiro-Wilk (n<5000) / K-S test
    └── 등분산 → Levene's test / Bartlett's test
```

## 핵심 검정 상세

### 독립 표본 t-검정

```python
from scipy import stats

# 가정 확인
# 1. 정규성
stat, p = stats.shapiro(group_a)
print(f"정규성 검정: p={p:.4f}")

# 2. 등분산
stat, p = stats.levene(group_a, group_b)
print(f"등분산 검정: p={p:.4f}")

# 검정 수행
if levene_p >= 0.05:
    t, p = stats.ttest_ind(group_a, group_b)  # 등분산
else:
    t, p = stats.ttest_ind(group_a, group_b, equal_var=False)  # Welch

# 효과 크기 (Cohen's d)
d = (group_a.mean() - group_b.mean()) / np.sqrt(
    ((len(group_a)-1)*group_a.std()**2 + (len(group_b)-1)*group_b.std()**2)
    / (len(group_a) + len(group_b) - 2)
)
```

### 효과 크기 해석

| 지표 | 작음 | 중간 | 큼 |
|------|------|------|-----|
| Cohen's d | 0.2 | 0.5 | 0.8 |
| Pearson r | 0.1 | 0.3 | 0.5 |
| eta-squared (η²) | 0.01 | 0.06 | 0.14 |
| Cramer's V | 0.1 | 0.3 | 0.5 |

### ANOVA + 사후 검정

```python
# One-way ANOVA
f_stat, p = stats.f_oneway(group_a, group_b, group_c)

if p < 0.05:
    # 사후 검정 (어느 그룹 간 차이?)
    from statsmodels.stats.multicomp import pairwise_tukeyhsd
    tukey = pairwise_tukeyhsd(
        endog=all_values, groups=all_labels, alpha=0.05
    )
    print(tukey.summary())
```

### 카이제곱 검정

```python
# 독립성 검정 (범주 × 범주)
contingency = pd.crosstab(df['gender'], df['purchase'])
chi2, p, dof, expected = stats.chi2_contingency(contingency)

# 효과 크기 (Cramer's V)
n = contingency.sum().sum()
v = np.sqrt(chi2 / (n * (min(contingency.shape) - 1)))
```

## 다중 비교 보정

| 방법 | 보수성 | 수식 | 사용 |
|------|--------|------|------|
| Bonferroni | 매우 보수적 | α/n | 비교 수 적을 때 |
| Holm-Bonferroni | 보수적 | 단계적 조정 | 범용 |
| Benjamini-Hochberg | 덜 보수적 | FDR 제어 | 탐색적 분석 |
| Tukey HSD | 중간 | ANOVA 사후 | 전체 쌍비교 |

```python
from statsmodels.stats.multitest import multipletests

reject, pvals_corrected, _, _ = multipletests(
    p_values, alpha=0.05, method='holm'
)
```

## 검정력 분석

```python
from statsmodels.stats.power import TTestIndPower

analysis = TTestIndPower()

# 필요 표본 크기 계산
n = analysis.solve_power(
    effect_size=0.5,    # Cohen's d = 0.5 (중간 효과)
    alpha=0.05,         # 유의수준
    power=0.8,          # 검정력 80%
    alternative='two-sided'
)
print(f"그룹당 필요 표본 수: {int(np.ceil(n))}")
```

| 효과 크기 | 검정력 80% 필요 n (그룹당) |
|----------|------------------------|
| d = 0.2 (작음) | 394 |
| d = 0.5 (중간) | 64 |
| d = 0.8 (큼) | 26 |

## p-value 올바른 해석

```
p = 0.03일 때:

✅ 올바른 해석:
"귀무가설이 참일 때, 이 데이터만큼 극단적인 결과를 관찰할 확률이 3%이다."

❌ 잘못된 해석:
"대립가설이 참일 확률이 97%이다." (베이지안이 아님)
"효과가 크다." (효과 크기는 별도 측정)
"결과가 중요하다." (통계적 유의성 ≠ 실용적 중요성)
```

## 보고 템플릿

```markdown
### 분석: A/B 그룹 전환율 비교

**가설**: 새 디자인(B)이 기존(A)보다 전환율이 높다
**검정**: 이표본 비율 z-검정 (단측)
**표본**: A: n=1000, 전환율 5.2% | B: n=1000, 전환율 6.8%
**결과**: z=1.58, p=0.057, 95% CI: [-0.05%, 3.25%]
**효과 크기**: h=0.067 (작음)
**결론**: 유의수준 5%에서 통계적으로 유의미하지 않음 (p=0.057).
         검정력 분석: 현재 효과 크기로 80% 검정력 달성에
         그룹당 n=3,500 필요. 표본 확대 권장.
```
