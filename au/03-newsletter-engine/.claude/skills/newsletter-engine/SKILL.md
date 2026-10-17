---
name: newsletter-engine
description: "A full production pipeline where an agent team collaborates to generate newsletter content — curation, writing, A/B testing, and send optimisation — all at once. Use this skill for requests like 'write a newsletter,' 'newsletter planning,' 'email newsletter,' 'newsletter curation,' 'newsletter A/B test,' 'subscriber email,' 'weekly newsletter,' 'newsletter send optimisation,' and other newsletter production tasks. Also supports editing and optimisation when existing content is provided. Note: email sending system (Mailchimp, ConvertKit) API integration, subscriber database management, and actual A/B test execution are outside this skill's scope."
---

# Newsletter Engine — Full Newsletter Production Pipeline

An agent team collaborates to produce newsletters through the pipeline of curation → writing → A/B testing → editing → publishing, all at once.

## Execution Mode

**Agent Team** — 5 members communicate directly via SendMessage and cross-validate each other's work.

## Agent Roster

| Agent | File | Role | Type |
|-------|------|------|------|
| curator | `.claude/agents/curator.md` | Source collection, trend analysis, content selection | general-purpose |
| copywriter | `.claude/agents/copywriter.md` | Headlines, body copy, CTA writing | general-purpose |
| analyst | `.claude/agents/analyst.md` | A/B test design, send optimisation | general-purpose |
| editor-in-chief | `.claude/agents/editor-in-chief.md` | Tone consistency, final editing | general-purpose |
| quality-reviewer | `.claude/agents/quality-reviewer.md` | Cross-validation, consistency checks | general-purpose |

## Workflow

### Phase 1: Preparation (Performed directly by the orchestrator)

1. Extract from user input:
   - **Topic/Theme**: The subject the newsletter will cover
   - **Newsletter Info** (optional): Brand tone, subscriber count, publication frequency
   - **Target Reader** (optional): Subscriber characteristics, interests
   - **Constraints** (optional): Length, specific section requirements
   - **Existing Files** (optional): Content, previous issues, etc. provided by the user
2. Create the `_workspace/` directory at the project root
3. Organise the input and save it as `_workspace/00_input.md`
4. If existing files are provided, copy them to `_workspace/` and skip the corresponding phase
5. Determine the **execution mode** based on request scope

### Phase 2: Team Assembly and Execution

| Order | Task | Owner | Depends On | Deliverable |
|-------|------|-------|------------|-------------|
| 1 | Content curation | curator | None | `_workspace/01_curation_brief.md` |
| 2 | Newsletter writing | copywriter | Task 1 | `_workspace/02_newsletter_draft.md` |
| 3 | A/B test design | analyst | Tasks 1, 2 | `_workspace/03_ab_test_plan.md` |
| 4 | Final editing | editor-in-chief | Tasks 2, 3 | `_workspace/04_editorial_final.md` |
| 5 | Quality review | quality-reviewer | Tasks 2, 3, 4 | `_workspace/05_review_report.md` |

**Inter-agent communication flow:**
- curator complete → deliver angles & content to copywriter, trending keywords to analyst
- copywriter complete → deliver A/B variant materials to analyst, draft to editor-in-chief
- analyst complete → deliver send optimisation & A/B recommendations to editor-in-chief
- editor-in-chief complete → deliver final version to quality-reviewer
- reviewer cross-validates all deliverables. On 🔴 Must Fix: request revision → rework → re-validate (up to 2 rounds)

### Phase 3: Integration and Final Deliverables

1. Verify all files in `_workspace/`
2. Confirm all 🔴 Must Fix items have been addressed
3. Report the final summary to the user:
   - Curation Brief — `01_curation_brief.md`
   - Newsletter Draft — `02_newsletter_draft.md`
   - A/B Test Plan — `03_ab_test_plan.md`
   - Editor-in-Chief Final — `04_editorial_final.md`
   - Review Report — `05_review_report.md`

## Scope-Based Modes

| User Request Pattern | Execution Mode | Agents Deployed |
|---------------------|----------------|-----------------|
| "Plan a newsletter," "full production" | **Full Pipeline** | All 5 |
| "Just write the newsletter copy" | **Copy Mode** | curator + copywriter + quality-reviewer |
| "Make a newsletter from this content" (existing file) | **Edit Mode** | copywriter + editor-in-chief + quality-reviewer |
| "Design an A/B test" (existing newsletter) | **Analysis Mode** | analyst + quality-reviewer |
| "Review this newsletter" | **Review Mode** | quality-reviewer only |

**Using Existing Files**: If the user provides content or a previous newsletter, copy it to the appropriate location in `_workspace/` and skip that phase.

## Data Transfer Protocol

| Strategy | Method | Purpose |
|----------|--------|---------|
| File-based | `_workspace/` directory | Primary deliverable storage and sharing |
| Message-based | SendMessage | Real-time key information transfer, revision requests |
| Task-based | TaskCreate/TaskUpdate | Progress tracking, dependency management |

File naming convention: `{order}_{deliverable}.{extension}`

## Error Handling

| Error Type | Strategy |
|-----------|----------|
| Web search failure | Curator works from user-provided materials, notes "real-time data not reflected" |
| Brand tone unclear | Apply default tone (professional + friendly), editor-in-chief recommends tone refinement after first issue |
| Agent failure | Retry once → if still failing, proceed without that deliverable, note omission in review report |
| 🔴 found in review | Request revision from responsible agent → rework → re-validate (up to 2 rounds) |

## Test Scenarios

### Happy Path
**Prompt**: "Create a weekly newsletter covering AI industry trends. Target audience: developers. Tone: professional with wit"
**Expected Results**:
- Curation: 5+ latest AI articles, trend analysis, recommended resources
- Copy: Subject line (A/B 2 variants), preheader, intro + main story + sub stories + resources + closing
- Analysis: 2 A/B tests (subject line, CTA), send time recommendations, performance forecast
- Editorial: Tone review, legal check, final version
- Review: All consistency matrix items verified

### Existing File Flow
**Prompt**: "Make a newsletter from this collection of articles" + content file attached
**Expected Results**:
- Existing content organised into `_workspace/01_curation_brief.md`
- Edit Mode: copywriter + editor-in-chief + quality-reviewer deployed
- curator skipped

### Error Flow
**Prompt**: "Just design A/B tests for this newsletter subject line"
**Expected Results**:
- Switch to Analysis Mode (analyst + quality-reviewer)
- No newsletter body exists, so analyst proposes subject-line-pattern-based A/B variants
- Review report notes "body copy/curation not generated"

## Agent Extension Skills

Each agent leverages the following extension skills to enhance deliverable quality:

| Agent | Extension Skill | Knowledge Provided |
|-------|----------------|-------------------|
| copywriter | `/email-copywriting` | CURVE subject line framework, CTA design, F-pattern body structure |
| analyst, curator | `/audience-segmentation` | BEAR segmentation model, send time optimisation, welcome series |
| editor-in-chief, analyst | `/deliverability-optimization` | Spam filter avoidance, Gmail Promotions tab strategies, legal compliance |
