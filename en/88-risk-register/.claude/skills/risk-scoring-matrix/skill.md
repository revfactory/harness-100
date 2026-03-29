---
name: risk-scoring-matrix
description: "Risk assessment matrix and quantitative analysis tools. Referenced by the assessment-analyst agent when systematically assessing risk probability and impact. Use for requests involving 'risk matrix', 'probability-impact analysis', or 'risk scoring'. Does not cover actuarial analysis or financial risk modeling."
---

# Risk Scoring Matrix — Risk Assessment Matrix

Standardizes quantitative and qualitative risk assessment for the assessment-analyst agent.

## 5×5 Probability-Impact Matrix

### Probability Scale

| Level | Score | Probability Range | Description |
|-------|-------|------------------|-------------|
| Very Low | 1 | < 5% | Rarely occurs |
| Low | 2 | 5–20% | Low likelihood |
| Medium | 3 | 20–50% | May occur |
| High | 4 | 50–80% | Likely to occur |
| Very High | 5 | > 80% | Almost certain |

### Impact Scale

| Level | Score | Schedule | Cost | Quality | Scope |
|-------|-------|----------|------|---------|-------|
| Negligible | 1 | < 1 week | < 1% | Negligible | Negligible |
| Minor | 2 | 1–2 weeks | 1–5% | Some areas | Some features |
| Moderate | 3 | 2–4 weeks | 5–10% | Key areas | Key features |
| Significant | 4 | 1–3 months | 10–25% | Pervasive | Core features |
| Critical | 5 | > 3 months | > 25% | Unusable | Project failure |

### Risk Score = Probability × Impact

```
        Impact
     1   2   3   4   5
  ┌───┬───┬───┬───┬───┐
5 │ 5 │10 │15 │20 │25 │  P
4 │ 4 │ 8 │12 │16 │20 │  r
3 │ 3 │ 6 │ 9 │12 │15 │  o
2 │ 2 │ 4 │ 6 │ 8 │10 │  b
1 │ 1 │ 2 │ 3 │ 4 │ 5 │
  └───┴───┴───┴───┴───┘

Rating: 🟢 1–4 Low | 🟡 5–9 Medium | 🟠 10–15 High | 🔴 16–25 Extreme
```

## Risk Category Classification (RBS)

### Risk Breakdown Structure

```
Project Risks
├── Technical Risks
│   ├── Technical Complexity
│   ├── Technology Maturity
│   ├── Integration Issues
│   └── Performance / Quality
├── Management Risks
│   ├── Schedule Estimation
│   ├── Resource Availability
│   ├── Scope Changes
│   └── Communication
├── External Risks
│   ├── Vendor / Supply Chain
│   ├── Regulatory Changes
│   ├── Market Shifts
│   └── Environmental / Disaster
└── Organizational Risks
    ├── Staff Attrition
    ├── Priority Changes
    ├── Budget Cuts
    └── Organizational Restructuring
```

## Quantitative Risk Analysis

### EMV (Expected Monetary Value)

```
EMV = Probability × Impact (monetary amount)

Threat:      EMV = 30% × (−₩500M) = −₩150M
Opportunity: EMV = 40% × (+₩300M) = +₩120M

Project Total EMV = Σ Individual EMVs
→ Basis for calculating Contingency Reserve
```

### Sensitivity Analysis (Tornado Diagram)

```
Impact range by variable (based on project cost):

Exchange rate fluctuation  ████████████████████ ±₩300M
Labor cost                 ███████████████ ±₩220M
Delivery delay             ██████████ ±₩150M
Quality issues             ████████ ±₩120M
Regulatory change          ██████ ±₩80M

→ Exchange rate is the most sensitive variable → prioritize management
```

## Risk Register Template

| ID | Risk | Category | Probability | Impact | Score | Grade | Response | Owner | Status |
|----|------|----------|------------|--------|-------|-------|---------|-------|--------|
| R01 | [Description] | Technical | 4 | 5 | 20 | 🔴 | Mitigate | [Name] | Active |
| R02 | [Description] | Management | 3 | 3 | 9 | 🟡 | Accept | [Name] | Monitoring |

## KRI (Key Risk Indicator) Design

| KRI | Threshold | Measurement Frequency | Trigger |
|-----|-----------|----------------------|---------|
| Schedule SPI | < 0.9 | Weekly | Re-assess schedule risk |
| Cost CPI | < 0.9 | Monthly | Re-assess budget risk |
| Defect rate | > 5% | Per sprint | Re-assess quality risk |
| Attrition rate | > 15% | Monthly | Re-assess resource risk |

## Quality Checklist

| Item | Criterion |
|------|-----------|
| Matrix | 5×5 probability-impact applied |
| Categories | All 4 RBS categories covered |
| Quantitative Analysis | EMV or scenario analysis completed |
| KRIs | At least 1 KRI per risk |
| Grade Criteria | 4-level color coding applied |
| Update Cadence | Risk re-assessment schedule specified |
