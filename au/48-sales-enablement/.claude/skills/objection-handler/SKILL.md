---
name: objection-handler
description: "A methodology for systematically classifying and responding to customer objections in B2B sales. Used for 'objection handling,' 'rebuttal management,' 'sales rebuttals,' 'price objections,' 'competitive comparison responses,' and 'budget constraint responses' when handling sales objections. Note: Legal advisory, contract drafting, and actual negotiation representation are outside the scope of this skill."
---

# Objection Handler — Sales Objection Response Framework

A skill that enhances objection handling capabilities for followup-manager and proposal-writer.

## Target Agents

- **followup-manager** — Systematically handles customer objections during the follow-up process
- **proposal-writer** — Includes pre-emptive objection responses in the proposal

## Objection Classification System (BANT+C)

### Budget

| Objection | Response Strategy |
|-----------|-----------------|
| "We don't have the budget" | 1. Shift from cost to investment perspective 2. Quantify the cost of the current problem 3. Propose phased adoption |
| "It's too expensive" | 1. TCO comparison (including competitors) 2. Present ROI 3. Break down pricing components |
| "This year's budget is already spent" | 1. Help secure next year's budget 2. Propose free/low-cost pilot 3. Justify with cost-saving benefits |

### Authority

| Objection | Response Strategy |
|-----------|-----------------|
| "I'm not the decision-maker" | 1. Request introduction to decision-maker 2. Provide materials to build an internal champion 3. Offer executive briefing |
| "Multiple departments need to agree" | 1. Create department-specific value propositions 2. Provide internal presentation materials 3. Arrange multi-department meeting |

### Need

| Objection | Response Strategy |
|-----------|-----------------|
| "We don't need it right now" | 1. Quantify the cost of latent problems 2. Share competitor adoption cases 3. Present market change scenarios |
| "Our current system is sufficient" | 1. Current vs. future comparison 2. Identify hidden inefficiencies 3. Present next-generation requirements |
| "We have other priorities" | 1. Show synergy with other projects 2. Propose lightweight parallel adoption 3. Reset the timing |

### Timeline

| Objection | Response Strategy |
|-----------|-----------------|
| "Not this year" | 1. Calculate cost of delay 2. Propose phased adoption schedule 3. Start with preparation work only |
| "It takes too long" | 1. Show quick wins first 2. Propose parallel execution schedule 3. Share comparable implementation timelines |

### Competition

| Objection | Response Strategy |
|-----------|-----------------|
| "The competitor is cheaper" | 1. Feature-to-price comparison 2. Expose hidden costs 3. TCO including switching costs |
| "We're already working with another vendor" | 1. Three differentiating points 2. Offer a pre-emptive PoC 3. Position as a second opinion |
| "The competitor has more references" | 1. Focus on relevant industry cases 2. Offer direct customer introductions 3. Propose a pilot |

## LAER Response Framework

```
L - Listen
  "I understand that's a concern. Could you tell me more about that?"

A - Acknowledge
  "That makes perfect sense. Other customers have had the same concern initially."

E - Explore
  "Specifically, which aspect concerns you the most?"
  → Uncover the real reason behind the surface-level objection

R - Respond
  Present specific data, case studies, and solutions
```

## Objection Severity Assessment

```
GREEN Soft Objection (Information gap)
  → Resolved by providing additional information
  → "Tell me more" = Signal of interest

YELLOW Medium Objection (Process/Timing)
  → Resolved by adjusting schedule/process
  → "Not now, but..." = Timing can be adjusted

RED Hard Objection (Fundamental mismatch)
  → Requires product changes or deal withdrawal
  → "It's not a fit for us" = Honest assessment needed
```

## Pre-emptive Objection Handling

```
FAQ to include in the proposal proactively:

Q: "How long does implementation take?"
A: "Average N weeks, based on similarly sized customers. Includes phased milestones."

Q: "Does it integrate with our existing systems?"
A: "Supports API integration with major systems (SAP, Salesforce, etc.). Custom integration takes N weeks."

Q: "How do you handle data security?"
A: "ISO 27001 certified, SOC 2 Type II compliant, hosted in certified data centers."

Q: "What happens to our data if we cancel?"
A: "Full data export via CSV/API. Data retained for 90 days after contract termination."
```

## Negotiation Strategy Matrix

```
            Customer Price Sensitivity
            Low              High
Customer  High │ Premium      │ Value Proof    │
Value          │ Full Package │ ROI Emphasis   │
Perception Low │ Educate+Demo │ Pilot/Discount │
```

## Objection Response Script Template

```markdown
### Objection: [Objection content]
**Classification**: [Budget/Authority/Need/Timeline/Competition]
**Severity**: [GREEN/YELLOW/RED]

**Immediate Response** (30 seconds):
"[Acknowledgment]. [Exploratory question]."

**Detailed Response** (2 minutes):
1. [Data/case study 1]
2. [Data/case study 2]
3. [Proposal/alternative]

**Follow-up Actions**:
- [Materials to send]
- [Next meeting agenda]
```
