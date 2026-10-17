# Market Research Harness

Market research: a harness where an agent team collaborates to perform industry analysis → competitor analysis → consumer analysis → trend analysis → research review.

## Structure

```
.claude/
├── agents/
│   ├── industry-analyst.md    — Industry Analyst (market size, growth rate, value chain, regulatory environment)
│   ├── competitor-analyst.md  — Competitor Analyst (competitive landscape, SWOT, positioning, benchmarking)
│   ├── consumer-analyst.md    — Consumer Analyst (persona, journey mapping, needs analysis, segmentation)
│   ├── trend-analyst.md       — Trend Analyst (technology trends, market trends, future outlook)
│   └── research-reviewer.md   — Research Reviewer (data verification, methodology review, insight synthesis)
├── skills/
│   ├── market-research/
│   │   └── skill.md              — Orchestrator (team coordination, workflow, error handling)
│   ├── porter-five-forces/
│   │   └── skill.md              — Porter's Five Forces analysis framework
│   └── tam-sam-som-calculator/
│       └── skill.md              — TAM/SAM/SOM market sizing methodology
└── CLAUDE.md                  — This file
```

## Usage

Trigger the `/market-research` skill or use natural language like "Conduct market research for me."

## Outputs

All outputs are stored in the `_workspace/` directory:
- `00_input.md` — User input and research scope
- `01_industry_analysis.md` — Industry analysis report
- `02_competitor_analysis.md` — Competitor analysis report
- `03_consumer_analysis.md` — Consumer analysis report
- `04_trend_analysis.md` — Trend analysis report
- `05_research_summary.md` — Integrated research summary and recommendations

## AU Localisation Change History

| Date | Change | Scope | Why |
|------|--------|-------|-----|
| 2026-10-17 | 0 regulatory/currency term substitutions (Privacy Act 1988 (Cth)/APPs, Spam Act 2003 (Cth), IP Australia, ATO, AUD); 13 Australian English spellings | agents/, skills/ prose only (code fences, inline code, identifiers untouched) | FinHub (Australia): AU law, currency and spelling |
