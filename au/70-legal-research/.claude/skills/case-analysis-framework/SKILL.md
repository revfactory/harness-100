---
name: case-analysis-framework
description: "A systematic framework for case analysis and issue structuring methodology. The 'case-searcher' and 'legal-analyst' agents must use this skill's IRAC framework, case analysis matrix, and issue structuring techniques when searching, analyzing cases, and deriving legal principles. Used for 'case analysis', 'issue organization', 'legal principle derivation', etc. However, drafting opinions or developing strategy is outside the scope of this skill."
---

# Case Analysis Framework

A methodology for systematically analyzing cases, structuring legal issues, and evaluating precedential value.

## IRAC Analysis Framework

### Structure

```
I — Issue
  "The legal issue in this case is whether ~"

R — Rule
  Relevant statutory provisions + case law principles + academic doctrine

A — Application
  Concrete application of legal rules to the facts of the case

C — Conclusion
  Result of legal analysis + confidence level
```

### Confidence Level Scale

| Level | Expression | Meaning |
|-------|-----------|---------|
| L5 | "~ is well-established" | Established Supreme Court precedent |
| L4 | "~ is likely to be held" | Majority of lower courts agree |
| L3 | "~ may be arguable" | Some case law supports |
| L2 | "~ is unclear" | Conflicting case law |
| L1 | "~ has no precedent" | Uncharted territory |

## Case Analysis Matrix

### Individual Case Analysis Card

```markdown
### [Case Number] — [One-line holding summary]

**Court/Decision Date**: [Supreme Court/High Court/District Court] [YYYY.MM.DD]
**Case Type**: [Civil/Criminal/Administrative]
**Outcome**: [Plaintiff won/lost, appeal dismissed/remanded]

**Key Issue**: [One sentence]

**Summary of Facts**:
- [Key fact 1]
- [Key fact 2]

**Holding** (Court's determination):
> "[Direct quote of key passage from opinion]"

**Legal Principles Extracted**:
- General principle: [Universal rule]
- Application standard: [Specific criteria for judgment]
- Exceptions/Limitations: [Limits on application of the rule]

**Precedential Value**: [L1-L5] — [Reason]
**Relevance to This Case**: [High/Medium/Low] — [Reason for relevance]
```

### Case Comparison Matrix

```
| Comparison Item | Case A | Case B | Case C | This Case |
|----------------|--------|--------|--------|-----------|
| Factual similarity | - | - | - | Baseline |
| Legal issue | - | - | - | - |
| Court's holding | - | - | - | (predicted) |
| Conclusion | - | - | - | (predicted) |
| Distinguishability | - | - | - | - |
```

## Issue Structuring Techniques

### Issue Tree

```
Main Issue: [Whether a claim for damages arising from breach of contract should be granted]
├── Sub-issue 1: Whether a contract was formed
│   ├── Detail 1-1: Validity of the offer
│   └── Detail 1-2: Existence of acceptance
├── Sub-issue 2: Whether a breach of obligation exists
│   ├── Detail 2-1: Whether the performance date has arrived
│   └── Detail 2-2: Attributable fault
├── Sub-issue 3: Scope of damages
│   ├── Detail 3-1: General damages
│   └── Detail 3-2: Special damages (foreseeability)
└── Sub-issue 4: Comparative negligence / set-off of benefits
```

### Issue Strength Assessment

```
Issue Strength = Legal_Basis(1-5) × Factual_Support(1-5) × Case_Law_Support(1-5)

Legal Basis:    5=Express statutory provision  4=Analogous application  3=Doctrinal support  2=Minority view  1=Weak basis
Factual Support: 5=Sufficient evidence  4=Mostly secured  3=Partial  2=Relies on inference  1=No evidence
Case Law Support: 5=Established Supreme Court  4=Majority agree  3=Some support  2=Conflicting  1=No precedent

Results:
  75-125: 🟢 Very favorable
  40-74:  🟡 Favorable but uncertainty exists
  15-39:  🟠 Uncertain, outcome could go either way
  1-14:   🔴 Unfavorable
```

## Key Legal Principle Patterns by Area of Law

### Civil — Contract Disputes

| Issue Type | Key Legal Principle | Authority |
|-----------|-------------------|-----------|
| Contract interpretation | Comprehensive consideration of text, party intent, and trade custom | Civil Act Art. 105 |
| Breach of obligation | Attributable fault + illegality + causation + damages | Civil Act Art. 390 |
| Scope of damages | General damages + special damages (foreseeable) | Civil Act Art. 393 |
| Comparative negligence | Deduction for victim's proportionate fault | Civil Act Art. 396 |

### Civil — Torts

| Issue Type | Key Legal Principle | Authority |
|-----------|-------------------|-----------|
| General tort | Intent/negligence + unlawful act + causation + damages | Civil Act Art. 750 |
| Employer liability | Relation to scope of employment | Civil Act Art. 756 |
| Consolation damages | Objective recognition of mental distress | Civil Act Art. 751 |

### Labor — Wrongful Termination Disputes

| Issue Type | Key Legal Principle | Authority |
|-----------|-------------------|-----------|
| Just cause | Impossibility of maintaining employment relationship by social norms | Labor Standards Act Art. 23 |
| Termination procedure | 30-day advance notice or pay in lieu | Labor Standards Act Art. 26 |
| Remedy for unfair dismissal | Reinstatement + back pay equivalent | Labor Standards Act Art. 30 |

## References

- Utilize the Supreme Court Comprehensive Legal Information system and the Ministry of Government Legislation's National Law Information Center
- Detailed legal principle patterns: see `references/legal-doctrine-patterns.md`
