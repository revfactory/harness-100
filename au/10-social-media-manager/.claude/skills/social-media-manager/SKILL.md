---
name: social-media-manager
description: "A full production pipeline where an agent team collaborates to generate SNS content strategy, post copy, visual plans, and hashtag strategies all at once. Use this skill for 'create SNS content,' 'write Instagram posts,' 'social media strategy,' 'SNS content calendar,' 'hashtag strategy,' 'Instagram copy,' 'TikTok content,' 'LinkedIn posts,' 'SNS marketing,' and all other aspects of social media content management. Also supports post writing or hashtag analysis when existing brand guides are provided. Note: actual SNS account operations (posting, replies, DMs), ad execution, analytics API integration, and influencer outreach are outside the scope of this skill."
---

# Social Media Manager — SNS Content Full Production Pipeline

An agent team collaborates to generate SNS content strategy, posts, visuals, and hashtags all at once.

## Execution Mode

**Agent Team** — 5 members communicate directly via SendMessage and cross-validate each other's work.

## Agent Composition

| Agent | File | Role | Type |
|-------|------|------|------|
| sns-strategist | `.claude/agents/sns-strategist.md` | Channel analysis, content calendar, campaign design | general-purpose |
| copywriter | `.claude/agents/copywriter.md` | Post copy, captions, CTAs | general-purpose |
| visual-planner | `.claude/agents/visual-planner.md` | Image concepts, card news, Reels planning | general-purpose |
| hashtag-analyst | `.claude/agents/hashtag-analyst.md` | Hashtag strategy, trend analysis | general-purpose |
| performance-reviewer | `.claude/agents/performance-reviewer.md` | KPI alignment, quality verification | general-purpose |

## Workflow

### Phase 1: Preparation (Performed Directly by the Orchestrator)

1. Extract from user input:
   - **Brand/Account Info**: Industry, tone & voice, target customers
   - **Platforms**: Instagram, Twitter/X, TikTok, Facebook, LinkedIn
   - **Period**: Weekly/monthly content plan
   - **Goals** (optional): Brand awareness, conversion, community growth
   - **Existing Files** (optional): Brand guide, existing content
2. Create the `_workspace/` directory in the project root
3. Organise the input and save it to `_workspace/00_input.md`
4. If existing files are present, copy them to `_workspace/` and skip the corresponding Phase
5. **Determine the execution mode** based on the scope of the request

### Phase 2: Team Assembly and Execution

| Order | Task | Assigned To | Dependencies | Deliverable |
|-------|------|------------|--------------|-------------|
| 1 | SNS strategy | sns-strategist | None | `_workspace/01_strategy.md` |
| 2a | Post copy | copywriter | Task 1 | `_workspace/02_posts.md` |
| 2b | Hashtag strategy | hashtag-analyst | Task 1 | `_workspace/04_hashtags.md` |
| 3 | Visual planning | visual-planner | Tasks 1, 2a | `_workspace/03_visuals.md` |
| 4 | Performance review | performance-reviewer | Tasks 2a, 2b, 3 | `_workspace/05_review_report.md` |

Tasks 2a (copy) and 2b (hashtags) are **executed in parallel**. Visual planning (3) starts after copy is complete.

**Inter-team communication flow:**
- sns-strategist complete -> Deliver tone and calendar to copywriter, keywords and competitor accounts to hashtag-analyst, brand guide to visual-planner
- copywriter complete -> Deliver text overlays and image keywords to visual-planner, post topics to hashtag-analyst
- hashtag-analyst complete -> Deliver trend hashtags to visual-planner
- performance-reviewer cross-validates all deliverables. When RED Must Fix is found, request revisions from the relevant agent -> rework -> re-verify (up to 2 times)

### Phase 3: Integration and Final Deliverables

1. Verify all files in `_workspace/`
2. Confirm that all RED Must Fix items from the review report have been addressed
3. Report the final summary to the user:
   - Strategy/Calendar — `01_strategy.md`
   - Post Copy — `02_posts.md`
   - Visual Plan — `03_visuals.md`
   - Hashtag Strategy — `04_hashtags.md`
   - Review Report — `05_review_report.md`

## Modes by Task Scale

| User Request Pattern | Execution Mode | Agents Deployed |
|---------------------|---------------|-----------------|
| "Create SNS content," "Full management" | **Full Pipeline** | All 5 |
| "Just create a content calendar" | **Strategy Mode** | strategist + reviewer |
| "Just write Instagram posts" | **Copy Mode** | copywriter + hashtag-analyst + reviewer |
| "Just analyse hashtags" | **Hashtag Mode** | hashtag-analyst + reviewer |
| "Review this post" | **Review Mode** | reviewer only |

**Using Existing Files**: When the user provides brand guides, content calendars, etc., copy the files to the appropriate location in `_workspace/` and skip the corresponding agents.

## Data Transfer Protocol

| Strategy | Method | Purpose |
|----------|--------|---------|
| File-Based | `_workspace/` directory | Storing and sharing major deliverables |
| Message-Based | SendMessage | Real-time delivery of key information, revision requests |
| Task-Based | TaskCreate/TaskUpdate | Progress tracking, dependency management |

File naming convention: `{sequence}_{deliverable_name}.{extension}`

## Error Handling

| Error Type | Strategy |
|-----------|----------|
| Brand info insufficient | Apply industry-standard guide, note "customisation needed" |
| Web search failure | Work with general SNS knowledge, note "trend data limited" |
| Agent failure | 1 retry -> if still fails, proceed without that deliverable, note omission in review report |
| RED found in review | Request revision from relevant agent -> rework -> re-verify (up to 2 times) |
| Image generation failure | Proceed with text concepts and prompts only, available for user retry |

## Test Scenarios

### Normal Flow
**Prompt**: "Plan monthly Instagram content for a health food brand. Target is women in their 20s-30s, tone is friendly and bright."
**Expected Result**:
- Strategy: Monthly calendar (3-4x/week), content pillar mix, KPI settings
- Posts: 12-16 Instagram captions (feed + Reels + carousel mix)
- Visuals: Image concepts per post, carousel layouts, Reels storyboards
- Hashtags: Hashtag sets per post (pyramid strategy applied)
- Review: Full consistency matrix verified

### Existing File Utilisation Flow
**Prompt**: "Write 3 Instagram posts this week using this brand guide" + guide file attached
**Expected Result**:
- Copy brand guide to `_workspace/`
- Copy Mode: Deploy copywriter + hashtag-analyst + reviewer
- Skip strategist, visual-planner (or minimal involvement)

### Error Flow
**Prompt**: "Just analyse SNS hashtags, topic is cafe entrepreneurship"
**Expected Result**:
- Switch to Hashtag Mode (hashtag-analyst + reviewer)
- Brand info insufficient, so generate hashtag library based on "cafe entrepreneurship" industry
- Review report notes "Strategy/Posts/Visuals not generated"

## Extended Skills per Agent

Each agent leverages the following extended skills' specialised knowledge to enhance deliverable quality:

| Agent | Extended Skill | Knowledge Provided |
|-------|---------------|-------------------|
| sns-strategist, visual-planner | `/platform-algorithms` | Instagram/TikTok/LinkedIn/X algorithms, golden hours, format optimisation |
| copywriter | `/viral-copywriting` | 15 hook patterns, platform-specific copy structure, emotion triggers, CTA design |
| hashtag-analyst | `/hashtag-science` | Pyramid strategy, platform-specific hashtag rules, research process, shadowban prevention |
