---
name: wedding-budget-optimizer
description: "A budget management tool that optimizes per-category allocation and cost reduction strategies for a wedding budget. When the 'budget-controller' and 'wedding-reviewer' agents allocate budgets and verify costs, they must use this skill's budget allocation formulas, cost reference table, and savings strategies. Use for 'wedding budget allocation', 'cost reduction', and 'budget simulation' contexts. Vendor comparison and timeline design are outside this skill's scope."
---

# Wedding Budget Optimizer — Wedding Budget Optimization Tool

Provides per-category allocation ratios, cost standards, and savings strategies for a wedding budget.

## Wedding Cost Structure (Korea, 2024–2025)

### Overall Cost Averages

```
Korean Average Wedding Costs (2024):
  Total cost: approximately ₩250,000,000–350,000,000 (both families combined)

Breakdown:
  Housing (lease / purchase): ₩150,000,000–250,000,000 (50–70%)
  Ceremony and party: ₩20,000,000–50,000,000 (10–15%)
  Wedding gifts and betrothal gifts: ₩10,000,000–30,000,000 (5–10%)
  Trousseau: ₩10,000,000–20,000,000 (3–7%)
  Honeymoon: ₩2,000,000–6,000,000 (2–3%)
```

### Detailed Ceremony Cost Allocation (Based on ₩30,000,000 Ceremony Budget)

| Item | Ratio | Amount | Notes |
|------|-------|--------|-------|
| Catering (meals) | 40–50% | ₩12,000,000–15,000,000 | 200 guests × ₩60,000–75,000 |
| Studio/dress/makeup | 15–25% | ₩4,500,000–7,500,000 | Studio + dress + makeup |
| Venue rental | 5–10% | ₩1,500,000–3,000,000 | Rental fee (if separate from catering) |
| Invitations | 2–3% | ₩600,000–900,000 | 250 pieces |
| MC and wedding song | 1–3% | ₩300,000–900,000 | |
| Flowers and décor | 3–5% | ₩900,000–1,500,000 | Bouquet, venue floral decoration |
| Return gifts | 2–3% | ₩600,000–900,000 | Guest return gifts |
| Paebaek | 1–2% | ₩300,000–600,000 | Paebaek food, ceremonial attire rental |
| Contingency reserve | 5–10% | ₩1,500,000–3,000,000 | Emergency fund |

## Budget Allocation Formulas

### Guest-Based Catering Cost Calculation

```
Total catering cost = Expected guests × per-person cost × (1 + VAT rate)

Attendance adjustment factors:
  Invited 200 → Expected actual attendance: 160–180 guests (80–90%)
  Invited 300 → Expected actual attendance: 230–260 guests (77–87%)

Safety margin: Minimum guaranteed headcount = Expected actual attendance × 0.9 (conservative)
```

### Congratulatory Gift Estimation

```
Expected congratulatory gifts = Σ(guests by relationship × expected amount)

Average congratulatory gift amounts by relationship (2024):
  Relatives: ₩100,000–300,000
  Colleagues: ₩50,000–100,000
  Friends: ₩50,000–70,000
  Acquaintances: ₩30,000–50,000

Gift coverage ratio = Total congratulatory gifts / Total catering cost
  Typical: 60–80%
  Many guests: 80–100% (can offset catering cost)
```

## Top 10 Cost Reduction Strategies

### Large Savings (₩1,000,000+ reduction)

```
1. Off-season or Saturday morning ceremony (10–15% catering discount + venue savings)
   Savings: ₩1,500,000–3,000,000

2. Individual studio/dress/makeup contracts (compare value vs. package)
   Savings: ₩1,000,000–2,000,000 (situation-dependent)

3. Guest count optimization (reduce unnecessary invitations)
   Savings: 50 fewer guests × ₩70,000 = ₩3,500,000

4. DIY wedding elements (partial self-arrangement)
   - Invitations: Mobile invitations (80–90% reduction)
   - Return gifts: Direct purchase (50% reduction)
   - Videography: Use a friend (₩1,000,000 reduction)
```

### Medium Savings (₩300,000–1,000,000 reduction)

```
5. Bridal fair contract discount (10–20% special pricing)
   Savings: ₩500,000–1,000,000

6. Referral discount (through already-married friends)
   Savings: ₩300,000–500,000

7. Use seasonal flowers (instead of imported flowers)
   Savings: ₩300,000–500,000

8. Return gifts purchased online directly
   Savings: ₩200,000–400,000
```

### Small Savings (under ₩300,000)

```
9. Mobile invitations (replacing printed)
   Savings: ₩200,000–300,000

10. Prepare paebaek food yourself (with family help)
    Savings: ₩150,000–250,000
```

## Budget Scenarios by Level

### Economy (₩20,000,000)

```
Catering: 150 guests × ₩60,000 = ₩9,000,000
Studio/dress/makeup: ₩1,500,000 (mid-low package)
Venue: ₩1,000,000 (standard wedding hall, off-season)
Invitations: ₩100,000 (mobile)
Flowers and décor: ₩500,000
Other: ₩1,500,000
Contingency reserve: ₩1,400,000
→ Congratulatory gifts can offset a significant portion of catering cost
```

### Standard (₩35,000,000)

```
Catering: 200 guests × ₩80,000 = ₩16,000,000
Studio/dress/makeup: ₩4,000,000 (mid-tier package)
Venue: ₩2,000,000
Invitations: ₩500,000 (printed + mobile)
Flowers and décor: ₩1,000,000
MC and wedding song: ₩500,000
Return gifts: ₩500,000
Paebaek: ₩400,000
Videography: ₩800,000
Contingency reserve: ₩3,300,000
```

### Premium (₩50,000,000)

```
Catering: 250 guests × ₩120,000 = ₩30,000,000 (hotel)
Studio/dress/makeup: ₩7,000,000 (premium)
Venue: ₩3,000,000 (hotel rental)
Invitations: ₩800,000
Flowers and décor: ₩2,000,000
MC: ₩800,000
Return gifts: ₩800,000
Videography (directed): ₩1,500,000
Other: ₩2,000,000
Contingency reserve: ₩2,100,000
```

## Budget Management Tracking Table

```markdown
## Wedding Budget Tracking Table

**Total Budget**: ₩X | **Spent**: ₩X | **Remaining**: ₩X | **Progress**: X%

| Item | Budget | Deposit | Final Payment | Total Spent | Status |
|------|--------|---------|---------------|-------------|--------|
| Wedding hall | ₩X | ₩X | ₩X | ₩X | ✅ Contracted |
| Studio/dress/makeup | ₩X | - | - | - | 🔍 Comparing |
| Honeymoon | ₩X | - | - | - | ⏳ Not started |

### Payment Schedule
| Date | Vendor | Amount | Type | Notes |
|------|--------|--------|------|-------|
| D-180 | Wedding hall | ₩X | Deposit | |
| D-30 | Wedding hall | ₩X | Final payment | After guest count confirmed |
```

## Reference

- Based on the Korean wedding market 2024–2025
- Detailed cost data: see `references/wedding-cost-data.md`
