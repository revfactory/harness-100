---
name: content-repurposer
description: "A full repurposing pipeline that transforms a single source piece of content into multiple formats — blog, social media, newsletter, presentation, script — all at once. Use this skill for requests like 'repurpose this content,' 'convert this blog to social media,' 'content recycling,' 'multi-format conversion,' 'turn this into a presentation,' 'convert this report to a blog,' 'multi-channel content,' and other content repurposing tasks. Note: actual image/video production, presentation file (.pptx) generation, and automated social media posting are outside this skill's scope."
---

# Content Repurposer — Multi-Format Content Conversion Pipeline

An agent team collaborates to convert a single source piece of content into blog → social media → presentation, all at once.

## Execution Mode

**Agent Team** — 5 members communicate directly via SendMessage and cross-validate each other's work.

## Agent Roster

| Agent | File | Role | Type |
|-------|------|------|------|
| source-analyst | `.claude/agents/source-analyst.md` | Source analysis, conversion strategy | general-purpose |
| blog-writer | `.claude/agents/blog-writer.md` | SEO blog post writing | general-purpose |
| sns-copywriter | `.claude/agents/sns-copywriter.md` | Platform-specific social posts | general-purpose |
| presentation-builder | `.claude/agents/presentation-builder.md` | Slide presentation | general-purpose |
| quality-reviewer | `.claude/agents/quality-reviewer.md` | Message consistency cross-validation | general-purpose |

## Workflow

### Phase 1: Preparation (Performed directly by the orchestrator)

1. Extract from user input:
   - **Source Content**: The original to convert (text, file, URL)
   - **Output Formats** (optional): Desired conversion formats (default: blog + social + presentation)
   - **Target Audience** (optional): Target audience for each format
   - **Brand Tone** (optional): Consistent brand voice
   - **Constraints** (optional): Specific platforms, length limits, etc.
2. Create the `_workspace/` directory at the project root
3. Organise the input and save it as `_workspace/00_input.md`
4. If the source is a URL, fetch its content via WebFetch
5. Determine the **execution mode** based on request scope

### Phase 2: Team Assembly and Execution

| Order | Task | Owner | Depends On | Deliverable |
|-------|------|-------|------------|-------------|
| 1 | Source analysis | source-analyst | None | `_workspace/01_source_analysis.md` |
| 2a | Blog conversion | blog-writer | Task 1 | `_workspace/02_blog_post.md` |
| 2b | Social media conversion | sns-copywriter | Task 1 | `_workspace/03_sns_package.md` |
| 2c | Presentation conversion | presentation-builder | Task 1 | `_workspace/04_presentation.md` |
| 3 | Quality review | quality-reviewer | Tasks 2a, 2b, 2c | `_workspace/05_review_report.md` |

Tasks 2a (blog), 2b (social), and 2c (presentation) run **in parallel**. All depend only on Task 1 (source analysis), so they can start simultaneously.

**Inter-agent communication flow:**
- source-analyst complete → deliver format-specific strategies to each conversion agent
- blog-writer complete → deliver blog quotes & links to sns-copywriter
- sns-copywriter complete → deliver visual consistency info to presentation-builder
- reviewer cross-validates all deliverables. On 🔴 Must Fix: request revision → rework → re-validate (up to 2 rounds)

### Phase 3: Integration and Final Deliverables

1. Verify all files in `_workspace/`
2. Confirm all 🔴 Must Fix items have been addressed
3. Report the final summary to the user:
   - Source Analysis — `01_source_analysis.md`
   - Blog Post — `02_blog_post.md`
   - Social Media Package — `03_sns_package.md`
   - Presentation — `04_presentation.md`
   - Review Report — `05_review_report.md`

## Scope-Based Modes

| User Request Pattern | Execution Mode | Agents Deployed |
|---------------------|----------------|-----------------|
| "Repurpose this content," "full conversion" | **Full Pipeline** | All 5 |
| "Convert to a blog post" | **Blog Mode** | source-analyst + blog-writer + quality-reviewer |
| "Create social media posts" | **Social Mode** | source-analyst + sns-copywriter + quality-reviewer |
| "Convert to a presentation" | **Presentation Mode** | source-analyst + presentation-builder + quality-reviewer |
| "Review these conversions" | **Review Mode** | quality-reviewer only |

**Using Existing Files**: If the user provides already-converted content, copy it to `_workspace/` and skip that conversion agent.

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
| Source URL inaccessible | Request text input from user, or work with cached content |
| Source too short (under 500 words) | Supplement with related material via web search, note "source augmented" |
| Agent failure | Retry once → if still failing, proceed without that format, note omission in review report |
| 🔴 found in review | Request revision from responsible agent → rework → re-validate (up to 2 rounds) |

## Test Scenarios

### Happy Path
**Prompt**: "Repurpose this blog post into social media and a presentation" + 2,000-word blog post attached
**Expected Results**:
- Source analysis: Structure map, 3 core messages, format-specific conversion strategies
- Blog: SEO-optimized rewrite (improved version if source is already a blog)
- Social: Twitter thread (8 tweets), Instagram carousel (8 slides), LinkedIn post
- Presentation: 15 slides with speaker notes
- Review: All message consistency matrix items verified

### Existing File Flow
**Prompt**: "Convert this report into a presentation only" + PDF file attached
**Expected Results**:
- Presentation Mode: source-analyst + presentation-builder + quality-reviewer deployed
- blog-writer, sns-copywriter skipped

### Error Flow
**Prompt**: "Repurpose the article at this URL" + inaccessible URL
**Expected Results**:
- URL access failure → request text input from user
- If user provides text, proceed with normal pipeline
- Review report notes "source URL inaccessible, based on user-provided text"

## Agent Extension Skills

Each agent leverages the following extension skills to enhance deliverable quality:

| Agent | Extension Skill | Knowledge Provided |
|-------|----------------|-------------------|
| sns-copywriter, blog-writer | `/platform-adaptation` | Platform DNA, conversion matrix, message consistency checks |
| source-analyst, presentation-builder | `/content-atomization` | MINE analysis framework, atom classification system, slide conversion formulas |
