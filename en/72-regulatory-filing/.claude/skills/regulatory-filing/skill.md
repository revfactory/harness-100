---
name: regulatory-filing
description: "A full pipeline where an agent team collaborates to handle the entire process from requirements research to submission checklists for regulatory permits and filings. Use this skill for all document preparation related to permits, filings, and registrations — including requests like 'prepare permit documents', 'business registration documents', 'business license application', 'building permit preparation', 'food manufacturing permit', 'medical device licensing', 'prepare filing documents', 'required document list', 'permit requirements research', 'submission checklist'. Also supports validation and supplementation of existing documents. However, acting as a representative for electronic civil affairs submissions at administrative agencies, providing legal advice (replacing attorneys/administrative agents), or representing in administrative appeals/litigation is outside the scope of this skill."
---

# Regulatory Filing — Full Permit & Filing Pipeline

An agent team collaborates to generate the complete pipeline in one pass: requirements research → required document list → application drafting → attachment preparation → submission checklist.

## Execution Modes

**Agent Team** — 4 agents communicate directly via SendMessage and perform cross-validation.

## Agent Composition

| Agent | File | Role | Type |
|---------|------|------|------|
| requirements-investigator | `.claude/agents/requirements-investigator.md` | Laws & requirements research, required document list | general-purpose |
| document-drafter | `.claude/agents/document-drafter.md` | Application forms, business plans, form drafting | general-purpose |
| attachment-preparer | `.claude/agents/attachment-preparer.md` | Attachment preparation guide, consistency checks | general-purpose |
| submission-verifier | `.claude/agents/submission-verifier.md` | Final verification, submission checklist | general-purpose |

## Workflow

### Phase 1: Preparation (Orchestrator performs directly)

1. Extract from user input:
    - **Permit type**: What permit/registration/filing is being sought
    - **Industry/business content**: Specific business area
    - **Business location info** (optional): Address, area, facility status
    - **Applicant info** (optional): Individual/corporation, qualifications, experience
    - **Existing documents** (optional): Documents already prepared
2. Create a `_workspace/` directory at the project root
3. Organize the input and save to `_workspace/00_input.md`
4. If existing documents are provided, copy them to `_workspace/` and skip the corresponding phase
5. **Determine execution mode** based on the scope of the request (see "Mode by Task Scale" below)

### Phase 2: Team Formation and Execution

| Order | Task | Owner | Depends On | Output |
|------|------|------|------|--------|
| 1 | Requirements research & document list | investigator | None | `_workspace/01_requirements_research.md`, `_workspace/02_document_list.md` |
| 2a | Application form drafting | drafter | Task 1 | `_workspace/03_application_draft.md` |
| 2b | Attachment preparation guide | preparer | Task 1 | `_workspace/04_attachments_guide.md` |
| 3 | Submission verification & checklist | verifier | Tasks 2a, 2b | `_workspace/05_submission_checklist.md` |

Tasks 2a (application drafting) and 2b (attachment preparation) are executed **in parallel**.

**Team communication flow:**
- investigator completes → sends form types & entry notes to drafter, sends required document list & issuing offices to preparer
- drafter completes → sends entered figures & names to preparer (for consistency check), sends completed documents to verifier
- preparer completes → sends document preparation status & consistency check results to verifier
- verifier cross-validates all outputs. If 🔴 rejection reasons are found, sends correction requests to the relevant agent → rework → re-verification (maximum 2 times)

### Phase 3: Integration and Final Output

1. Review all files in `_workspace/`
2. Confirm all 🔴 rejection reasons in the verification report have been resolved
3. Report final summary to the user:
    - Requirements research report — `01_requirements_research.md`
    - Required document list — `02_document_list.md`
    - Application draft — `03_application_draft.md`
    - Attachment guide — `04_attachments_guide.md`
    - Submission checklist — `05_submission_checklist.md`

## Mode by Task Scale

| User Request Pattern | Execution Mode | Agents Deployed |
|----------------|----------|-------------|
| "Prepare the full set of permit documents" | **Full Pipeline** | All 4 agents |
| "Just tell me what documents I need" | **Requirements Research Mode** | investigator only |
| "Review this application" (existing file) | **Verification Mode** | verifier only |
| "Just draft the application" (requirements already known) | **Drafting Mode** | drafter + verifier |
| "Tell me how to prepare the attachments" | **Document Preparation Mode** | investigator + preparer |

**Leveraging existing files**: If the user provides existing documents, copy those files to the appropriate location in `_workspace/` and skip the corresponding agent's phase.

## Data Transfer Protocol

| Strategy | Method | Purpose |
|------|------|------|
| File-based | `_workspace/` directory | Storing and sharing primary outputs |
| Message-based | SendMessage | Real-time key information delivery, correction requests |
| Task-based | TaskCreate/TaskUpdate | Progress tracking, dependency management |

File naming convention: `{sequence}_{agent}_{output}.{extension}`

## Error Handling

| Error Type | Strategy |
|----------|------|
| Web search failure | Work from general legal knowledge base; note "verification of current regulations required" in the report |
| Ambiguous regulations | List multiple interpretations; recommend preliminary consultation with the competent authority |
| Insufficient user information | Insert placeholders + entry guide; provide a summary of unfilled items |
| Agent failure | Retry once → if still failing, proceed without that output; note the omission in the checklist |
| 🔴 found during verification | Send correction request to the relevant agent → rework → re-verification (maximum 2 times) |

## Test Scenarios

### Normal Flow
**Prompt**: "I want to get a general restaurant business license in Seoul — create all the documents I need and tell me how to prepare them"
**Expected result**:
- Requirements research: Legal basis in the Food Sanitation Act, competent district office public health division, personal and facility requirements
- Required documents: Business license application, food hygiene training certificate, building register, water quality test report, etc.
- Application: Draft application per official form + guidance on items the user must fill in
- Attachments: Issuing office, cost, processing time, and validity period for each document
- Checklist: Completeness and consistency verification of all documents + submission order

### Existing File Flow
**Prompt**: "Please review this application draft and let me know if any documents are missing" + application file attached
**Expected result**:
- Copy existing application to `_workspace/03_application_draft.md`
- Verification mode: investigator + verifier deployed
- drafter, preparer are skipped (verifier may request supplements as needed)

### Error Flow
**Prompt**: "I want to register a cosmetics manufacturing business — can you prepare the documents? I haven't signed a lease yet."
**Expected result**:
- After researching facility requirements, distinguish between "documents that can be prepared before securing a location" vs. "documents to prepare after securing a location"
- Items related to the business location are handled with placeholders
- A separate section in the checklist for "items requiring follow-up after securing a location"

## Per-Agent Extended Skills

| Agent | Extended Skill | Purpose |
|---------|----------|------|
| requirements-investigator, submission-verifier | `permit-requirements-db` | Industry-specific permit requirements DB, document issuing office guide |
| document-drafter, attachment-preparer | `form-filling-guide` | Administrative form entry guide, document quality standards |
