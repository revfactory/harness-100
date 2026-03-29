---
name: competency-model
description: "Competency model design framework. Referenced by jd-writer and screening-expert agents when defining role-specific core competencies and establishing evaluation criteria. Use for 'competency model', 'job competencies', 'skills matrix' requests. Out of scope: building performance management systems and designing compensation structures."
---

# Competency Model — Competency Model Design

Enhances the competency-based hiring design capabilities of the jd-writer and screening-expert agents.

## Competency Model Structure

### 3-Layer Competency Framework

| Layer | Description | Examples |
|-------|-------------|---------|
| Core Competencies | Company-wide | Customer focus, collaboration, integrity |
| Leadership Competencies | Manager level and above | Vision setting, coaching, decision-making |
| Functional Competencies | Role-specific | Programming, data analysis, design |

### Competency Proficiency Levels

| Level | Name | Description | Typical Grade |
|-------|------|-------------|--------------|
| L1 | Foundation | Performs under supervision; basic understanding | Intern / Entry-level |
| L2 | Practitioner | Performs independently; handles standard tasks | Junior |
| L3 | Skilled | Handles complex situations; can mentor others | Senior |
| L4 | Expert | Organizational impact; drives innovation | Lead / Manager |
| L5 | Master | Industry-level expertise; strategic influence | Director+ |

### Competency Definition Card Template

```markdown
## Competency: [Competency Name]

### Definition
[One-sentence definition]

### Behavioral Indicators

**L1 (Foundation)**
- [Observable behavior 1]
- [Observable behavior 2]

**L2 (Practitioner)**
- [Observable behavior 1]
- [Observable behavior 2]

**L3 (Skilled)**
- [Observable behavior 1]
- [Observable behavior 2]

### Assessment Methods
- Interview question: [Structured question]
- Task: [Practical task]
- Reference check: [Verification points]
```

## Competency Mapping Examples by Role

### Software Engineer

| Competency | Junior (L2) | Senior (L3) | Lead (L4) |
|------------|------------|------------|---------|
| Coding ability | ★★★ Required | ★★★ Required | ★★★ Required |
| System design | ★ Foundation | ★★★ Required | ★★★ Required |
| Code review | ★ Passive | ★★★ Active | ★★★ Leads |
| Mentoring | — | ★★ Preferred | ★★★ Required |
| Technical strategy | — | ★ Participates | ★★★ Leads |

## Linking Competencies to JD Writing

### STAR-Based Qualification Requirements

```markdown
## Qualifications

### Must-Have
- [Competency 1] at L3 or above: [Specific experience / performance criteria]
  Example: "2+ years operating high-traffic systems (1M+ DAU)"
- [Competency 2] at L2 or above: [Specific criteria]

### Nice-to-Have
- [Competency 3]: [Specific criteria]
- [Competency 4]: [Specific criteria]

### What We're Looking For (Behavioral Description)
- [L3 behavioral indicators of Competency 1, written naturally]
- [L3 behavioral indicators of Competency 2, written naturally]
```

## Screening Matrix

| Evaluation Item | Points | PASS Threshold | Assessment Method |
|----------------|--------|---------------|------------------|
| Must-have competency A | 30 | 21+ | Resume + task |
| Must-have competency B | 25 | 18+ | Resume + interview |
| Nice-to-have competency C | 15 | — | Resume |
| Culture fit | 15 | 10+ | Interview |
| Growth potential | 15 | 10+ | Interview |
| **Total** | **100** | **70+** | |

## Quality Checklist

| Item | Standard |
|------|---------|
| Number of competencies | 5–8 per role |
| Level definitions | Specific behavioral indicators for L1–L5 |
| Must-have / Nice-to-have | 3–4 must-have, 2–3 nice-to-have |
| Assessment methods | At least 1 per competency |
| Bias prevention | Gender / age neutral language |
