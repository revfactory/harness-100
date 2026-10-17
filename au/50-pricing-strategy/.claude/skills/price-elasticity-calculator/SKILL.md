---
name: price-elasticity-calculator
description: "A methodology for calculating price elasticity and deriving optimal pricing. Use this skill for 'price elasticity', 'demand elasticity', 'price change impact', 'optimal price derivation', 'price increase simulation', and other price change analysis needs. However, econometric model construction and real-time dynamic pricing engines are outside the scope of this skill."
---

# Price Elasticity Calculator — Price Elasticity Analysis + Optimal Pricing

A skill that enhances the pricing analysis capabilities of pricing-simulator and competitive-analyst.

## Target Agents

- **pricing-simulator** — Quantitatively analyses the impact of price change scenarios
- **competitive-analyst** — Analyses cross-price elasticity of competitor price changes

## Price Elasticity Core Formulas

### Price Elasticity of Demand (PED)

```
PED = (% Change in Quantity Demanded) / (% Change in Price)
    = (dQ/Q) / (dP/P)

Midpoint Formula (more accurate):
PED = [(Q2-Q1)/((Q1+Q2)/2)] / [(P2-P1)/((P1+P2)/2)]

Interpretation:
  |PED| > 1: Elastic — demand is sensitive to price changes
  |PED| = 1: Unit elastic — no change in revenue
  |PED| < 1: Inelastic — demand is insensitive to price changes

Example:
  10% price increase, 15% demand decrease
  PED = -15% / 10% = -1.5 (elastic)
```

### Cross-Price Elasticity (XED)

```
XED = (% Change in Own Demand) / (% Change in Competitor Price)

Interpretation:
  XED > 0: Substitute relationship (competitor price up → own demand up)
  XED < 0: Complement relationship
  XED ≈ 0: Unrelated

Example:
  Competitor price increase 20%, own demand increase 10%
  XED = 10% / 20% = 0.5 (weak substitute)
```

## Industry Elasticity Benchmarks

| Industry/Product | PED Range | Characteristics |
|-----------------|-----------|-----------------|
| SaaS (Enterprise) | -0.5 to -1.0 | Inelastic (high switching costs) |
| SaaS (Consumer) | -1.0 to -2.0 | Elastic (many alternatives) |
| E-commerce (General) | -1.5 to -2.5 | Elastic (easy price comparison) |
| E-commerce (Luxury) | -0.5 to -1.0 | Inelastic (brand loyalty) |
| Groceries (Essentials) | -0.1 to -0.5 | Very inelastic |
| Dining Out | -1.0 to -2.0 | Elastic |
| Mobile Apps | -2.0 to -3.0 | Very elastic |

## Optimal Price Derivation

### Revenue-Maximizing Price

```
Revenue R = P x Q(P)
Demand function: Q(P) = a - b*P  (linear assumption)

Optimal price P* = a / (2b)

Example:
  Q = 10,000 - 50P (monthly demand)
  P* = 10,000 / (2x50) = 100
  Q* = 10,000 - 50x100 = 5,000
  R* = 100 x 5,000 = 500,000
```

### Profit-Maximizing Price

```
Profit pi = (P - C) x Q(P)
  C = unit variable cost

Optimal price P* = (a + b*C) / (2b)

Example:
  Q = 10,000 - 50P, unit variable cost C = 30
  P* = (10,000 + 50x30) / (2x50) = 115
  Q* = 10,000 - 50x115 = 4,250
  pi* = (115-30) x 4,250 = 361,250
```

## Price Change Simulation

### Scenario Analysis Template

```
Current State:
  Price: P0 = $100
  Demand: Q0 = 5,000 units/month
  Revenue: R0 = $500,000/month
  Elasticity: PED = -1.5

Scenario 1: 10% Increase
  New Price: $110
  Demand Change: -15% → 4,250 units
  New Revenue: $467,500 (-6.5%)
  Net Profit Change: [Calculate with margin]

Scenario 2: 10% Decrease
  New Price: $90
  Demand Change: +15% → 5,750 units
  New Revenue: $517,500 (+3.5%)
  Net Profit Change: [Calculate with margin]

Scenario 3: 20% Increase + Feature Addition
  New Price: $120
  Expected Elasticity: -1.0 (dampened by increased value)
  Demand Change: -20% x (-1.0/-1.5) = -13.3%
  ...
```

### P&L Impact Analysis

```
| Item | Current | Scenario 1 | Scenario 2 | Scenario 3 |
|------|---------|-----------|-----------|-----------|
| Price | $100 | $110 | $90 | $120 |
| Demand | 5,000 | 4,250 | 5,750 | 4,333 |
| Revenue | $500K | $467.5K | $517.5K | $520K |
| Variable Cost | $150K | $127.5K | $172.5K | $130K |
| Contribution Margin | $350K | $340K | $345K | $390K |
| Fixed Cost | $200K | $200K | $200K | $220K |
| Net Profit | $150K | $140K | $145K | $170K |
```

## Price Increase Execution Strategy

```
1. Gradual Increase
   - 2-3 small increases per year (5-10%)
   - Minimize customer resistance
   - Set grace period for existing customer discounts

2. Value-Based Increase
   - Increase simultaneously with new feature launch
   - Message: "We are delivering more value"
   - Maintain existing plans + add premium plan

3. Segmented Increase
   - Apply to new customers first
   - 6-12 month grace period for existing customers
   - Separate management for price-sensitive segments

4. Discount Reduction
   - Maintain list price, reduce discount depth
   - Positioned as "discount normalization" rather than price increase
```

## Price War Response

```
Decision tree when competitor cuts price:

1. High cross-elasticity (XED > 0.5)?
   +-- Yes → High churn risk
   |   +-- Do we have cost advantage? → Price matching
   |   +-- If not → Strengthen value differentiation
   +-- No → Can ignore, maintain price

2. Is competitor's cut sustainable?
   +-- Temporary (promotion) → Ignore or limited-time promotion
   +-- Structural (cost advantage) → Compete on non-price factors
```
