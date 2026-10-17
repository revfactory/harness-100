---
name: tam-sam-som-calculator
description: "Methodology for systematically calculating market size (TAM/SAM/SOM). Use this skill for 'TAM SAM SOM calculation', 'market size estimation', 'market sizing', 'market opportunity analysis', 'addressable market', and other market sizing tasks. Note: purchasing paid market research reports and directly collecting census data are outside the scope of this skill."
---

# TAM SAM SOM Calculator — Market Sizing Methodology

A skill that enhances market sizing for the industry-analyst and research-reviewer.

## Target Agents

- **industry-analyst** — Calculates market size systematically
- **research-reviewer** — Validates market size calculations

## Definitions

```
TAM (Total Addressable Market):
  Total revenue opportunity if 100% market share
  "If everyone who could use our product, did"

SAM (Serviceable Addressable Market):
  Portion of TAM targeted by your product/service
  "Our market segment based on geography, customer type, etc."

SOM (Serviceable Obtainable Market):
  Realistic market share you can capture
  "What we can actually achieve in 1-3 years"
```

## Top-Down Approach

```
Start with total industry data, narrow down:

TAM = Industry report market size
SAM = TAM x (Target segment %)
SOM = SAM x (Realistic market share %)

Example:
TAM: Global CRM market = $80B
SAM: SMB CRM in North America = $80B x 15% x 40% = $4.8B
SOM: Year 3 target = $4.8B x 0.5% = $24M
```

## Bottom-Up Approach

```
Start with unit economics, scale up:

SOM = Target customers x Revenue per customer
SAM = Total addressable customers x Revenue per customer
TAM = Total potential customers globally x Revenue per customer

Example:
SOM: 500 customers x $2,000/yr = $1M
SAM: 50,000 potential SMBs x $2,000/yr = $100M
TAM: 2M potential businesses globally x $2,000/yr = $4B
```

## Cross-Validation

```
Compare Top-Down and Bottom-Up results:
- If within 2x of each other: Good convergence
- If >3x difference: Review assumptions
- Present both with reasoning
```

## Data Sources

| Source Type | Examples | Best For |
|-----------|---------|---------|
| Industry reports | Gartner, IDC, Statista, Grand View Research | TAM |
| Government data | Census, trade statistics, economic indicators | Market sizing |
| Company filings | SEC filings, annual reports | Competitor sizing |
| App/web analytics | App Annie, SimilarWeb, Alexa | Digital market estimation |
| Job postings | LinkedIn, Indeed | Market growth signals |

## Common Mistakes

```
1. TAM too large ("the whole internet")
2. Confusing TAM with SAM (not everyone is your customer)
3. SOM too aggressive (>5% in year 1 for new market)
4. No sources cited
5. Static analysis (no growth rate consideration)
6. Not accounting for pricing differences across segments
```
