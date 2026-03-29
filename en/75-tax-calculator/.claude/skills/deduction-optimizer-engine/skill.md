---
name: deduction-optimizer-engine
description: "A deduction optimization engine that maximizes income deductions and tax credits through optimal combinations. The 'deduction-optimizer' agent must use this skill's deduction limit tables, priority algorithms, and simulation methods when analyzing deduction items and deriving optimal combinations. Used for 'deduction optimization', 'tax credit maximization', 'year-end tax settlement simulation', etc. However, income classification and tax calculation are outside the scope of this skill."
---

# Deduction Optimizer Engine

Provides limits, requirements, and optimal combination strategies for income deductions and tax credits.

## Income Deduction Item Framework (Based on Employment Income)

### Personal Deductions

| Category | Deduction Amount | Requirements |
|------|--------|------|
| Basic deduction (self) | 1,500,000 KRW | Unconditional |
| Basic deduction (spouse) | 1,500,000 KRW | Annual income 1,000,000 KRW or less |
| Basic deduction (lineal ascendants) | 1,500,000 KRW/person | Age 60+, annual income 1,000,000 KRW or less |
| Basic deduction (lineal descendants) | 1,500,000 KRW/person | Age 20 or under, or disabled |
| Additional deduction (senior citizen) | 1,000,000 KRW/person | Age 70 or older |
| Additional deduction (disabled) | 2,000,000 KRW/person | Registered disability |
| Additional deduction (working woman) | 500,000 KRW | Female with aggregate income 30,000,000 KRW or less |
| Additional deduction (single parent) | 1,000,000 KRW | Children on basic deduction with no spouse |

### Special Income Deductions

| Item | Deduction Limit | Notes |
|------|----------|------|
| National pension | Full amount | Employee contribution |
| Health insurance | Full amount | Employee contribution |
| Employment insurance | Full amount | Employee contribution |
| Housing rental loan | 4,000,000 KRW/year | Head of household with no home |
| Long-term home mortgage | 3,000,000–18,000,000 KRW/year | Varies by repayment period |

### Other Income Deductions

| Item | Deduction Rate | Limit | Requirements |
|------|--------|------|------|
| Credit cards, etc. | 15–40% | Based on total salary | Amount exceeding 25% of total salary |
| Home savings | 40% | 2,400,000 KRW | Total salary 70,000,000 KRW or less |
| Small business deduction | Full amount | 3,000,000 KRW | Business owners |
| Employee stock ownership contribution | Full amount | 4,000,000 KRW | — |

## Tax Credit Item Framework

### Major Tax Credits

| Item | Credit Rate | Limit | Requirements |
|------|--------|------|------|
| Pension savings | 12–15% | Contributions up to 6,000,000 KRW | Based on total salary of 55,000,000 KRW |
| IRP (retirement pension) | 12–15% | Combined with pension savings up to 9,000,000 KRW | Based on total salary of 55,000,000 KRW |
| Insurance premiums | 12% | 1,000,000 KRW (general), 1,500,000 KRW (disabled) | Insurance for basic deduction subjects |
| Medical expenses | 15–20% | No limit (infertility treatment, etc.) | Amount exceeding 3% of total salary |
| Education expenses | 15% | No limit for self, 3,000,000 KRW per child | — |
| Donations | 15–30% | Income limit | Varies by type |
| Monthly rent | 15–17% | 7,500,000 KRW | Total salary 70,000,000 KRW or less |
| Child tax credit | Fixed amount | 1 child: 150,000; 2 children: 350,000; 3+ children: 350,000 + 300,000 × additional | — |

### Tax Credit Rate Breakdown (Based on Total Salary)

```
Pension savings / IRP tax credit rate:
  Total salary 55,000,000 KRW or less: 15%
  Total salary above 55,000,000 KRW: 12%

Maximum tax credit:
  Pension savings 6,000,000 KRW × 15% = 900,000 KRW
  Including IRP 9,000,000 KRW × 15% = 1,350,000 KRW
```

## Deduction Optimization Algorithm

### Priority Determination Formula

```
Deduction Efficiency = Actual Tax Reduction / Required Expenditure

Income deduction actual reduction: Deduction amount × marginal tax rate
Tax credit actual reduction: Deduction amount × credit rate (direct offset)

Priority:
1. Tax credits (direct tax reduction) > Income deductions (indirect reduction)
2. High credit rate items > Low credit rate items
3. Items below limit > Items at limit
4. Items with mandatory spending > Items requiring additional spending
```

### Optimization Simulation Steps

```
Step 1: Apply unconditional deductions (personal deductions, social insurance)
Step 2: Maximize pension savings/IRP tax credits (highest ROI)
Step 3: Optimize allocation of credit card usage deductions
Step 4: Verify medical and education expense tax credits
Step 5: Verify monthly rent and housing fund deductions
Step 6: Verify donation deductions
Step 7: Readjust items exceeding or falling short of limits
```

### Credit Card Deduction Optimization

```
Deduction rate differences:
  Credit card: 15%
  Check card / cash receipts: 30%
  Traditional markets: 40%
  Public transportation: 40%
  Books and performances: 30%

Optimal strategy:
  1. Up to 25% of total salary → Credit card (maximize card benefits)
  2. Amount exceeding 25% → Check card / cash receipts (2x deduction rate)
  3. Traditional markets / public transportation → Utilize additional limits
```

## Deduction Effect by Tax Bracket

| Taxable Income | Tax Rate | Effect of 1,000,000 KRW Income Deduction | Notes |
|---------|------|-------------------|------|
| Up to 14,000,000 | 6% | 60,000 KRW savings | Low deduction effect |
| Up to 50,000,000 | 15% | 150,000 KRW savings | |
| Up to 88,000,000 | 24% | 240,000 KRW savings | |
| Up to 150,000,000 | 35% | 350,000 KRW savings | |
| Up to 300,000,000 | 38% | 380,000 KRW savings | High deduction effect |
| Up to 500,000,000 | 40% | 400,000 KRW savings | |
| Up to 1,000,000,000 | 42% | 420,000 KRW savings | |
| Over 1,000,000,000 | 45% | 450,000 KRW savings | |

## Notes

- Based on the Income Tax Act and Restriction of Special Taxation Act (must verify annual amendments)
- Detailed deduction requirements: refer to `references/deduction-details.md`
