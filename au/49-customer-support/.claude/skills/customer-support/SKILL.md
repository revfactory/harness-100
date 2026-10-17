---
name: customer-support
description: "A full pipeline that systematizes a customer support system into FAQ, response manual, escalation policy, and CS analytics framework. Use this skill for requests like 'build a customer support system', 'write FAQs', 'response manual', 'CS manual', 'escalation policy', 'customer response scripts', 'complaint handling', 'customer complaint processing', 'CS operations system', 'customer service process', and other customer support system building needs. Also supports supplementing and improving existing FAQs or manuals. However, CRM/helpdesk software development, call centre infrastructure setup, real-time chatbot development, and agent recruitment are outside the scope of this skill."
---

# Customer Support — Customer Support System Building Pipeline

An agent team collaborates to generate FAQ, response manual, escalation policy, and analytics all at once.

## Execution Mode

**Agent Team** — 5 members communicate directly via SendMessage and perform cross-validation.

## Agent Composition

| Agent | File | Role | Type |
|-------|------|------|------|
| faq-builder | `.claude/agents/faq-builder.md` | FAQ construction, search optimisation | general-purpose |
| response-specialist | `.claude/agents/response-specialist.md` | Response scripts, tone & manner | general-purpose |
| escalation-manager | `.claude/agents/escalation-manager.md` | Escalation tiers, SLA | general-purpose |
| cs-analyst | `.claude/agents/cs-analyst.md` | Metrics, VOC, improvement proposals | general-purpose |
| cs-reviewer | `.claude/agents/cs-reviewer.md` | Cross-validation, customer journey simulation | general-purpose |

## Workflow

### Phase 1: Preparation (Performed directly by orchestrator)

1. Extract from user input:
    - **Service Information**: Product/service name, type, customer base size
    - **Support Channels**: Which channels are in use — phone/chat/email/social media
    - **Current State**: Whether an existing CS system exists, team size
    - **Existing Materials** (optional): Existing FAQs, manuals, data
2. Create `_workspace/` directory at the project root
3. Organise the input and save to `_workspace/00_input.md`
4. If existing files are provided, copy them to `_workspace/` and skip the corresponding Phase

### Phase 2: Team Assembly and Execution

| Order | Task | Assigned To | Dependencies | Deliverable |
|-------|------|-------------|-------------|-------------|
| 1a | FAQ Construction | faq-builder | None | `_workspace/01_faq.md` |
| 1b | Response Manual | response-specialist | None | `_workspace/02_response_manual.md` |
| 2 | Escalation Policy | escalation-manager | Tasks 1a, 1b | `_workspace/03_escalation_policy.md` |
| 3 | CS Analytics Framework | cs-analyst | Tasks 1a, 1b, 2 | `_workspace/04_cs_analytics.md` |
| 4 | CS Review | cs-reviewer | Tasks 1a, 1b, 2, 3 | `_workspace/05_review_report.md` |

Tasks 1a (FAQ) and 1b (Manual) are **executed in parallel**. Both can start simultaneously as they have no initial dependencies.

**Inter-team Communication Flow:**
- faq-builder completes → delivers out-of-FAQ-scope scenarios to response-specialist, delivers self-service boundary to escalation-manager
- response-specialist completes → delivers escalation trigger conditions to escalation-manager
- escalation-manager completes → delivers SLA metrics to cs-analyst
- cs-analyst completes → delivers all documents to cs-reviewer
- cs-reviewer cross-validates all deliverables. If 🔴 Must Fix items are found, sends revision requests to the relevant agent → rework → re-validate (up to 2 times)

### Phase 3: Integration and Final Deliverables

1. Verify all files in `_workspace/`
2. Confirm that all 🔴 Must Fix items from the review report have been addressed
3. Report the final summary to the user

## Execution Modes by Request Scale

| User Request Pattern | Execution Mode | Agents Deployed |
|---------------------|----------------|-----------------|
| "Build a customer support system", "Full CS setup" | **Full Pipeline** | All 5 |
| "Just create FAQs" | **FAQ Mode** | faq-builder + reviewer |
| "Write a response manual" | **Manual Mode** | response-specialist + reviewer |
| "Create an escalation policy" | **Escalation Mode** | escalation-manager + reviewer |
| "Design CS metrics" | **Analytics Mode** | cs-analyst + reviewer |
| "Review this FAQ" | **Review Mode** | reviewer only |

## Data Transfer Protocol

| Strategy | Method | Purpose |
|----------|--------|---------|
| File-based | `_workspace/` directory | Storing and sharing main deliverables |
| Message-based | SendMessage | Real-time key information transfer, revision requests |

## Error Handling

| Error Type | Strategy |
|-----------|----------|
| Insufficient service info | Build a generic CS system based on industry type, tag as "requires service customisation" |
| No existing CS data | Set targets based on industry benchmarks, propose initial measurement methods |
| Web search failure | Work from general CS best practices, note "data limited" |
| Agent failure | Retry once → if still fails, proceed without that deliverable, note the omission in the review report |
| 🔴 found in review | Send revision request to the relevant agent → rework → re-validate (up to 2 times) |

## Test Scenarios

### Normal Flow
**Prompt**: "Build a customer support system for a B2C SaaS project management tool. We have 10,000 monthly active users and operate chat and email channels. The CS team has 5 members."
**Expected Results**:
- FAQ: Sign-up/billing/features/integration categories, 30+ Q&As
- Manual: 5+ scenario scripts, channel-specific guides for chat + email
- Escalation: L1-L3 tiers, SLA matrix, crisis response protocol
- Analytics: CSAT/NPS/FCR/AHT metrics + weekly/monthly report templates
- Review: Includes 3 customer journey simulations

### Existing File Utilisation Flow
**Prompt**: "I have this FAQ; create a response manual and escalation policy" + FAQ file attached
**Expected Results**:
- Copy existing FAQ to `_workspace/01_faq.md`
- Skip faq-builder and deploy response-specialist + escalation-manager + cs-analyst + reviewer

### Error Flow
**Prompt**: "Create a customer support FAQ"
**Expected Results**:
- Switch to FAQ Mode (faq-builder + reviewer)
- If service info is insufficient, ask follow-up questions about industry/product type
- If only minimal info is provided, generate a generic SaaS FAQ template

## Agent Extension Skills

Extension skills that enhance agent domain expertise:

| Skill | File | Target Agents | Role |
|-------|------|---------------|------|
| csat-analyzer | `.claude/skills/csat-analyzer/skill.md` | cs-analyst, cs-reviewer | CSAT/NPS/CES design, operational metrics, VOC analysis, CS dashboard design |
| escalation-flowchart | `.claude/skills/escalation-flowchart/skill.md` | escalation-manager, response-specialist | L1/L2/L3 structure, severity classification, trigger conditions, SLA matrix, crisis response |
