---
name: fitness-program
description: "A full pipeline where an agent team collaborates to generate everything from goal-based fitness program design to progress tracking templates. Use this skill for requests related to fitness and training programs such as 'create a workout program', 'gym routine', 'strength program', 'diet workout', 'home training', 'weekly workout schedule', 'bulk-up program', 'marathon training', 'workout routine recommendation', 'PPL program', 'bodyweight routine', etc. If an existing program is provided, analysis or improvement is supported. However, rehabilitation program prescription (physical therapist work), performance-enhancing drug consultation, and real-time personal training are outside the scope of this skill."
---

# Fitness Program — Full Design Pipeline

An agent team collaborates to generate goal-based program design → weekly schedule → exercise guide document → nutrition pairing chart → progress tracking template all at once.

## Execution Modes

**Agent Team** — 4 agents communicate directly via SendMessage and perform cross-validation.

## Agent Roster

| Agent | File | Role | Type |
|---------|------|------|------|
| program-architect | `.claude/agents/program-architect.md` | Program design, periodization, scheduling | general-purpose |
| exercise-guide | `.claude/agents/exercise-guide.md` | Exercise descriptions, form guides, substitutions | general-purpose |
| nutrition-linker | `.claude/agents/nutrition-linker.md` | Nutrition strategy per workout, supplements, timing | general-purpose |
| template-builder | `.claude/agents/template-builder.md` | Logs, tracking sheets, evaluation forms | general-purpose |

## Workflow

### Phase 1: Preparation (Orchestrator handles directly)

1. Extract from user input:
    - **Goal**: hypertrophy / strength / fat loss / fitness improvement / rehabilitation
    - **Fitness level**: beginner / intermediate / advanced, training history
    - **Available resources**: X sessions/week, X minutes/session, equipment (gym / home / bodyweight)
    - **Physical info** (optional): sex, age, height, weight
    - **Injury history** (optional): area, current condition
    - **Existing program** (optional): currently running program
2. Create a `_workspace/` directory at the project root
3. Organize inputs and save to `_workspace/00_input.md`
4. **Determine execution mode** based on request scope

### Phase 2: Team Assembly and Execution

| Order | Task | Owner | Depends on | Output |
|------|------|------|------|--------|
| 1 | Program design + weekly schedule | architect | none | `01_program_design.md`, `02_weekly_schedule.md` |
| 2a | Exercise guide document | guide | Task 1 | `03_exercise_guide.md` |
| 2b | Nutrition pairing chart | linker | Task 1 | `04_nutrition_plan.md` |
| 3 | Progress tracking template | builder | Tasks 1, 2a, 2b | `05_tracking_template.md` |

Tasks 2a (exercise guide) and 2b (nutrition pairing) run **in parallel**.

**Inter-agent communication flow:**
- architect completes → sends exercise list and precautions to guide, sends intensity/volume/goal to linker, sends periodization schedule to builder
- guide completes → sends high-intensity exercise list to linker, sends logging items to builder
- linker completes → sends nutrition tracking items to builder
- builder integrates all information to create the template; if missing items are found, requests clarification from the relevant agent

### Phase 3: Integration and Final Deliverables

1. Review all files in `_workspace/`
2. Verify consistency across program–schedule–guide–nutrition–template
3. Report final summary to the user:
    - Program design doc — `01_program_design.md`
    - Weekly schedule — `02_weekly_schedule.md`
    - Exercise guide — `03_exercise_guide.md`
    - Nutrition pairing chart — `04_nutrition_plan.md`
    - Tracking template — `05_tracking_template.md`

## Mode by Request Scope

| User Request Pattern | Execution Mode | Agents Involved |
|----------------|----------|-------------|
| "Build me a full workout program" | **Full Pipeline** | All 4 |
| "Just the weekly workout schedule" | **Schedule Mode** | architect only |
| "Teach me squat form" | **Guide Mode** | guide only |
| "Link a bulk-up diet" (program exists) | **Nutrition Mode** | linker only |
| "Make a workout log" | **Template Mode** | builder only |
| "Analyze this program" (existing file) | **Analysis Mode** | architect + guide |

**Using existing files**: If the user provides an existing program, copy it to `_workspace/01_program_design.md` and skip the architect.

## Data Transfer Protocol

| Strategy | Method | Purpose |
|------|------|------|
| File-based | `_workspace/` directory | Store and share primary deliverables |
| Message-based | SendMessage | Real-time key information transfer, revision requests |
| Task-based | TaskCreate/TaskUpdate | Progress tracking, dependency management |

File naming convention: `{order}_{agent}_{deliverable}.{extension}`

## Error Handling

| Error Type | Strategy |
|----------|------|
| Insufficient user info | Design using conservative (beginner) baseline; note "fitness level unconfirmed" |
| Injury history | Exclude or substitute exercises for the affected area + "consult a specialist" note |
| Equipment limitations | Compose with substitute exercises within available equipment |
| Agent failure | Retry once → if still failing, proceed without that deliverable and note the omission in the report |
| Program inconsistency | Request revision from architect (up to 2 times) |

## Test Scenarios

### Normal Flow
**Prompt**: "I'm a beginner at the gym and want a hypertrophy-focused program, 4 days a week. 178cm, 75kg, 28-year-old male."
**Expected output**:
- Program: upper/lower 4-day split, 12-week periodization (adaptation → accumulation → intensification → deload)
- Schedule: 4 sessions/week × 60 min, sets/reps/RPE specified per exercise
- Guide: form descriptions + substitutions for all exercises in the program (15–20 exercises)
- Nutrition: bulk-up calories (TDEE+300), macros, pre/post-workout timing
- Template: daily log, weekly summary, 4-week evaluation form, body composition tracker

### Existing File Flow
**Prompt**: "Here's my current PPL routine — can you pair it with a diet?" + program file attached
**Expected output**:
- Copy existing program to `_workspace/01_program_design.md`
- Nutrition mode: deploy linker, analyze existing program intensity, generate nutrition pairing chart

### Error Flow
**Prompt**: "I have a herniated disc — create a workout program for me."
**Expected output**:
- Injury history applied: exclude high-lumbar-load exercises (deadlifts, barbell squats)
- Include core stabilization exercises, suggest substitutes (leg press, machine-based)
- All exercises marked with "lumbar caution" ⚠️ + "consult orthopedics/rehabilitation medicine"
- Progressive overload set more conservatively

## Per-Agent Extended Skills

| Agent | Extended Skill | Purpose |
|---------|----------|------|
| exercise-guide | `exercise-biomechanics` | Exercise biomechanics, muscle activation, substitution exercises |
| program-architect, template-builder | `periodization-engine` | Periodization design, volume/intensity calculation, deload strategy |
chitect, template-builder | `periodization-engine` | Periodization design, volume/intensity calculation, deload strategy |
