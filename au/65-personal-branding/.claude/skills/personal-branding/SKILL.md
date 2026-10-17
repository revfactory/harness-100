---
name: personal-branding
description: "A pipeline where an agent team systematically performs personal branding. Use this skill for requests such as 'write my resume,' 'personal branding,' 'CV writing,' 'create a portfolio,' 'optimise LinkedIn profile,' 'write a cover letter,' 'organise my career,' 'help with job preparation,' or 'prepare for a job change.' Note: job posting search, interview simulation, and salary negotiation coaching are outside the scope of this skill."
---

# Personal Branding — Personal Branding Pipeline

An agent team collaborates to produce: positioning analysis, resume/CV, portfolio, LinkedIn profile, and cover letter.

## Execution Mode

**Agent Team** — Five agents communicate directly via SendMessage to build a consistent brand.

## Agent Composition

| Agent | File | Role | Type |
|-------|------|------|------|
| positioning-strategist | `.claude/agents/positioning-strategist.md` | Strength analysis, differentiation, keyword strategy | general-purpose |
| resume-writer | `.claude/agents/resume-writer.md` | Resume/CV writing | general-purpose |
| portfolio-designer | `.claude/agents/portfolio-designer.md` | Portfolio curation and design | general-purpose |
| profile-optimizer | `.claude/agents/profile-optimizer.md` | LinkedIn profile optimisation | general-purpose |
| cover-letter-writer | `.claude/agents/cover-letter-writer.md` | Cover letter writing | general-purpose |

## Workflow

### Phase 1: Preparation (Performed Directly by Orchestrator)

1. Extract from user input:
    - **Career Information**: Current role, years of experience, key experiences
    - **Goals**: Desired position, target companies/industries
    - **Existing Materials** (optional): Current resume, portfolio, LinkedIn URL
    - **Request Scope** (optional): Full package or specific documents only
2. Create the `_workspace/` directory in the project root
3. Organise inputs and save to `_workspace/00_input.md`
4. If existing materials are provided, copy them to `_workspace/` and use as analysis basis
5. Determine the **execution mode** based on the scope of the request

### Phase 2: Team Assembly and Execution

| Order | Task | Owner | Dependencies | Deliverable |
|-------|------|-------|-------------|-------------|
| 1 | Positioning Strategy | positioning-strategist | None | `_workspace/01_positioning_brief.md` |
| 2a | Resume Writing | resume-writer | Task 1 | `_workspace/02_resume.md` |
| 2b | Portfolio Design | portfolio-designer | Task 1 | `_workspace/03_portfolio.md` |
| 3a | LinkedIn Profile | profile-optimizer | Tasks 1, 2a | `_workspace/04_linkedin_profile.md` |
| 3b | Cover Letter | cover-letter-writer | Tasks 1, 2a | `_workspace/05_cover_letter.md` |

Tasks 2a (resume) and 2b (portfolio) are executed **in parallel**.
Tasks 3a (LinkedIn) and 3b (cover letter) are executed **in parallel**.

**Inter-agent Communication Flow:**
- positioning-strategist completes -> Delivers UVP, keywords, and narrative to all agents
- resume-writer completes -> Delivers career descriptions to profile-optimizer; delivers key achievements to cover-letter-writer
- portfolio-designer completes -> Delivers featured items to profile-optimizer; delivers project achievements to cover-letter-writer
- Cross-verify **brand consistency** across all deliverables

### Phase 3: Integration and Final Deliverables

1. Review all files in `_workspace/`
2. Verify brand message consistency across deliverables:
    - Resume <-> LinkedIn career descriptions consistency
    - Portfolio <-> Resume project alignment
    - Cover letter <-> Positioning UVP reflection
3. Present the final summary to the user

## Execution Modes by Request Scope

| User Request Pattern | Execution Mode | Deployed Agents |
|---------------------|---------------|-----------------|
| "Do personal branding," "Job preparation" | **Full Package** | All 5 agents |
| "Just write a resume" | **Resume Mode** | positioning-strategist + resume-writer |
| "Create a portfolio" | **Portfolio Mode** | positioning-strategist + portfolio-designer |
| "Optimise my LinkedIn profile" | **Profile Mode** | positioning-strategist + profile-optimizer |
| "Write a cover letter" | **Cover Letter Mode** | positioning-strategist + cover-letter-writer |

**Using Existing Files**: If an existing resume is provided, positioning-strategist analyses it to inform strategy development.

## Data Transfer Protocol

| Strategy | Method | Purpose |
|----------|--------|---------|
| File-based | `_workspace/` directory | Primary deliverable storage and sharing |
| Message-based | SendMessage | Real-time critical information transfer, revision requests |
| Web exploration | WebSearch/WebFetch | JD analysis, industry trend research |

## Error Handling

| Error Type | Strategy |
|-----------|----------|
| Insufficient career information | Present a list of key questions; draft based on available info |
| Goal unspecified | Propose 3 positioning scenarios |
| Web search failure | Work based on general JD trend knowledge; note "limited market data" |
| Agent failure | Retry once; if still failing, proceed without that deliverable; note omission in report |
| Confidential career details | Apply number/company name abstraction guidelines |

## Test Scenarios

### Normal Flow
**Prompt**: "I'm a backend developer with 3 years of experience, preparing to transition to a senior position. Create a full branding package for me."
**Expected Results**:
- Positioning: UVP suited for senior role, technical + leadership strengths analysis
- Resume: ATS-optimized, quantified achievements, senior keywords included
- Portfolio: 3-5 project case studies emphasising technical decision-making
- LinkedIn: Senior developer keywords, About section narrative
- Cover Letter: Growth story + senior role readiness

### Single Document Request Flow
**Prompt**: "Just write a cover letter matching this JD" + JD provided
**Expected Results**:
- positioning-strategist analyses JD and extracts key requirements
- cover-letter-writer creates a customised cover letter
- Other agents are skipped

### Error Flow
**Prompt**: "Write my resume"
**Expected Results**:
- Career info is insufficient, so positioning-strategist presents a question list
- Execute resume mode based on user responses
- Skip LinkedIn, portfolio, cover letter but note "additional creation available"

## Agent Extension Skills

Extension skills that enhance each agent's domain expertise:

| Agent | Extension Skill | Role |
|-------|----------------|------|
| resume-writer | `ats-optimizer` | ATS parsing principles, keyword optimisation, achievement quantification (STAR-Q), format rules |
| profile-optimizer | `linkedin-seo` | LinkedIn search algorithm, section-by-section optimisation, recruiter search patterns, SSI |
