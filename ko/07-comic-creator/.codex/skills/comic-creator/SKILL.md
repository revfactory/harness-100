---
name: comic-creator
description: "Use this skill for Korean comic, 4-panel comic, short comic, long comic, webtoon, storyboard, comic dialogue, panel image prompt, panel image generation with imagegen, page layout, and quality review workflows. It turns a user idea or existing script into concrete workspace artifacts: input brief, storyboard, dialogue script, image prompts, generated panel images when requested/available, layout/editing directions, and review report. Use it when the user asks for 만화 만들어줘, 4컷 만화, 웹툰 제작, 만화 콘티, 만화 시나리오, 코믹 스트립, panel prompts, or comic production help. It does not operate Photoshop/Clip Studio, submit print files, or upload to webtoon platforms."
---

# Comic Creator

Create a comic production package from a user idea or existing script. Work in Korean unless the user asks otherwise.

## Output Contract

Create or update these files under a unique dated workspace folder. Use `WORKSPACE_DIR` below as the concrete folder for the current run.

- `WORKSPACE_DIR/00_input.md`: normalized user brief, format, genre, style, constraints, source files
- `WORKSPACE_DIR/01_storyboard.md`: synopsis, character sheet, page/panel storyboard
- `WORKSPACE_DIR/02_dialogue.md`: dialogue, narration, sound effects, speech bubble notes
- `WORKSPACE_DIR/03_image_prompts.md`: character reference prompts, panel prompts, generation status
- `WORKSPACE_DIR/04_layout.md`: page or webtoon layout/editing directions
- `WORKSPACE_DIR/05_review_report.md`: cross-check report and required fixes
- `WORKSPACE_DIR/panels/`: generated or expected panel images, when image generation is available

If a step is outside the current tool capability, still produce the corresponding prompt/spec file and mark the missing executable step clearly in `05_review_report.md`.

## Workflow

1. Parse the request.
   - Identify story idea, target format, genre, tone, art style, audience, page/panel count, and any supplied source files.
   - If required information is missing but a reasonable default is safe, proceed and record the assumption in `00_input.md`.
   - Default format is a 4-panel comic when the user asks generally for a small comic.
2. Prepare the dated workspace folder.
   - Use today's local date in `YYYY-MM-DD` format.
   - Set `WORKSPACE_DIR` before writing any artifact:
     - If `_workspace/YYYY-MM-DD/` does not exist, use `_workspace/YYYY-MM-DD/`.
     - If `_workspace/YYYY-MM-DD/` already exists, do not reuse it. Create the next numbered sibling folder: `_workspace/YYYY-MM-DD-01/`, `_workspace/YYYY-MM-DD-02/`, and so on.
     - Choose the first number whose folder does not already exist. Use two digits and preserve lexical order.
   - Create `WORKSPACE_DIR/` and `WORKSPACE_DIR/panels/`.
   - Save the normalized brief to `00_input.md`.
   - Copy or summarize any existing scenario/character material into the appropriate numbered artifact.
3. Choose the production mode.
   - Full pipeline: storyboard, dialogue, image prompts or images, layout, review.
   - Storyboard mode: `01_storyboard.md` plus `05_review_report.md`.
   - Dialogue mode: `01_storyboard.md`, `02_dialogue.md`, review.
   - Image mode: use existing script/storyboard, then `03_image_prompts.md`, generate panel images with the `imagegen` skill when requested and available, update `04_layout.md`, review.
   - Review mode: inspect supplied artifacts and write `05_review_report.md`.
4. Produce artifacts in dependency order.
   - Storyboard first.
   - Dialogue and image prompts can be developed independently from the storyboard.
   - Layout depends on storyboard, dialogue, and image prompts/results.
   - Review all outputs together before reporting completion.
5. Verify the final package.
   - Confirm each promised file exists.
   - If image generation was requested and an image tool is available, use `imagegen`. If unavailable or refused, provide production-ready prompts instead.
   - Resolve all critical review items if feasible; otherwise leave them explicit in `05_review_report.md`.

## Image Generation With `imagegen`

Use the `imagegen` skill when the user asks to turn comic prompts into actual raster images, generate panel art, create character sheets, or produce visual comic assets. Default to prompt/spec files only unless the user asks for actual images or the current request clearly includes image generation.

Workflow:

1. Read `03_image_prompts.md` and identify the requested assets.
   - For a 4-panel comic, expected filenames are usually `panels/page1_panel1.png` through `panels/page1_panel4.png`.
   - If a character reference is useful, generate it first as `panels/character_<name>.png` and use its description as a consistency anchor for the panel prompts.
2. Invoke the `imagegen` skill before calling image tools.
   - Use built-in `image_gen` by default.
   - Do not use the CLI/API fallback unless the user explicitly requests it or confirms a fallback path required by the `imagegen` skill.
3. Generate one panel per prompt.
   - Keep exact Korean text out of generated art unless the user explicitly accepts possible text errors.
   - Prefer empty space for later Korean lettering and speech bubbles.
   - Repeat the character anchor phrase in every panel prompt.
4. Persist project-bound images.
   - Move or copy final selected images into `WORKSPACE_DIR/panels/`.
   - Never leave a project-referenced panel only under `$CODEX_HOME/generated_images/`.
   - Do not overwrite existing panel images unless the user asked for replacement; otherwise use a versioned filename such as `page1_panel1-v2.png`.
5. Update artifacts after generation.
   - In `03_image_prompts.md`, change each generated panel's status from prompt-only to generated and record the saved filename.
   - In `04_layout.md`, reference the actual saved panel filenames.
   - In `05_review_report.md`, note whether images were generated, which files exist, and any visual issues that still need correction.
6. Validate before completion.
   - Confirm all requested image files exist under `WORKSPACE_DIR/panels/`.
   - Inspect generated images when possible for character consistency, panel framing, readability, unwanted text, and whether space remains for lettering.

If image generation is unavailable, do not stop the comic workflow. Keep `03_image_prompts.md` production-ready and mark the missing executable step in `05_review_report.md`.

## Codex Collaboration Rules

- Do not rely on legacy harness commands, hooks, or custom message-passing APIs.
- Use normal Codex file editing and verification.
- Use Codex subagents only when the user explicitly asks for subagents/delegation/parallel agent work; otherwise perform the role passes yourself using the role guides.
- Keep durable outputs in the unique dated `WORKSPACE_DIR/` folder, not only in chat.
- Prefer concise, usable production artifacts over long theory.

## Role Passes

Use these role lenses during the workflow. Read [role-guides.md](references/role-guides.md) when detailed output formats are needed.

- Storyboarder: synopsis, character sheet, page/panel breakdown, shot size, angle, transitions.
- Dialogue writer: character voice, speech bubbles, narration, Korean sound effects.
- Image generator: character consistency, art style anchors, panel-level image prompts.
- Image producer: uses `imagegen` to create raster panel assets from `03_image_prompts.md` and saves them under `WORKSPACE_DIR/panels/`.
- Comic editor: speech bubble placement, sound effect layering, gutters, reading flow, page/webtoon layout.
- Quality reviewer: cross-check story, dialogue, image prompts/results, layout, character consistency, and reading flow.

## Specialist References

Load these only when the task needs the detail:

- [panel-composition.md](references/panel-composition.md): panel layout, camera angles, reading flow, page rhythm, prompt structure.
- [visual-narrative.md](references/visual-narrative.md): speech bubbles, sound effects, show-don't-tell, scene transitions, text/image balance.
- [character-design-system.md](references/character-design-system.md): character sheets, silhouettes, expression charts, AI consistency anchors.

## Review Severity

Use these labels in `05_review_report.md`:

- Critical: must fix before the comic package is usable.
- Recommended: improves clarity, pacing, or production quality.
- Note: optional observation or future production guidance.
