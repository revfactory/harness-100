---
name: unit-economics
description: "A specialised skill providing a Unit Economics analysis framework. Used by the revenue-modeler agent when designing revenue models and calculating LTV, CAC, and contribution margin. Automatically applied in contexts such as 'unit economics', 'LTV/CAC', 'contribution margin', 'cohort analysis', 'payback period'. However, direct CRM data extraction and real-time customer analytics are outside the scope of this skill."
---

# Unit Economics — Unit Economics Analysis Framework

A specialised skill that enhances the revenue model design capabilities of the revenue-modeler agent.

## Target Agent

- **revenue-modeler** — Revenue stream definition, unit economics, LTV/CAC analysis

## Core Unit Economics Metrics

### LTV (Customer Lifetime Value)

**Basic Formula:**
```
LTV = ARPA x Gross Margin / Monthly Churn Rate
```

**Cohort-Based LTV (More Accurate):**
```
LTV = Sum(t=1→inf) [ARPA_t x GM x Retention_t / (1+d)^t]

ARPA_t = Average revenue per account at month t (reflecting expansion/contraction)
GM = Gross Margin
Retention_t = Retention rate at month t
d = Monthly discount rate
```

**LTV Calculation Variants by Business Model:**

| Model | LTV Formula | Key Variables |
|-------|-------------|---------------|
| SaaS Subscription | ARPA x GM / Churn | Churn rate, NRR |
| E-commerce | AOV x Annual Orders x GM x Customer Lifespan | Repeat rate, AOV |
| Marketplace | GMV x Take Rate x GM x Customer Lifespan | GMV, Take Rate |
| Gaming | ARPPU x Conversion Rate x GM / Churn | ARPPU, Conversion Rate |

### CAC (Customer Acquisition Cost)

```
CAC = (Marketing Cost + Sales Cost) / New Customers

Blended CAC = Total S&M / Total New Customers
Paid CAC = Paid Channel Cost / Paid Channel New Customers
Organic CAC = Overhead Allocation / Organic New Customers
```

### CAC Payback Period

```
CAC Payback (months) = CAC / (ARPA x Gross Margin)
```

| Rating | Benchmark |
|--------|-----------|
| Excellent | < 12 months |
| Good | 12-18 months |
| Caution | 18-24 months |
| At Risk | > 24 months |

### LTV/CAC Ratio

```
LTV/CAC = LTV / CAC
```

| Ratio | Interpretation |
|-------|---------------|
| < 1x | Losing money on each customer acquired — immediate improvement needed |
| 1-3x | Not sustainable — reduce CAC or improve LTV |
| 3-5x | Healthy — can invest in growth |
| > 5x | Potentially under-investing — can grow more aggressively |

## Contribution Margin Analysis

### 3-Layer Margin Structure

```
Revenue 100%
  (-) Variable Costs (COGS, shipping, transaction fees)
  = Contribution Margin 1 (CM1) — Per-transaction profitability
  (-) Variable Marketing (performance marketing)
  = Contribution Margin 2 (CM2) — Profitability including marketing efficiency
  (-) Fixed Cost Allocation (labor, infrastructure, other)
  = Contribution Margin 3 (CM3) — Business unit profitability
```

### CM Analysis by Product/Channel/Segment

| Analysis Dimension | Purpose | Action |
|-------------------|---------|--------|
| Per-Product CM | Which products contribute to profit? | Price adjust/discontinue low-margin products |
| Per-Channel CM | Which channels are efficient? | Reallocate budget to high-efficiency channels |
| Per-Customer Segment CM | Which customers are valuable? | Focus on high-value segments |

## Cohort Analysis Framework

### Revenue Cohort Table

```markdown
| Sign-up Month | M0 | M1 | M2 | M3 | M6 | M12 |
|--------------|-----|-----|-----|-----|-----|------|
| 2024-01 | 100% | 85% | 78% | 73% | 62% | 48% |
| 2024-04 | 100% | 88% | 82% | 77% | 68% | - |
| 2024-07 | 100% | 90% | 85% | 80% | - | - |
```

### Analysis Points

1. **Retention Pattern Over Time**: Identify stabilisation point
2. **Cross-Cohort Comparison**: Are newer cohorts improving?
3. **NDR/NRR Decomposition**: Track expansion vs. contraction vs. churn separately
4. **LTV Convergence Estimation**: Estimate actual LTV from cohort data

## Bottom-Up Revenue Estimation

### Step-by-Step Estimation Formula

```
Revenue = Target Market Size (SAM)
        x Reachable Ratio
        x Conversion Rate
        x Average Order Value
        x Repeat Purchase Frequency
```

| Step | Estimation Method | Validation |
|------|------------------|------------|
| TAM | Industry reports + government statistics | Cross-check multiple sources |
| SAM | TAM x Accessible segment ratio | Clearly define actual target |
| SOM | SAM x Realistic share | Reference similar companies' initial share |

## Unit Economics Health Scorecard

| Metric | At Risk | Caution | Good | Excellent |
|--------|---------|---------|------|-----------|
| LTV/CAC | <1x | 1-3x | 3-5x | >5x |
| CAC Payback | >24M | 18-24M | 12-18M | <12M |
| Gross Margin | <40% | 40-60% | 60-75% | >75% |
| NDR | <90% | 90-100% | 100-115% | >115% |
| CM2 | Negative | 0-10% | 10-20% | >20% |

The revenue-modeler uses this scorecard to self-diagnose model health.
