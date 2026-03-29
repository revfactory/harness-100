---
name: wedding-planner
description: "A pipeline where an agent team collaborates to comprehensively plan wedding preparation. Use this skill for all wedding preparation topics: 'help me plan my wedding', 'wedding plan', 'wedding budget', 'wedding hall recommendation', 'studio/dress/makeup comparison', 'invitation wording', 'wedding checklist', 'honeymoon plan', 'betrothal gifts preparation', 'trousseau list', 'wedding timeline', and similar requests. Partial support is available when only specific items are needed. However, actual vendor booking, payment processing, and marriage registration filing are outside this skill's scope."
---

# Wedding Planner — Comprehensive Wedding Preparation Pipeline

An agent team collaborates to generate the timeline, budget table, vendor comparison table, checklist, and invitation wording all at once.

## Execution Mode

**Agent team** — 5 agents communicate directly via SendMessage and cross-verify each other's work.

## Agent Composition

| Agent | File | Role | Type |
|-------|------|------|------|
| timeline-designer | `.claude/agents/timeline-designer.md` | D-day countdown, monthly schedule | general-purpose |
| budget-controller | `.claude/agents/budget-controller.md` | Budget allocation, cost reduction | general-purpose |
| vendor-analyst | `.claude/agents/vendor-analyst.md` | Vendor research, comparison table | general-purpose |
| checklist-builder | `.claude/agents/checklist-builder.md` | Checklist, invitation wording | general-purpose |
| wedding-reviewer | `.claude/agents/wedding-reviewer.md` | Cross-verification, consistency check | general-purpose |

## Workflow

### Phase 1: Preparation (Orchestrator performs directly)

1. Extract from user input:
    - **Wedding date**: D-day or target period
    - **Wedding type** (optional): Wedding hall / hotel / outdoor / small wedding
    - **Budget** (optional): Total budget or per-category budget
    - **Guest count** (optional): Expected number of guests
    - **Special requests** (optional): Region, style, religion, etc.
    - **Existing files** (optional): Existing checklist, budget table, etc.
2. Create the `_workspace/` directory at the project root
3. Organize input and save to `_workspace/00_input.md`
4. If existing files are provided, copy them to `_workspace/` and skip the corresponding phase
5. Determine the **execution mode** based on the scope of the request

### Phase 2: Team Assembly and Execution

| Order | Task | Responsible | Dependency | Deliverable |
|-------|------|-------------|------------|-------------|
| 1 | Timeline design | timeline | None | `_workspace/01_timeline.md` |
| 2a | Budget management | budget | Task 1 | `_workspace/02_budget.md` |
| 2b | Vendor comparison | vendor | Task 1 | `_workspace/03_vendor_comparison.md` |
| 3 | Checklist and invitations | checklist | Tasks 1, 2a, 2b | `_workspace/04_checklist_invitation.md` |
| 4 | Comprehensive review | reviewer | Tasks 1–3 | `_workspace/05_review_report.md` |

Tasks 2a (budget) and 2b (vendor) are **executed in parallel**. Both depend only on Task 1 (timeline), so they can start simultaneously.

**Inter-team communication flow:**
- timeline completes → delivers expenditure timing to budget, booking periods to vendor, monthly tasks to checklist
- budget ↔ vendor: coordinate budget limits against vendor pricing
- checklist integrates results from timeline + budget + vendor to produce the checklist
- reviewer cross-verifies all deliverables. When a 🔴 required fix is found, request revision from the relevant agent → rework → re-verify (up to 2 rounds)

### Phase 3: Integration and Final Deliverables

1. Verify all files in `_workspace/`
2. Confirm all 🔴 required fixes from the review report have been addressed
3. Report the final summary to the user

## Mode by Request Scope

| User Request Pattern | Execution Mode | Agents Deployed |
|----------------------|----------------|-----------------|
| "Help me with all wedding preparation" | **Full pipeline** | All 5 agents |
| "Just build me a wedding timeline" | **Timeline mode** | timeline + reviewer |
| "Help me organize the wedding budget" | **Budget mode** | timeline + budget + reviewer |
| "Compare wedding halls for me" | **Vendor mode** | vendor + reviewer |
| "Write invitation wording for me" | **Wording mode** | checklist + reviewer |
| "Review this wedding plan" | **Review mode** | reviewer only |

**Using existing files**: If the user provides an existing budget table, vendor list, etc., skip the corresponding step.

## Data Transfer Protocol

| Strategy | Method | Purpose |
|----------|--------|---------|
| File-based | `_workspace/` directory | Store and share major deliverables |
| Message-based | SendMessage | Real-time key information transfer, revision requests |
| Task-based | TaskCreate/TaskUpdate | Progress tracking, dependency management |

File naming convention: `{sequence}_{agent}_{deliverable}.{extension}`

## Error Handling

| Error Type | Strategy |
|------------|----------|
| Wedding date not set | Present two scenarios: 6 months and 12 months from now |
| Budget not provided | Proceed based on Korean average wedding costs; note "budget confirmation needed" |
| Web search failure | Work from general market rates; note "latest information should be verified" |
| Agent failure | Retry once → if it fails, proceed without that deliverable and note the gap in the review report |
| 🔴 finding in review | Request revision from the relevant agent → rework → re-verify (up to 2 rounds) |

## Test Scenarios

### Normal Flow
**Prompt**: "I'm getting married in May next year. About 200 guests, total budget ₩50,000,000. Looking for a wedding hall in Gangnam, Seoul."
**Expected result**:
- Timeline: D-12 month countdown schedule; emphasize early booking given May peak season
- Budget: ₩50,000,000 allocated by category; high catering proportion (200 guests)
- Vendor: Compare 3 Gangnam wedding halls; recommend studio/dress/makeup
- Checklist: Full checklist + 4 invitation wording styles
- Review: All items in consistency matrix verified

### Existing File Utilization Flow
**Prompt**: "We've already decided on the wedding hall and studio/dress/makeup. Help us organize the rest of the checklist and budget."
**Expected result**:
- Record existing decisions in `_workspace/`
- Deploy budget + checklist + reviewer
- Simplify timeline; skip vendor

### Error Flow
**Prompt**: "What should I start with for wedding preparation? We haven't decided anything yet."
**Expected result**:
- Date not set → timeline presents two scenarios: 6 months and 12 months
- Budget not set → budget presents average cost ranges by scale
- Provide a guide for the first steps (agreeing on date and budget)

## Extension Skills by Agent

| Agent | Extension Skill | Purpose |
|-------|-----------------|---------|
| vendor-analyst, budget-controller | `vendor-negotiation-guide` | Vendor comparison matrix, pricing reference table, negotiation strategies |
| budget-controller, wedding-reviewer | `wedding-budget-optimizer` | Budget allocation formulas, cost reference table, savings strategies |
