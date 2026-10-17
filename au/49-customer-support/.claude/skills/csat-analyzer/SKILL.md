---
name: csat-analyzer
description: "A methodology for systematically designing and analysing customer satisfaction metrics (CSAT/NPS/CES). Use this skill for 'CSAT analysis', 'NPS design', 'CES measurement', 'CS metrics', 'customer satisfaction system', 'VOC analysis', and other CS performance measurement needs. However, actual survey distribution and statistical software execution are outside the scope of this skill."
---

# CSAT Analyser — Customer Satisfaction Metric Design + Analysis

A skill that enhances the CS performance measurement capabilities of cs-analyst.

## Target Agents

- **cs-analyst** — Designs and analyses CS metric systems
- **cs-reviewer** — Validates CS quality based on metrics

## 3 Core CS Metrics

### CSAT (Customer Satisfaction Score)

```
Question: "How satisfied were you with this interaction?" (1-5 scale)

CSAT = (4 + 5 rated responses) / Total responses x 100%

Benchmarks:
  Excellent: 85%+
  Good: 70-84%
  Needs Improvement: 60-69%
  At Risk: <60%

Measurement Timing: Immediately after interaction (interaction-based)
```

### NPS (Net Promoter Score)

```
Question: "How likely are you to recommend this service to a friend or colleague?" (0-10 scale)

Classification:
  Promoter: 9-10
  Passive: 7-8
  Detractor: 0-6

NPS = Promoter% - Detractor%  (Range: -100 to +100)

Benchmarks (B2C SaaS):
  Excellent: 50+
  Good: 30-49
  Average: 0-29
  At Risk: <0

Measurement Timing: Quarterly (relationship-based)
```

### CES (Customer Effort Score)

```
Question: "How easy was it to resolve your issue?" (1-7 scale)

CES = Average of all responses

Benchmarks:
  Excellent: 5.5+
  Good: 4.5-5.4
  Needs Improvement: 3.5-4.4
  At Risk: <3.5

Measurement Timing: Immediately after interaction (effort-based)
Note: Strongest predictor of repeat purchase behavior
```

## Operational Metrics

### Efficiency Metrics

| Metric | Formula | Benchmark |
|--------|---------|-----------|
| FCR (First Contact Resolution) | 1st contact resolutions / Total cases x 100 | 70-75% |
| AHT (Average Handle Time) | Total handle time / Number of cases | Chat 5-8 min, Phone 6-10 min |
| ASA (Average Speed of Answer) | Total wait time / Answered cases | Chat 30 sec, Phone 60 sec |
| Escalation Rate | Escalated cases / Total cases | <15% |
| Re-inquiry Rate | Re-inquiries within 7 days / Total cases | <20% |

### Productivity Metrics

| Metric | Formula | Purpose |
|--------|---------|---------|
| Cases per Agent | Daily cases / Number of agents | Capacity planning |
| Cost per Channel | Channel cost / Channel cases | Channel optimisation |
| Self-Service Ratio | FAQ/bot resolutions / Total inquiries | Automation effectiveness |

## VOC (Voice of Customer) Analysis Framework

### Sentiment Classification

```
Positive Keywords: thank you, fast, friendly, resolved, satisfied, great
Negative Keywords: complaint, slow, inconvenient, repeated, no response, angry
Neutral: inquiry, confirmation, curious, please let me know

Sentiment Score = (Positive count - Negative count) / Total count
```

### Topic Classification

```
1. Category-based Classification:
   - Product Feature Issues (40%)
   - Billing/Refunds (25%)
   - Shipping/Logistics (15%)
   - Account/Authentication (10%)
   - Other (10%)

2. Trend Analysis:
   - Surging topic detection (week-over-week +50%)
   - New topic identification
   - Seasonal patterns

3. Severity Classification:
   - Critical: Service outage, financial loss
   - Major: Feature malfunction, recurring issues
   - Minor: Inconvenience, improvement requests
```

## CS Dashboard Design

```
Real-Time Monitor (Operations Team):
+------------+------------+------------+
| Queue Count| Avg Wait   | Agents     |
| [Real-time]| [Real-time]| [Avail/Total]|
+------------+------------+------------+
| Hourly Incoming Volume Graph          |
+---------------------------------------+
| Channel Status (Chat/Phone/Email)     |
+---------------------------------------+

Weekly/Monthly Report (Management):
+------------+------------+------------+
| CSAT       | NPS        | FCR        |
| [Trend]    | [Trend]    | [Trend]    |
+------------+------------+------------+
| Inquiry Distribution by Topic + WoW   |
+---------------------------------------+
| Agent Performance (Volume, CSAT)      |
+---------------------------------------+
| Top 5 VOC Issues                      |
+---------------------------------------+
```

## Improvement Framework

```
When CSAT is low:
  1. Agent training (response quality)
  2. Improve response templates
  3. Authority delegation (immediate resolution capability)

When FCR is low:
  1. Strengthen FAQ/knowledge base
  2. Expand agent authority
  3. Redefine escalation criteria

When AHT is high:
  1. Provide macros/templates
  2. Improve internal tool UX
  3. Training + mentoring
```
