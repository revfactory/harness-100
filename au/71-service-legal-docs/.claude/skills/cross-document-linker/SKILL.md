---
name: cross-document-linker
description: "A document linking tool that manages cross-references and consistency across service legal documents. The 'consistency-reviewer' and each specialist agent MUST use this skill's linking matrix and check rules to maintain consistent definitions, clauses, and terminology across documents. Use for 'cross-document consistency', 'cross-reference management', 'terminology unification', etc. Note: authoring individual documents is outside the scope of this skill."
---

# Cross Document Linker — Legal Document Cross-Reference & Consistency Management

Manages reference relationships and consistency across Terms of Service, Privacy Policy, Cookie Policy, Refund Policy, and Copyright Notice.

## Cross-Reference Matrix Between Documents

### Shared Definition Framework

| Shared Term | Source Document | Referencing Documents | Consistency Rule |
|-------------|----------------|-----------------------|-----------------|
| "Service" | Terms of Service Article 2 | All documents | Use identical definition |
| "Member/User" | Terms of Service Article 2 | All documents | Unify identical terminology |
| "Personal Information" | Privacy Policy Article 1 | Terms, Cookie Policy | Apply Privacy Policy definition |
| "Cookie" | Cookie Policy Article 1 | Privacy Policy | Apply Cookie Policy definition |
| "Paid Service" | Terms of Service Article X | Refund Policy | Same scope |
| "Content" | Terms of Service Article X | Copyright Notice | Identical definition |

### Clause Linkage Relationships

```
[Terms of Service]
├── Article X (Personal Information) → [Privacy Policy] full reference
│   "Members' personal information is processed in accordance with the separate Privacy Policy."
├── Article X (Cookies) → [Cookie Policy] full reference
│   "For matters regarding cookie use, please refer to the Cookie Policy."
├── Article X (Refunds) → [Refund Policy] full reference
│   "Detailed matters regarding refunds and cancellations are governed by the Refund Policy."
├── Article X (Copyright) → [Copyright Notice] reference
│   "For matters regarding copyright of content within the Service, please refer to the Copyright Notice."
└── Article X (Terms Amendment) → Amendment procedures applied consistently to all documents

[Privacy Policy]
├── Collected items → Consistent with [Terms of Service] membership registration clauses
├── Consignment information → Consistent with [Terms of Service] third-party provision clauses
└── Cookie-related → Cross-reference with [Cookie Policy]

[Refund Policy]
├── Payment conditions → Consistent with [Terms of Service] paid service clauses
└── Personal information (refunds) → Consistent with [Privacy Policy] payment information retention clauses
```

## Consistency Check Rules

### Mandatory Compliance Rules (🔴 Immediate correction required on violation)

| Rule ID | Rule | Targets |
|---------|------|---------|
| CR-01 | Service name is identical across all documents | All documents |
| CR-02 | Company name, representative, and contact information match | Terms, Privacy Policy |
| CR-03 | Personal information collection items match between Terms and Privacy Policy | Terms ↔ Privacy Policy |
| CR-04 | Refund conditions match between Terms and Refund Policy | Terms ↔ Refund Policy |
| CR-05 | Cookie types match between Cookie Policy and Privacy Policy | Privacy Policy ↔ Cookie Policy |
| CR-06 | Effective date is identical across all documents | All documents |
| CR-07 | Jurisdiction court and governing law match between Terms and Privacy Policy | Terms ↔ Privacy Policy |

### Recommended Compliance Rules (🟡 Improvement recommended)

| Rule ID | Rule | Targets |
|---------|------|---------|
| CR-08 | Unified terminology (prohibit mixed use of member/user/subscriber) | All documents |
| CR-09 | Amendment notification procedures are identical | Terms ↔ Privacy Policy |
| CR-10 | Age criteria unified (age 14 / age 19) | Terms ↔ Privacy Policy |
| CR-11 | Dispute resolution procedures consistent | Terms ↔ Refund Policy |
| CR-12 | Indemnification scope has no mutual contradictions | Terms ↔ each policy |

## Consistency Report Output Structure

```markdown
## Cross-Document Consistency Verification Report

### Verification Summary
| Rule ID | Rule | Status | Documents |
|---------|------|--------|-----------|
| CR-01 | Service name match | ✅ | All |
| CR-03 | Collection items match | ❌ | Terms ↔ Privacy Policy |

### Inconsistency Details (🔴)
1. **CR-03**: Terms of Service specifies collection of "phone number"; missing from Privacy Policy
   - Fix: Add "phone number" to Privacy Policy collection items

### Improvement Recommendations (🟡)
1. **CR-08**: Terms of Service uses "member"; Refund Policy uses "user"
   - Fix: Unify to "member"
```

## Version Control Rules

```
Document version synchronisation:
  - When any one document is changed, related documents must be reviewed
  - Set identical effective dates
  - Record cross-impact documents in the change history table
  - Keep previous versions accessible for at least 30 days
```

## References

- Cross-application of E-Commerce Act, Terms Regulation Act, and Personal Information Protection Act
- Detailed checklist: see `references/cross-check-templates.md`
