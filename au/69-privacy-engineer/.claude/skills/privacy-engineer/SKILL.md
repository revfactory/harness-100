---
name: privacy-engineer
description: "Full privacy engineering pipeline. An agent team collaborates to perform GDPR/PIPA analysis → PIA → consent forms → process design in a single run. Use this skill for all privacy-related needs including: 'privacy by design', 'GDPR compliance', 'privacy impact assessment', 'PIA execution', 'consent form drafting', 'privacy policy', 'privacy design', 'personal data protection law compliance', 'PIPA response', 'data protection framework', etc. Note: actual submissions to the Personal Information Protection Commission, legal litigation representation, ISMS-P certification audits, and physical security system implementation are outside the scope of this skill."
---

# Privacy Engineer — Privacy Engineering Pipeline

Systematically builds a service's privacy protection framework from legal analysis through process design.

## Execution Mode

**Agent Team** — 4 agents communicate directly via SendMessage and perform cross-validation.

## Agent Composition

| Agent | File | Role | Type |
|---------|------|------|------|
| privacy-law-analyst | `.claude/agents/privacy-law-analyst.md` | GDPR/PIPA analysis, applicability determination | general-purpose |
| pia-assessor | `.claude/agents/pia-assessor.md` | Privacy impact assessment, risk scoring | general-purpose |
| consent-designer | `.claude/agents/consent-designer.md` | Consent form design, notices, privacy policy | general-purpose |
| process-architect | `.claude/agents/process-architect.md` | Processing workflows, technical safeguards | general-purpose |

## Workflow

### Phase 1: Preparation (Orchestrator performs directly)

1. Extract from user input:
    - **Service name/type**: web, app, SaaS, e-commerce, etc.
    - **Data processed**: personal data items collected
    - **User regions**: domestic, EU, US, etc.
    - **Service scale**: number of users, data volume
    - **Existing materials** (optional): current privacy policy, consent forms, system architecture diagrams
2. Create a `_workspace/` directory at the project root
3. Organise inputs and save to `_workspace/00_input.md`
4. **Determine execution mode** based on request scope

### Phase 2: Team Assembly and Execution

| Step | Task | Owner | Depends On | Output |
|------|------|------|------|--------|
| 1 | Legal analysis | privacy-law-analyst | None | `_workspace/01_privacy_law_analysis.md` |
| 2 | PIA execution | pia-assessor | Step 1 | `_workspace/02_pia_report.md` |
| 3a | Consent form drafting | consent-designer | Steps 1, 2 | `_workspace/03_consent_documents.md` |
| 3b | Process design | process-architect | Steps 1, 2 | `_workspace/04_process_design.md` |

Steps 3a (consent) and 3b (process) run **in parallel**. Both depend on legal analysis and PIA, so they can start simultaneously after Step 2 completes.

**Inter-agent communication flow:**
- privacy-law-analyst completes → sends processing activity list and risk factors to pia-assessor
- pia-assessor completes → sends disclosure requirements to consent-designer, sends safeguard recommendations to process-architect
- consent-designer → sends consent collection timing and management requirements to process-architect
- process-architect cross-validates logical consistency across all outputs during final design

### Phase 3: Integration and Final Deliverables

1. Review all files in `_workspace/`
2. Verify consistency across legal analysis → PIA → consent forms → process design
3. Report final summary to user:
    - Legal analysis report — `01_privacy_law_analysis.md`
    - PIA report — `02_pia_report.md`
    - Consent forms and notices set — `03_consent_documents.md`
    - Process design document — `04_process_design.md`

## Modes by Task Scope

| User Request Pattern | Execution Mode | Agents Engaged |
|----------------|----------|-------------|
| "Design the full privacy protection framework", "Full privacy design" | **Full pipeline** | All 4 agents |
| "Analyse whether GDPR applies" | **Legal analysis mode** | privacy-law-analyst only |
| "Run PIA only" (legal analysis available) | **PIA mode** | pia-assessor |
| "Just draft the consent form" | **Consent mode** | consent-designer |
| "Just design the personal data processing workflow" | **Process mode** | process-architect |

## Data Handoff Protocol

| Strategy | Method | Purpose |
|------|------|------|
| File-based | `_workspace/` directory | Storing and sharing primary deliverables |
| Message-based | SendMessage | Real-time key information delivery, revision requests |

File naming convention: `{sequence}_{agent}_{deliverable}.{extension}`

## Error Handling

| Error Type | Strategy |
|----------|------|
| Web search failure | Legal analyst works from general knowledge, notes "latest guidelines not verified" |
| Insufficient service information | Assumes standard web service baseline, notes "assumption-based" |
| Uncertain GDPR applicability | Proceeds assuming GDPR applies, recommends separate confirmation |
| Agent failure | Retry once → if still failing, proceed without that deliverable, note omission in final report |
| Inconsistency between PIA and legal analysis | process-architect identifies inconsistency, applies conservative judgment |

## Test Scenarios

### Normal Flow
**Prompt**: "Design a privacy protection framework for a SaaS service that includes EU users. We process registration, payment, and marketing data."
**Expected result**:
- Legal analysis: simultaneous GDPR + PIPA application, mapping 10+ processing activities
- PIA: 15+ risk assessments, safeguard recommendations
- Consent forms: required/optional separation, GDPR valid consent requirements reflected, cross-border transfer consent
- Process: full lifecycle, technical safeguards, incident response framework

### Partial Flow
**Prompt**: "Just write a personal data collection consent form for our app"
**Expected result**:
- Switches to consent mode (consent-designer only)
- Drafts based on standard consent form template, notes that specific items require confirmation

### Error Flow
**Prompt**: "Design a privacy protection framework — we're a startup and don't know where to start"
**Expected result**:
- Full pipeline executes, asks follow-up questions due to insufficient service information
- Proceeds with assumptions based on typical startup baseline, notes "requires review once service details are confirmed"
- Prioritises minimum legal obligations (publishing privacy policy, obtaining consent) as first steps

## Per-Agent Extended Skills

| Agent | Extended Skill | Purpose |
|---------|----------|------|
| pia-assessor, process-architect | `data-flow-mapper` | Data flow mapping, risk point identification |
| privacy-law-analyst, consent-designer | `gdpr-pipa-cross-reference` | GDPR/PIPA article mapping, integrated compliance guide |
