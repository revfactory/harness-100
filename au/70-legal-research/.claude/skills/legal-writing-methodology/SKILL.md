---
name: legal-writing-methodology
description: "Professional methodology for drafting legal opinions and strategy reports. The 'opinion-writer' and 'strategy-advisor' agents must utilize the document structure, argumentation techniques, and citation formats in this skill when drafting legal opinions or formulating strategies. Used for 'legal opinion drafting', 'legal document structure', 'argumentation methods', etc. Note: case law research and legal doctrine analysis are outside the scope of this skill."
---

# Legal Writing Methodology

Professional structure and argumentation techniques for legal opinions and strategy reports.

## Standard Legal Opinion Structure

### Official Opinion Template

```markdown
# Legal Opinion

**To**: [Client/Department]
**From**: [Author]
**Date**: [YYYY.MM.DD]
**Re**: [Matter/Issue Title]
**Document No.**: LO-[YYYY]-[Sequence]

---

## I. Issue Presented
[Clearly state the client's legal question]

## II. Statement of Facts
[Organise the facts underlying the analysis, in chronological or thematic order]
※ Unverified facts should be noted as "assumed to be ~"

## III. Analysis

### 1. Issue [1]: [Issue Name]
#### a. Applicable Law
[Relevant statutory provisions + commentary]

#### b. Relevant Case Law
[Key cases + extracted legal principles]

#### c. Analysis
[Analysis using the IRAC method]

#### d. Sub-Conclusion
[Conclusion on this issue]

### 2. Issue [2]: [Issue Name]
[Repeat same structure]

## IV. Overall Opinion
[Overall conclusion + level of certainty + risk summary]

## V. Recommendations
1. [Immediate action items]
2. [Medium-term action items]
3. [Items requiring caution]

## VI. Disclaimer
This opinion is a legal review based on the facts presented and current applicable law,
and does not constitute legal advice.
Please consult a qualified attorney before making any final decisions.
```

## Argumentation Techniques

### Deductive Reasoning

```
Major Premise: [Legal Rule] "If ~, then ~" (Civil Code § 750)
Minor Premise: [Fact] "In this case, the defendant ~"
Conclusion:   "Therefore, the defendant is obligated to ~"
```

### Analogical Reasoning

```
Precedent Facts: [Facts from Case A]
Precedent Holding: [Court's ruling in Case A]
Similarity: [Key similarities to the present case]
Distinctions: [Why differences do not affect the conclusion]
Conclusion: "The legal principle from Case A applies to the present case"
```

### Policy Argument

```
Current Doctrine: [Current interpretation/application]
Problem: [Limitations of the current interpretation]
Alternative Interpretation: [Proposed interpretation]
Policy Justification: [Social validity, legislative intent]
```

## Citation Formats

### Case Citation

```
Supreme Court, May 15, 2023, Case No. 2022Da12345
Seoul High Court, Aug. 10, 2022, Case No. 2021Na67890
Constitutional Court, Mar. 20, 2023, Case No. 2022HeonMa123
```

### Statutory Citation

```
Civil Code § 750 (Content of Unlawful Acts)
Personal Information Protection Act § 15(1)(1)
Enforcement Decree of the Labour Standards Act § 12
```

### Literature Citation

```
[Author], "[Title of Article/Book]", [Publisher/Journal], [Year], [Page(s)]
Example: Kim Sang-yong, "Law of Obligations — Special Part", Hwasan Media, 2023, p. 205
```

## Risk Response Strategy Framework

### Strategy Options Comparison Table

```markdown
| Option | Litigation | Mediation/Arbitration | Negotiation | Avoidance |
|--------|------------|-----------------------|-------------|-----------|
| Expected Duration | 1–3 years | 3–6 months | 1–3 months | Immediate |
| Expected Cost | High | Medium | Low | None |
| Win Probability | [%] | - | - | - |
| Confidentiality | Not possible | Possible | Possible | - |
| Precedential Effect | Yes | No | No | - |
| Enforceability | Strong | Medium | Weak | - |
| Relationship Impact | Destructive | Neutral | Preserved | Preserved |
```

### Cost-Benefit Analysis

```
Expected Value of Litigation = (Win Probability × Award Amount) - (Litigation Costs + Opportunity Costs + Loss Risk)

Decision Criteria:
  Expected Value > 0: Litigation worth considering
  Expected Value < 0: Prioritise negotiation/mediation
  Expected Value ≈ 0: Consider non-monetary factors (precedent, deterrence effect)
```

## References

- Refer to the Korean Bar Association opinion template
- Detailed writing examples: see `references/legal-writing-examples.md`
