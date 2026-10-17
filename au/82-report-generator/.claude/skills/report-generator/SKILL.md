---
name: report-generator
description: "work report agent team to datacollection→analysis→visualisation→→summaryto Korean creation Full pipeline. 'work report create it', 'monthbetween report writing', 'minutebasis results reporting', 'project report', 'marketanalysis report', ' report', 'KPI report', 'data analysis report', 'results summary reporting' etc. work report writing before skill usage. existing data analysis result case also visualisation, , summary degreeKRW. However, actualtime BI dashboard building, data directly annual, ERP whensystem integration is outside this skill's scope."
---

# Report Generator — work report Full pipeline

work report datacollection→analysis→visualisation→→summary An agent team collaborates to generate all deliverables at once.

## execution mode

**agent team** — 5 agents communicate directly via SendMessage and cross-verify each other's work.

## agent composition

| agent | file | role | type |
|---------|------|------|------|
| data-collector | `.claude/agents/data-collector.md` | data , figure , refinement | general-purpose |
| analyst | `.claude/agents/analyst.md` | statistics analysis, trend, insight derive | general-purpose |
| visualiser | `.claude/agents/visualizer.md` | chart, , diagram peopletax | general-purpose |
| report-writer | `.claude/agents/report-writer.md` | report structure and | general-purpose |
| executive-summarizer | `.claude/agents/executive-summarizer.md` | management summary, cross-verification | general-purpose |

## workflow

### Phase 1: preparation (Orchestrator directly perform)

1. Extract from user input:
 - **report week**: regarding reportperson
 - **reporting type**: basis(monthbetween/minutebasis/annualbetween) / project / analysis
 - **reporting target**: management / team / actualspecialist / external
 - **duration**: reporting target duration
 - **existing material** (optional): user provideKorean data, analysis result, before report
2. `_workspace/` Create the directory at the project root
3. Organise input and save to `_workspace/00_input.md`
4. If existing files are provided, copy them to `_workspace/`and skip the corresponding Phase
5. Determine the **execution mode** based on the scope of the request ( "task scaleby mode" reference)

### Phase 2: team composition and execution

| order | task | responsible | dependency | deliverable |
|------|------|------|------|--------|
| 1 | data collection | collector | None | `_workspace/01_data_collection.md` |
| 2 | data analysis | analyst | task 1 | `_workspace/02_analysis_report.md` |
| 3a | visualisation peopletax | visualiser | task 2 | `_workspace/03_visualization_spec.md` |
| 3b | report | writer | task 2 | `_workspace/04_full_report.md` |
| 4 | summary and verify | summariser | task 3a, 3b | `_workspace/05_executive_summary.md` |

task 3a(visualisation) and 3b ** execution**. task 2(analysis) only dependency.

**teamKRW between flow:**
- collector complete → analystto data+quality deliver, visualizerto data deliver
- analyst complete → visualizerto visualisation proposal deliver, writerto insight+ beforeitems proposal deliver
- visualiser complete → writerto visualisation peopletax+ position deliver
- writer complete → summarizerto report specialist deliver
- summariser all deliverable cross-verification. 🔴 required revision findings when Request revision from the relevant agent -> rework -> re-verify (up to 2 rounds)

### Phase 3: integration and final deliverable

1. `_workspace/` Verify all files in the directory
2. verify reportConfirm that all critical revisions from the review report have been addressed
3. Report the final summary to the user:
 - data collection — `01_data_collection.md`
 - analysis report — `02_analysis_report.md`
 - visualisation peopletax — `03_visualization_spec.md`
 - final report — `04_full_report.md`
 - management summary — `05_executive_summary.md`

## task scaleby mode

| user request pattern | execution mode | deploy agent |
|----------------|----------|-------------|
| "work report create it", "Full report" | **Full pipeline** | 5people beforeKRW |
| " data analysis report " (data provide) | **analysis mode** | analyst + visualiser + writer + summariser |
| " report summaryplease do" (report provide) | **summary mode** | summariser |
| "visualisation only please do" (analysis result provide) | **visualisation mode** | visualiser + summariser |
| " report reviewplease do" | **review mode** | summariser |

**existing file utilisation**: user data, analysis result etc. existing file provide applicable stage case.

## data deliver protocol

| strategy | method | also |
|------|------|------|
| File-based | `_workspace/` | Store and share major deliverables |
| Message-based | SendMessage | Real-time key information transfer, revision requests |

File naming convention: `{}_{agent}_{deliverable}.{extensionspecialist}`

## error handling

| error type | strategy |
|----------|------|
| web search failure | collection user provide material basedas task, "external data un-secure" specify |
| data insufficient | report data scope within analysis perform, addition secure possible item specify |
| agent failure | Retry once -> proceed without that deliverable, verify report specify |
| verifyfrom 🔴 findings | Request revision from the relevant agent -> rework -> re-verify (up to 2 rounds) |
| reporting target people | management reporting (PREP structure) basicas applied |

## test scenario

### flow
**Prompt**: "2024year 4minutebasis sales performance report create it. reporting target management."
**expected result**:
- data collection: sales related items data, trend collection
- analysis: beforeyear basis versus, minutebasisby , total pyeongbalanced comparison
- visualisation: sales chart, by proportion KRW chart, KPI 
- report: PREP structure, management tone, 3items or more
- summary: 1degree management summary + consistency matrix beforeitem confirm

### existing data utilisation flow
**Prompt**: " CSV data analysis report create it" + data file provide
**expected result**:
- data collection stage case
- providedone data `_workspace/01_data_collection.md` organisation
- analyst + visualiser + writer + summariser deploy

### error flow
**Prompt**: "market report create it, material "
**expected result**:
- collection web searchas items data secure when
- search failure when general market degree basedas task
- verify report "data limitation — web search based estimationvalue utilisation" specify

## agentby extension skill

| extension skill | | target agent | role |
|----------|------|-------------|------|
| data-visualization-guide | `.claude/skills/data-visualization-guide/skill.md` | visualiser | chart optional framework, visualisation principle, rule |
| kpi-dashboard-patterns | `.claude/skills/kpi-dashboard-patterns/skill.md` | analyst, executive-summarizer | KPI definition, dashboard , minute/trend analysis |
