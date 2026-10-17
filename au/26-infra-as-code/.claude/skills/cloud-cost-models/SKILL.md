---
name: cloud-cost-models
description: "AWS/GCP/Azure cost models, sizing guides, Reserved Instance/Savings Plan strategies, and FinOps framework guide. Use this skill for 'cloud costs', 'cost optimisation', 'FinOps', 'instance sizing', 'Savings Plan', 'reserved instances', 'Spot instances', 'cost estimation', and other infrastructure cost-related decisions. Enhances the cost analysis capabilities of cost-optimizer. Note: actual resource provisioning and billing configuration are outside the scope of this skill."
---

# Cloud Cost Models — Cloud Cost Model and FinOps Guide

A practical guide for accurately estimating and optimising cloud infrastructure costs.

## AWS Core Service Cost Models

### EC2 Purchase Option Comparison (ap-northeast-2 basis)

| Option | Discount | Commitment | Flexibility | Suitable Workload |
|--------|---------|-----------|------------|-------------------|
| On-Demand | 0% | None | Maximum | Variable workloads, testing |
| Savings Plan (Compute) | ~30% | 1 year | Instance changeable | Stable baseline load |
| Savings Plan (EC2) | ~40% | 1 year | Within family | Predictable workloads |
| Reserved Instance | ~40% | 1yr/3yr | Limited | 24/7 servers |
| Spot Instance | ~70% | None | Interruptible | Batch, CI/CD, ML |

### Sizing Decision Table

```
CPU utilization < 20% sustained -> Downsizing recommended
CPU utilization > 80% sustained -> Upsize or scale out
Memory utilization < 30%        -> Memory-optimized instance unnecessary

Workload type -> Instance family:
+-- General purpose: t3, m6i (CPU/memory balanced)
+-- Compute intensive: c6i (API servers, computation)
+-- Memory intensive: r6i (cache, in-memory DB)
+-- Storage intensive: i3, d3 (databases)
+-- GPU: p4d, g5 (ML training/inference)
```

### RDS Cost Components

```
Monthly cost = Instance cost + Storage + I/O + Backup + Transfer

Example: db.r6g.xlarge, Multi-AZ, 500GB gp3
+-- Instance: $0.54/h x 730h x 2(Multi-AZ) = $788.40
+-- Storage: 500GB x $0.138/GB = $69.00
+-- Backup (excess): 100GB x $0.095/GB = $9.50
+-- Monthly total: ~$866.90
```

## Per-environment Cost Optimisation Strategies

| Environment | Strategy | Expected Savings |
|------------|----------|-----------------|
| **dev** | Business hours only (12h/day, 5 days/week) = 36% uptime | ~60% savings |
| **staging** | Same as dev + smaller instances | ~70% savings |
| **prod** | Savings Plan + Right-sizing + Auto-scaling | ~40% savings |

### Dev Environment Scheduling

```hcl
# Lambda for auto start/stop of dev environment
resource "aws_cloudwatch_event_rule" "start_dev" {
  schedule_expression = "cron(0 0 ? * MON-FRI *)"  # Weekdays 09:00 KST
}
resource "aws_cloudwatch_event_rule" "stop_dev" {
  schedule_expression = "cron(0 12 ? * MON-FRI *)"  # Weekdays 21:00 KST
}
```

## Cost Estimation Template

```markdown
# Monthly Cost Estimate

## Architecture Summary
| Component | Specs | Quantity |

## Per-environment Costs
| Service | Dev | Staging | Prod | Total |
|---------|-----|---------|------|-------|
| EC2/ECS | | | | |
| RDS | | | | |
| ElastiCache | | | | |
| ALB | | | | |
| S3 | | | | |
| CloudWatch | | | | |
| Data Transfer | | | | |
| **Subtotal** | | | | |

## Optimization Applied
| Optimization | Savings |
|-------------|---------|
| Savings Plan (1 year) | |
| Dev env scheduling | |
| Right-sizing | |
| **Total savings** | |

## Final Cost
- Before optimization: $N/month
- After optimization: $N/month
- Savings rate: N%
```

## FinOps Maturity Model

| Phase | Activities | Tools |
|-------|-----------|-------|
| **Inform** | Cost visibility, tagging, allocation | AWS Cost Explorer, tag policies |
| **Optimise** | Right-sizing, reservations, spot | Compute Optimiser, Trusted Advisor |
| **Operate** | Budget alerts, automated actions, governance | AWS Budgets, Lambda auto-cleanup |
