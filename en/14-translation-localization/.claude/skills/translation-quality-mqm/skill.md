---
name: translation-quality-mqm
description: "MQM (Multidimensional Quality Metrics) translation quality assessment framework providing error classification system, severity weights, and score calculation formulas as an extended skill for the quality-reviewer agent. Use when quantitative verification of translation quality is needed for 'MQM assessment', 'translation quality score', 'error classification', 'translation QA', 'quality metrics', etc. Note: performing translation itself or applying localization is outside the scope of this skill."
---

# Translation Quality MQM — Translation Quality Assessment Framework

MQM error classification, severity system, and score calculation formulas used by the quality-reviewer agent when verifying translation quality.

## Target Agent

`quality-reviewer` — Applies the MQM framework in this skill directly to translation quality assessment.

## MQM Error Classification System

### Level 1: Major Categories (7 Dimensions)

| Dimension | Code | Description | Weight |
|-----------|------|-------------|--------|
| **Accuracy** | ACC | Faithful conveyance of the source text meaning | x2.0 |
| **Fluency** | FLU | Naturalness of the target language | x1.5 |
| **Terminology** | TER | Terminology consistency and accuracy | x1.5 |
| **Style** | STY | Writing style appropriate to the text type | x1.0 |
| **Locale** | LOC | Compliance with localization rules | x1.5 |
| **Design** | DES | Formatting, layout, markup | x0.5 |
| **Verity** | VER | Factual accuracy, reference correctness | x2.0 |

### Level 2: Detailed Error Types

#### ACC (Accuracy)
| Code | Type | Description | Example |
|------|------|-------------|---------|
| ACC-ADD | Over-translation | Added information not in the source | "good" → "extremely good" |
| ACC-OMI | Omission | Source information not translated | Part of sentence omitted |
| ACC-MIS | Mistranslation | Meaning distorted | "decrease" → "increase" |
| ACC-UNT | Untranslated | Source text left as-is | Target-language text remains in source language |
| ACC-AMB | Ambiguity | Ambiguous translation | Two interpretations possible |

#### FLU (Fluency)
| Code | Type | Description |
|------|------|-------------|
| FLU-GRA | Grammar error | Articles, verb endings, tense, agreement |
| FLU-PUN | Punctuation error | Commas, periods, parentheses |
| FLU-SPE | Spelling error | Typos, spacing |
| FLU-REG | Register | Inappropriate formality level |
| FLU-AWK | Awkwardness | Grammatically correct but unnatural |

#### TER (Terminology)
| Code | Type | Description |
|------|------|-------------|
| TER-INC | Terminology inconsistency | Translation differs from glossary |
| TER-DNT | DNT violation | Translating a Do-Not-Translate term |
| TER-WRG | Wrong terminology | Term differs from industry standard |

#### LOC (Locale)
| Code | Type | Description |
|------|------|-------------|
| LOC-DAT | Date format | Local date format not applied |
| LOC-NUM | Number format | Thousands separator, decimal point |
| LOC-CUR | Currency format | Currency symbol, unit |
| LOC-UNI | Units of measurement | Metric/imperial, Celsius/Fahrenheit |
| LOC-CUL | Cultural mismatch | Expression conflicts with local culture |

## Severity Levels

| Level | Code | Penalty | Criteria |
|-------|------|---------|----------|
| **Critical** | CRI | 25 pts | Complete meaning distortion, legal risk, offensive expression |
| **Major** | MAJ | 10 pts | Partial meaning damage, causes user confusion |
| **Minor** | MIN | 1 pt | Style preference, minor awkwardness |

## Score Calculation Formula

```
Raw Score = SUM(severity score per error × dimension weight)
Score per 1000 words = Raw Score / Total word count × 1000

Quality Grades:
  0~5    → Excellent (publishable)
  5~15   → Good (publishable after minor edits)
  15~30  → Acceptable (requires revision)
  30~50  → Poor (requires major revision)
  50+    → Reject (requires re-translation)
```

## Quality Assessment Report Template

```markdown
# Translation Quality Assessment Report

## Assessment Summary
- Source Language / Target Language: [X → Y]
- Total Word Count: [N]
- Assessment Standard: MQM v3.0
- Final Score: [X.X] / Grade: [Excellent|Good|Acceptable|Poor|Reject]

## Error Distribution

| Dimension | CRI | MAJ | MIN | Weighted Subtotal |
|-----------|-----|-----|-----|------------------|
| Accuracy (ACC) | 0 | 0 | 0 | 0 |
| Fluency (FLU) | 0 | 0 | 0 | 0 |
| Terminology (TER) | 0 | 0 | 0 | 0 |
| Style (STY) | 0 | 0 | 0 | 0 |
| Locale (LOC) | 0 | 0 | 0 | 0 |
| Design (DES) | 0 | 0 | 0 | 0 |
| Verity (VER) | 0 | 0 | 0 | 0 |
| **Total** | 0 | 0 | 0 | **0** |

## Detailed Error List

| # | Location | Source Text | Translated Text | Error Code | Severity | Suggested Fix |
|---|----------|------------|----------------|------------|----------|--------------|
| 1 | p.3 L12 | ... | ... | ACC-MIS | MAJ | ... |

## Strengths (Positive Findings)
- [Description of what was done well]

## Recommendations
1. [Highest priority fix]
2. [Improvement direction]
```

## Priority Verification Items by Domain

| Domain | Top Priority | Special Attention |
|--------|-------------|------------------|
| **Legal** | ACC accuracy, VER verity | Legal terminology accuracy, article number consistency |
| **Medical** | ACC accuracy, TER terminology | Medical terminology, dosage/unit accuracy |
| **Marketing** | FLU fluency, STY style | Cultural resonance, tone & voice |
| **Technical/IT** | TER terminology, ACC accuracy | UI string length, variable preservation |
| **Gaming** | FLU fluency, LOC locale | Character voice, cultural references |
| **Finance** | ACC accuracy, VER verity | Numbers, currency, regulatory compliance |

## Common Pitfalls by Language Pair

### English → Korean
| Pitfall | Description | Correct Handling |
|---------|-------------|-----------------|
| Passive voice overuse | Directly translating English passive constructions | Convert to active voice |
| Excessive translationese | Repeated "It is important that ~" pattern | Natural Korean sentences |
| Subject overuse | Repeating subjects in the English style | Omit subjects when implied by context |
| Article translation | Translating "the/a" as "그/하나의" | Omit in most cases |

### English → Japanese
| Pitfall | Description | Correct Handling |
|---------|-------------|-----------------|
| Honorific level | Choosing honorifics without context | Select honorific level appropriate to audience |
| Katakana overuse | Converting all loanwords to katakana | Check for established kanji alternatives |
| Sentence length | Keeping long English sentences intact | Split into shorter Japanese sentences |
