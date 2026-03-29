---
name: meal-planner
description: "A full pipeline where an agent team collaborates to handle everything from nutritional analysis to cooking guides for meal management. Use this skill for any meal, nutrition, or recipe-related requests such as 'create a meal plan', 'weekly meal plan', 'diet meal plan', 'bulking meal plan', 'diabetic meal plan', 'baby food plan', 'grocery list', 'analyze my nutrition', 'give me a recipe', 'meal prep plan', 'calorie count', 'manage my diet'. If an existing meal plan is provided, supports nutritional analysis and improvement. Does NOT cover medical nutrition therapy (MNT) prescriptions, food safety certification, or restaurant menu development consulting."
---

# Meal Planner — Full Meal Management Pipeline

An agent team collaborates to generate nutrition analysis → meal design → recipes → grocery list → cooking guide all at once.

## Execution Modes

**Agent Team** — 4 agents communicate directly via SendMessage and cross-validate each other.

## Agent Composition

| Agent | File | Role | Type |
|---------|------|------|------|
| nutritionist | `.claude/agents/nutritionist.md` | Nutritional analysis, calorie & macro goal setting | general-purpose |
| meal-designer | `.claude/agents/meal-designer.md` | Daily/weekly meal plan design | general-purpose |
| recipe-writer | `.claude/agents/recipe-writer.md` | Detailed recipes, nutritional info, ingredient substitutions | general-purpose |
| shopping-coordinator | `.claude/agents/shopping-coordinator.md` | Grocery list, cooking guide, meal prep | general-purpose |

## Workflow

### Phase 1: Preparation (Orchestrator performs directly)

1. Extract from user input:
    - **Physical info**: gender, age, height, weight, activity level
    - **Goal**: weight loss / maintenance / weight gain / muscle gain / health management
    - **Dietary restrictions** (optional): allergies, vegetarian, religious restrictions, medical conditions
    - **Preferences** (optional): liked/disliked foods, cooking time constraints
    - **Duration**: how many days/weeks of meal plan
    - **Number of people**: single / family size
2. Create a `_workspace/` directory in the project root
3. Organize the input and save to `_workspace/00_input.md`
4. **Determine execution mode** based on the scope of the request

### Phase 2: Team Assembly and Execution

| Order | Task | Assigned To | Depends On | Output |
|------|------|------|------|--------|
| 1 | Nutritional analysis & goal setting | nutritionist | None | `_workspace/01_nutrition_analysis.md` |
| 2 | Meal plan design | meal-designer | Task 1 | `_workspace/02_meal_plan.md` |
| 3 | Recipe writing | recipe-writer | Tasks 1, 2 | `_workspace/03_recipes.md` |
| 4a | Grocery list | shopping-coordinator | Task 3 | `_workspace/04_shopping_list.md` |
| 4b | Cooking guide | shopping-coordinator | Tasks 2, 3 | `_workspace/05_cooking_guide.md` |

**Team communication flow:**
- nutritionist completes → sends calorie & macro targets and dietary restrictions to meal-designer
- meal-designer completes → requests recipe writing per menu item from recipe-writer, sends meal prep strategy to shopping-coordinator
- recipe-writer completes → sends full ingredient list to shopping-coordinator
- shopping-coordinator verifies consistency when consolidating ingredients. If gaps or mismatches found, requests confirmation from recipe-writer

### Phase 3: Integration and Final Deliverables

1. Review all files in `_workspace/`
2. Verify that nutrient totals in the meal plan and recipes match the targets
3. Report final summary to the user:
    - Nutritional analysis — `01_nutrition_analysis.md`
    - Meal plan — `02_meal_plan.md`
    - Recipe collection — `03_recipes.md`
    - Grocery list — `04_shopping_list.md`
    - Cooking guide — `05_cooking_guide.md`

## Mode by Task Scope

| User Request Pattern | Execution Mode | Agents Deployed |
|----------------|----------|-------------|
| "Create a full meal plan", "weekly meal plan" | **Full Pipeline** | All 4 agents |
| "Calculate my calories" | **Nutrition Analysis Mode** | nutritionist only |
| "Give me a recipe for tonight's dinner" | **Recipe Mode** | recipe-writer only |
| "Analyze the nutrition of this meal plan" (existing file) | **Analysis Mode** | nutritionist only |
| "Just make me a grocery list" (meal plan provided) | **Shopping Mode** | shopping-coordinator only |

**Using existing files**: If the user provides an existing meal plan, copy it to `_workspace/02_meal_plan.md` and skip that step.

## Data Transfer Protocol

| Strategy | Method | Purpose |
|------|------|------|
| File-based | `_workspace/` directory | Store and share primary deliverables |
| Message-based | SendMessage | Real-time key info delivery, revision requests |
| Task-based | TaskCreate/TaskUpdate | Progress tracking, dependency management |

File naming convention: `{order}_{agent}_{deliverable}.{extension}`

## Error Handling

| Error Type | Strategy |
|----------|------|
| Insufficient physical info from user | Use default values based on population averages, mark as "estimated" |
| Extreme calorie targets | Adjust to safe range + display warning |
| Dietary restrictions make menu composition difficult | Suggest alternative menus + nutrition supplementation guidance |
| Agent failure | 1 retry → if still failing, proceed without that deliverable and note the gap in the report |
| Nutrient targets not met | Request menu replacement from meal-designer (max 2 times) |

## Test Scenarios

### Normal Flow
**Prompt**: "Male in his 30s, 178cm, 82kg, office worker who exercises 3 times a week. Create a 1-week meal plan to lose 5kg."
**Expected Results**:
- Nutritional analysis: BMR → TDEE calculation, deficit calories (~1800kcal), macro distribution
- Meal plan: 7 days × 3 meals + snacks, daily calorie target achievement rate 95% or above
- Recipes: minimum 15 recipes (excluding duplicates), with ingredient substitutions
- Grocery list: consolidated list by category, split into 2 shopping trips per week, budget estimate
- Cooking guide: Sunday meal prep plan + daily cooking timeline

### Existing File Flow
**Prompt**: "Here's my current meal plan — analyze the nutrition and tell me how to improve it" + attached meal plan file
**Expected Results**:
- Copy existing meal plan to `_workspace/02_meal_plan.md`
- nutritionist performs nutritional analysis of the current meal plan
- Generate report including improvement recommendations

### Error Flow
**Prompt**: "I have a nut allergy and can't eat dairy. Create a vegan meal plan."
**Expected Results**:
- Apply dietary restrictions: exclude all nuts, dairy, and animal products
- Inform of protein deficiency risk + strengthen plant-based protein sources in the meal plan
- Recommend supplementation for vitamin B12, calcium, and omega-3
- Provide thorough list of ingredient substitutions

## Per-Agent Extended Skills

| Agent | Extended Skill | Purpose |
|---------|----------|------|
| nutritionist, meal-designer | `nutrition-calculator` | BMR/TDEE calculation, macro distribution formulas |
| recipe-writer, meal-designer | `ingredient-substitution-engine` | Allergy substitutions, dietary restriction handling |
