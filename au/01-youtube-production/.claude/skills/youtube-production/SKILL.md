---
name: youtube-production
description: "A full production pipeline where an agent team collaborates to generate YouTube video content — strategy, script, thumbnail, and SEO metadata — all at once. Use this skill for requests like 'plan a YouTube video,' 'write a video script,' 'video scriptwriting,' 'YouTube content strategy,' 'video scenario,' 'YouTube Shorts planning,' 'create a YouTube thumbnail,' 'video SEO optimisation,' 'YouTube channel content,' and other YouTube video production tasks. Also supports SEO optimisation or thumbnail creation when an existing script is provided. Note: actual video editing (Premiere, DaVinci), YouTube Analytics API integration, and channel operations dashboard setup are outside this skill's scope."
---

# YouTube Production — Full Video Content Production Pipeline

An agent team collaborates to produce YouTube video content through the pipeline of strategy → script → thumbnail → SEO, all at once.

## Execution Mode

**Agent Team** — 5 members communicate directly via SendMessage and cross-validate each other's work.

## Agent Roster

| Agent | File | Role | Type |
|-------|------|------|------|
| content-strategist | `.claude/agents/content-strategist.md` | Topic analysis, competitive benchmarking, concept design | general-purpose |
| scriptwriter | `.claude/agents/scriptwriter.md` | Script writing, visual cue insertion | general-purpose |
| thumbnail-designer | `.claude/agents/thumbnail-designer.md` | Thumbnail concept + image generation | general-purpose |
| seo-optimizer | `.claude/agents/seo-optimizer.md` | Title/description/tags/chapters/subtitles | general-purpose |
| production-reviewer | `.claude/agents/production-reviewer.md` | Cross-validation, consistency checks | general-purpose |

## Workflow

### Phase 1: Preparation (Performed directly by the orchestrator)

1. Extract from user input:
   - **Topic/Keywords**: The subject the video will cover
   - **Channel Info** (optional): Channel tone, subscriber count, existing content direction
   - **Constraints** (optional): Video length, specific requirements
   - **Existing Files** (optional): Scripts, briefs, or other materials provided by the user
2. Create the `_workspace/` directory at the project root
3. Organise the input and save it as `_workspace/00_input.md`
4. If existing files are provided, copy them to `_workspace/` and skip the corresponding phase
5. Determine the **execution mode** based on request scope (see "Scope-Based Modes" below)

### Phase 2: Team Assembly and Execution

Assemble the team and assign tasks. Task dependencies are as follows:

| Order | Task | Owner | Depends On | Deliverable |
|-------|------|-------|------------|-------------|
| 1 | Content strategy | strategist | None | `_workspace/01_strategist_brief.md` |
| 2a | Script writing | writer | Task 1 | `_workspace/02_scriptwriter_script.md` |
| 2b | Thumbnail design & generation | designer | Task 1 | `_workspace/03_thumbnail_concept.md` |
| 3 | SEO package | seo | Tasks 1, 2a | `_workspace/04_seo_package.md`, `_workspace/subtitle.srt` |
| 4 | Production review | reviewer | Tasks 2a, 2b, 3 | `_workspace/05_review_report.md` |

Tasks 2a (script) and 2b (thumbnail) run **in parallel**. Both depend only on Task 1 (strategy), so they can start simultaneously.

**Inter-agent communication flow:**
- strategist complete → deliver core angle & tone to writer, title candidates & emotional triggers to designer, keyword map to seo
- writer complete → deliver hook core message to designer (thumbnail-hook consistency), deliver script to seo
- seo complete → deliver title-thumbnail combination feedback to designer
- reviewer cross-validates all deliverables. On 🔴 Must Fix: request revision from the responsible agent → rework → re-validate (up to 2 rounds)

### Phase 3: Integration and Final Deliverables

Compile the final deliverables based on the reviewer's report:

1. Verify all files in `_workspace/`
2. Confirm all 🔴 Must Fix items from the review report have been addressed
3. Report the final summary to the user:
   - Strategy Brief — `01_strategist_brief.md`
   - Video Script — `02_scriptwriter_script.md`
   - Thumbnail Concept + Images — `03_thumbnail_concept.md`
   - SEO Package — `04_seo_package.md`
   - Review Report — `05_review_report.md`
   - Subtitle File — `subtitle.srt`

## Scope-Based Modes

Adjust the agents deployed based on the scope of the user's request:

| User Request Pattern | Execution Mode | Agents Deployed |
|---------------------|----------------|-----------------|
| "Plan a YouTube video," "full production" | **Full Pipeline** | All 5 |
| "Just write the script," "script only" | **Script Mode** | strategist + writer + reviewer |
| "Optimise SEO for this script" (existing file) | **SEO Mode** | seo + reviewer |
| "Create a thumbnail for this video" (existing brief) | **Thumbnail Mode** | designer + reviewer |
| "Review this script" | **Review Mode** | reviewer only |

**Using Existing Files**: If the user provides a script, brief, or other existing file, copy it to the appropriate numbered position in `_workspace/` and skip that phase's agent. Example: existing script provided → copy to `_workspace/02_scriptwriter_script.md` → skip writer, deploy only seo, designer, and reviewer.

## Data Transfer Protocol

| Strategy | Method | Purpose |
|----------|--------|---------|
| File-based | `_workspace/` directory | Primary deliverable storage and sharing |
| Message-based | SendMessage | Real-time key information transfer, revision requests |
| Task-based | TaskCreate/TaskUpdate | Progress tracking, dependency management |

File naming convention: `{order}_{agent}_{deliverable}.{extension}`

## Error Handling

| Error Type | Strategy |
|-----------|----------|
| Web search failure | Strategist works from general knowledge, report notes "data limitation" |
| Thumbnail image generation failure | Proceed with text concept only, include Gemini prompt for user retry |
| Agent failure | Retry once → if still failing, proceed without that deliverable, note omission in review report |
| 🔴 found in review | Request revision from responsible agent → rework → re-validate (up to 2 rounds) |

## Agent Extension Skills

| Skill | Path | Target Agent | Purpose |
|-------|------|-------------|---------|
| hook-writing | `skills/hook-writing/skill.md` | scriptwriter | 15 hook patterns, retention psychology, hook-thumbnail-title triangle alignment |
| thumbnail-psychology | `skills/thumbnail-psychology/skill.md` | thumbnail-designer | Colour psychology, 7 composition patterns, text readability, 3-second test |

Agents reference their respective extension skills during task execution to enhance domain expertise.

## Test Scenarios

### Happy Path
**Prompt**: "Plan a 10-minute YouTube video as a beginner's guide to AI prompt engineering"
**Expected Results**:
- Strategy brief: 3+ competitive analyses, keyword map, 3 title candidates
- Script: 10-minute length (~1,500 words in English), hook + 3–4 segments + closing
- Thumbnail: A/B concept options + image generation attempt
- SEO: Title/description/tags/chapters/SRT
- Review: All consistency matrix items verified

### Existing File Flow
**Prompt**: "Create SEO optimisation and a thumbnail for this script" + script file attached
**Expected Results**:
- Existing script copied to `_workspace/02_scriptwriter_script.md`
- SEO Mode + Thumbnail Mode merged: seo + designer + reviewer deployed
- strategist, writer skipped

### Error Flow
**Prompt**: "Just write a YouTube script quickly, any topic"
**Expected Results**:
- Switch to Script Mode (strategist + writer + reviewer)
- Topic is unclear, so strategist proposes 3 trending topics before proceeding
- Review report notes "thumbnail/SEO not generated"
