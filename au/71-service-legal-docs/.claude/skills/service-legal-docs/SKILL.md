---
name: service-legal-docs
description: "Full pipeline for generating a service legal document set. An agent team collaborates to generate Terms of Service → Privacy Policy → Cookie Policy → Refund Policy → Copyright Notice all at once. Use this skill for any service legal document creation including: 'create service terms', 'write terms of service', 'privacy policy', 'legal document set', 'service launch legal documents', 'terms package', 'write refund policy', 'cookie policy', 'copyright notice', 'legal document package', etc. Note: actual legal counsel (attorney review), terms review (fair trade commission), legal dispute response, and notarization of legal documents are outside the scope of this skill."
---

# Service Legal Docs — Service Legal Document Set Generation Pipeline

Generates all legal documents required for service launch: Terms of Service, Privacy Policy, Cookie Policy, Refund Policy, and Copyright Notice.

## Execution Modes

**Agent Team** — 4 members communicate directly via SendMessage and perform cross-validation.

## Agent Configuration

| Agent | File | Role | Type |
|---------|------|------|------|
| tos-specialist | `.claude/agents/tos-specialist.md` | Terms of Service, unfair terms prevention | general-purpose |
| privacy-specialist | `.claude/agents/privacy-specialist.md` | Privacy policy, cookie policy, consent framework | general-purpose |
| consumer-analyst | `.claude/agents/consumer-analyst.md` | Refund policy, copyright notice | general-purpose |
| consistency-reviewer | `.claude/agents/consistency-reviewer.md` | Cross-document consistency, final QA | general-purpose |

## Workflow

### Phase 1: Preparation (Orchestrator performs directly)

1. Extract from user input:
    - **Service Name**: Company/service name
    - **Service Type**: SaaS, e-commerce, content platform, community, etc.
    - **Service Region**: Domestic, global (including EU or not)
    - **Payment**: Paid/free/freemium (in-app purchases, subscriptions)
    - **Personal Data Collected** (optional): List of data collected
    - **Existing Materials** (optional): Current terms, privacy policy, etc.
2. Create `_workspace/` directory in the project root
3. Organise input and save to `_workspace/00_input.md`
4. **Determine execution mode** based on request scope

### Phase 2: Team Formation and Execution

| Order | Task | Owner | Depends On | Output |
|------|------|------|------|--------|
| 1a | Terms of Service | tos-specialist | None | `_workspace/01_terms_of_service.md` |
| 1b | Privacy Policy + Cookie Policy | privacy-specialist | None | `_workspace/02_privacy_policy.md`, `_workspace/03_cookie_policy.md` |
| 1c | Refund Policy + Copyright Notice | consumer-analyst | None | `_workspace/04_refund_policy.md`, `_workspace/05_copyright_notice.md` |
| 2 | Consistency Review | consistency-reviewer | Tasks 1a, 1b, 1c | `_workspace/06_review_report.md` |

Tasks 1a, 1b, and 1c are executed **in parallel**. All three agents can work independently. However, agents communicate with each other during work to ensure cross-document alignment.

**Inter-team Communication Flow:**
- tos-specialist ↔ privacy-specialist: Coordinate privacy-related terms clauses
- tos-specialist ↔ consumer-analyst: Coordinate refund, cancellation, and copyright clauses
- privacy-specialist ↔ consumer-analyst: Coordinate personal data processing during payment and refund
- consistency-reviewer cross-validates all outputs. If 🔴 critical issues are found, revision requests are sent to the relevant agent (maximum 2 times)

### Phase 3: Integration and Final Output

1. Verify all files in `_workspace/`
2. Confirm all 🔴 critical issues from the review report have been addressed
3. Report final summary to the user:
    - Terms of Service — `01_terms_of_service.md`
    - Privacy Policy — `02_privacy_policy.md`
    - Cookie Policy — `03_cookie_policy.md`
    - Refund Policy — `04_refund_policy.md`
    - Copyright Notice — `05_copyright_notice.md`
    - Review Report — `06_review_report.md`

## Mode by Request Scope

| User Request Pattern | Execution Mode | Agents Involved |
|----------------|----------|-------------|
| "Full legal document set", "Create terms package" | **Full Pipeline** | All 4 agents |
| "Write terms of service only" | **Terms Mode** | tos-specialist + reviewer |
| "Write privacy policy only" | **Privacy Policy Mode** | privacy-specialist + reviewer |
| "Create refund policy only" | **Refund Policy Mode** | consumer-analyst + reviewer |
| "Review existing terms" | **Review Mode** | consistency-reviewer only |

**Using Existing Files**: If the user provides existing terms, privacy policy, etc., copy the relevant files to the appropriate numbered location in `_workspace/` and skip the corresponding agent.

## Data Transfer Protocol

| Strategy | Method | Purpose |
|------|------|------|
| File-based | `_workspace/` directory | Store and share primary outputs |
| Message-based | SendMessage | Real-time clause coordination, revision requests |

Filename convention: `{sequence}_{document_type}.{extension}`

## Error Handling

| Error Type | Strategy |
|----------|------|
| Insufficient service information | Draft based on general online service standards, note "service customisation required" |
| Agent failure | 1 retry → if still failing, proceed without that document and note the omission in the review report |
| 🔴 issues found in review | Send revision request to relevant agent → rework → re-review (maximum 2 times) |
| Cross-document contradictions found | consistency-reviewer proposes resolution direction, simultaneously requests revision from related agents |
| Unverified legal amendments | Note "latest law verification required", recommend legal counsel |

## Test Scenarios

### Normal Flow
**Prompt**: "I'm preparing to launch a SaaS service and need the full legal document set. The service is called TaskFlow, it's a monthly subscription model, and we collect email, name, and phone number at signup."
**Expected Result**:
- Terms of Service: SaaS-specific clauses (subscription, service level, data ownership, etc.)
- Privacy Policy: Reflects email/name/phone number collection items
- Cookie Policy: Cookie type classification based on web service standards
- Refund Policy: Subscription model-specific withdrawal criteria
- Copyright Notice: SaaS content copyright provisions
- Review: Cross-document consistency verified across all 6 documents

### Partial Flow
**Prompt**: "I already have the terms of service, just write the privacy policy"
**Expected Result**:
- Switches to Privacy Policy Mode (privacy-specialist + reviewer)
- References existing terms for consistency verification

### Error Flow
**Prompt**: "Create service terms, it's an app but I'll give you the details later"
**Expected Result**:
- Full pipeline executes based on general mobile app standards
- All documents include "[Verification Required]" markers for items requiring service customisation
- Review report includes "Document update required after confirming service details"

## Agent Extended Skills

| Agent | Extended Skill | Purpose |
|---------|----------|------|
| tos-specialist, consistency-reviewer | `unfair-terms-detector` | Detect unfair terms, check for terms law violations |
| consistency-reviewer, all agents | `cross-document-linker` | Cross-document referencing, consistency management |
