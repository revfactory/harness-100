---
name: risk-scoring-matrix
description: "risk assessment matrix and analysis tool. assessment-analyst agent risk probability and impact systematicas assessmentto do when reference. 'risk matrix', 'probability impact analysis', 'risk score' request when usage. However, insurance total risk model scope outside."
---

# Risk Scoring Matrix — risk assessment matrix

assessment-analyst agent risk /nature assessment tablelevel.

## 5x5 probability-impact matrix

### probability etc.grade

| etc.grade | score | probability scope | description |
|------|------|----------|------|
| Low | 1 | <5% | occurrencedegree |
| Low | 2 | 5~20% | possiblenature Low |
| report | 3 | 20~50% | occurrenceto do number |
| High | 4 | 50~80% | occurrence possiblenature High |
| High | 5 | >80% | actual |

### impact etc.grade

| etc.grade | score | schedule | cost | quality | scope |
|------|------|------|------|------|------|
| un- | 1 | <1week | <1% | un-un- | un-un- |
| un- | 2 | 1~2week | 1~5% | daydepartment | daydepartment feature |
| report | 3 | 2~4week | 5~10% | key | key feature |
| each | 4 | 1~3month | 10~25% | beforequality | core feature |
| valuepeople | 5 | >3month | >25% | usage impossible | project failure |

### risk score = probability × impact

```
 impact
 1 2 3 4 5
 ┌───┬───┬───┬───┬───┐
5 │ 5 │10 │15 │20 │25 │ 
4 │ 4 │ 8 │12 │16 │20 │ rate
3 │ 3 │ 6 │ 9 │12 │15 │
2 │ 2 │ 4 │ 6 │ 8 │10 │
1 │ 1 │ 2 │ 3 │ 4 │ 5 │
 └───┴───┴───┴───┴───┘

etc.grade: 🟢 1~4 Low | 🟡 5~9 report | 🟠 10~15 High | 🔴 16~25 
```

## risk category classification (RBS)

### Risk Breakdown Structure

```
project risk
├── technical risk
│ ├── technical 
│ ├── technical nature
│ ├── integration issue
│ └── nature/quality
├── management risk
│ ├── schedule estimation
│ ├── specialistKRW nature
│ ├── scope change
│ └── company
├── external risk
│ ├── /grade
│ ├── change
│ ├── market 
│ └── environment/re-
└── risk
 ├── personcapability 
 ├── priority change
 ├── budget 
 └── change
```

## quality risk analysis

### EMV (Expected Monetary Value)

```
EMV = probability × impact(amount)

: EMV = 30% × (-₩500M) = -₩1.500M
opportunity: EMV = 40% × (+₩300M) = +₩1.200M

project total EMV = Σ individual EMV
→ example(Contingency Reserve) calculation basis
```

### also analysis (Tornado Diagram)

```
numberby impact scope (project cost standard):

exchange ████████████████████ ±₩300M
personcase ███████████████ ±₩2.200M
delivery date degreeannual ██████████ ±₩1.500M
quality issue ████████ ±₩1.200M
 change ██████ ±₩0.800M

→ exchange Korean number → management
```

## risk etc.recorddepartment template

| ID | risk | category | probability | impact | score | etc.grade | response | responsible | status |
|----|--------|---------|------|------|------|------|------|------|------|
| R01 | [description] | technical | 4 | 5 | 20 | 🔴 | mitigation | [name] | nature |
| R02 | [description] | management | 3 | 3 | 9 | 🟡 | acceptance | [name] | monitoring |

## KRI (Key Risk Indicator) design

| KRI | total | cycle | |
|-----|--------|----------|--------|
| schedule SPI | <0.9 | weekbetween | schedule risk re-assessment |
| cost CPI | <0.9 | monthbetween | budget risk re-assessment |
| rate | >5% | sprint | quality risk re-assessment |
| rate | >15% | monthbetween | personcapability risk re-assessment |

## quality checklist

| item | standard |
|------|------|
| matrix | 5x5 probability-impact applied |
| category | RBS 4versus category |
| analysis | EMV or scenario analysis |
| KRI | risk 1items or more |
| etc.grade standard | 4stage |
| cycle | risk re-assessment schedule specify |
