---
name: market-research
description: "Full research pipeline where an agent team collaborates to generate industry analysis, competitive analysis, consumer research, trend analysis, and integrated reports. Use this skill for requests like 'do market research', 'competitive analysis', 'industry analysis', 'consumer analysis', 'trend analysis', 'market research', 'market size', 'analyse competitors', 'PESTLE analysis', 'Porter 5 Forces', 'market entry strategy', 'target customer analysis', and other market research tasks. Also supports additional analysis or integrated report writing when existing analysis materials are available. Note: conducting actual surveys, running interviews, statistical software analysis, and purchasing market research reports are outside the scope of this skill."
---

# Market Research — Full Market Research Pipeline

An agent team collaborates to generate industry analysis, competitive analysis, consumer research, trend analysis, and integrated reports.

## Execution Mode

**Agent Team** — Five agents communicate directly via SendMessage and perform cross-validation.

## Agent Composition

| Agent | File | Role | Type |
|-------|------|------|------|
| industry-analyst | `.claude/agents/industry-analyst.md` | Market size, value chain, industry structure | general-purpose |
| competitor-analyst | `.claude/agents/competitor-analyst.md` | Competitor mapping, SWOT, positioning | general-purpose |
| consumer-analyst | `.claude/agents/consumer-analyst.md` | Segmentation, personas, needs analysis | general-purpose |
| trend-analyst | `.claude/agents/trend-analyst.md` | PESTLE, technology trends, scenarios | general-purpose |
| research-reviewer | `.claude/agents/research-reviewer.md` | Cross-validation, insight synthesis, strategic recommendations | general-purpose |

## Workflow

### Phase 1: Preparation (performed directly by the orchestrator)

1. Extract the following from user input:
    - **Research objective**: What business decision will this inform?
    - **Industry/Market**: Target industry, geography, market segment
    - **Existing data** (optional): Prior research, internal data
    - **Deliverable focus**: Full research or specific analysis area
2. Create `_workspace/` directory and save input to `_workspace/00_input.md`
3. Determine execution mode based on request scope

### Phase 2: Team Assembly and Execution

| Order | Task | Owner | Dependencies | Deliverable |
|-------|------|-------|-------------|-------------|
| 1a | Industry analysis | industry-analyst | None | `_workspace/01_industry_analysis.md` |
| 1b | Competitor analysis | competitor-analyst | None | `_workspace/02_competitor_analysis.md` |
| 2a | Consumer analysis | consumer-analyst | Tasks 1a, 1b | `_workspace/03_consumer_analysis.md` |
| 2b | Trend analysis | trend-analyst | Tasks 1a, 1b | `_workspace/04_trend_analysis.md` |
| 3 | Research review | research-reviewer | Tasks 2a, 2b | `_workspace/05_research_report.md` |

Tasks 1a and 1b run in parallel. Tasks 2a and 2b run in parallel.

### Phase 3: Integration and Final Deliverables

1. Verify all files, confirm CRITICAL findings addressed
2. Report final summary to user

## Execution Modes by Request Scope

| User Request Pattern | Execution Mode | Agents Deployed |
|---------------------|---------------|----------------|
| "Full market research" | **Full pipeline** | All 5 agents |
| "Just industry analysis" | **Industry mode** | industry-analyst + reviewer |
| "Competitive analysis only" | **Competition mode** | competitor-analyst + reviewer |
| "Consumer research" | **Consumer mode** | consumer-analyst + reviewer |
| "Trend analysis" | **Trend mode** | trend-analyst + reviewer |

## Error Handling

| Error Type | Strategy |
|-----------|----------|
| Industry not specified | Request clarification or propose 3 related industries |
| Insufficient data | Use analogous markets, clearly note assumptions |
| Agent failure | Retry once > proceed without that deliverable |

## Agent Extension Skills

| Skill | File | Target Agent | Role |
|-------|------|-------------|------|
| tam-sam-som-calculator | `.claude/skills/tam-sam-som-calculator/skill.md` | industry-analyst, research-reviewer | Market sizing methodology |
| porter-five-forces | `.claude/skills/porter-five-forces/skill.md` | industry-analyst, competitor-analyst | Industry structure analysis framework |
