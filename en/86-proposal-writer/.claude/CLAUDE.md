# Proposal Writer Harness

A harness where an agent team collaborates to produce a complete proposal, covering client analysis, solution design, pricing, differentiation strategy, and document design.

## Structure

```
.claude/
├── agents/
│   ├── client-analyst.md        — Client analysis (needs, decision-making structure, competitive landscape)
│   ├── solution-architect.md    — Solution design (technical/service composition, implementation plan)
│   ├── pricing-strategist.md    — Pricing strategy (cost analysis, pricing models, ROI)
│   ├── differentiator.md        — Differentiation strategy (USP, competitive advantage, references)
│   └── proposal-designer.md     — Proposal integration and cross-validation (structure, design, QA)
├── skills/
│   ├── proposal-writer/
│   │   └── skill.md             — Orchestrator (team coordination, workflow, error handling)
│   ├── roi-calculator/
│   │   └── skill.md             — ROI calculation framework (pricing-strategist extension)
│   └── win-theme-builder/
│       └── skill.md             — Win Theme development (differentiator extension)
└── CLAUDE.md                    — This file
```

## Usage

Trigger the `/proposal-writer` skill, or make a natural language request such as "create a proposal" or "write a business proposal."

## Deliverables

All deliverables are saved in the `_workspace/` directory:
- `00_input.md` — Organized user input
- `01_client_analysis.md` — Client analysis report
- `02_solution_design.md` — Solution design document
- `03_pricing_model.md` — Pricing strategy document
- `04_differentiation.md` — Differentiation strategy document
- `05_final_proposal.md` — Final proposal and validation report
