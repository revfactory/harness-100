---
name: brand-identity
description: "A full branding pipeline where an agent team collaborates to design brand identity all at once, from naming through slogans, tone and manner, and visual guidelines. Use this skill for 'create a brand,' 'brand identity design,' 'brand naming,' 'create a slogan,' 'brand guidelines,' 'logo concept,' 'tone and manner design,' 'brand strategy,' and all other brand identity tasks. Also supports slogan/visual design when an existing brand name is provided. Note: actual logo file production (.ai, .svg), print mock-ups, and trademark filing are outside this skill's scope."
---

# Brand Identity — Full Brand Identity Design Pipeline

Collaboratively design a brand's strategy, naming, verbal identity, and visual identity through an agent team, all in one pass.

## Execution Mode

**Agent Team** — Five agents communicate directly via SendMessage and cross-validate each other's work.

## Agent Roster

| Agent | File | Role | Type |
|-------|------|------|------|
| brand-strategist | `.claude/agents/brand-strategist.md` | Market analysis, positioning, archetypes | general-purpose |
| naming-specialist | `.claude/agents/naming-specialist.md` | Brand name development, domain/trademark review | general-purpose |
| copywriter | `.claude/agents/copywriter.md` | Slogans, tone and manner, brand story | general-purpose |
| visual-director | `.claude/agents/visual-director.md` | Colour, typography, logo concepts | general-purpose |
| identity-reviewer | `.claude/agents/identity-reviewer.md` | Cross-validation, consistency checks | general-purpose |

## Workflow

### Phase 1: Preparation (Performed Directly by the Orchestrator)

1. Extract from user input:
   - **Business Domain**: What product/service?
   - **Target Customer** (optional): Core customer segment
   - **Competitors** (optional): Brands to benchmark
   - **Brand Direction** (optional): Desired image, keywords
   - **Existing Elements** (optional): Already-finalized brand name, colours, etc.
2. Create the `_workspace/` directory at the project root
3. Organise the input and save it to `_workspace/00_input.md`
4. If existing files are available, copy them to `_workspace/` and skip the corresponding phase
5. Determine the **execution mode** based on the scope of the request

### Phase 2: Team Assembly and Execution

| Order | Task | Owner | Dependency | Deliverable |
|-------|------|-------|------------|-------------|
| 1 | Brand strategy | brand-strategist | None | `_workspace/01_brand_strategy.md` |
| 2 | Naming development | naming-specialist | Task 1 | `_workspace/02_naming_candidates.md` |
| 3a | Verbal identity | copywriter | Tasks 1, 2 | `_workspace/03_verbal_identity.md` |
| 3b | Visual identity | visual-director | Tasks 1, 2 | `_workspace/04_visual_identity.md` |
| 4 | Identity review | identity-reviewer | Tasks 2, 3a, 3b | `_workspace/05_review_report.md` |

Tasks 3a (verbal) and 3b (visual) run **in parallel**. Both depend on Task 2 (naming), so they can start simultaneously once naming is complete.

**Inter-agent communication flow:**
- brand-strategist completes -> delivers essence, archetype, and competitive analysis to naming-specialist; mission/vision/target to copywriter; archetype and positioning to visual-director
- naming-specialist completes -> delivers TOP 5 names + meanings to copywriter; visual characteristics of names to visual-director
- copywriter <-> visual-director: coordinate tone and manner with visual mood for consistency
- reviewer cross-validates all deliverables. On RED Must Fix findings, sends revision requests to the relevant agent -> rework -> re-validate (up to 2 cycles)

### Phase 3: Integration and Final Deliverables

1. Verify all files in `_workspace/`
2. Confirm that all RED Must Fix items from the review report have been addressed
3. Report the final summary to the user:
   - Brand strategy — `01_brand_strategy.md`
   - Naming candidates — `02_naming_candidates.md`
   - Verbal identity — `03_verbal_identity.md`
   - Visual identity — `04_visual_identity.md`
   - Review report — `05_review_report.md`

## Execution Modes by Scope

| User Request Pattern | Execution Mode | Agents Deployed |
|---------------------|---------------|----------------|
| "Full brand identity design," "full branding" | **Full Pipeline** | All 5 agents |
| "Just do the naming" | **Naming Mode** | brand-strategist + naming-specialist + identity-reviewer |
| "Create a slogan for this brand name" (existing name) | **Verbal Mode** | copywriter + identity-reviewer |
| "Create visual guidelines" (existing brand) | **Visual Mode** | visual-director + identity-reviewer |
| "Review this brand guideline" | **Review Mode** | identity-reviewer only |

**Using Existing Files**: If the user provides an existing brand name, guidelines, etc., copy them to `_workspace/` and skip the corresponding phase.

## Data Transfer Protocol

| Strategy | Method | Use Case |
|----------|--------|----------|
| File-based | `_workspace/` directory | Store and share major deliverables |
| Message-based | SendMessage | Real-time key information delivery, revision requests |
| Task-based | TaskCreate/TaskUpdate | Progress tracking, dependency management |

File naming convention: `{order_number}_{deliverable}.{extension}`

## Error Handling

| Error Type | Strategy |
|-----------|----------|
| Web search failure | Strategist works from general knowledge; note "Real-time market data not reflected" |
| Domain/trademark verification unavailable | Mark as "[Verification Needed]"; recommend user verify directly |
| Image generation failure | Proceed with text concepts + prompts only; user can retry |
| Agent failure | Retry once -> if still failing, proceed without that deliverable; note the gap in the review report |
| RED found in review | Send revision request to relevant agent -> rework -> re-validate (up to 2 cycles) |

## Test Scenarios

### Normal Flow
**Prompt**: "I want to create an eco-friendly household goods brand. Targeting women aged 20-30, premium positioning. Design the brand identity."
**Expected Result**:
- Strategy: Eco-friendly market analysis, 3+ competitive benchmarks, persona, archetype (Caregiver/Explorer)
- Naming: 10+ candidates narrowed to TOP 5, domain/trademark review, evaluation matrix
- Verbal: 5+ slogans, tagline, brand story (3 versions), tone and manner guide
- Visual: Colour palette (nature tones), typography, 2+ logo concepts, application examples
- Review: Consistency score, alignment matrix, touchpoint simulation

### Existing File Flow
**Prompt**: "The brand name is 'Greenleaf.' Create a slogan and visual guidelines."
**Expected Result**:
- Record existing name in `_workspace/02_naming_candidates.md`
- Merged verbal + visual mode: deploy copywriter + visual-director + identity-reviewer
- brand-strategist builds minimal strategy only; naming-specialist is skipped

### Error Flow
**Prompt**: "Create a brand, any field is fine"
**Expected Result**:
- Strategist proposes 3 business domains + positioning directions
- Proceed with full pipeline after user selection
- Review report notes "Proceeded based on user selection"

## Agent Extension Skills

Each agent leverages the following extension skills to enhance deliverable quality:

| Agent | Extension Skill | Knowledge Provided |
|-------|----------------|-------------------|
| naming-specialist | `/naming-methodology` | 12 naming techniques, SMILE evaluation, phonological analysis, domain/trademark review |
| visual-director | `/color-psychology` | Color-emotion mapping, 60-30-10 rule, accessibility standards, palette construction |
| brand-strategist, copywriter | `/brand-archetype` | 12 archetype mapping, tone-and-voice conversion, 5-chapter brand story structure |
