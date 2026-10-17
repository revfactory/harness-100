---
name: ats-optimizer
description: "A specialised skill that provides resume keyword strategies and formatting guidelines for passing ATS (Applicant Tracking Systems). Used by the resume-writer agent to create ATS-friendly resumes and maximise JD matching rates. Automatically applied in contexts such as 'ATS optimisation', 'resume keywords', 'JD matching', 'resume format', 'applicant tracking system', 'application pass rate', etc. Note: Directly accessing ATS software (Workday, Greenhouse) or handling actual recruitment processes is outside the scope of this skill."
---

# ATS Optimiser — ATS Pass Optimisation Tool

A specialised skill that enhances the resume-writer agent's ATS optimisation capabilities.

## Target Agents

- **resume-writer** — ATS-friendly resume writing, keyword optimisation

## ATS Parsing Principles

### How ATS Reads Documents

```
1. Text extraction (PDF/DOCX -> Plain Text)
2. Section recognition (Experience, Education, Skills, etc.)
3. Keyword extraction + frequency analysis
4. Matching score calculation against JD keywords
5. Ranking and submission to recruiter
```

### ATS-Compatible Formatting Rules

| Item | Recommended | Not Recommended |
|------|-------------|-----------------|
| File Format | DOCX > PDF | Image PDF, HTML |
| Layout | Single column | Multi-column, table-based |
| Font | Arial, Calibri, Georgia | Special fonts |
| Headers | Text headers | Image/icon headers |
| Bullets | Standard bullets (-, *) | Custom graphic bullets |
| Section Names | Use standard names | Creative names |

### Standard Section Names (Ordered by ATS Recognition Rate)

```
- Work Experience / Professional Experience
- Education
- Skills / Technical Skills
- Certifications
- Projects
- Awards
```

## Keyword Optimisation Strategy

### JD Keyword Extraction Process

```
1. Copy the full JD text
2. Extract the following types of keywords:
   - Hard Skills: Programming languages, tools, frameworks
   - Soft Skills: Leadership, communication, problem-solving
   - Industry Terms: Domain-specific terminology
   - Action Verbs: Designed, built, optimized, led
   - Qualifications: Degrees, certifications, years of experience
3. Count frequency and prioritize
4. Naturally incorporate into the resume
```

### Keyword Density Guide

| Keyword Type | Recommended Count | Placement |
|-------------|-------------------|-----------|
| JD Core Keywords (3-5) | 2-3 times | Summary, Experience, Skills |
| JD Supporting Keywords (5-10) | 1-2 times | Experience, Projects |
| Industry Terms | 1 time | Distributed naturally |

### Keyword Matching Methods

| JD Expression | Resume Reflection | Principle |
|--------------|-------------------|-----------|
| "Python experience required" | "Built data pipelines using Python" | Action + Result |
| "Team leading experience" | "Led a 5-person dev team, completed 3 projects" | Quantification |
| "CI/CD experience" | "Built and operated CI/CD pipelines using Jenkins/GitHub Actions" | Specific tools |

## Achievement Quantification Formula (STAR-Q)

### Quantification Patterns

```
[Action Verb] + [Specific Activity] + [Quantitative Result]

Examples:
- "Designed and built an API server, reducing response time by 40% and achieving 1M daily transactions"
- "Introduced code review process, reducing post-deployment bugs by 60%"
- "Led a 5-person team to launch MVP within 3 months, acquiring 5,000 users"
```

### Quantifiable Metric Types

| Category | Example Metrics |
|----------|----------------|
| Performance | Response time, throughput, error rate, availability |
| Efficiency | Time savings, cost savings, automation rate |
| Scale | User count, traffic, data size |
| Team | Team size, mentees |
| Business | Revenue contribution, customer acquisition, conversion rate |

## Section-by-Section ATS Optimisation

### Professional Summary (3-4 lines)

```
[Title/Role] + [Core Experience] + [Differentiating Competency] + [Quantitative Achievement]

Example:
"Backend developer with 7 years of experience designing and operating large-scale traffic processing systems.
Designed microservice architectures based on Java/Spring Boot,
built systems handling 100M daily transactions.
Reduced operational costs by 35% through AWS infrastructure optimization."
```

### Work Experience

```
[Company] | [Title] | [Duration]

- [Action Verb] [Specific activity] achieving [Quantitative result]
- [Include JD keywords] [Achievement description]
- [Mention tech stack] [Project scale/impact]
```

### Skills Section

```
Technical Skills:
- Languages: Python, Java, TypeScript, SQL
- Frameworks: Spring Boot, React, FastAPI
- Infrastructure: AWS (EC2, RDS, Lambda), Docker, Kubernetes
- Tools: Git, Jenkins, Grafana, Jira

(List technologies from the JD using exact notation)
```

## ATS Score Self-Assessment

| Check Item | Weight | Status |
|-----------|--------|--------|
| 80%+ of JD core keywords included | 30% | [ ] |
| Standard section names used | 15% | [ ] |
| Single-column layout | 10% | [ ] |
| Achievements quantified (2+ per role) | 20% | [ ] |
| ATS-compatible file format | 10% | [ ] |
| Standard fonts, no tables | 5% | [ ] |
| Abbreviations written with full names | 5% | [ ] |
| No spelling/grammar errors | 5% | [ ] |
