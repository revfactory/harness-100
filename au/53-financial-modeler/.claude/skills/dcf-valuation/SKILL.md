---
name: dcf-valuation
description: "A specialised skill providing detailed DCF (Discounted Cash Flow) valuation methodology and practical guidelines. Used by the valuation-expert agent for WACC calculation, FCF estimation, and terminal value computation when calculating enterprise value. Automatically applied in contexts such as 'DCF analysis', 'discounted cash flow', 'WACC calculation', 'enterprise valuation', 'terminal value'. However, real-time market data retrieval and actual transaction advisory are outside the scope of this skill."
---

# DCF Valuation — Discounted Cash Flow Valuation Methodology

A specialised skill that enhances the DCF analysis capabilities of the valuation-expert agent.

## Target Agent

- **valuation-expert** — DCF model construction, WACC calculation, terminal value computation

## DCF Model Construction Process

### Step 1: FCFF (Free Cash Flow to Firm) Estimation

```
FCFF = EBIT x (1 - Tax Rate)
     + Depreciation & Amortization
     - Capital Expenditures (CAPEX)
     - Change in Net Working Capital (dNWC)
```

| Item | Estimation Method | Key Considerations |
|------|------------------|---------------------|
| EBIT | Revenue x Operating Margin estimate | Use normalised EBIT |
| Tax Rate | Effective or statutory rate | Consider deferred tax |
| D&A | Tangible Assets x Depreciation Rate | Verify balance with CAPEX |
| CAPEX | Maintenance CAPEX + Growth CAPEX | Validate ratio vs. D&A |
| dNWC | NWC as % of Revenue | Cash outflow with revenue growth |

### Step 2: WACC (Weighted Average Cost of Capital) Calculation

```
WACC = E/(E+D) x Ke + D/(E+D) x Kd x (1-T)
```

| Variable | Calculation Method | Reference Values |
|----------|-------------------|-----------------|
| Ke (Cost of Equity) | CAPM = Rf + B x MRP + SP | 10-15% |
| Rf (Risk-Free Rate) | 10-year government bond yield | 3-4% |
| MRP (Market Risk Premium) | Equity Risk Premium | 5-7% |
| B (Beta) | Peer Unlevered B average → Re-lever | 0.8-1.5 |
| SP (Size Premium) | Market cap based | Startups 3-5% |
| Kd (Cost of Debt) | Weighted average borrowing rate | 4-6% |
| T (Tax Rate) | Effective tax rate | 20-25% |

### CAPM Beta Calculation Process

```
1. Select 5+ comparable companies
2. Collect each company's Levered Beta
3. Calculate Unlevered Beta: BU = BL / [1 + (1-T) x D/E]
4. Calculate average Unlevered Beta of comparables
5. Re-lever for target company's capital structure: BL = BU x [1 + (1-T) x D/E]
```

### Step 3: Terminal Value

**Method 1: Perpetuity Growth Model (Gordon Growth)**
```
TV = FCFFn+1 / (WACC - g)
   = FCFFn x (1+g) / (WACC - g)
```

| Variable | Standard | Caution |
|----------|---------|---------|
| g (Perpetual Growth Rate) | At or below GDP growth (1.5-3%) | Model invalid if g > WACC |
| FCFFn | Last forecast year FCF | Must be at normalised level |

**Method 2: Exit Multiple**
```
TV = EBITDAn x Exit Multiple
```

| Industry | Typical EV/EBITDA Range |
|---------|------------------------|
| SaaS | 15-30x |
| Manufacturing | 6-10x |
| Retail | 8-12x |
| Financial Services | 8-12x |
| Biotech | 20-40x (pipeline value) |

### Step 4: Enterprise Value Calculation

```
Enterprise Value = Sum(FCFFt / (1+WACC)^t) + TV / (1+WACC)^n
Equity Value = EV - Net Debt - Preferred Stock - Minority Interest
Per-Share Value = Equity Value / Shares Outstanding
```

## DCF Quality Validation Checklist

- [ ] Is terminal value within 60-75% of total value? (Warning if exceeded)
- [ ] Is perpetual growth rate at or below GDP growth?
- [ ] Is the beta used in WACC calculation reasonable?
- [ ] Is FCF projection consistent with historical trends?
- [ ] Is D&A approximately equal to maintenance CAPEX? (for mature companies)
- [ ] Does revenue growth rate gradually converge?
- [ ] Does operating margin converge to industry average?

## Startup/High-Growth Company DCF Adjustments

| Issue | Solution |
|-------|----------|
| Negative cash flows | Explicitly state breakeven timing, model cash burn until then |
| High growth rates | 2-stage model (high growth period + stable growth period) |
| Beta not estimable | Use comparable public company beta, or directly apply VC discount rate (25-35%) |
| Insufficient market data | Parallel VC Method, Berkus Method |

## Multiples Valuation (Cross-check)

| Multiple | Applicable To | Calculation |
|---------|--------------|-------------|
| EV/Revenue (PSR) | Early SaaS, high growth | EV / Annual Revenue (NTM) |
| EV/EBITDA | Profitable companies | EV / EBITDA (NTM) |
| P/E | Public companies | Stock Price / EPS |
| EV/ARR | SaaS | EV / ARR |

Always cross-validate DCF results with multiples valuation.
