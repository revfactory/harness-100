---
name: financial-ratio-analyzer
description: "A financial ratio analysis tool for diagnosing personal financial health. The 'financial-analyst' and 'finance-reviewer' agents must use this skill's financial ratio formulas, health benchmarks, and diagnostic framework when evaluating financial status and verifying figures. Use for 'financial health diagnosis', 'financial ratio analysis', 'household financial checkup', and similar requests. However, investment strategy and tax optimization are outside the scope of this skill."
---

# Financial Ratio Analyzer — Personal Financial Ratio Analyzer

Diagnoses the financial health of individuals and households using core ratios and provides improvement directions.

## 8 Core Financial Ratios

### 1. Savings Rate

```
Savings Rate = (Monthly savings + Investments) / After-tax monthly income × 100

Good: 20%+    Adequate: 10–20%    At Risk: below 10%

Benchmarks by age:
  20s: 15%+ (asset-building phase)
  30s: 20%+ (preparing for home purchase)
  40s: 25%+ (education costs / retirement prep)
  50s: 30%+ (retirement focus)
```

### 2. Consumption Ratio

```
Consumption Ratio = Monthly consumer spending / After-tax monthly income × 100

Good: 60% or less    Adequate: 60–80%    At Risk: above 80%

50/30/20 Rule:
  Essential expenses (housing, food, transport): 50% or less
  Discretionary expenses (leisure, shopping): 30% or less
  Savings + investments + debt repayment: 20% or more
```

### 3. Emergency Fund Ratio

```
Emergency Fund Ratio = Liquid assets / Monthly essential expenses

Good: 6 months+    Adequate: 3–6 months    At Risk: below 3 months

Liquid assets: checking accounts + CMA + MMF (immediately cashable)
Essential expenses: housing + food + transport + insurance + telecom + loan repayments
```

### 4. Debt-to-Asset Ratio

```
Debt-to-Asset Ratio = Total liabilities / Total assets × 100

Good: 40% or less    Adequate: 40–60%    At Risk: above 60%

Liabilities include: mortgage, personal loans, student loans, credit card loans, installment payments
Assets include: real estate, financial assets, severance fund, deposits, etc.
```

### 5. Debt-to-Income Ratio (DTI)

```
DTI = Annual debt principal + interest payments / Annual income × 100

Good: 30% or less    Adequate: 30–40%    At Risk: above 40%

Bank lending standards:
  Mortgage DTI limit: 40–60% (varies by region)
  DSR (all loans): within 40%
```

### 6. Housing Cost Ratio

```
Housing Cost Ratio = (Monthly rent or loan interest + maintenance) / After-tax monthly income × 100

Good: 25% or less    Adequate: 25–30%    At Risk: above 30%

Included: monthly rent / loan interest, maintenance fees, home insurance
Excluded: principal repayment (counts as asset building)
```

### 7. Insurance Adequacy Ratio

```
Insurance Ratio = Total monthly premiums / After-tax monthly income × 100

Good: 7–10%    Excessive: above 15%    Insufficient: below 5%

Recommended coverage:
  Death benefit: 5–10× annual income
  Medical/indemnity: required
  Critical illness: diagnosis benefit 30,000,000 KRW+
```

### 8. Investment Asset Ratio

```
Investment Asset Ratio = (Stocks + Funds + ETFs + Bonds) / Total financial assets × 100

Recommended ratio = 100 − Age (%)
  Age 25: 75% investment / 25% safe
  Age 35: 65% / 35%
  Age 45: 55% / 45%
  Age 55: 45% / 55%
```

## Comprehensive Financial Health Score

```
Comprehensive Score = Σ(Ratio score × Weight) / Σ(Weights)

Score by status:
  Good:     100 points
  Adequate: 60 points
  At Risk:  20 points

Weights:
  Savings Rate:     3.0
  Emergency Fund:   2.5
  Debt-to-Asset:    2.5
  DTI:              2.0
  Consumption:      1.5
  Housing Cost:     1.5
  Insurance:        1.0
  Investment:       1.0

Grade scale:
  A (85+):   Very healthy — aggressive asset building possible
  B (70–84): Healthy — well-balanced status
  C (55–69): Average — some improvement needed
  D (40–54): Weak — systematic improvement needed
  F (<40):   At Risk — urgent financial restructuring required
```

## Financial Diagnosis Report Output Format

```markdown
## Personal Financial Health Diagnosis

**Diagnosis Date**: [date] | **Overall Grade**: [A/B/C/D/F] | **Score**: [XX/100]

### Core Ratio Dashboard
| Ratio | Current | Benchmark | Status | Improvement Direction |
|-------|---------|-----------|--------|----------------------|
| Savings Rate | X% | 20%+ | 🟢/🟡/🔴 | - |
| Emergency Fund | X months | 6 months+ | 🟢/🟡/🔴 | - |
| Debt-to-Asset | X% | 40% or less | 🟢/🟡/🔴 | - |
| DTI | X% | 30% or less | 🟢/🟡/🔴 | - |

### Immediate Improvement Required (🔴)
1. [Item]: Current X% → Target X% (improvement method)

### Improvement Recommended (🟡)
1. [Item]: Current X% → Target X%

### Healthy Items (🟢)
1. [Item]: Meets benchmark
```

## Reference

- Reflects Bank of Korea Household Finance and Welfare Survey and Financial Supervisory Service standards
- Detailed diagnostic model: see `references/financial-diagnosis.md`
