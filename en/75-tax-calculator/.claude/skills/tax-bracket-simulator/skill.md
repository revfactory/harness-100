---
name: tax-bracket-simulator
description: "A tax bracket analyzer that simulates tax liability by bracket and identifies tax-saving points. The 'tax-engine' and 'strategy-advisor' agents must use this skill's tax rate tables, calculation formulas, and bracket analysis methods when computing taxes and building tax-saving strategies. Use for 'tax bracket analysis', 'tax liability simulation', 'marginal rate calculation', etc. Note: deduction optimization and income classification are outside the scope of this skill."
---

# Tax Bracket Simulator

Income tax calculation by bracket, marginal rate analysis, and tax-saving point identification.

## Comprehensive Income Tax Rate Table

### 2024 Tax Rates

| Taxable Income Bracket | Rate | Progressive Deduction | Bracket Tax |
|------------------------|------|-----------------------|-------------|
| ~14,000,000 KRW | 6% | 0 | Max 840,000 KRW |
| 14,000,000~50,000,000 KRW | 15% | 1,260,000 KRW | Max 5,400,000 KRW |
| 50,000,000~88,000,000 KRW | 24% | 5,760,000 KRW | Max 9,120,000 KRW |
| 88,000,000~150,000,000 KRW | 35% | 15,440,000 KRW | Max 21,700,000 KRW |
| 150,000,000~300,000,000 KRW | 38% | 19,940,000 KRW | Max 57,000,000 KRW |
| 300,000,000~500,000,000 KRW | 40% | 25,940,000 KRW | Max 80,000,000 KRW |
| 500,000,000~1,000,000,000 KRW | 42% | 35,940,000 KRW | Max 210,000,000 KRW |
| Over 1,000,000,000 KRW | 45% | 65,940,000 KRW | - |

### Quick Tax Calculation Formula

```
Calculated Tax = Taxable Income × Rate - Progressive Deduction

Example: Taxable Income 60,000,000 KRW
  = 60,000,000 × 24% - 5,760,000 = 14,400,000 - 5,760,000 = 8,640,000 KRW

Effective Tax Rate = Calculated Tax / Taxable Income × 100
  = 8,640,000 / 60,000,000 × 100 = 14.4%
```

## Bracket Boundary Analysis

### Bracket Boundary Tax-Saving Points

```
Key Principle: When taxable income enters the next bracket, the higher rate applies only to the excess amount

Tax-Saving Point = Bracket Boundary - Current Taxable Income

Example: Taxable Income 51,000,000 KRW
  - 24% applied to 1,000,000 KRW exceeding 50,000,000 KRW
  - With an additional 1,000,000 KRW income deduction → 240,000 KRW → 150,000 KRW (save 90,000 KRW)
  - Tax-saving effect: 90,000 KRW additional savings per 1,000,000 KRW income deduction
```

### Key Bracket Boundary Strategies

| Boundary | Rate Jump | Strategy |
|----------|-----------|----------|
| 14,000,000 KRW | 6%→15% | Review deductions for low-income earners |
| 50,000,000 KRW | 15%→24% | Maximize pension savings and IRP contributions |
| 88,000,000 KRW | 24%→35% | Focus on high-value deduction items |
| 150,000,000 KRW | 35%→38% | Consider income splitting, corporate conversion |
| 300,000,000 KRW | 38%→40% | Establish corporation, utilize retirement funds |

## Tax Calculation by Income Type

### Employment Income

```
Gross Salary
- Employment Income Deduction = Employment Income Amount
- Income Deductions = Taxable Income
× Rate - Progressive Deduction = Calculated Tax
- Tax Credits = Determined Tax
- Pre-paid Tax (Withholding) = Tax Payable / Refund

Employment Income Deduction:
  ~5,000,000: 70%
  5,000,000~15,000,000: 3,500,000 + excess × 40%
  15,000,000~45,000,000: 7,500,000 + excess × 15%
  45,000,000~100,000,000: 12,000,000 + excess × 5%
  Over 100,000,000: 14,750,000 + excess × 2%
```

### Business Income

```
Gross Revenue
- Necessary Expenses = Business Income Amount

Expense Recognition Methods:
  1. Bookkeeping: Actual expenses recognized (standard expense ratio applied)
  2. Estimated Filing: Simple expense ratio / Standard expense ratio

Simple Expense Ratio Eligibility (by industry):
  - Manufacturing: Prior revenue under 150,000,000 KRW
  - Service industry: Prior revenue under 75,000,000 KRW
  - Real estate rental: Prior revenue under 75,000,000 KRW
```

### Capital Gains Tax

```
Transfer Price - Acquisition Price - Necessary Expenses = Capital Gain
- Long-term Holding Special Deduction = Capital Gains Amount
- Basic Capital Gains Deduction (2,500,000 KRW) = Taxable Income
× Rate = Capital Gains Tax

Real Estate Tax Rates:
  Held less than 1 year: 70%
  Held 1~2 years: 60%
  Held 2+ years: Basic rate (6-45%)
  Multi-home surcharge: Basic rate + 20~30%p

Long-term Holding Special Deduction:
  3+ years: 2% per year (max 30%)
  1-household 1-home: 4% per year (holding) + 4% per year (occupancy) (max 80%)
```

## Simulation Comparison Output Format

```markdown
## Tax Simulation Comparison

| Item | Current | Scenario A | Scenario B |
|------|---------|------------|------------|
| Total Income | X KRW | X KRW | X KRW |
| Total Income Deductions | X KRW | X KRW | X KRW |
| Taxable Income | X KRW | X KRW | X KRW |
| Marginal Tax Rate | X% | X% | X% |
| Calculated Tax | X KRW | X KRW | X KRW |
| Total Tax Credits | X KRW | X KRW | X KRW |
| Determined Tax | X KRW | X KRW | X KRW |
| Effective Tax Rate | X% | X% | X% |
| **Tax Savings Effect** | Baseline | X KRW ↓ | X KRW ↓ |
```

## References

- Income Tax Act Article 55, Special Tax Treatment Control Act
- Detailed tax rate history: see `references/tax-rate-history.md`
