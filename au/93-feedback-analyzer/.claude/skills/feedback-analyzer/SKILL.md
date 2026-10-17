---
name: feedback-analyzer
description: "A comprehensive customer/employee feedback analysis pipeline. An agent team collaborates to handle data collection, sentiment analysis, topic classification, trend detection, and insight reporting. Use this skill for 'analyse feedback', 'customer review analysis', 'survey results analysis', 'VOC analysis', 'employee satisfaction analysis', 'NPS analysis', 'customer complaint analysis', 'feedback trends', 'sentiment analysis', and similar feedback/review/survey analysis topics. Survey design, customer response manual creation, and CRM system development are out of scope."
---

# Feedback Analyser — Comprehensive Feedback Analysis Pipeline

Collects and analyses customer/employee feedback data to produce sentiment analysis, topic classification, trend detection, and insight reports through agent team collaboration.

## Execution Mode

**Agent Team** — 5 members communicate directly via SendMessage and cross-validate each other's work.

## Agent Roster

| Agent | File | Role | Type |
|-------|------|------|------|
| data-collector | `.claude/agents/data-collector.md` | Data collection, cleansing, normalisation | general-purpose |
| sentiment-analyst | `.claude/agents/sentiment-analyst.md` | Sentiment analysis, emotion scoring | general-purpose |
| topic-classifier | `.claude/agents/topic-classifier.md` | Topic classification, category design | general-purpose |
| trend-detector | `.claude/agents/trend-detector.md` | Trend analysis, anomaly detection | general-purpose |
| insight-writer | `.claude/agents/insight-writer.md` | Insight report, action items | general-purpose |

## Workflow

### Phase 1: Preparation (performed directly by the orchestrator)

1. Extract from user input:
    - **Feedback data**: Text files, CSV, paste, or verbal description
    - **Data source type**: Customer reviews/surveys/support logs/employee feedback/social media
    - **Analysis purpose**: Product improvement/service quality/employee satisfaction/competitive analysis
    - **Comparison baseline** (optional): Previous period, competitors, targets
    - **Existing categories** (optional): User-defined classification system
2. Create the `_workspace/` directory in the project root
3. Organise the input and save to `_workspace/00_input.md`
4. Determine the **execution mode** based on the request scope

### Phase 2: Team Assembly and Execution

| Order | Task | Owner | Dependencies | Deliverable |
|-------|------|-------|-------------|-------------|
| 1 | Data collection/cleansing | collector | None | `_workspace/01_data_collection.md` |
| 2a | Sentiment analysis | sentiment | Task 1 | `_workspace/02_sentiment_analysis.md` |
| 2b | Topic classification | classifier | Task 1 | `_workspace/03_topic_classification.md` |
| 3 | Trend analysis | trend | Tasks 2a, 2b | `_workspace/04_trend_report.md` |
| 4 | Insight report | writer | Tasks 2a, 2b, 3 | `_workspace/05_insight_report.md` |

Tasks 2a (sentiment) and 2b (topic) run **in parallel**. Both depend only on Task 1.

**Inter-team communication flow:**
- collector completes → sends cleansed data to sentiment, dataset/keywords to classifier, distribution data to trend
- sentiment completes → sends emotion-tagged data to classifier (for cross-analysis), time-series emotion data to trend
- classifier completes → sends topic time-series to trend, categories/urgent issues to writer
- trend completes → sends key trends/anomalies/forecasts to writer
- writer synthesizes all agent results into the insight report

### Phase 3: Integration and Final Deliverables

1. Verify all files in `_workspace/`
2. Cross-validation:
    - [ ] Sentiment analysis count matches data collection count
    - [ ] Topic classification unclassified rate is 10% or below
    - [ ] Insights cite data evidence
    - [ ] Action items follow SMART principles
3. Request corrections from the relevant agent if discrepancies are found (up to 2 rounds)
4. Report the final summary to the user

## Execution Modes by Scope

| User Request Pattern | Execution Mode | Agents Involved |
|---------------------|----------------|-----------------|
| "Analyse all feedback" | **Full Pipeline** | All 5 |
| "Just do sentiment analysis" | **Sentiment Mode** | collector + sentiment |
| "Classify this data by topic" | **Classification Mode** | collector + classifier |
| "Just look at trends" (existing analysis) | **Trend Mode** | trend + writer |
| "Just write the executive report" (existing analysis) | **Report Mode** | writer solo |

**Leveraging existing analysis**: When the user provides previous analysis results, copy to `_workspace/` and skip the corresponding agent.

## Data Transfer Protocol

| Strategy | Method | Usage |
|----------|--------|-------|
| File-based | `_workspace/` directory | Primary deliverable storage and sharing |
| Message-based | SendMessage | Real-time key information transfer, correction requests |
| Task-based | TaskCreate/TaskUpdate | Progress tracking, dependency management |

## Error Handling

| Error Type | Strategy |
|-----------|----------|
| Data parsing failure | collector processes text-extractable portions only, notes failure sections |
| Extremely small data (fewer than 5) | Include "insufficient for statistical significance" warning, switch to qualitative analysis |
| Mixed languages | Separate analysis by language, analyse primary language only if cross-comparison is not possible |
| High sentiment analysis uncertainty | Tag with "[Confidence: Low]", recommend manual review |
| Agent failure | 1 retry → proceed without that deliverable if still failing, note omission in report |

## Test Scenarios

### Normal Flow
**Prompt**: "Analyse this customer review data. It's 200 app store reviews from the last 3 months."
**Expected Results**:
- Data collection: 200 entries cleansed, basic statistics, channel distribution
- Sentiment: Positive/negative/neutral ratios, NPS estimate, extreme sentiment highlights
- Topic: 3-5 major categories, topic × sentiment cross-analysis
- Trends: 3-month sentiment trajectory, anomaly detection
- Insights: Executive Summary, Top 3 insights, priority matrix

### Existing File Flow
**Prompt**: "I have a previous sentiment analysis. Based on that, just create trends and a report."
**Expected Results**:
- Existing sentiment results copied to `_workspace/02_sentiment_analysis.md`
- Trend mode: trend + writer only
- Trend analysis and insight report generated from existing data

### Error Flow
**Prompt**: "Analyse just 5 customer feedback entries"
**Expected Results**:
- Include "insufficient for statistical significance" warning
- Switch to qualitative analysis: in-depth analysis of individual feedback
- Provide "snapshot analysis" instead of trend analysis
- Report specifies "Additional data collection recommended"

## Agent Extension Skills

| Extension Skill | Path | Target Agent | Role |
|----------------|------|--------------|------|
| sentiment-scoring | `.claude/skills/sentiment-scoring/skill.md` | sentiment-analyst | Sentiment classification, scoring, NPS, context correction |
| text-analytics-methods | `.claude/skills/text-analytics-methods/skill.md` | topic-classifier, trend-detector | Topic classification, keyword analysis, trend detection, insight derivation |
