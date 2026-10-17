---
name: presentation-designer
description: "of Planning, Storyboard, Slide Deck, Speaker notes an agent team collaborates to in production to line. ' ', 'Presentation Planning', 'PPT composition', 'Slide Deck ', 'Presentation and', ' ', ' Deck', ' Slide', 'Presentation vs ', ' Presentation ' etc. production beforein . casein Presentation Coaching . , PowerPoint/Keynote File , Slide to, Presentation of ."
---

# Presentation Designer — Presentation Full Production Pipeline

An agent team collaborates to produce presentation planning, storyboards, slides, and speaker notes all at once.

## Execution Mode

**Agent Team** — 5 members communicate directly via SendMessage and cross-validate each other's work.

## Agent Composition

| Agent | File | Role | Type |
|---------|------|------|------|
| storyteller | `.claude/agents/storyteller.md` | Message Structure, Logic Flow Design | general-purpose |
| info-architect | `.claude/agents/info-architect.md` | Visualisation, Information Hierarchy Design | general-purpose |
| visual-designer | `.claude/agents/visual-designer.md` | Slide Layout, design system | general-purpose |
| presentation-coach | `.claude/agents/presentation-coach.md` | Speaker notes, Timing, Q&A | general-purpose |
| deck-reviewer | `.claude/agents/deck-reviewer.md` | cross-validate, Verification | general-purpose |

## Workflow

### Phase 1: Preparation (Performed Directly by the Orchestrator)

1. Extract from user input:
 - **Presentation **: within
 - **Audience Information** (Selection): Audienceof background, expectations, decision-making authority
 - **Presentation whenbetween** (Selection): goal whenbetween
 - **Presentation Format** (Selection): //Suggestion//
 - ** File** (Selection): , 
2. `_workspace/` to in generate
3. Organise input and save to `_workspace/00_input.md`in save
4. If existing files are present `_workspace/`, copy to _workspace/ and skip the corresponding Phase
5. Based on the scope of the request **determine the execution mode** ( " per mode" )

### Phase 2: Team Assembly and Execution

 compositionand . between of relationship and :

| sequence | | | of | |
|------|------|------|------|--------|
| 1 | Story Structure Design | storyteller | None | `_workspace/01_story_structure.md` |
| 2 | Information Design | info-architect | 1 | `_workspace/02_info_design.md` |
| 3 | Slide Deck production | visual-designer | 1, 2 | `_workspace/03_slide_deck.md` |
| 4a | Speaker notes Writing | presentation-coach | 1, 3 | `_workspace/04_speaker_notes.md` |
| 4b | Deck Review | deck-reviewer | 2, 3, 4a | `_workspace/05_review_report.md` |

**Inter-team communication flow:**
- storyteller complete -> info-architectTo Visualisation Slide before, visual-designerTo before, coachTo before before
- info-architect complete -> visual-designerTo Chart Style·Colour before, coachTo description before
- visual-designer complete -> coachTo Slide before Timing before
- reviewer cross-validate. 🔴 Must Fix when AgentTo → → Verification (vs 2)

### Phase 3: Integration and Final Deliverables

Reviewof based on :

1. `_workspace/` within File verify
2. from the review report 🔴 Must Fix reflected verify
3. summary To :
 - Story Structure — `01_story_structure.md`
 - Information Design — `02_info_design.md`
 - Slide Deck — `03_slide_deck.md`
 - Speaker notes — `04_speaker_notes.md`
 - Review — `05_review_report.md`

## Modes by Task Scale

 of in Agent :

| Pattern | mode | Agent |
|----------------|----------|-------------|
| " ", " Deck" | **Full Pipeline** | 5 All |
| "Presentation Storyboard " | **Story mode** | storyteller + reviewer |
| " to Slide " ( within) | **Slide mode** | info-architect + visual-designer + reviewer |
| "Presentation and" ( Slide) | **Coaching mode** | coach + reviewer |
| " " | **Review mode** | reviewer only |

**Using Existing Files**: , copy the files to `_workspace/`of in and of Agent .

## Data Transfer Protocol

| Strategy | | |
|------|------|------|
| File-Based | `_workspace/` | Storing and sharing major deliverables |
| Message-Based | SendMessage | Real-time delivery of key information, revision requests |
| Task-Based | TaskCreate/TaskUpdate | Progress tracking, dependency management |

File naming convention: `{}_{Agent}_{}.{}`

## Error Handling

| in type | Strategy |
|----------|------|
| Audience Information | Audience , in the report "Audience " when |
| Presentation whenbetween | 15(15Slide) application |
| | to Chart Structure Design, when |
| Agent failure | 1 retry -> if still fails, proceed without that deliverable, note omission in review report |
| RED found in review | Request revision from relevant agent -> rework -> re-verify (up to 2 times) |

## Test Scenarios

### Normal Flow
**Prompt**: " SaaS Deck 20 to . Audience when A "
**Expected Result**:
- Story Structure: arc(→→market→Model→→), Emotion Curve
- Information Design: market Chart, , Competitive matrix
- Slide Deck: 20 within, design system definition, Slideper Layout
- Speaker notes: Slideper , Timing , Q&A 10
- Review: matrix before Verification

### Existing File Utilisation Flow
**Prompt**: " withinto Slide " + File
**Expected Result**:
- `_workspace/`in 
- Slide mode: info-architect + visual-designer + reviewer 
- storyteller Structure based on between Story , coach 

### Error Flow
**Prompt**: "Presentation , AI "
**Expected Result**:
- Full Pipelineto , Audience/whenbetween to application
- storyteller Audience , 15 
- Review in the report "Audience/whenbetween application" when

## Extended Skills per Agent

per Agentof before Extended Skill:

| | subject Agent | Role |
|------|-------------|------|
| `slide-layout-patterns` | visual-designer | 20 Slide Layout, grid system, |
| `data-visualization-guide` | info-architect | Chart Selection matrix, Information Hierarchy(LATCH), Colour |
