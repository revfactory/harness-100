---
name: psm-analyzer
description: "A Van Westendorp PSM (Price Sensitivity Meter) methodology for price sensitivity analysis. Use this skill for 'PSM analysis', 'price sensitivity', 'Van Westendorp', 'optimal price', 'price acceptance range', 'willingness to pay analysis', and other price sensitivity research needs. However, actual survey execution and statistical software operation are outside the scope of this skill."
---

# PSM Analyser — Van Westendorp Price Sensitivity Analysis

A skill that enhances the pricing capabilities of value-assessor and pricing-simulator.

## Target Agents

- **value-assessor** — Systematically analyses WTP (willingness to pay)
- **pricing-simulator** — Incorporates PSM results into simulations

## Van Westendorp PSM 4 Core Questions

```
Q1: "At what price would you consider the product too cheap, making you question its quality?"
    → Too Cheap (TC) curve

Q2: "At what price would you consider the product a bargain — a great buy for the money?"
    → Cheap/Bargain (C) curve

Q3: "At what price would you start to feel the product is expensive?"
    → Expensive (E) curve

Q4: "At what price would you consider the product too expensive to even consider?"
    → Too Expensive (TE) curve
```

## PSM Analysis Method

### Step 1: Data Collection

```
Respondents: 50-200 target customers
Format: Specific monetary amounts for each question
Prerequisite: Sufficient product/service description provided

Data Table:
| Respondent | Too Cheap | Cheap | Expensive | Too Expensive |
|-----------|-----------|-------|-----------|---------------|
| 1         | 5         | 10    | 30        | 50            |
| 2         | 3         | 8     | 25        | 40            |
| ...       | ...       | ...   | ...       | ...           |
```

### Step 2: Cumulative Distribution Graph

```
X-axis: Price ($0 to maximum response price)
Y-axis: Cumulative percentage (0% to 100%)

TC (Too Cheap): Left-to-right cumulative (at or below percentage)
C (Cheap):      Left-to-right cumulative (at or below percentage)
E (Expensive):  Right-to-left cumulative (at or above percentage)
TE (Too Expensive): Right-to-left cumulative (at or above percentage)
```

### Step 3: Intersection Point Derivation

```
4 Key Price Points:

PMC (Point of Marginal Cheapness):
  TC (Too Cheap) ∩ E (Expensive) intersection
  → Below this price, quality suspicion begins

OPP (Optimal Price Point):
  TC (Too Cheap) ∩ TE (Too Expensive) intersection
  → Minimum purchase resistance = optimal price

IPP (Indifference Price Point):
  C (Cheap) ∩ E (Expensive) intersection
  → Equal proportion cheap/expensive = market expected price

PME (Point of Marginal Expensiveness):
  C (Cheap) ∩ TE (Too Expensive) intersection
  → Above this price, churn increases sharply

Acceptable Price Range: PMC to PME
```

## Gabor-Granger Supplementary Analysis

```
PSM Limitation: May differ from actual purchase intent

Gabor-Granger Question:
  "Would you purchase this product at [Price X]?" (Yes/No)
  → Repeat while varying price (from high to low or low to high)

Demand Curve Derivation:
  "Yes" percentage by price → Demand curve
  Revenue-maximizing price = Price x Purchase intent rate at maximum point

| Price  | Purchase Intent | Expected Revenue (per 100 people) |
|--------|----------------|----------------------------------|
| $10    | 90%            | $900                             |
| $20    | 70%            | $1,400 ← Maximum                |
| $30    | 40%            | $1,200                           |
| $40    | 15%            | $600                             |
```

## Segment-Based PSM Analysis

```
Segment Classification Criteria:
  1. Company Size (SMB / Mid-Market / Enterprise)
  2. Use Case (Personal / Professional / Team)
  3. Existing Solution (New / Switching)
  4. Price Sensitivity Level (Low / High)

OPP Comparison by Segment:
| Segment    | PMC  | OPP  | IPP  | PME  |
|-----------|------|------|------|------|
| SMB       | $50  | $80  | $100 | $150 |
| Enterprise| $200 | $350 | $500 | $800 |

→ Basis for segment-based price differentiation
```

## Pricing Structure Design Integration

```
PSM Results → Plan Design:

1. Free/Freemium: Below PMC
   → Quality-suspect price = remove entry barrier with free

2. Starter: PMC to OPP
   → Minimum price to optimal price

3. Professional: OPP to IPP
   → Optimal to market expected price

4. Enterprise: IPP to PME
   → Market expected to maximum acceptable price
   → Justified by additional value (support, SLA, customization)
```

## PSM Report Template

```markdown
## Price Sensitivity Analysis (PSM)

### Survey Overview
- Target: [Target customer description]
- Respondents: [N] people
- Survey Period: [Period]

### Key Price Points
| Point | Price | Meaning |
|-------|-------|---------|
| PMC | [$] | Minimum acceptable price |
| OPP | [$] | Optimal price |
| IPP | [$] | Market expected price |
| PME | [$] | Maximum acceptable price |

### Acceptable Price Range: [PMC] to [PME]
### Recommended Price: [OPP-based recommendation]

### Segment Analysis
[Segment-specific table]

### Pricing Structure Recommendation
[Plan-specific price proposals]
```
