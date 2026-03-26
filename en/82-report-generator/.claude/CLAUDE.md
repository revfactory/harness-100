# Report Generator Harness

A harness where an agent team collaborates to produce business report deliverables — data collection, analysis, visualization, writing, and executive summary.

## Structure

```
.claude/
├── agents/
│   ├── data-collector.md      — Data collection (source exploration, data extraction, cleansing)
│   ├── analyst.md             — Data analysis (statistics, trends, insight generation)
│   ├── visualizer.md          — Visualization design (charts, tables, infographic specs)
│   ├── report-writer.md       — Report writing (structured report composition)
│   └── executive-summarizer.md — Summary and cross-verification (executive summary, consistency check)
├── skills/
│   ├── report-generator/
│   │   └── skill.md           — Orchestrator (team coordination, workflow, error handling)
│   ├── data-visualization-guide/
│   │   └── skill.md           — Data visualization guide (for visualizer)
│   └── kpi-dashboard-patterns/
│       └── skill.md           — KPI dashboard design patterns (for analyst)
└── CLAUDE.md                  — This file
```

## Usage

Trigger the `/report-generator` skill, or make a natural language request such as "Create a business report for me."

## Deliverables

All deliverables are saved in the `_workspace/` directory:
- `00_input.md` — Organized user input
- `01_data_collection.md` — Collected data summary
- `02_analysis_report.md` — Analysis results
- `03_visualization_spec.md` — Visualization specifications
- `04_full_report.md` — Final report
- `05_executive_summary.md` — Executive summary and verification report
