---
name: sensitivity-analysis
description: "A specialised skill providing sensitivity analysis and scenario table construction methodology for financial models. Used by the scenario-planner agent when designing Bear/Base/Bull scenarios and analysing key variable impact. Automatically applied in contexts such as 'sensitivity analysis', 'scenario analysis', 'sensitivity table', 'tornado chart', 'Monte Carlo'. However, statistical software (R, Python) execution and real-time simulation are outside the scope of this skill."
---

# Sensitivity Analysis — Sensitivity Analysis Methodology

A specialised skill that enhances the scenario analysis capabilities of the scenario-planner agent.

## Target Agent

- **scenario-planner** — Bear/Base/Bull scenarios, sensitivity table construction

## 1-Way Sensitivity Analysis

Vary one variable while holding all others constant and observe changes in the result.

### Tornado Chart Construction Method

1. Select 5-8 key assumption variables
2. Vary each variable by +/-20% (or a reasonable range)
3. Calculate the variation in the result metric (enterprise value, IRR, etc.)
4. Arrange horizontal bars in descending order of variation magnitude

```
                    Enterprise Value Change
Revenue Growth  ████████████████████████   Most Sensitive
Operating Margin ██████████████████
WACC            ████████████████
Perpetual Growth █████████████
CAPEX/Revenue    ███████████
NWC/Revenue      ████████                   Least Sensitive
```

### Key Variable Selection Guide

| Financial Model Type | 1st Priority | 2nd Priority | 3rd Priority |
|---------------------|-------------|-------------|-------------|
| SaaS | Revenue Growth Rate | NRR/Churn | CAC |
| Manufacturing | Utilisation Rate | Raw Material Price | FX Rate |
| Retail | GMV Growth Rate | Take Rate | Shipping Cost |
| Biotech | Clinical Success Rate | Market Size | Drug Price |

## 2-Way Sensitivity Analysis (Data Table)

Matrix varying two variables simultaneously:

```markdown
### Enterprise Value ($M) — Revenue Growth vs WACC

|              | WACC 8% | WACC 9% | WACC 10% | WACC 11% | WACC 12% |
|-------------|---------|---------|----------|----------|----------|
| Growth 10%  |   52    |   46    |   41     |   37     |   34     |
| Growth 15%  |   68    |   59    |   52     |   46     |   41     |
| Growth 20%  |   87    |   74    |   64     |   56     |   49     |
| Growth 25%  |  109    |   91    |   78     |   67     |   59     |
| Growth 30%  |  135    |  111    |   93     |   80     |   70     |
```

**Colour Coding Rules:**
- Above current enterprise value = Green (Investment attractive)
- 80-100% of current enterprise value = Yellow (Watch)
- Below 80% of current enterprise value = Red (Warning)

## 3-Scenario Analysis (Bear/Base/Bull)

### Scenario Definition Framework

| Category | Bear (Pessimistic) | Base | Bull (Optimistic) |
|----------|-------------------|------|-------------------|
| Probability Weight | 20-25% | 50-60% | 20-25% |
| Revenue Growth | Bottom 25% benchmark | Median | Top 25% benchmark |
| Margin | Maintain or decline | Gradual improvement | Target achieved |
| Market Environment | Economic slowdown, intensified competition | Status quo | Boom, market expansion |

### Per-Scenario Key Assumptions Table

```markdown
| Assumption | Bear | Base | Bull | Basis |
|-----------|------|------|------|-------|
| Revenue Growth Y1 | 10% | 25% | 40% | Industry distribution |
| Revenue Growth Y3 | 5% | 15% | 30% | Convergence assumption |
| Operating Margin Y5 | 8% | 15% | 22% | Benchmark |
| Customer Churn | 5% | 3% | 1.5% | Peer data |
| CAPEX/Revenue | 12% | 8% | 6% | Economies of scale |
```

### Probability-Weighted Value

```
Weighted Enterprise Value = P(Bear) x V(Bear) + P(Base) x V(Base) + P(Bull) x V(Bull)
```

## Break-Even Analysis

### Key Questions

"At what level must an assumption deteriorate for the investment to fail?"

| Analysis Item | Formula | Meaning |
|-------------|---------|---------|
| Revenue BEP | Fixed Costs / Contribution Margin Ratio | Minimum required revenue |
| Customer BEP | Fixed Costs / (ARPU x Margin) | Minimum required customers |
| Growth Rate BEP | Growth rate where NPV = 0 | Minimum required growth |
| IRR BEP | Discount rate where NPV = 0 | Internal rate of return |

## Output Format Requirements

### Required Deliverables

1. **Tornado Chart** — Variable sensitivity ranking
2. **2-Way Tables** — Cross-analysis of top 2 variables (minimum 2)
3. **3-Scenario Summary** — Bear/Base/Bull key assumptions + results
4. **Probability-Weighted Value** — Final estimate
5. **Break-Even Points** — Per key variable break-even
6. **Implications** — Risk management recommendations for the most sensitive variables
