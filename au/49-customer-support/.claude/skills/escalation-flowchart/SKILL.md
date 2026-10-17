---
name: escalation-flowchart
description: "A methodology for systematically designing escalation tiers and defining SLAs. Use this skill for 'escalation design', 'SLA definition', 'issue severity classification', 'crisis response protocol', 'support routing', and other escalation system design needs. However, CRM system configuration and call centre routing implementation are outside the scope of this skill."
---

# Escalation Flowchart — Escalation Design Methodology

A skill that enhances the escalation policy design capabilities of escalation-manager.

## Target Agents

- **escalation-manager** — Designs systematic escalation policies
- **response-specialist** — Reflects escalation trigger conditions in responses

## 3-Tier Escalation Structure

### L1: Frontline (First Response)

```
Assigned To: CS Agents (General)
Scope: FAQ, general inquiries, simple processing
Authority:
  - Information guidance
  - Basic account settings
  - Small credits (under $50)
  - Standard refund processing
Response SLA:
  Chat 30 sec, Email 4 hours, Phone immediate
Resolution Target: 70-80% of all inquiries
```

### L2: Specialist Support (Second Response)

```
Assigned To: Senior Agents, Technical Support
Scope: Technical issues, complex account problems, special requests
Authority:
  - Technical investigation and resolution
  - Medium credits (under $500)
  - Exception processing approval
  - Cross-department coordination
Response SLA:
  Chat 2 min, Email 8 hours
Resolution Target: 80% of L1 unresolved cases
```

### L3: Expert/Manager (Third Response)

```
Assigned To: Team Leaders, Development Team, Legal Team
Scope: Service outages, legal issues, VIP complaints
Authority:
  - Large compensation decisions
  - Service modification/patch requests
  - Official apology issuance
  - Legal response initiation
Response SLA:
  Critical 1 hour, Normal 24 hours
Resolution Target: All unresolved cases
```

## Issue Severity Classification

| Grade | Description | Example | SLA | Escalation |
|-------|-------------|---------|-----|------------|
| SEV-1 (Critical) | Full service outage, data breach | Entire service down | 15 min response, 4 hr resolution | Immediate L3 + Executives |
| SEV-2 (Major) | Core feature failure, multiple users affected | Payments not working | 30 min response, 8 hr resolution | L3 if unresolved in 1 hr |
| SEV-3 (Moderate) | Partial feature failure, workaround available | Specific feature error | 4 hr response, 24 hr resolution | L1 or L2 |
| SEV-4 (Low) | Minor issue, inconvenience | UI display error | 24 hr response, 72 hr resolution | L1 |

## Escalation Trigger Conditions

### Automatic Escalation

```
L1 → L2 Triggers:
  - Interaction exceeds 15 minutes
  - Same issue inquired 3+ times
  - Technical investigation required (log review, etc.)
  - Customer requests supervisor

L2 → L3 Triggers:
  - Unresolved for 24 hours
  - Customer mentions on social media/press
  - Legal action mentioned
  - SEV-1/SEV-2 issue
  - VIP/Enterprise customer
```

### Emotion-Based Escalation

```
Emotion Level Assessment:
  Green (Stable): Proceed with normal response
  Yellow (Dissatisfied): Strengthen empathy, attempt L1 resolution
  Red (Agitated): Immediate L2 escalation
  Black (Threatening): Immediate L3 + Legal team alert

Detection Keywords:
  Red: "Let me speak to your manager", "consumer protection", "lawsuit", "press"
  Black: Threats, hacking mentions, personal attacks, threatening language
```

## Escalation Process Flow

```
Customer Inquiry Incoming
     |
     +-- Auto-classification (keyword/customer grade)
     |
     +-- L1 Assignment
     |   +-- Resolved → Close + CSAT survey
     |   +-- Unresolved → Check triggers
     |       +-- Auto trigger → L2 assignment
     |       +-- Manual judgment → L2 request
     |
     +-- L2 Assignment
     |   +-- Resolved → Close + CSAT survey
     |   +-- Unresolved → L3 escalation
     |       +-- Technical issue → Development team
     |       +-- Legal issue → Legal team
     |       +-- Business → Team leader
     |
     +-- L3 Processing
         +-- Resolved → Notify customer + follow-up management
         +-- Unresolved → Executive report
```

## SLA Matrix Template

```markdown
| Channel | First Response | Update Frequency | Resolution Target |
|---------|---------------|------------------|-------------------|
| Chat | 30 sec | Real-time | 10 min |
| Phone | Immediate | Real-time | During call |
| Email | 4 hours | 24 hours | 48 hours |
| Social Media | 1 hour | 4 hours | 24 hours |

After Hours:
  SEV-1/2: 24/7 response (on-call)
  SEV-3/4: Next business day
```

## Crisis Response Protocol (SEV-1)

```
T+0 min: Issue detected
  → Immediate Slack/phone alert
  → Assign owner

T+15 min: Initial assessment
  → Determine impact scope
  → Draft customer notice

T+30 min: Customer communication
  → In-app notice / Status page update
  → "We are aware of [issue] and are actively working to resolve it"

T+1 hour: Executive report
  → Impact scope, estimated resolution time, required resources

T+Resolution: Post-incident actions
  → Customer notice (resolution complete)
  → Determine compensation for affected customers
  → Post-mortem (5 Whys)
```
