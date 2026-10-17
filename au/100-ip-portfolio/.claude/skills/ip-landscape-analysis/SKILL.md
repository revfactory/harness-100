---
name: ip-landscape-analysis
description: "IP landscape analysis guide. Referenced by the patent-mapper and protection-advisor agents when analysing technology-specific patent landscapes and developing strategies. Use for 'IP landscape', 'patent map', or 'technology trends' requests. Patent filing services and patent search database access are out of scope."
---

# IP Landscape Analysis — IP Landscape Analysis

Enhances the IP strategy analysis capabilities of the patent-mapper and protection-advisor agents.

## IP Landscape Analysis Process

### 5-Step Analysis Procedure

```
Step 1: Define Technology Scope
  - Technology keywords + IPC/CPC codes
  - Search query design

Step 2: Data Collection
  - KIPRIS (Korea), USPTO (US), EPO (Europe)
  - Search range: Last 10-20 years

Step 3: Quantitative Analysis
  - Filing trends, applicant rankings, technology classification
  - Patent family analysis

Step 4: Qualitative Analysis
  - Key patent selection, claims analysis
  - White space identification

Step 5: Strategy Derivation
  - Opportunity/threat mapping
  - Filing/acquisition/licensing/design-around strategies
```

## Patent Map Types

### Technology-Timeline Map

```
         2020  2021  2022  2023  2024
Tech A    ##    ###   ####  ##### ######
Tech B    #     ##    ###   ####  ####
Tech C    ###   ##    ##    #     #
Tech D    -     -     #     ##    ####

-> Tech A: Rapid growth, Tech D: Emerging
-> Tech C: Declining
```

### Applicant Portfolio Map

| Applicant | Tech A | Tech B | Tech C | Total |
|-----------|--------|--------|--------|-------|
| Company X | 45 | 32 | 18 | 95 |
| Company Y | 38 | 28 | 25 | 91 |
| Competitor Z | 52 | 15 | 8 | 75 |
| Our Company | 12 | 20 | 5 | 37 |

### Citation Network Map

```
Key patent identification criteria:
- Top 10% by forward citations
- Examiner citations (higher weight)
- Betweenness centrality
```

## White Space Analysis

### Technology-Market Matrix

```
         Market A    Market B    Market C
Tech 1    ####       ##         ....  <- Gap
Tech 2    ###        ....       ##    <- Gap
Tech 3    ....       ###        ####  <- Gap

.... = White Space (no/few filings)
-> Strategic filing opportunities
```

### White Space Types

| Type | Description | Strategy |
|------|------------|----------|
| Technology Gap | Unexplored technology area | Preemptive filing |
| Market Gap | Unapplied market/region | Foreign filing |
| Applicant Gap | Area competitors have not entered | Rapid portfolio build |

## FTO (Freedom to Operate) Analysis

### FTO Analysis Procedure

```
1. Confirm target product/technology specifications
2. Search relevant patents (registered/valid patents)
3. Claims analysis (element-by-element comparison)
4. Infringement risk assessment
   - Literal infringement: All elements match
   - Doctrine of equivalents: Substantially identical
5. FTO opinion preparation
```

### Infringement Risk Matrix

| Risk | Infringement Likelihood | Impact | Response |
|------|----------------------|--------|----------|
| High | Literal infringement possible | Core functionality | Design-around / License |
| Medium | Equivalents infringement possible | Some functionality | Design-around review |
| Low | Low infringement likelihood | Non-core | Monitoring |

## IP Strategy Framework

### Offensive/Defensive Strategies

| Strategy | Purpose | Means |
|----------|---------|-------|
| Patent Fence | Protect core technology | File surrounding patents |
| Preemptive Filing | Market entry barrier | Fast filing on new technology |
| Cross-Licensing | Mutual practice rights | Portfolio exchange |
| Defensive Publication | Block competitor filings | Publish technology (establish prior art) |
| Patent Pool | Access standard technology | Industry-wide joint licensing |

### IP Portfolio Optimisation

```
Retention Criteria:
  3 stars - Core: Directly business-related, high value
  2 stars - Important: Defensive value, revenue potential
  1 star - Moderate: Review value vs maintenance cost

Pruning Criteria:
  - No business relevance + no licensing demand -> Abandon
  - Maintenance cost > value -> Sell or abandon
  - Expiring within 3 years + no utilization plan -> Consider abandonment
```

## Renewal Management

### Country-Specific Patent Life/Renewal Costs

| Country | Patent Term | Renewal Cycle | Cost Trend |
|---------|-----------|-------------|-----------|
| Korea | Filing date + 20 years | Annual (from year 4) | Increases annually |
| United States | Filing date + 20 years | At 3.5/7.5/11.5 years | 3 stages |
| Europe (EP) | Filing date + 20 years | Annual (from year 3) | Increases annually |
| Japan | Filing date + 20 years | Annual (from year 4) | Increases annually |
| China | Filing date + 20 years | Annual | Increases annually |

## Quality Checklist

| Item | Criteria |
|------|----------|
| Search Scope | IPC/CPC + keyword combination |
| Quantitative Analysis | Trends, rankings, classification |
| White Space Analysis | Technology-market matrix |
| FTO | Core products/technologies covered |
| Strategy | Offensive/defensive strategies specified |
| Portfolio | Retention/pruning criteria defined |
