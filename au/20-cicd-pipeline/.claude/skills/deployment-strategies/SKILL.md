---
name: deployment-strategies
description: "Deployment strategy catalog. An extension skill for pipeline-designer that provides pros/cons, implementation patterns, rollback procedures, health check design, and DORA metrics for Blue-Green/Canary/Rolling/A-B Test/Shadow deployment strategies. Use when designing deployment pipelines involving 'deployment strategy', 'Blue-Green', 'Canary', 'Rolling', 'rollback', 'zero-downtime deployment', 'DORA metrics', etc. Note: actual infrastructure configuration and monitoring tool setup are outside the scope of this skill."
---

# Deployment Strategies — Deployment Strategy Catalog

A reference of deployment strategies, rollback procedures, health checks, and DORA metrics used by the pipeline-designer agent when designing deployment pipelines.

## Target Agent

`pipeline-designer` — Directly applies the deployment strategies and rollback patterns from this skill to pipeline design.

## Deployment Strategy Comparison

| Strategy | Downtime | Risk | Infra Cost | Rollback Speed | Best For |
|----------|----------|------|-----------|---------------|----------|
| **Rolling** | None | Medium | Low | Medium | General web services |
| **Blue-Green** | None | Low | 2x | Instant | Mission-critical |
| **Canary** | None | Very low | Slightly extra | Instant | High-traffic systems |
| **Recreate** | Yes | High | None | Slow | Dev/staging |
| **A/B Test** | None | Low | Slightly extra | Instant | Feature experiments |
| **Shadow** | None | None | 2x | N/A | Performance/compatibility validation |

## Strategy Details

### 1. Rolling Update (Sequential Replacement)
```
Server pool: [v1] [v1] [v1] [v1]
Step 1:      [v2] [v1] [v1] [v1]  -- 1 replaced
Step 2:      [v2] [v2] [v1] [v1]  -- 2 replaced
Step 3:      [v2] [v2] [v2] [v1]  -- 3 replaced
Step 4:      [v2] [v2] [v2] [v2]  -- Complete
```

**Configuration parameters**:
- `maxUnavailable`: Maximum instances to take down simultaneously (1 or 25%)
- `maxSurge`: Maximum instances to add simultaneously (1 or 25%)

**Kubernetes example**:
```yaml
strategy:
  type: RollingUpdate
  rollingUpdate:
    maxUnavailable: 1
    maxSurge: 1
```

**Pros**: Minimal extra infrastructure, gradual replacement
**Cons**: v1+v2 coexistence period (requires compatibility)

### 2. Blue-Green Deployment
```
Blue (current):  [v1] [v1] [v1]  <- 100% traffic
Green (standby): [v2] [v2] [v2]  <- 0% traffic

Switch:
Blue:   [v1] [v1] [v1]  <- 0% traffic (standby/remove)
Green:  [v2] [v2] [v2]  <- 100% traffic
```

**Procedure**:
1. Deploy new version to Green environment
2. Run smoke tests/health checks on Green
3. Switch load balancer traffic to Green
4. Monitor Blue environment (rollback standby)
5. After stabilisation, remove Blue or hold for next deployment

**Rollback**: Re-switch load balancer to Blue (within seconds)

### 3. Canary Deployment
```
Step 1: [v1 x 95%] [v2 x 5%]   -- Start with 5% traffic
Step 2: [v1 x 80%] [v2 x 20%]  -- Expand if metrics are normal
Step 3: [v1 x 50%] [v2 x 50%]  -- Further expansion
Step 4: [v2 x 100%]             -- Full rollout
```

**Per-stage validation criteria**:
| Stage | Traffic | Wait Time | Validation |
|-------|---------|-----------|------------|
| 1 | 5% | 10-30 min | Error rate, latency |
| 2 | 20% | 30-60 min | Add business metrics |
| 3 | 50% | 1-2 hours | All metrics |
| 4 | 100% | - | Complete |

**Automatic rollback conditions**:
- Error rate > 1% (2x normal)
- p99 latency > 2 seconds (50% increase from normal)
- Business metric anomaly (conversion rate, revenue, etc.)

### 4. A/B Testing (Feature Experiment)
- Traffic splitting based on user segments
- Integrated with Feature Flag systems
- Decide after achieving statistical significance

### 5. Shadow (Mirroring)
- Replicate production traffic to new version (responses discarded)
- Used only for performance, error, and compatibility validation
- Zero user impact

## Health Check Design

### Three-Level Health Checks

| Type | Validates | Endpoint | Interval |
|------|----------|----------|----------|
| **Liveness** | Process survival | `/healthz` | 10s |
| **Readiness** | Ready to receive traffic | `/readyz` | 5s |
| **Startup** | Initialisation complete | `/healthz` | 1s (max 300s) |

### Health Check Response Structure
```json
{
  "status": "healthy",
  "version": "2.1.0",
  "uptime": 86400,
  "checks": {
    "database": { "status": "healthy", "latency": "2ms" },
    "redis": { "status": "healthy", "latency": "1ms" },
    "external_api": { "status": "degraded", "latency": "500ms" }
  }
}
```

### Kubernetes Probe Configuration
```yaml
livenessProbe:
  httpGet:
    path: /healthz
    port: 8080
  initialDelaySeconds: 15
  periodSeconds: 10
  failureThreshold: 3

readinessProbe:
  httpGet:
    path: /readyz
    port: 8080
  initialDelaySeconds: 5
  periodSeconds: 5
  failureThreshold: 3
```

## Rollback Procedures

### Automatic Rollback Triggers
| Metric | Threshold | Duration |
|--------|-----------|----------|
| HTTP 5xx rate | > 5% | 2 min consecutive |
| Latency p99 | > 3s | 5 min consecutive |
| Pod restarts | > 3 times | Within 10 min |
| Memory/CPU | > 90% | 5 min consecutive |

### Rollback Procedure
```
1. Trigger detected -> Auto-alert (Slack/PagerDuty)
2. Immediate switch to previous version
   - Blue-Green: Switch load balancer
   - Canary: Set canary traffic to 0%
   - Rolling: kubectl rollout undo
3. Root Cause Analysis (RCA)
4. Fix and redeploy
```

## DORA Metrics

### 4 Key Metrics

| Metric | Description | Elite | High | Medium | Low |
|--------|-------------|-------|------|--------|-----|
| **Deployment frequency** | Production deployment cadence | On demand (multiple/day) | Daily-weekly | Monthly | Less than monthly |
| **Lead time** | Commit-to-deploy time | < 1 hour | 1 day-1 week | 1 week-1 month | 1 month+ |
| **Change failure rate** | Post-deployment failure ratio | < 5% | 6-15% | 16-30% | > 30% |
| **Recovery time** | Incident-to-recovery time | < 1 hour | < 1 day | 1 day-1 week | 1 week+ |

### Measurement Automation
```
Deployment frequency = Production deployment event count / period
Lead time = Production deploy time - First commit time
Change failure rate = Rollback deployments / Total deployments x 100
Recovery time = Incident resolution time - Incident detection time
```

## Branch Strategy and Deployment Mapping

| Branch Strategy | Deployment Flow | Best For |
|----------------|----------------|----------|
| **Trunk-Based** | main -> staging -> production | Small teams, frequent deployments |
| **GitHub Flow** | feature -> PR -> main -> production | Medium teams, mature CI/CD |
| **GitFlow** | feature -> develop -> release -> main | Large teams, fixed release cycles |

### Per-Environment Auto-Deployment Rules
```
feature/* -> PR -> preview environment (ephemeral)
main       -> auto -> staging (automated testing)
main + tag -> manual approval -> production
hotfix/*   -> emergency -> production (simplified approval)
```
