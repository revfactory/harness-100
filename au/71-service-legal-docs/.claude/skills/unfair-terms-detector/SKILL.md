---
name: unfair-terms-detector
description: "A specialized tool for detecting unfair contract terms and suggesting revisions. The 'tos-specialist' and 'consistency-reviewer' agents MUST use this skill's judgment criteria and revision patterns when drafting or validating terms of service. Use for 'unfair terms detection', 'terms of service law violation checks', 'FTC standard application', and similar tasks. Note: drafting privacy policies or cookie policies is outside the scope of this skill."
---

# Unfair Terms Detector — Detection & Revision Tool

Automatically detects unfair clauses based on the Act on the Regulation of Terms and Conditions (Terms Act) and suggests fair alternatives.

## Classification of Unfair Terms Types (Terms Act Standards)

### Liability Exemption Clauses (Article 7)

| Violation Type | Description | Unfair Example | Fair Revision |
|----------|------|-----------|-----------|
| Exemption for intent/negligence | Exemption from operator's own liability | "We are not responsible for damages caused by our negligence" | "We will compensate for damages caused by our intentional misconduct or negligence in accordance with applicable laws" |
| Data loss exemption | Loss of user data | "We are not responsible for data loss due to service interruption" | "In the event of data loss caused by our fault, we will make recovery efforts and provide compensation" |
| Service quality exemption | Full exemption from service defects | "The service is provided as-is" | "We maintain a reasonable level of service quality and will remedy any significant defects" |

### Termination & Cancellation (Article 9)

| Violation Type | Unfair Example | Fair Revision |
|----------|-----------|-----------|
| Unilateral termination | "We may delete your account without prior notice" | "In the event of a terms violation, we will restrict service if not remedied within 14 days after a prior warning" |
| Disadvantage upon termination | "Fees already paid will not be refunded upon termination" | "Upon termination, fees for the remaining period will be prorated and refunded" |
| Difficult termination process | "Termination is only available by calling customer support" | "Termination can be done directly from online account settings" |

### Damages (Articles 7 & 8)

| Violation Type | Unfair Example | Fair Revision |
|----------|-----------|-----------|
| Excessive penalty | "Early termination incurs a penalty of 100% of remaining period fees" | "Early termination incurs a penalty of 10% of remaining period fees" |
| Imbalanced compensation | "User shall compensate for all damages in the event of a terms violation" (coexisting with operator exemption) | "Both parties are subject to the same standard of liability for damages" |

### Implied Consent (Article 10)

| Violation Type | Unfair Example | Fair Revision |
|----------|-----------|-----------|
| Implied consent | "Failure to object within 30 days will be deemed consent to the terms change" | "Separate consent will be sought for material changes; if consent is refused, the previous terms will be maintained or the contract may be terminated" |

## Automatic Detection Keyword Patterns

### High-Risk Keywords (Immediate Review Required)

```
- "shall bear no responsibility whatsoever"
- "under any circumstances"
- "without prior notice"
- "non-refundable"
- "as-is"
- "may not raise any objection"
- "deemed to have consented"
- "may change at discretion"
- "at our sole discretion"
```

### Medium-Risk Keywords (Review Recommended)

```
- "unavoidable reasons"
- "within reasonable scope" (criteria unclear)
- "customary" (undefined)
- "when necessary" (requirements unclear)
- "in accordance with applicable laws" (no specific provisions cited)
```

## Review Scoring

```
Unfairness Score = Σ(severity of violation per clause) / total number of clauses

Severity:
  5: Definite Terms Act violation (subject to FTC corrective order)
  4: High likelihood of violation
  3: Potential for violation
  2: Improvement recommended
  1: Best practice

Grade:
  A (1.0–1.5): Fair terms
  B (1.6–2.5): Good (minor improvements needed)
  C (2.6–3.5): Insufficient (improvement needed)
  D (3.6–4.5): Poor (urgent improvement required)
  F (4.6–5.0): Dangerous (legal risk)
```

## Required Clauses by Service Type

### SaaS Services

- [ ] SLA (Service Level Agreement) specified
- [ ] Data ownership and portability clause
- [ ] Auto-renewal and cancellation conditions
- [ ] Price change notification obligation

### E-Commerce

- [ ] Right of withdrawal (7 days) specified
- [ ] Shipping, return, and exchange procedures
- [ ] Minor's contract cancellation right
- [ ] E-Commerce Act display and advertising obligations

### Platforms / Marketplaces

- [ ] Scope of liability as online marketplace intermediary
- [ ] Dispute resolution procedures
- [ ] Seller and buyer protection policies
- [ ] Commission change notification

## References

- Based on the Act on the Regulation of Terms and Conditions and the Fair Trade Commission review guidelines
- Detailed case law: see `references/unfair-terms-cases.md`
