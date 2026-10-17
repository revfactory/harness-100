---
name: patent-valuation
description: "Patent valuation framework. Referenced by the ip-analyst and license-strategist agents when calculating the economic value of IP assets. Use for 'patent value', 'IP valuation', or 'royalty calculation' requests. Legal patent infringement assessment and litigation representation are out of scope."
---

# Patent Valuation — Patent Value Assessment

Enhances the IP valuation capabilities of the ip-analyst and license-strategist agents.

## Valuation Methodologies

### Three Approaches

| Approach | Method | Best Suited For |
|----------|--------|----------------|
| Cost Approach | Cost of development/acquisition | Early-stage, no alternative technology |
| Market Approach | Comparable IP transaction data | Comparable transactions exist |
| Income Approach | Present value of future income | Clear monetisation pathway |

### Cost Approach

```
Reproduction Cost:
  = R&D Labor + Materials + Equipment + Overhead
  + Opportunity Cost (time value)
  - Depreciation (functional/economic obsolescence)

Example:
  R&D Cost: $500,000
  Overhead: $100,000
  Obsolescence Depreciation: -20%
  Value: (500,000 + 100,000) x 0.8 = $480,000
```

### Market Approach

```
Comparable Transaction Comparison:
  Value = Comparable IP Transaction Price x Adjustment Factor

Adjustment Factors:
  - Technology similarity (0.5-1.5)
  - Market size ratio
  - Remaining protection period ratio
  - Rights scope (exclusive/non-exclusive)
```

### Income Approach (Relief from Royalty)

```
Value = Sum of [Revenue_t x Royalty Rate x (1-Tax Rate) / (1+r)^t]

t: Remaining patent term (1 to N years)
r: Discount rate (WACC basis, 12-20%)
Royalty Rate: Industry-specific benchmark (see below)
```

## Industry Royalty Benchmarks

| Industry | Royalty Rate Range | Median |
|----------|-------------------|--------|
| Pharmaceutical/Biotech | 3-10% | 5% |
| Semiconductor/Electronics | 1-5% | 3% |
| Software | 5-25% | 10% |
| Chemical/Materials | 2-5% | 3% |
| Machinery/Equipment | 1-5% | 3% |
| Consumer Goods | 2-8% | 4% |
| Automotive | 1-3% | 2% |

## 25% Rule (Rule of Thumb)

```
Royalty = Licensee Operating Profit x 25%

Rationale: 25% of patent-contributed profit goes to the patent holder
Caveat: Courts use this only as a reference, not an absolute standard
```

## Patent Strength Assessment

### Patent Scorecard

| Evaluation Item | Weight | Score (1-5) |
|----------------|--------|------------|
| Claim Scope | 20% | Broader = higher |
| Design-Around Difficulty | 20% | More difficult = higher |
| Technical Importance | 15% | More critical = higher |
| Citation Frequency | 15% | More cited = higher |
| Remaining Term | 15% | Longer = higher |
| Market Relevance | 15% | Greater applicability = higher |

### Strength Ratings

| Total Score | Rating | Strategy |
|------------|--------|----------|
| 4.0-5.0 | A (Core) | Active protection, licensing monetisation |
| 3.0-3.9 | B (Important) | Retain, portfolio strengthening |
| 2.0-2.9 | C (Moderate) | Cost-efficiency review, sale consideration |
| 1.0-1.9 | D (Weak) | Abandonment/sale recommended |

## License Structure Design

### License Types

| Type | Description | Royalty Structure |
|------|------------|-----------------|
| Exclusive | Only licensee may practice | High upfront + royalty |
| Non-exclusive | Multiple licensees | Lower upfront + royalty |
| Sublicensable | Relicensing permitted | Royalty sharing agreement |
| Cross-license | Mutual practice rights | Royalty-free or balancing |

### Royalty Structures

```
Lump-sum: One-time payment at agreement
Running Royalty: Periodic payment based on sales/volume
Minimum Royalty: Annual minimum guarantee
Milestone: Stage-based payments (development/commercialization)
Hybrid: Lump-sum + running combination
```

## Quality Checklist

| Item | Criteria |
|------|----------|
| Valuation Methods | At least 2 of the 3 approaches |
| Royalty Basis | Industry benchmarks cited |
| Discount Rate | Calculation basis specified |
| Patent Strength | 6-item scorecard |
| Scenarios | Conservative/Baseline/Optimistic (3 scenarios) |
| Remaining Term | Present value based on expiration date |
