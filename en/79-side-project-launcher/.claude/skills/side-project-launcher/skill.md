---
name: side-project-launcher
description: "A pipeline where an agent team collaborates to comprehensively plan a side project. Use this skill for requests like 'help me plan a side project', 'side project idea', 'toy project', 'I want to build an MVP', 'I want to launch an app', 'service launch', 'solo development', 'indie hacking', 'weekend project', 'what tech stack should I use', 'side hustle', and other side project planning needs. Also supports tech stack selection and MVP design when an idea already exists. However, actual code writing, design mockup creation, and domain/server purchase assistance are outside the scope of this skill."
---

# Side Project Launcher — Side Project Planning Pipeline

An agent team collaborates to generate idea validation, tech stack selection, MVP spec, development roadmap, and launch checklist all at once.

## Execution Mode

**Agent Team** — 5 agents communicate directly via SendMessage and cross-verify each other's work.

## Agent Composition

| Agent | File | Role | Type |
|-------|------|------|------|
| idea-validator | `.claude/agents/idea-validator.md` | Market analysis, competitive research, differentiation validation | general-purpose |
| techstack-analyst | `.claude/agents/techstack-analyst.md` | Tech stack comparison, recommendations, infrastructure design | general-purpose |
| mvp-designer | `.claude/agents/mvp-designer.md` | Core feature definition, wireframes, spec | general-purpose |
| roadmap-builder | `.claude/agents/roadmap-builder.md` | Development schedule, launch strategy, checklist | general-purpose |
| launch-reviewer | `.claude/agents/launch-reviewer.md` | Cross-verification, feasibility confirmation | general-purpose |

## Workflow

### Phase 1: Preparation (Performed directly by orchestrator)

1. Extract from user input:
    - **Idea**: What to build, what problem to solve
    - **Development Skills** (optional): Available technologies, development experience level
    - **Available Time** (optional): Hours available per week
    - **Budget** (optional): Monthly operating cost limit
    - **Existing Files** (optional): Planning documents, wireframes, etc.
2. Create `_workspace/` directory at the project root
3. Organize the input and save to `_workspace/00_input.md`
4. If existing files are provided, copy them to `_workspace/` and skip the corresponding Phase
5. Determine the **execution mode** based on the scope of the request

### Phase 2: Team Assembly and Execution

| Order | Task | Assigned To | Dependencies | Deliverable |
|-------|------|-------------|--------------|-------------|
| 1 | Idea validation | validator | None | `_workspace/01_idea_validation.md` |
| 2 | Tech stack selection | techstack | Task 1 | `_workspace/02_techstack_recommendation.md` |
| 3 | MVP design | designer | Tasks 1, 2 | `_workspace/03_mvp_spec.md` |
| 4 | Roadmap and launch | roadmap | Tasks 2, 3 | `_workspace/04_roadmap_launch.md` |
| 5 | Launch review | reviewer | Tasks 1–4 | `_workspace/05_review_report.md` |

**Inter-team Communication Flow:**
- validator completes → delivers project type and difficulty to techstack, UVP and differentiation points to designer, market timing to roadmap
- techstack completes → delivers technical constraints and implementation difficulty to designer, learning time and technical risks to roadmap
- designer completes → delivers per-feature time estimates and priorities to roadmap
- launch-reviewer cross-validates all deliverables. If 🔴 Must Fix, sends revision request → rework → re-validate (up to 2 times)

### Phase 3: Integration and Final Deliverables

1. Verify all files in `_workspace/`
2. Confirm that all 🔴 Must Fix items from the review report have been addressed
3. Report the final summary to the user

## Execution Modes by Request Scale

| User Request Pattern | Execution Mode | Agents Deployed |
|---------------------|----------------|-----------------|
| "Full side project planning" | **Full Pipeline** | All 5 |
| "Validate this idea" | **Validation Mode** | validator + reviewer |
| "Recommend a tech stack" (idea exists) | **Technical Mode** | validator + techstack + reviewer |
| "Design the MVP spec" (tech decided) | **MVP Mode** | designer + roadmap + reviewer |
| "Create a launch checklist" | **Launch Mode** | roadmap + reviewer |

**Existing file utilization**: If the user provides planning documents, tech stack decisions, etc., skip the corresponding phase.

## Data Transfer Protocol

| Strategy | Method | Purpose |
|----------|--------|---------|
| File-based | `_workspace/` directory | Storing and sharing main deliverables |
| Message-based | SendMessage | Real-time key information transfer, revision requests |
| Task-based | TaskCreate/TaskUpdate | Progress tracking, dependency management |

File naming convention: `{number}_{agent}_{deliverable}.{extension}`

## Error Handling

| Error Type | Strategy |
|-----------|----------|
| No idea provided | Suggest 3 trend-based ideas, guide selection |
| No development experience | Prioritize no-code/low-code recommendations, include learning roadmap |
| Web search failure | Analyze with general market knowledge, note "data limitation" |
| Agent failure | Retry once → if still fails, proceed without that deliverable, note omission in review |
| 🔴 found in review | Send revision request → rework → re-validate (up to 2 times) |

## Test Scenarios

### Normal Flow
**Prompt**: "I want to build a web app as a side project to help developers prepare for interviews. I know React and will work on it on weekends."
**Expected Results**:
- Validation: Interview prep market analysis, differentiation from existing services (LeetCode, etc.)
- Technical: React + Supabase + Vercel recommendation, free tier utilization
- MVP: 3–5 core features, text wireframes, data model
- Roadmap: 4-week sprints, Product Hunt launch strategy
- Review: Full consistency check, risk matrix

### Existing File Utilization Flow
**Prompt**: "I've already validated the idea and decided on the tech stack. Just design the MVP spec" + planning doc attached
**Expected Results**:
- MVP Mode: designer + roadmap + reviewer deployed
- validator and techstack phases skipped

### Error Flow
**Prompt**: "I want to build something but I don't have an idea"
**Expected Results**:
- validator asks about user interests or proposes 3 trend-based ideas
- Select one, then proceed with full pipeline
- Review report notes "in idea exploration phase"

## Agent Extension Skills

| Agent | Extension Skill | Purpose |
|-------|----------------|---------|
| idea-validator | `market-sizing-calculator` | TAM/SAM/SOM calculation, revenue model validation |
| techstack-analyst | `techstack-decision-matrix` | Tech stack comparison matrix, infrastructure cost calculation |
