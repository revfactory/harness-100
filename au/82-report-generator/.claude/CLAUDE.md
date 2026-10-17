# Report Generator Harness

work report datacollection→analysis→visualisation→→summary A harness where an agent team collaborates to produce deliverables.

## structure

```
.claude/
├── agents/
│ ├── data-collector.md — data collection ( , figure , refinement)
│ ├── analyst.md — data analysis (statistics, trend, insight derive)
│ ├── visualizer.md — visualization design (chart, , infographic peopletax)
│ ├── report-writer.md — report (structuredone report writing)
│ └── executive-summarizer.md — summary and cross-verification (core summary, consistency confirm)
├── skills/
│ ├── report-generator/
│ │ └── skill.md — Orchestrator (team , workflow, error handling)
│ ├── data-visualization-guide/
│ │ └── skill.md — data visualization guide (visualizer extension)
│ └── kpi-dashboard-patterns/
│ └── skill.md — KPI dashboard design pattern (analyst extension)
└── CLAUDE.md — file
```

## usage

`/report-generator` skill , "work report create it" specialistannual request.

## deliverable

all deliverable `_workspace/` save:
- `00_input.md` — user input organisation
- `01_data_collection.md` — collectiondone data organisation
- `02_analysis_report.md` — analysis result
- `03_visualization_spec.md` — visualisation peopletax
- `04_full_report.md` — final report
- `05_executive_summary.md` — management summary and verify reporting

## AU Localisation Change History

| Date | Change | Scope | Why |
|------|--------|-------|-----|
| 2026-10-17 | 0 regulatory/currency term substitutions (Privacy Act 1988 (Cth)/APPs, Spam Act 2003 (Cth), IP Australia, ATO, AUD); 74 Australian English spellings | agents/, skills/ prose only (code fences, inline code, identifiers untouched) | FinHub (Australia): AU law, currency and spelling |
