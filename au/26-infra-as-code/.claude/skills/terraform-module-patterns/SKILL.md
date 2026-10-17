---
name: terraform-module-patterns
description: "Detailed guide on Terraform module design patterns, directory structures, state management, and environment separation strategies. Use this skill for 'Terraform modules', 'module structure', 'state management', 'remote state', 'environment separation', 'workspace', 'terragrunt', 'module patterns', and other Terraform module design tasks. Enhances the IaC design capabilities of infra-architect and drift-detector. Note: actual terraform apply and infrastructure provisioning execution are outside the scope of this skill."
---

# Terraform Module Patterns — Terraform Module Design Pattern Guide

Patterns and best practices for designing reusable and maintainable Terraform modules.

## Directory Structure Patterns

### Pattern 1: Module Layer Separation

```
infrastructure/
├── modules/                    # Reusable modules
│   ├── networking/
│   │   ├── vpc/
│   │   │   ├── main.tf
│   │   │   ├── variables.tf
│   │   │   ├── outputs.tf
│   │   │   └── README.md
│   │   ├── security-group/
│   │   └── load-balancer/
│   ├── compute/
│   │   ├── ecs-service/
│   │   ├── lambda/
│   │   └── ec2-asg/
│   └── data/
│       ├── rds/
│       ├── elasticache/
│       └── s3/
├── environments/               # Per-environment configuration
│   ├── dev/
│   │   ├── main.tf            # Module invocations
│   │   ├── terraform.tfvars   # Environment variables
│   │   └── backend.tf         # State storage
│   ├── staging/
│   └── prod/
└── global/                    # Cross-environment (IAM, DNS)
    ├── iam/
    └── route53/
```

### Pattern 2: Terragrunt-based DRY

```
infrastructure/
├── modules/                    # Same as above
├── terragrunt.hcl             # Root config (backend, provider)
└── environments/
    ├── terragrunt.hcl         # Common variables
    ├── dev/
    │   ├── terragrunt.hcl     # include root + env vars
    │   ├── vpc/
    │   │   └── terragrunt.hcl # module source + inputs
    │   ├── ecs/
    │   └── rds/
    └── prod/
```

## Module Design Principles

### 1. Single Responsibility Module

```hcl
# Good: VPC module handles only VPC
module "vpc" {
  source = "./modules/networking/vpc"
  cidr_block = "10.0.0.0/16"
  az_count   = 3
}

# Bad: One module for all infrastructure
module "everything" {  # Anti-pattern!
  source = "./modules/full-stack"
}
```

### 2. Input/Output Design

```hcl
# variables.tf — Validation required
variable "instance_type" {
  type        = string
  description = "EC2 instance type"
  default     = "t3.medium"
  validation {
    condition     = can(regex("^t3\\.", var.instance_type))
    error_message = "Only t3 family is allowed."
  }
}

variable "environment" {
  type = string
  validation {
    condition     = contains(["dev", "staging", "prod"], var.environment)
    error_message = "Must be one of dev, staging, prod."
  }
}

# outputs.tf — Expose only values needed by other modules
output "vpc_id" {
  value       = aws_vpc.main.id
  description = "ID of the created VPC"
}
```

### 3. Conditional Resources

```hcl
variable "enable_monitoring" {
  type    = bool
  default = true
}

resource "aws_cloudwatch_metric_alarm" "cpu" {
  count = var.enable_monitoring ? 1 : 0
  # ...
}
```

## State Management Patterns

### Remote State Configuration

```hcl
# backend.tf
terraform {
  backend "s3" {
    bucket         = "company-terraform-state"
    key            = "environments/prod/vpc/terraform.tfstate"
    region         = "ap-northeast-2"
    dynamodb_table = "terraform-locks"
    encrypt        = true
  }
}
```

### State Separation Strategies

| Strategy | Separation Basis | Pros | Cons |
|----------|-----------------|------|------|
| **Per-environment** | dev/staging/prod | Environment isolation, independent deployment | Need data source for cross-env references |
| **Per-layer** | network/compute/data | Reduced blast radius | Complex reference management |
| **Per-team** | Team-owned resources | Autonomy | Shared resource management difficulty |
| **Per-lifecycle** | Change frequency | Stable resource protection | Boundary definition difficulty |

### Cross-State References

```hcl
# Read VPC ID from network state
data "terraform_remote_state" "network" {
  backend = "s3"
  config = {
    bucket = "company-terraform-state"
    key    = "environments/prod/network/terraform.tfstate"
    region = "ap-northeast-2"
  }
}

# Usage
resource "aws_ecs_service" "app" {
  network_configuration {
    subnets = data.terraform_remote_state.network.outputs.private_subnet_ids
  }
}
```

## Tagging Strategy

```hcl
locals {
  common_tags = {
    Environment = var.environment
    Project     = var.project_name
    ManagedBy   = "terraform"
    Team        = var.team_name
    CostCenter  = var.cost_center
  }
}

resource "aws_instance" "app" {
  tags = merge(local.common_tags, {
    Name = "${var.project_name}-${var.environment}-app"
    Role = "application"
  })
}
```

## Anti-patterns and Solutions

| Anti-pattern | Problem | Solution |
|-------------|---------|----------|
| **Giant state file** | Slow plan/apply, large blast radius | Split by layer |
| **Hardcoded values** | Cannot reuse across environments | variables + tfvars |
| **Provider inside module** | Lost flexibility | Provider only at root |
| **Complex conditions with count** | Resource recreation on index changes | Use for_each |
| **Plaintext secrets** | Security violation | SSM/Vault references |
