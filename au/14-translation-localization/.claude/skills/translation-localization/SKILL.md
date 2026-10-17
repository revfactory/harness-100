---
name: translation-localization
description: " Translation, Localisation, Cultural adaptation, Terminology Management an agent team collaborates to Translation line. ' Translation', 'to Translation', ' Localisation', 'Translation ', 'Glossary ', ' ', ' Localisation', ' Translation', ' Translation', ' Translation' etc. Translation·Localisation beforein . Translation casein quality verification Localisation application . , whenbetween , CAT (Trados/MemoQ) , DTP(Desktop Publishing) of ."
---

# Translation & Localisation — Translation & Localisation Full Pipeline

An agent team collaborates to perform multilingual translation, localisation, cultural adaptation, and terminology management all at once.

## Execution Mode

**Agent Team** — 5 members communicate directly via SendMessage and cross-validate each other's work.

## Agent Composition

| Agent | File | Role | Type |
|---------|------|------|------|
| translator | `.claude/agents/translator.md` | Source text Analysis, 1 Translation | general-purpose |
| localiser | `.claude/agents/localizer.md` | Cultural adaptation, Format Localisation | general-purpose |
| terminology-manager | `.claude/agents/terminology-manager.md` | Glossary , Consistency Management | general-purpose |
| style-harmonizer | `.claude/agents/style-harmonizer.md` | Tone & voice , Writing style | general-purpose |
| quality-reviewer | `.claude/agents/quality-reviewer.md` | MQM quality verification | general-purpose |

## Workflow

### Phase 1: Preparation (Performed Directly by the Orchestrator)

1. Extract from user input:
 - **Source text**: Translation Text File
 - **Source text language / Target language**: Translation 
 - **** (Selection): IT/of///
 - **Target market** (Selection): specific /
 - **Style Guide** (Selection): Brand , Formality level
 - ** Glossary** (Selection): before to Glossary
2. `_workspace/` to in generate
3. Organise input and save to `_workspace/00_input.md`in save
4. If existing files are present `_workspace/`, copy to _workspace/ and skip the corresponding Phase
5. Based on the scope of the request **determine the execution mode** ( " per mode" )

### Phase 2: Team Assembly and Execution

 compositionand . between of relationship and :

| sequence | | | of | |
|------|------|------|------|--------|
| 1a | Source text Analysis·Translation Strategy | translator | None | `_workspace/01_source_analysis.md` |
| 1b | Glossary | terminology | None | `_workspace/02_terminology.md` |
| 2 | 1 Translation | translator | 1b | `_workspace/03_translation.md` |
| 3 | Localisation application | localiser | 2 | `_workspace/04_localization.md` |
| 3+ | Style | harmoniser | 3 | `_workspace/04_localization.md` |
| 4 | quality verification | reviewer | 2, 3, 3+ | `_workspace/05_review_report.md` |

 1a(Source text Analysis)and 1b(Glossary ) **executed in parallel**.

**Inter-team communication flow:**
- terminology complete -> translatorTo Glossary before (Translation when before )
- translator complete -> localizerTo 1 Translated text + before
- localiser complete -> harmonizerTo Localisation application + before
- harmoniser complete -> reviewerTo Style application and before
- reviewer cross-validate. 🔴 Must Fix when AgentTo → → Verification (vs 2)

### Phase 3: Integration and Final Deliverables

Reviewof based on :

1. `_workspace/` within File verify
2. from the review report 🔴 Must Fix reflected verify
3. summary To :
 - Source text Analysis — `01_source_analysis.md`
 - Glossary — `02_terminology.md`
 - Translated text — `03_translation.md`
 - Localisation and — `04_localization.md`
 - Quality — `05_review_report.md`

## Modes by Task Scale

 of in Agent :

| Pattern | mode | Agent |
|----------------|----------|-------------|
| " Translation", " Localisation" | **Full Pipeline** | 5 All |
| "between Translation " | **Translation mode** | translator + terminology + reviewer |
| " Translation Localisation" ( Translation) | **Localisation mode** | localiser + harmoniser + reviewer |
| "Glossary " | **Terminology mode** | terminology only |
| " Translation " | **Review mode** | reviewer only |

**Using Existing Files**: Translation, Glossary etc. , copy the files to `_workspace/`in and .

## Data Transfer Protocol

| Strategy | | |
|------|------|------|
| File-Based | `_workspace/` | Storing and sharing major deliverables |
| Message-Based | SendMessage | Real-time delivery of key information, revision requests |
| Task-Based | TaskCreate/TaskUpdate | Progress tracking, dependency management |

File naming convention: `{}_{Agent}_{}.{}`

## Error Handling

| in type | Strategy |
|----------|------|
| Source text language per | and when + Verification |
| before | web searchto , Translation in when |
| etc. | Source text + description to |
| Agent failure | 1 when → when , Review in the report when |
| RED found in review | Request revision from relevant agent -> rework -> re-verify (up to 2 times) |

## Test Scenarios

### Normal Flow
**Prompt**: " to Translation·Localisation. Target 20~30vs" + Source text File
**Expected Result**:
- Source text Analysis: , , 
- Glossary: brand names DNT, Terminology 
- Translated text: Translation, Translation 
- Localisation: Format(Date/Currency/Units of measurement), Reference substitution
- Quality : MQM , error classification, matrix

### Existing File Utilisation Flow
**Prompt**: " Translation and Localisation " + Translation File
**Expected Result**:
- Translation `_workspace/03_translation.md`to 
- Localisation mode: localiser + harmoniser + reviewer 
- translator, terminology (, reviewer Terminology Consistency Verification)

### Error Flow
**Prompt**: " Translation, language "
**Expected Result**:
- Target market → ( ) application
- Terminology web searchto Terminology Verification
- Review in the report "Target market : " when

## Extended Skills per Agent

per Agentof before Extended Skill:

| | subject Agent | Role |
|------|-------------|------|
| `translation-quality-mqm` | quality-reviewer | MQM error classification, severity , Quality score calculation Formula |
| `cultural-adaptation-guide` | localiser | marketper Format conversion, taboo, Idioms substitution Strategy |
