---
name: translation-quality-mqm
description: "MQM(Multidimensional Quality Metrics) Translation Quality Framework, error classification , severity weight, score calculation Formula quality-reviewer Extended Skill. 'MQM ', 'Translation Quality ', 'error classification', 'Translation QA', 'Quality ric' etc. Translation Qualityof Verification . , Translation Localisation application of ."
---

# Translation Quality MQM — Translation Quality Assessment Framework

MQM error classification, severity system, and score calculation formulas used by the quality-reviewer agent when verifying translation quality.

## subject Agent

`quality-reviewer` — of MQM Framework Translation Quality in apply.

## MQM error classification 

### 1: vs (7 )

| | | description | weight |
|------|------|------|--------|
| **Accuracy** (Accuracy) | ACC | Source text ofof before | x2.0 |
| **Fluency** (Fluency) | FLU | Target languageof | x1.5 |
| **Terminology** (Terminology) | TER | Terminology Consistencyand Accuracy | x1.5 |
| **Style** (Style) | STY | Text typein Writing style | x1.0 |
| **to** (Locale) | LOC | Localisation | x1.5 |
| **Design** (Design) | DES | , Layout, | x0.5 |
| **** (Verity) | VER | relationship, Accuracy | x2.0 |

### 2: type

#### ACC (Accuracy)
| | type | description | when |
|------|------|------|------|
| ACC-ADD | andTranslation | Source textin Information | "good" → " " |
| ACC-OMI | omission | Source text Information Translation | omission |
| ACC-MIS | mistranslation | of | "decrease" → "" |
| ACC-UNT | Translation | Source text vsto | Translation subject |
| ACC-AMB | duringof | Translation | |

#### FLU (Fluency)
| | type | description |
|------|------|------|
| FLU-GRA | | , , when, |
| FLU-PUN | | , , |
| FLU-SPE | customised | , |
| FLU-REG | language etc. | Formality level |
| FLU-AWK | | |

#### TER (Terminology)
| | type | description |
|------|------|------|
| TER-INC | Terminology | Glossaryand Translation |
| TER-DNT | DNT | Translation Terminology Translation |
| TER-WRG | Terminology | Industry standardsand Terminology |

#### LOC (to)
| | type | description |
|------|------|------|
| LOC-DAT | Date Format | Date application |
| LOC-NUM | number Format | , |
| LOC-CUR | Currency Format | Currency , |
| LOC-UNI | Units of measurement | /, / |
| LOC-CUL | | and conflict expression |

## severity etc.

| etc. | | | |
|------|------|------|------|
| **** (Critical) | CRI | 25 | of before , , expression |
| **major** (Major) | MAJ | 10 | of , |
| **** (Minor) | MIN | 1 | Style , |

## score calculation Formula

```
when = SUM(per severity x weight)
 = when / x 1000

Quality etc.:
 0~5 → Excellent (Publishing )
 5~15 → Good ( after Publishing)
 15~30 → Acceptable ( )
 30~50 → Poor (vs )
 50+ → Reject (Translation )
```

## Quality 

```markdown
# Translation Quality 

## summary
- Source text language / Target language: [X → Y]
- : [N]
- : MQM v3.0
- : [X.X] / etc.: [Excellent|Good|Acceptable|Poor|Reject]

## distribution

| | CRI | MAJ | MIN | during |
|------|-----|-----|-----|----------|
| Accuracy (ACC) | 0 | 0 | 0 | 0 |
| Fluency (FLU) | 0 | 0 | 0 | 0 |
| Terminology (TER) | 0 | 0 | 0 | 0 |
| Style (STY) | 0 | 0 | 0 | 0 |
| to (LOC) | 0 | 0 | 0 | 0 |
| Design (DES) | 0 | 0 | 0 | 0 |
| (VER) | 0 | 0 | 0 | 0 |
| **** | 0 | 0 | 0 | **0** |

## detailed 

| # | | Source text | Translated text | | severity | Suggestion |
|---|------|------|--------|---------|--------|----------|
| 1 | p.3 L12 | ... | ... | ACC-MIS | MAJ | ... |

## (Positive Findings)
- [ ]

## 
1. [ ]
2. [ ]
```

## per during Verification 

| | Verification | per of |
|--------|-----------|----------|
| **** | ACC Accuracy, VER | Terminology Accuracy, |
| **of** | ACC Accuracy, TER Terminology | of Terminology, / Accuracy |
| **** | FLU Fluency, STY Style | , Tone & voice |
| **/IT** | TER Terminology, ACC Accuracy | UI , Preservation |
| **** | FLU Fluency, LOC to | ric , |
| **** | ACC Accuracy, VER | number, Currency, |

## languageper major 

### → 
| | description | correct |
|------|------|-----------|
| | vsto Translation | to before |
| and Translation | "~ during" | |
| and | | |
| Translation | "the/a" "/of"to | vs |

### → 
| | description | correct |
|------|------|-----------|
| level | when Selection | Audiencein |
| | to | Verification |
| | vsto | |
