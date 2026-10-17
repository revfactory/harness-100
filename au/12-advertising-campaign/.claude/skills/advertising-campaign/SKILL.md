---
name: advertising-campaign
description: "ad Campaignof TargetAnalysis, Copy, Creative Design, an agent team collaborates to in Campaign line. 'ad Campaign Planning', 'ad Copy ', ' ', 'banner ad ', ' ad Planning', 'search ad ', 'Target Analysis', 'ad Creative', 'SNS ad Strategy' etc. ad Campaign production beforein . Copy Creative casein Review . , ad Platform(Google Ads, Meta Business Suite) API , whenbetween and vswhen , ad production(/illustration) of ."
---

# Advertising Campaign — Advertising Campaign Full Production Pipeline

An agent team collaborates to generate advertising campaign target analysis, copy, creative, and media plans all at once.

## Execution Mode

**Agent Team** — 5 members communicate directly via SendMessage and cross-validate each other's work.

## Agent Composition

| Agent | File | Role | Type |
|---------|------|------|------|
| market-analyst | `.claude/agents/market-analyst.md` | Target Segmentation, Competitive Analysis, Insight Extraction | general-purpose |
| copywriter | `.claude/agents/copywriter.md` | line, Copy, CTA Writing | general-purpose |
| creative-director | `.claude/agents/creative-director.md` | Visual Concept, Storyboard, Image | general-purpose |
| media-planner | `.claude/agents/media-planner.md` | channel , Budget allocation, Schedule | general-purpose |
| campaign-reviewer | `.claude/agents/campaign-reviewer.md` | cross-validate, Verification | general-purpose |

## Workflow

### Phase 1: Preparation (Performed Directly by the Orchestrator)

1. Extract from user input:
 - **/**: ad subject
 - **Campaign goal**: //before/
 - **Budget** (Selection): Budget Budget
 - **between** (Selection): Campaign between
 - **channel** (Selection): channel
 - ** File** (Selection): Copy, Brand Guide etc.
2. `_workspace/` to in generate
3. Organise input and save to `_workspace/00_input.md`in save
4. If existing files are present `_workspace/`, copy to _workspace/ and skip the corresponding Phase
5. Based on the scope of the request **determine the execution mode** ( " per mode" )

### Phase 2: Team Assembly and Execution

 compositionand . between of relationship and :

| sequence | | | of | |
|------|------|------|------|--------|
| 1 | market·Target Analysis | analyst | None | `_workspace/01_market_analysis.md` |
| 2 | ad Copy Writing | copywriter | 1 | `_workspace/02_ad_copy.md` |
| 3a | Creative Design | creative | 1, 2 | `_workspace/03_creative_concept.md` |
| 3b | | planner | 1, 2 | `_workspace/04_media_plan.md` |
| 4 | Campaign Review | reviewer | 2, 3a, 3b | `_workspace/05_review_report.md` |

 3a(Creative)and 3b() **executed in parallel**. 1(Analysis)and 2(Copy)in ofto Copy after whenin when .

**Inter-team communication flow:**
- analyst complete -> copywriterTo Target Insight·USP before, creativeTo Visual before, plannerTo consumption Pattern before
- copywriter complete -> creativeTo line·to before (Copy-Visual Integration), plannerTo Per-channel Copy before
- creative complete -> plannerTo · Information before
- reviewer cross-validate. 🔴 Must Fix when AgentTo → → Verification (vs 2)

### Phase 3: Integration and Final Deliverables

Reviewof based on :

1. `_workspace/` within File verify
2. from the review report 🔴 Must Fix reflected verify
3. summary To :
 - market·Target Analysis — `01_market_analysis.md`
 - ad Copy — `02_ad_copy.md`
 - Creative Concept — `03_creative_concept.md`
 - — `04_media_plan.md`
 - Review — `05_review_report.md`

## Modes by Task Scale

 of in Agent :

| Pattern | mode | Agent |
|----------------|----------|-------------|
| "ad Campaign Planning", " Campaign" | **Full Pipeline** | 5 All |
| "ad Copy " | **Copy mode** | analyst + copywriter + reviewer |
| " Copyto Creative " ( Copy) | **Creative mode** | creative + reviewer |
| " " | ** mode** | analyst + planner + reviewer |
| " Campaign " | **Review mode** | reviewer only |

**Using Existing Files**: Copy, Brand Guide etc. File , copy the files to `_workspace/`of in and of Agent .

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
| web search | Analysis based on , in the report " " when |
| Image | Text Conceptto , Gemini Prompt when |
| Agent failure | 1 retry -> if still fails, proceed without that deliverable, note omission in review report |
| RED found in review | Request revision from relevant agent -> rework -> re-verify (up to 2 times) |
| Budget | 3 when(500/1,000/3,000)to Writing |

## Test Scenarios

### Normal Flow
**Prompt**: " when digital ad Campaign Planning. Budget 2,000, between 4"
**Expected Result**:
- market Analysis: Competitive Analysis 3 , Target Persona 2, 
- Copy: banner+SNS++video Per-channel Copy , to 3
- Creative: Visual Concept + A/B + Storyboard + Image when
- : Per-channel Budget allocation, 4 lean, KPI goal
- Review: matrix before Verification

### Existing File Utilisation Flow
**Prompt**: " Brand Guideand Copy based on banner Creative " + File 
**Expected Result**:
- Copy `_workspace/02_ad_copy.md`to 
- Creative mode: creative + reviewer 
- analyst, copywriter, planner 

### Error Flow
**Prompt**: "ad Copy , "
**Expected Result**:
- Copy modeto before (analyst + copywriter + reviewer)
- Target to Analysis Target 3 Suggestion after 
- Review in the report "Creative/ " when

## Extended Skills per Agent

per Agentof before Extended Skill:

| | subject Agent | Role |
|------|-------------|------|
| `ad-copywriting-formulas` | copywriter | AIDA/PAS/BAB/4Ps Formula, Psychology Trigger, Per-channel Character limit |
| `media-mix-calculator` | media-planner | GRP/CPM/ROAS Calculation Formula, Budget allocation Model, Per-channel Benchmark |
