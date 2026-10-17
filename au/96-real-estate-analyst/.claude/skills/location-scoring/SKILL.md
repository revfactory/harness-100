---
name: location-scoring
description: "Location scoring scorecard. Referenced by the location-analyst agent for systematic real estate location evaluation. Use for requests involving 'location analysis', 'location assessment', or 'commercial area analysis'. On-site inspections and surveying are out of scope."
---

# Location Scoring — Location Evaluation Scorecard

Systematizes the location-analyst agent's location analysis capabilities.

## Location Evaluation Framework

### Weighted Scorecard

| Evaluation Category | Weight (Residential) | Weight (Commercial) | Weight (Office) |
|--------------------|---------------------|--------------------|-----------------|
| Transit Accessibility | 25% | 20% | 30% |
| Living Infrastructure | 20% | 10% | 10% |
| School District | 20% | 5% | 5% |
| Development Catalysts | 15% | 20% | 20% |
| Population/Commercial Area | 5% | 25% | 15% |
| Environment/Safety | 10% | 10% | 10% |
| Future Value | 5% | 10% | 10% |

### Category Scoring Criteria

#### Transit Accessibility

| Score | Criteria |
|-------|----------|
| 5 | Subway station within 5-minute walk, 2+ lines |
| 4 | Subway station within 10-minute walk, multiple bus routes |
| 3 | Subway station within 15-minute walk, major road access |
| 2 | Subway distant, bus-dependent |
| 1 | Poor public transit, personal vehicle required |

#### School District (Residential)

| Score | Criteria |
|-------|----------|
| 5 | Top-tier specialised schools, dense tutoring district |
| 4 | Strong school district, good educational environment |
| 3 | Average school district, basic educational facilities |
| 2 | Weak school district, limited tutoring options |
| 1 | Inadequate educational infrastructure |

#### Development Catalysts

| Score | Criteria |
|-------|----------|
| 5 | Confirmed development (under construction/in effect), direct beneficiary |
| 4 | Confirmed development, indirect beneficiary |
| 3 | In progress (permitting stage) |
| 2 | Planning stage (uncertain) |
| 1 | No catalysts or presence of nuisance facilities |

## Commercial Area Analysis Framework

### Commercial Area Types

| Type | Characteristics | Suitable Businesses |
|------|----------------|-------------------|
| Transit Hub | High foot traffic, high rents | F&B, convenience stores, pharmacies |
| Office District | Weekday lunch crowd, office workers | Restaurants, cafes, convenience stores |
| Residential Area | Stable, repeat customers | Grocery, laundry, tutoring centres |
| University Area | Young demographic, trend-driven | Cafes, bars, fashion retail |
| Tourist Area | Weekends/peak season, high variability | Dining, souvenirs, lodging |

### Foot Traffic Analysis

```
Evaluation Metrics:
- Average weekday foot traffic
- Average weekend foot traffic
- Time-of-day distribution (peak times)
- Age/gender breakdown
- Purpose (commuting/shopping/leisure)

Data Sources:
- National statistics foot traffic data
- Credit card transaction data
- On-site surveys (2 hours x 3 time slots)
```

## Future Value Assessment

### Development Potential Indicators

| Indicator | Positive Signal | Negative Signal |
|-----------|----------------|----------------|
| Population Trends | Inflow > Outflow | Population decline |
| Transaction Volume | Upward trend | Decline/stagnation |
| New Supply | Balanced (relative to demand) | Oversupply |
| Development Plans | Express rail, new towns, industrial parks | Restrictions, nuisance facilities |
| Rental Demand | Waitlist demand exists | Rising vacancies |

## Location Comparison Report Template

```markdown
## Location Comparison: Area A vs Area B vs Area C

### Overall Scores

| Category | Area A | Area B | Area C |
|----------|--------|--------|--------|
| Transit | 4.5 | 3.8 | 4.0 |
| ... | ... | ... | ... |
| **Weighted Total** | **4.12** | **3.75** | **3.90** |

### Strengths & Weaknesses Summary

#### Area A
- Strengths: [Specific strengths]
- Weaknesses: [Specific weaknesses]
- Opportunities: [Development catalysts, etc.]
- Threats: [Risk factors]

### Investment Opinion
[Overall assessment and ranked recommendation]
```

## Quality Checklist

| Item | Criteria |
|------|----------|
| Evaluation Categories | All 7 categories with weights applied |
| Comparison Targets | 3 or more locations |
| Data Basis | Public data utilised |
| On-Site Verification | Photos/field notes |
| SWOT | SWOT analysis per location |
| Future Outlook | 3-5 year forecast |
