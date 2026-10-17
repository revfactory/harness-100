---
name: cap-rate-calculator
description: "Real estate yield calculator. Reference formulas and models used by the profitability-analyst agent for quantitative investment return analysis. Use for requests involving 'Cap Rate', 'yield analysis', 'DCF', or 'cash flow analysis'. Tax advisory and loan underwriting are out of scope."
---

# Cap Rate Calculator — Real Estate Yield Calculator

Enhances the profitability-analyst agent's investment return analysis capabilities.

## Core Yield Metrics

### Cap Rate (Capitalisation Rate)

```
Cap Rate = NOI / Purchase Price x 100

NOI (Net Operating Income) = Total Rental Income - Operating Expenses
Operating Expenses = Management Fees + Maintenance + Insurance + Taxes + Vacancy Loss

Example:
  Purchase Price: $1,000,000
  Annual Rental Income: $72,000 ($6,000/month)
  Operating Expenses: $12,000
  NOI: $60,000
  Cap Rate: 60,000 / 1,000,000 x 100 = 6.0%
```

### Cap Rate Benchmarks

| Property Type | Cap Rate Range | Risk |
|--------------|---------------|------|
| Office (Prime) | 3.5-4.5% | Low |
| Office (Other) | 4.5-6.0% | Medium |
| Retail (Commercial) | 4.0-7.0% | Medium |
| Residential (Apartment) | 2.0-4.0% | Low |
| Logistics/Warehouse | 5.0-7.0% | Medium |
| Studio/Serviced Apartment | 3.5-5.5% | Medium |

### Rental Yield (Gross Yield vs Net Yield)

```
Gross Yield = Annual Gross Rental Income / Purchase Price x 100
Net Yield = NOI / Purchase Price x 100

Typically Net Yield = Gross Yield x 0.7-0.85
(Operating expense ratio 15-30%)
```

## Cash Flow Analysis

### Leveraged Return

```
Cash-on-Cash Return = Pre-Tax Cash Flow / Equity x 100

Pre-Tax Cash Flow = NOI - Annual Debt Service

Example:
  Purchase Price: $1,000,000 (LTV 60% = Loan $600,000)
  Equity: $400,000
  NOI: $60,000
  Annual Debt Service: $36,000 (3.5%, 30 years)
  Pre-Tax Cash Flow: $24,000
  Cash-on-Cash: 24,000 / 400,000 x 100 = 6.0%
```

### Monthly Cash Flow Template

| Item | Monthly | Annual |
|------|---------|--------|
| (+) Rental Income | $6,000 | $72,000 |
| (-) Vacancy Loss (5%) | -$300 | -$3,600 |
| (-) Management Fees | -$500 | -$6,000 |
| (-) Maintenance & Repairs | -$200 | -$2,400 |
| (-) Insurance | -$50 | -$600 |
| (-) Property Tax | -$150 | -$1,800 |
| **(=) NOI** | **$4,800** | **$57,600** |
| (-) Debt Service | -$3,000 | -$36,000 |
| **(=) Pre-Tax Cash Flow** | **$1,800** | **$21,600** |

## DCF (Discounted Cash Flow)

```
Property Value = Sum of [NOI_t / (1+r)^t] + Terminal Value / (1+r)^n

Terminal Value = NOI_{n+1} / Exit Cap Rate

Variables:
  r: Discount rate (typically 8-12%)
  n: Holding period (typically 5-10 years)
  Exit Cap Rate: Cap Rate at sale (typically +0.5% premium)

NOI Growth Rate Assumptions:
  Conservative: 1-2% per year (inflation rate)
  Baseline: 2-3% per year (rent escalation)
  Optimistic: 3-5% per year (area growth)
```

## Investment Scenario Analysis

### Scenario Template

| Item | Conservative | Baseline | Optimistic |
|------|-------------|----------|------------|
| Purchase Price | $1,000,000 | $1,000,000 | $1,000,000 |
| Initial Rent | $5,500/month | $6,000/month | $6,500/month |
| Vacancy Rate | 10% | 5% | 3% |
| Rent Escalation | 1%/year | 3%/year | 5%/year |
| Sale Price After 5 Years | $1,050,000 | $1,200,000 | $1,400,000 |
| **5-Year Total Return** | **18%** | **42%** | **68%** |
| **Annualized Return** | **3.4%** | **7.3%** | **10.9%** |

## Investment Decision Criteria

| Metric | Attractive | Hold | Reject |
|--------|-----------|------|--------|
| Cap Rate | > 5% | 3-5% | < 3% |
| Cash-on-Cash | > 8% | 5-8% | < 5% |
| IRR | > 12% | 8-12% | < 8% |
| Payback | < 8 years | 8-12 years | > 12 years |
| DSCR | > 1.3 | 1.1-1.3 | < 1.1 |

## Quality Checklist

| Item | Criteria |
|------|----------|
| Yield Metrics | Cap Rate + Cash-on-Cash + IRR |
| NOI Accuracy | Itemised operating expense calculation |
| Leverage | Loan terms reflected |
| Scenarios | Conservative/Baseline/Optimistic (3 scenarios) |
| Benchmarking | Comparable property comparison |
| Exit Strategy | Exit Cap Rate assumption |
