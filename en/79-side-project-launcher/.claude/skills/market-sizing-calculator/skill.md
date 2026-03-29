---
name: market-sizing-calculator
description: "A market sizing calculator for estimating a side project's market scale and validating its revenue model. The 'idea-validator' agent must use this skill's TAM/SAM/SOM framework, revenue model calculations, and competitive analysis matrix when validating the market viability of an idea. Use for 'market size estimation', 'revenue model validation', 'competitive analysis', and similar requests. However, tech stack selection and MVP design are outside the scope of this skill."
---

# Market Sizing Calculator — Market Size Calculator

Quantitatively estimates a side project's market opportunity and validates revenue potential.

## TAM/SAM/SOM Framework

### Definitions and Calculation Methods

```
TAM (Total Addressable Market): Total market size
  → Total potential customers with the problem × Annual spend intent

SAM (Serviceable Addressable Market): Accessible market
  → TAM × Geographic / language / platform constraint filters

SOM (Serviceable Obtainable Market): Realistically obtainable market
  → SAM × Realistic market share (1-person side project: 0.1–1%)
```

### Top-Down Method

```
Example: Developer interview preparation web app

TAM: 27 million software developers worldwide × $50/year spend intent
   = $1.35 billion

SAM: Korean language users (approx. 500,000 Korean developers) × $50
   = $25 million

SOM: 1% market share achievable (1-person operation)
   = $250,000 (approx. 330,000,000 KRW/year)
```

### Bottom-Up Method

```
Example: Developer interview preparation web app

Expected monthly paid conversions:
  Blog/SNS → Visitors: 10,000/month
  Sign-up conversion: 10% = 1,000 users
  Paid conversion: 5% = 50 users
  Monthly subscription: 9,900 KRW

MRR = 50 × 9,900 = 495,000 KRW
ARR = 5,940,000 KRW

Growth scenario (after 12 months):
  3× visitors → MRR 1,500,000 KRW → ARR 18,000,000 KRW
```

## Revenue Model Calculations by Type

### Subscription Model (SaaS)

```
Core metrics:
  MRR = Paid users × Monthly subscription price
  ARR = MRR × 12
  LTV = ARPU / Churn rate
  CAC = Marketing cost / New paid subscribers

Health benchmarks:
  LTV/CAC > 3 (good)
  Churn rate < 5%/month (good)
  Payback period < 12 months

Example:
  100 users × 9,900 KRW/month = MRR 990,000 KRW
  Monthly churn 5% → Average lifetime 20 months
  LTV = 9,900 × 20 = 198,000 KRW
  Ad CAC 30,000 KRW → LTV/CAC = 6.6 ✅
```

### Freemium Model

```
Free users → Paid conversion rate: 2–5% (typical)
Premium price: Feature differentiation vs. free tier

Example:
  Free: 10,000 users → Paid conversion 3% = 300 users
  Monthly 19,900 KRW → MRR 5,970,000 KRW
```

### One-Time Purchase

```
Expected sales = Exposure × Conversion rate

Example (digital product):
  Blog monthly visits 10,000 × purchase conversion 1% = 100 sales
  Price 29,000 KRW → Monthly 2,900,000 KRW
```

## Competitive Analysis Matrix

### Positioning Map

```
Price
  High ┌─────────┐
       │ [Comp B] │ [?Opportunity]
       │          │
       │          │
  Low  │ [Comp A] │ [Us]
       └─────────┘
       Low      High
         Features/Differentiation
```

### Competitive Comparison Table

```markdown
| Item | Us | Competitor A | Competitor B | Competitor C |
|------|----|-------------|-------------|-------------|
| Price | Free/9.9k KRW | Free | $19/month | Free |
| Core Feature 1 | ✅ | ✅ | ✅ | ❌ |
| Core Feature 2 | ✅ | ❌ | ✅ | ✅ |
| Differentiating Feature | ✅ | ❌ | ❌ | ❌ |
| Korean Language Support | ✅ | ❌ | ❌ | ✅ |
| Mobile | ✅ | ❌ | ✅ | ❌ |
```

## Side Project Revenue Viability Score

```
Viability = (market_size × 0.2) + (differentiation × 0.25) + (execution_feasibility × 0.3) + (revenue_model × 0.25)

Market size:   SOM > 100M KRW: 5, 50M+: 4, 10M+: 3, below: 2
Differentiation: Unique: 5, Strong: 4, Moderate: 3, Weak: 2, None: 1
Execution feasibility: Skills + ample time: 5, Learning needed: 3, Difficult: 1
Revenue model: Validated: 5, Similar precedents: 4, Experimental: 3, Uncertain: 2

Grade scale:
  4.0+:   🟢 Promising — proceed immediately
  3.0–3.9: 🟡 Review — validate with MVP
  2.0–2.9: 🟠 Reconsider — consider pivot
  below 2.0: 🔴 At Risk — re-explore idea
```

## Reference

- Use realistic figures appropriate for side project scale
- Detailed market analysis: see `references/market-analysis-guide.md`
