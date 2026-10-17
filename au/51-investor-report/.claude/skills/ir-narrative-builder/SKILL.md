---
name: ir-narrative-builder
description: "A skill that professionally supports investor report narrative construction. Used by strategy-updater and ir-reviewer when designing the tone, structure, and storyline of investor communications. Automatically applied in contexts such as 'investor narrative', 'equity story', 'IR message', 'strategy update story'. However, drafting statutory disclosure text or writing brokerage reports are outside the scope of this skill."
---

# IR Narrative Builder — Investor Communication Narrative Construction Tool

A specialised skill that enhances the investor narrative capabilities of strategy-updater and ir-reviewer agents.

## Target Agents

- **strategy-updater** — Equity Story construction, strategy narrative writing
- **ir-reviewer** — Narrative consistency verification, investor-type-specific tone review

## Equity Story 5-Stage Framework

```
1. WHY NOW — Why this market right now (market opportunity)
2. WHY US — Why us (competitive advantage)
3. PROOF POINTS — Is there evidence (performance data)
4. WHERE NEXT — What is the next step (growth strategy)
5. WHY INVEST — Why should you invest (value creation)
```

### Stage-by-Stage Writing Guide

| Stage | Core Question | Elements to Include | Cautions |
|-------|-------------|---------------------|----------|
| WHY NOW | Market inflection point | TAM/SAM/SOM, regulatory changes | Guard against overestimation |
| WHY US | Differentiation basis | Technology moat, network effects | Avoid abstract expressions |
| PROOF POINTS | Quantitative results | Revenue, customers, NPS | Guard against cherry-picking |
| WHERE NEXT | Execution roadmap | Product, market expansion | Feasibility |
| WHY INVEST | Valuation | Multiples, comparable companies | Conservative estimates |

## Narrative Tone by Investor Type

### For VCs
**Tone**: Vision-centered, emphasise growth potential
**Structure**: Executive Summary → Market Opportunity → Product Milestones → Growth Metrics → Team → Runway → Next Targets

### For PE
**Tone**: Numbers-centered, emphasise operational efficiency
**Structure**: Executive Summary → P&L/CF/BS → EBITDA Bridge → KPI Benchmarks → Value Creation Plan → Risks → Initiatives

### For Public Shareholders
**Tone**: Balanced, emphasise transparency
**Structure**: CEO Letter → Financial Highlights → Business Unit Performance → Market Environment → ESG → Shareholder Returns → Outlook

## EBITDA Bridge Construction

```
Prior Quarter EBITDA
  (+) Revenue increase effect
  (+) Margin improvement effect
  (-) Labor cost increase
  (-) Marketing cost increase
  (+/-) FX effect
  (+/-) One-time items
= Current Quarter EBITDA
```

**Principles:** List in order of magnitude, positive before negative, distinguish one-time vs. structural

## Narrative Quality Checklist (for ir-reviewer)

### Consistency Verification
- [ ] Do figures exactly match the financial analysis?
- [ ] Is the narrative direction consistent with the prior quarter report?
- [ ] Is the balance between positive/negative information appropriate?
- [ ] Do forward-looking statements have disclaimers?

### Persuasiveness Verification
- [ ] Do all claims have data-backed evidence?
- [ ] Are risks honestly disclosed?
- [ ] Do next quarter targets meet SMART criteria?

## Risk Disclosure 3-Level Matrix

| Grade | Criteria | Expression Approach |
|-------|---------|---------------------|
| HIGH | High probability and high impact risk | Specific response plan required |
| MEDIUM | Monitoring needed | Specify early warning indicators |
| LOW | Controllable | Brief mention |

**Principle:** Do not hide risks → build investor trust. Present risk + response plan as a pair.
