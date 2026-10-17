---
name: gdpr-pipa-cross-reference
description: "Cross-reference database for GDPR and Korea's Personal Information Protection Act (PIPA). The 'privacy-law-analyst' and 'consent-designer' agents must use this skill's article mappings and gap analysis when analyzing multi-jurisdiction privacy requirements and designing consent forms. Use for 'GDPR vs PIPA comparison', 'legal requirements cross-analysis', 'global compliance strategies', etc. Note: data flow mapping and technical safeguard design are outside the scope of this skill."
---

# GDPR-PIPA Cross Reference — GDPR & PIPA Cross-Reference DB

Article-level mapping, gap analysis, and unified compliance guide for EU GDPR and Korea's Personal Information Protection Act (PIPA).

## Core Principles Cross-Mapping

| Principle | GDPR (Article) | PIPA (Article) | Differences |
|-----------|---------------|----------------|-------------|
| Lawfulness | Art.6 (6 legal bases) | Art.15 (Consent principle) | GDPR provides more legal bases |
| Purpose Limitation | Art.5(1)(b) | Art.3 No.1 | Similar |
| Data Minimization | Art.5(1)(c) | Art.3 No.1, Art.16 | Similar |
| Accuracy | Art.5(1)(d) | Art.3 No.3 | Similar |
| Storage Limitation | Art.5(1)(e) | Art.21 | Similar |
| Security | Art.5(1)(f), Art.32 | Art.29 | GDPR more detailed |
| Accountability | Art.5(2) | Art.3 No.8 | GDPR more emphasized |

## Consent Requirements Comparison

### GDPR's 4 Requirements for Valid Consent

```
1. Freely given
   - No detriment for refusal
   - Bundling unnecessary consent with service provision is prohibited

2. Specific
   - Separate consent per processing purpose
   - Blanket consent not permitted

3. Informed
   - Prior notice of controller identity, purpose, and rights
   - Clear and plain language

4. Unambiguous indication
   - Affirmative action required (no pre-checked boxes)
   - Implied consent not recognised
```

### PIPA Consent Requirements

```
1. Notice and Consent (Art.15, Art.17)
   - Notify of collection/use purpose, items, and retention period
   - Mandatory and optional items must be separated

2. Cases requiring separate consent
   - Sensitive information (Art.23)
   - Unique identification information (Art.24)
   - Marketing purposes (Art.22)
   - Third-party provision (Art.17)
   - Cross-border transfer (Art.28-8)

3. Consent methods
   - Written or electronic methods
   - Important content must be distinguished by font size and colour
```

### Practical Differences

| Item | GDPR | PIPA | Unified Compliance Approach |
|------|------|------|-----------------------------|
| Pre-checked boxes | Prohibited | Prohibited | Opt-in method |
| Bundling prohibition | Strict (Art.7(4)) | Mandatory/optional separation | Separate consent per purpose |
| Ease of withdrawal | As easy as giving consent | Equivalent to consent method and procedure | One-click withdrawal UI |
| Child consent | Under 16: parental consent | Under 14: legal guardian consent | Age 14 threshold (stricter) |
| Proof of consent | Controller must demonstrate | Processor must demonstrate | Retain consent logs |

## Data Subject Rights Mapping

| Right | GDPR | PIPA | Level of Protection |
|-------|------|------|---------------------|
| Right of Access | Art.15 | Art.35 | Similar under both laws |
| Right to Rectification | Art.16 | Art.36 | Similar under both laws |
| Right to Erasure (Right to be Forgotten) | Art.17 | Art.36 | GDPR stronger |
| Right to Restriction of Processing | Art.18 | Art.37 | GDPR more detailed |
| Right to Data Portability | Art.20 | Art.35-2 (newly added) | Introduced in PIPA 2023 |
| Right to Object | Art.21 | Art.37 | GDPR includes profiling |
| Right to Object to Automated Decision-Making | Art.22 | Art.37-2 (newly added) | Similar under both laws |

## Cross-Border Transfer Regulation Comparison

| Item | GDPR | PIPA |
|------|------|------|
| Principle | Adequacy decision country or appropriate safeguards | Consent or safeguards |
| Adequacy Decision | European Commission decision | Personal Information Protection Commission designation |
| Standard Contractual Clauses | SCC (Art.46(2)(c)) | Standard Personal Information Protection Clauses |
| BCR | Art.47 | Not applicable |
| Exceptions | Art.49 (consent, contract performance, etc.) | Data subject consent |

## Fines and Penalties Comparison

| Category | GDPR | PIPA |
|----------|------|------|
| Maximum Fine | 4% of global turnover or EUR 20 million | 3% of total revenue |
| Minor Violations | 2% of global turnover or EUR 10 million | KRW 50 million administrative fine |
| Criminal Penalties | At member state discretion | Up to 5 years imprisonment |
| Class Actions | Art.80 (representative actions) | Class dispute mediation, representative actions |

## Unified Compliance Checklist

Minimum requirements for simultaneously satisfying both laws for global services:

- [ ] Maintain Records of Processing Activities (RoPA) (GDPR Art.30 + PIPA Art.30)
- [ ] Designate DPO/CPO (GDPR Art.37 + PIPA Art.31)
- [ ] Conduct impact assessments (DPIA/PIA) (GDPR Art.35 + PIPA Art.33)
- [ ] Separate consent per purpose + Opt-in (common to both laws)
- [ ] SCC + consent for cross-border transfers (dual application of both laws)
- [ ] Report breaches within 72 hours (GDPR Art.33 + PIPA Art.34)
- [ ] Data subject rights exercise procedures (unified under both laws)

## References

- Based on GDPR 2016/679 and Korea's Personal Information Protection Act (2023 comprehensive revision)
- Detailed article mapping: see `references/gdpr-pipa-article-map.md`
