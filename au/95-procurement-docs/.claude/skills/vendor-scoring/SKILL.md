---
name: vendor-scoring
description: "Vendor evaluation scorecard framework. Referenced by vendor-comparator and evaluation-designer agents when systematically comparing and evaluating vendors. Used for 'vendor evaluation', 'supplier comparison', 'bid evaluation' requests. Note: posting bid announcements and executing contracts are out of scope."
---

# Vendor Scoring — Vendor Evaluation Scorecard

Enhances the vendor evaluation capabilities of vendor-comparator / evaluation-designer agents.

## Evaluation Criteria Framework

### Standard Evaluation Categories

| Category | Weight (Default) | Sub-items |
|----------|-----------------|-----------|
| Technical Fit | 30% | Requirement fulfillment, technical capability, innovation |
| Price Competitiveness | 25% | Unit price, TCO, price structure transparency |
| Track Record/Reliability | 20% | Similar projects, references, financial stability |
| Service/Support | 15% | SLA, response speed, training, maintenance |
| Strategic Fit | 10% | Vision alignment, long-term partnership, innovation roadmap |

### Price Evaluation Formula

```
Technical score: Absolute evaluation (1-5 points per item)
Price score: Relative evaluation

Price score formula (lowest-price basis):
  Score = (Lowest bid / Vendor's bid) × Maximum points

Example:
  Vendor A $100K → (100/100) × 5 = 5.0 points
  Vendor B $120K → (100/120) × 5 = 4.17 points
  Vendor C $150K → (100/150) × 5 = 3.33 points
```

## Comprehensive Evaluation Template

| Evaluation Criteria (Weight) | Vendor A | Vendor B | Vendor C |
|-----------------------------|----------|----------|----------|
| Technical Fit (30%) | 4.2 (1.26) | 3.8 (1.14) | 4.5 (1.35) |
| Price Competitiveness (25%) | 5.0 (1.25) | 4.2 (1.05) | 3.3 (0.83) |
| Track Record/Reliability (20%) | 3.5 (0.70) | 4.5 (0.90) | 4.0 (0.80) |
| Service/Support (15%) | 4.0 (0.60) | 3.5 (0.53) | 4.2 (0.63) |
| Strategic Fit (10%) | 3.8 (0.38) | 4.0 (0.40) | 3.5 (0.35) |
| **Overall Score** | **4.19** | **4.02** | **3.96** |
| **Rank** | **1st** | **2nd** | **3rd** |

## Vendor Risk Evaluation

| Risk Type | Verification Items | Evaluation Method |
|-----------|-------------------|-------------------|
| Financial risk | Revenue, debt ratio, operating profit | Financial statement analysis |
| Operational risk | Workforce stability, processes | On-site audit |
| Dependency risk | Single vendor dependency | Alternative vendor research |
| Legal risk | Lawsuits, regulatory violations | Public disclosure review |
| Reputation risk | Customer complaints, media | Reference check |

## Reference Check Guide

### Question List

| Question | Verification Point |
|----------|-------------------|
| Project scale and duration? | Similarity check |
| On-time delivery rate? | Execution capability |
| Any quality issues? | Problem-solving ability |
| How was change management? | Flexibility |
| Would you select them again? | Overall satisfaction |

## Quality Checklist

| Item | Criteria |
|------|----------|
| Evaluation criteria | 5 categories + weights |
| Price formula | Relative evaluation formula specified |
| Minimum candidates | 3+ vendors |
| References | 2+ per vendor |
| Independence | Evaluator conflict of interest check |
| Transparency | Score calculation basis recorded |
