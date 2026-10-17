---
name: llm-app-builder
description: "Full pipeline where an agent team collaborates to develop an LLM app. Use this skill for requests like 'build me an LLM app', 'AI app development', 'build a RAG system', 'GPT app', 'AI chatbot development', 'prompt engineering', 'LLM pipeline', 'AI assistant development', 'generative AI app', 'RAG pipeline', and other LLM-based app development tasks. Also supports prompt-only mode when only prompt design is needed. Note: LLM model training (running fine-tuning), GPU infrastructure construction, and model serving (vLLM/TGI deployment) are outside the scope of this skill."
---

# LLM App Builder — LLM App Development Pipeline

An agent team collaborates to develop LLM apps through prompt engineering > RAG pipeline > evaluation > optimisation > deployment.

## Execution Mode

**Agent Team** — Five agents communicate directly via SendMessage and perform cross-validation.

## Agent Composition

| Agent | File | Role | Type |
|-------|------|------|------|
| prompt-engineer | `.claude/agents/prompt-engineer.md` | Prompt design | general-purpose |
| rag-architect | `.claude/agents/rag-architect.md` | RAG pipeline | general-purpose |
| eval-specialist | `.claude/agents/eval-specialist.md` | Evaluation framework | general-purpose |
| optimization-engineer | `.claude/agents/optimization-engineer.md` | Cost/performance optimisation | general-purpose |
| deploy-engineer | `.claude/agents/deploy-engineer.md` | Production deployment | general-purpose |

## Workflow

### Phase 1: Preparation (performed directly by the orchestrator)

1. Extract the following from user input:
    - **App purpose**: What the LLM app does
    - **Data sources**: Documents/data for RAG (optional)
    - **LLM model**: Model to use (default: Claude/GPT-4o)
    - **Deployment environment**: API/web app/chatbot/internal tool
    - **Budget**: Monthly API cost budget
    - **Constraints** (optional): Security, regulatory, performance requirements
2. Create the `_workspace/` directory at the project root
3. Organise the input and save it to `_workspace/00_input.md`
4. Create the `_workspace/src/` directory
5. **Determine the execution mode** based on the scope of the request

### Phase 2: Team Assembly and Execution

| Order | Task | Owner | Dependencies | Deliverable |
|-------|------|-------|-------------|-------------|
| 1a | Prompt design | prompt | None | `_workspace/01_prompt_design.md` |
| 1b | RAG pipeline | rag | None | `_workspace/02_rag_pipeline.md` + `src/` |
| 2 | Evaluation framework | eval | Tasks 1a, 1b | `_workspace/03_eval_framework.md` + `src/` |
| 3 | Optimisation | optimiser | Task 2 | `_workspace/04_optimization.md` + `src/` |
| 4 | Deployment config | deploy | Tasks 1b, 3 | `_workspace/05_deploy_config.md` + `src/` |

Tasks 1a (prompt) and 1b (RAG) run **in parallel**.

**Inter-agent communication flow:**
- prompt completes > passes context injection format to rag, passes expected outputs to eval
- rag completes > passes retrieval test data to eval, passes vector DB infra requirements to deploy
- eval completes > passes performance baseline to optimiser, passes weakness feedback to prompt
- optimiser completes > passes cache/routing config to deploy
- deploy integrates all components to complete the production deployment configuration

### Phase 3: Integration and Final Deliverables

1. Verify that the code in `_workspace/src/` is executable
2. Confirm that evaluation metrics meet the standards
3. Validate that deployment configuration is complete
4. Report the final summary to the user:
    - Prompt design — `01_prompt_design.md`
    - RAG pipeline — `02_rag_pipeline.md`
    - Evaluation framework — `03_eval_framework.md`
    - Optimisation strategy — `04_optimization.md`
    - Deployment config — `05_deploy_config.md`
    - Source code — `src/`

## Execution Modes by Request Scope

| User Request Pattern | Execution Mode | Agents Deployed |
|---------------------|---------------|----------------|
| "Build me an LLM app", "full RAG app" | **Full pipeline** | All 5 agents |
| "Just design prompts" | **Prompt mode** | prompt + eval |
| "Just build the RAG pipeline" | **RAG mode** | rag + eval + deploy |
| "Build an LLM app evaluation system" | **Eval mode** | eval only |
| "Optimise the cost of an existing app" | **Optimisation mode** | optimiser + eval |
| "Set up production deployment" | **Deploy mode** | deploy only |

**When RAG is not needed**: If the user specifies there is no external data source, skip the rag agent.

**Reusing existing files**: If the user provides existing prompts, RAG configs, or code, copy them to the appropriate numbered location in `_workspace/` and skip the corresponding agent. Example: Existing prompt provided > copy to `_workspace/01_prompt_design.md` > skip prompt and deploy remaining agents.

## Data Transfer Protocol

| Strategy | Method | Purpose |
|----------|--------|---------|
| File-based | `_workspace/` directory | Design documents and configuration sharing |
| Message-based | SendMessage | Real-time key information transfer, feedback |
| Code-based | `_workspace/src/` | Executable source code |

## Error Handling

| Error Type | Strategy |
|-----------|----------|
| No LLM API key | Provide environment variable setup guide, suggest local model alternatives |
| No RAG data source | Build as a pure LLM app without RAG, provide guide for adding RAG later |
| No evaluation dataset | Generate synthetic data with LLM, provide manual verification guide |
| Projected budget overrun | Suggest small model routing, enhanced caching, request limits |
| Agent failure | Retry once > if still failing, proceed without that deliverable |

## Test Scenarios

### Normal Flow
**Prompt**: "Build me an employee Q&A chatbot based on internal company documents. About 500 Confluence docs. Monthly budget $200"
**Expected result**:
- Prompt: Q&A system prompt, forced source citation, hallucination prevention guardrails
- RAG: Confluence > markdown conversion > semantic chunking > text-embedding-3-small > Chroma
- Evaluation: 20 golden Q&A sets, Recall@5, faithfulness LLM-as-Judge
- Optimisation: Semantic caching (expected 40% hit rate), small model routing (simple questions)
- Deployment: FastAPI + Docker + cost ceiling $200/month

### Existing File Reuse Flow
**Prompt**: "Based on this RAG code, just do evaluation framework and optimisation" + RAG code attached
**Expected result**:
- Copy existing code to `_workspace/src/`, copy RAG design to `_workspace/02_rag_pipeline.md`
- Skip rag; deploy eval + optimiser + deploy
- Extract prompt from existing code

### Error Flow
**Prompt**: "Build me an AI app" (purpose/data unclear)
**Expected result**:
- Request user to clarify app purpose and data sources
- Ask questions to determine RAG necessity
- Proceed with appropriate mode after confirmation

## Agent Extension Skills

Extension skills that enhance agent domain expertise:

| Skill | File | Target Agent | Role |
|-------|------|-------------|------|
| prompt-optimizer | `.claude/skills/prompt-optimizer/skill.md` | prompt-engineer, eval-specialist | CRISP rubric, RCTF template, guardrail patterns, A/B testing, token optimisation |
| chunking-strategy-guide | `.claude/skills/chunking-strategy-guide/skill.md` | rag-architect, eval-specialist | Chunking strategy comparison, semantic chunking algorithm, per-document preprocessing, quality metrics |
