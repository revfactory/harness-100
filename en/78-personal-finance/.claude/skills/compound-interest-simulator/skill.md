---
name: compound-interest-simulator
description: "A compound interest simulation and long-term asset growth projection tool. The 'investment-advisor' and 'tax-strategist' agents must use this skill's compound formulas, scenario comparisons, and retirement goal calculations when simulating investment returns and designing retirement funds. Use for 'compound interest calculation', 'asset growth projection', 'retirement fund simulation', and similar requests. However, budget design and tax calculation are outside the scope of this skill."
---

# Compound Interest Simulator — Compound Interest Simulator

Compound interest simulation, asset growth projection, and reverse retirement fund calculation.

## Core Compound Interest Formulas

### Lump-Sum Compound Interest

```
FV = PV × (1 + r)^n

FV: Future Value
PV: Present Value (current value)
r: Annual return rate (decimal)
n: Duration (years)

Example: Invest 10,000,000 KRW at 7% annual return for 30 years
  FV = 10,000,000 × (1.07)^30 = 76,120,000 KRW
```

### Regular Contribution Compound Interest (Monthly)

```
FV = PMT × [(1 + r/12)^(12n) - 1] / (r/12)

PMT: Monthly contribution
r: Annual return rate
n: Duration (years)

Example: Contribute 500,000 KRW/month at 7% annual return for 20 years
  FV = 500,000 × [(1.00583)^240 - 1] / 0.00583
     = 500,000 × 520.9 = 260,450,000 KRW
  (Principal: 120,000,000 KRW, Returns: 140,450,000 KRW)
```

### Retirement Fund Reverse Calculation (Required Monthly Contribution)

```
PMT = FV × (r/12) / [(1 + r/12)^(12n) - 1]

Example: Need 500,000,000 KRW in 20 years, expected 7% annual return
  PMT = 500,000,000 × 0.00583 / [(1.00583)^240 - 1]
     = 500,000,000 × 0.00192 = 959,000 KRW/month
```

## Rule of 72 (Time to Double Assets)

```
Years to double ≈ 72 / Annual return rate (%)

Doubling time by annual return rate:
  3%:  24 years
  5%:  14.4 years
  7%:  10.3 years
  10%: 7.2 years
  12%: 6 years
  15%: 4.8 years
```

## Expected Return Rates by Asset Class

| Asset | Annual Expected Return | Volatility (Std Dev) | Characteristics |
|-------|----------------------|----------------------|-----------------|
| Savings/Deposits | 3-4% | 0% | Principal guaranteed, below inflation |
| Bonds (Government) | 3-5% | 3-5% | Stable, inverse rate relationship |
| Bonds (Corporate) | 4-7% | 5-8% | Higher yield within bonds |
| Stocks (Domestic) | 7-10% | 15-20% | Long-term growth, high volatility |
| Stocks (Developed markets) | 7-10% | 14-18% | Global diversification |
| Stocks (Emerging markets) | 8-12% | 20-25% | High growth and risk |
| Real Estate (REITs) | 5-8% | 10-15% | Dividend + capital gains |
| Gold | 3-6% | 15-20% | Inflation hedge |

## Scenario Comparison Simulation

### Impact of Annual Return Rate Difference (Monthly 1,000,000 KRW, 30 years)

| Annual Return | Total Principal | Final Assets | Returns | Return Rate (Total) |
|--------------|----------------|--------------|---------|---------------------|
| 3% | 360,000,000 | 580,000,000 | 220,000,000 | 61% |
| 5% | 360,000,000 | 830,000,000 | 470,000,000 | 131% |
| 7% | 360,000,000 | 1,220,000,000 | 860,000,000 | 239% |
| 10% | 360,000,000 | 2,260,000,000 | 1,900,000,000 | 528% |

### Impact of Starting Time (Monthly 500,000 KRW, 7% annual return)

| Starting Age | Investment Period | Principal | Final Assets | Notes |
|-------------|-----------------|-----------|--------------|-------|
| 25 | 35 years | 210,000,000 | 1,080,000,000 | Early start |
| 30 | 30 years | 180,000,000 | 610,000,000 | 5-year gap: -470,000,000 |
| 35 | 25 years | 150,000,000 | 410,000,000 | |
| 40 | 20 years | 120,000,000 | 260,000,000 | |

## Retirement Planning Calculations

### Required Retirement Fund

```
Monthly expenses × 12 × Post-retirement years × Inflation adjustment

Conservative calculation (inflation 3%, investment return 5%):
  Real return rate = 5% - 3% = 2%

25 years of retirement, needing 3,000,000 KRW/month:
  Required fund = 3,000,000 × 12 / 0.02 × [1 - (1.02)^(-25)]
               ≈ 700,000,000 KRW

4% Withdrawal Rule (simple method):
  Retirement fund = Annual living expenses / 0.04
  = 36,000,000 KRW / 0.04 = 900,000,000 KRW
```

### National Pension Adjustment

```
Adjusted required fund = Total required fund - National pension present value

Expected national pension payout (2024 standard, 20 years of contributions):
  Monthly average income 3,000,000 KRW → approx. 600,000–800,000 KRW/month
  Monthly average income 5,000,000 KRW → approx. 1,000,000–1,200,000 KRW/month

Prepare the gap through personal assets
```

## Simulation Output Format

```markdown
## Asset Growth Simulation

**Initial Investment**: X KRW | **Monthly Contribution**: X KRW | **Expected Return**: X%
**Investment Period**: X years

| Year | Cumulative Principal | Asset Value | Returns | Return Rate |
|------|---------------------|-------------|---------|-------------|
| 5    | X KRW | X KRW | X KRW | X% |
| 10   | X KRW | X KRW | X KRW | X% |
| 15   | X KRW | X KRW | X KRW | X% |
| 20   | X KRW | X KRW | X KRW | X% |
| 30   | X KRW | X KRW | X KRW | X% |

**Key Insight**: [Point when compound effect becomes significant, additional gains from tax-advantaged accounts, etc.]
```

## Reference

- Past returns do not guarantee future performance
- Detailed simulation models: see `references/simulation-models.md`
