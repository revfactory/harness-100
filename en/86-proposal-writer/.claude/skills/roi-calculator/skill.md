---
name: roi-calculator
description: "ROI calculation framework. Referenced by the pricing-strategist and solution-architect agents when quantifying return on investment for a proposal. Use when 'ROI calculation', 'cost-benefit analysis', or 'TCO' is requested. Note: financial auditing and tax consulting are outside this skill's scope."
---

# ROI Calculator — ROI Calculation Framework

Standardizes investment return analysis for the pricing-strategist and solution-architect agents.

## Basic ROI Formula

```
ROI = (Net Profit / Total Investment Cost) × 100

Net Profit = Total Revenue (Benefits) - Total Costs
Total Investment Cost = Initial Investment + Operating Costs
```

## TCO (Total Cost of Ownership) Analysis

### Cost Categories

| Category | Items | Calculation Basis |
|----------|-------|------------------|
| Initial investment | Licensing, hardware, implementation | One-time |
| Implementation costs | Consulting, customization, training | Project duration |
| Operating costs | Maintenance, labor, infrastructure | Annual |
| Hidden costs | Productivity loss, opportunity cost, risk | Estimated |

### TCO Comparison Template

| Cost Item | Current (AS-IS) | Proposed (TO-BE) | Difference |
|-----------|----------------|-----------------|-----------|
| Initial investment | $0 | $500K | +$500K |
| Annual operating cost | $300K | $100K | -$200K |
| 3-year TCO | $900K | $800K | -$100K |
| 5-year TCO | $1,500K | $1,000K | -$500K |

## Payback Period

```
Simple Payback Period = Initial Investment / Annual Net Cash Flow

Example:
  Initial Investment: $500K
  Annual Savings: $200K
  Payback = $500K / $200K = 2.5 years
```

## NPV (Net Present Value)

```
NPV = Σ [CF_t / (1+r)^t] - Initial Investment

CF_t = Net cash flow in year t
r    = Discount rate (typically WACC or target rate of return)
t    = Year number (1 to N)

Decision rule:
  NPV > 0 → Investment is worthwhile
  NPV < 0 → Reject the investment
```

### NPV Calculation Template

| Year | Cash Flow | Discount Factor (10%) | Present Value |
|------|----------|----------------------|--------------|
| 0 | -$500K | 1.000 | -$500K |
| 1 | $150K | 0.909 | $136K |
| 2 | $200K | 0.826 | $165K |
| 3 | $250K | 0.751 | $188K |
| 4 | $250K | 0.683 | $171K |
| 5 | $250K | 0.621 | $155K |
| **NPV** | | | **$315K** |

## IRR (Internal Rate of Return)

```
IRR = The discount rate at which NPV = 0

Decision rule:
  IRR > WACC → Investment is worthwhile
  IRR > target rate of return → Investment is attractive

How to present:
  "This investment's IRR is 28%, which substantially
   exceeds our required return of 15%."
```

## Quantifying Qualitative Benefits

### Calculation Methods by Benefit Type

| Benefit Type | Calculation Method | Example |
|-------------|-------------------|---------|
| Time savings | Hours saved × hourly rate × annual occurrences | 20h × $50 × 50 = $50K |
| Error reduction | Errors reduced × cost per error | 100 errors × $500 = $50K |
| Productivity gain | Volume increase × revenue per unit | +200 units × $100 = $20K |
| Reduced turnover | Employees retained × hiring cost | 5 people × $20K = $100K |
| Customer satisfaction | NPS improvement → repurchase rate → revenue | Indirect estimate |

## Scenario Analysis

| Scenario | Assumptions | ROI | Payback |
|----------|------------|-----|---------|
| Conservative (Pessimistic) | 50% benefits, 120% costs | 85% | 3.2 years |
| Base Case | 100% benefits, 100% costs | 180% | 2.1 years |
| Optimistic | 130% benefits, 90% costs | 290% | 1.4 years |

**Proposal recommendation**: The investment case must be compelling even under the conservative scenario.

## ROI Presentation Guide for Proposals

### One-Page ROI Summary

```
┌──────────────────────────────┐
│  Investment Summary           │
│  Total Investment: $500K      │
│  3-Year ROI: 180%             │
│  Payback Period: 2.1 years    │
│  NPV: $315K (10% discount)    │
│                               │
│  Top 3 Benefits:              │
│  1. Operating savings: $200K/yr│
│  2. Productivity gain: $80K/yr │
│  3. Error cost reduction: $50K/yr│
└──────────────────────────────┘
```

## Quality Checklist

| Item | Standard |
|------|---------|
| Cost completeness | All 4 TCO categories covered |
| Benefit basis | Calculation logic stated for each benefit |
| Scenarios | Conservative / Base / Optimistic — 3 scenarios |
| Discount rate | Basis stated (WACC, etc.) |
| Time horizon | Minimum 3 years; 5 years recommended |
| Risk | Sensitivity analysis on key assumptions |
