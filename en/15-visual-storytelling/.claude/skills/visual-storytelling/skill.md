---
name: visual-storytelling
description: "Full visual storytelling pipeline where an agent team collaborates to produce story design, essay writing, AI image generation (Gemini), HTML layout, and editorial review. Use for "visual story", "image+text combination", "visual narrative", "story page production", etc. Note: video editing, DTP, and JavaScript interactivity are outside the scope of this skill."
---

# Visual Storytelling — Visual Storytelling Full Production Pipeline

An agent team collaborates to produce visual story design, text writing, AI image generation, HTML layout, and integrated editing.

## Execution Mode

**Agent Team** — 5 members communicate directly via SendMessage and cross-validate each other's work.

## Agent Composition

| Agent | File | Role | Type |
|---------|------|------|------|
| story-architect | `.claude/agents/story-architect.md` | Narrative Structure, Scene Design | general-purpose |
| essay-writer | `.claude/agents/essay-writer.md` | Body text, Caption, Quote writing | general-purpose |
| image-prompter | `.claude/agents/image-prompter.md` | Gemini Image Prompt, | general-purpose |
| layout-builder | `.claude/agents/layout-builder.md` | HTML/CSS Layout production | general-purpose |
| editorial-reviewer | `.claude/agents/editorial-reviewer.md` | cross-validate, Verification | general-purpose |

## Workflow

### Phase 1: Preparation (Performed Directly by the Orchestrator)

1. Extract from user input:
 - **Story **: Visual Storyof /
 - **type** (Selection): in/in/BrandStory/
 - **** (Selection): ///intense
 - **Scene ** (Selection): 
 - ** File** (Selection): Text, Image, 
2. `_workspace/` and `_workspace/images/` generate
3. Organize input and save to `_workspace/00_input.md`in save
4. If existing files are present `_workspace/`, copy to _workspace/ and skip the corresponding Phase
5. Based on the scope of the request **determine the execution mode** ( " per mode" )

### Phase 2: Team Assembly and Execution

 compositionand . between of relationship and :

| sequence | | | of | |
|------|------|------|------|--------|
| 1 | Story Design | architect | None | `_workspace/01_story_blueprint.md` |
| 2a | Text writing | writer | 1 | `_workspace/02_essay_text.md` |
| 2b | Image Prompt· | prompter | 1 | `_workspace/03_image_prompts.md`, `images/` |
| 3 | HTML Layout | builder | 2a, 2b | `_workspace/04_layout.html` |
| 4 | Editing Review | reviewer | 2a, 2b, 3 | `_workspace/05_review_report.md` |

 2a(Text)and 2b(Image) **executed in parallel**. 1(Story Design)in ofto whenin when .

**Inter-team communication flow:**
- architect complete -> writerTo Sceneper Text Role·Emotion before, prompterTo Visual ·Image concept before, builderTo Scene Structure·ratio before
- writer complete -> prompterTo Text Emotionand Image before, builderTo Text placement Guide before
- prompter complete -> builderTo Image File··placement Information before
- reviewer cross-validate. 🔴 Must Fix when AgentTo → → Verification (vs 2)

### Phase 3: Integration and Final Deliverables

Reviewof based on :

1. `_workspace/` within File verify
2. from the review report 🔴 Must Fix reflected verify
3. summary To :
 - Story lean — `01_story_blueprint.md`
 - in Text — `02_essay_text.md`
 - Image Prompt — `03_image_prompts.md`
 - HTML Layout — `04_layout.html`
 - Review — `05_review_report.md`
 - Image — `images/` 

## Modes by Task Scale

 of in Agent :

| Pattern | mode | Agent |
|----------------|----------|-------------|
| "Visual Story ", " to" | **Full Pipeline** | 5 All |
| "Story Planning " | **Planning mode** | architect + reviewer |
| " in Image " ( Text) | **Image mode** | prompter + reviewer |
| "Textand Imageto HTML " ( ) | **Layout mode** | builder + reviewer |
| " Visual Story " | **Review mode** | reviewer only |

**Using Existing Files**: Text Image , copy the files to `_workspace/`in and of Agent .

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
| Image | vs Prompt 1 when → when + Prompt Text |
| | StoryDesign 3 Suggestion after |
| Agent failure | 1 retry -> if still fails, proceed without that deliverable, note omission in review report |
| RED found in review | Request revision from relevant agent -> rework -> re-verify (up to 2 times) |
| Image-Text Emotion conflict | Image Prompt Text |

## Test Scenarios

### Normal Flow
**Prompt**: "'whenof ' to Visual in . 8Scene "
**Expected Result**:
- Story lean: 8Scene Narrative arc, Emotion Curve, Visual ( )
- in Text: Sceneper narration+Caption+Quote, rhythm Writing style
- Image: 8 Style , color palette
- HTML: Responsive Layout, +Text+Quote Pattern combination
- Review: matrix before Verification

### Existing File Utilization Flow
**Prompt**: " in in Image and HTMLto " + Text File
**Expected Result**:
- Text `_workspace/02_essay_text.md`to 
- architect Text Analysisto between lean 
- prompter + builder + reviewer 

### Error Flow
**Prompt**: "Visual Story , "
**Expected Result**:
- architect 3 Suggestion (//daily life etc.)
- to , 6Scene composition
- Review in the report " " when

## Extended Skills per Agent

per Agentof before Extended Skill:

| | subject Agent | Role |
|------|-------------|------|
| `image-prompt-engineering` | image-prompter | 5-Layer Prompt Structure, Style , Consistency technique |
| `narrative-structure-patterns` | story-architect | 3/5/hero's journey Structure, Emotion Curve, Visual rhythm |
