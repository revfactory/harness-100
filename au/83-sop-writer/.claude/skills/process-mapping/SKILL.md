---
name: process-mapping
description: "process mapping method. process-analyst agent work flow analysisand visualizationto do when reference mapping technique and tabletechnique. 'SIPOC', 'process map', 'Value Stream Map' request when usage. However, BPM whensystem building specialist development scope outside."
---

# Process Mapping — process mapping method

process-analyst agent work flow analysis quality mapping technique.

## SIPOC analysis framework

### SIPOC template

| S (Supplier) | I (Input) | P (Process) | O (Output) | C (Customer) |
|-------------|-----------|-------------|-----------|-------------|
| gradespecialist/beforestage | input specialistKRW/information | core process | deliverable | client/nextstage |

### writing rule
1. **Process ** — core process 5~7stage definition
2. **Output next** — each stage deliverable specify
3. **Customer identification** — deliverable receivespecialist
4. **Input tracking** — process perform neededKorean input
5. **Supplier identify** — input gradespecialist

### examplewhen: client weekdocument processing

| S | I | P | O | C |
|---|---|---|---|---|
| client | weekdocument | 1. weekdocument number | number confirm | client |
| re- whensystem | re- information | 2. re- confirm | department | logisticsteam |
| whensystem | information | 3. processing | complete | financialteam |
| logisticsteam | | 4. / | | company |
| company | | 5. | number confirm | client |

## process map tabletechnique

### BPMN between tablebasis

| basis | Mermaid tablecurrent | un- |
|------|-------------|------|
| KRW | `((whenwork))` | whenwork/ event |
| companyeach | `[task]` | / |
| | `{judgment}` | (minutebasis) |
| number | `subgraph` | departmentfrom/role minute |

### (Swim Lane)

```mermaid
flowchart TD
 subgraph client["client"]
 A([weekdocument request]) --> B[weekdocument writing]
 end
 subgraph ["team"]
 B --> C[weekdocument number]
 C --> D{re- confirm}
 end
 subgraph logistics["logisticsteam"]
 D -->|| E[ degreewhen]
 E --> F[/]
 end
 subgraph 2["team"]
 D -->|None| G[client report]
 F --> H[ confirm]
 end
```

## Value Stream Mapping (VSM)

### current process analysis indicator

| indicator | approx. | description | calculation |
|------|------|------|------|
| | LT | whenwork~complete total time | versusbasis + processing |
| processingtime | PT | actual task time | number value |
| versusbasistime | WT | stage between versusbasis | LT - PT |
| | PCE | process company | PT / LT × 100 |

### VSM analysis template

```
stage 1: [taskpeople]
 processingtime: 30minute
 versusbasistime: 2time
 responsible: team
 tool: CRM
 : ■ (/None)

stage 2: [taskpeople]
 ...

total : 24time
total processingtime: 3time
PCE: 12.5% → improvement goal: 30%
```

## RACI matrix

| role | un- | rule |
|------|------|------|
| **R** (Responsible) | execution responsible | each 1people or more |
| **A** (Accountable) | final person | each mustwhen 1people only |
| **C** (Consulted) | specialistdocument | companybefore number needed |
| **I** (Informed) | report | result only |

### RACI writing examplewhen

| | team | person responsible | QA | KRW |
|------|------|--------|-----|------|
| requirements | A | R | C | I |
| procedure document plan | C | R | I | - |
| review/person | A | I | R | I |
| deployment | A | R | - | I |

## / identification checklist

### 7versus (TIM WOODS)

| | description | SOP applied |
|------|------|---------|
| **T**ransport | neededKorean /deliver | person stage |
| **I**nventory | re-/ | processing versusbasis document quality |
| **M**otion | neededKorean work | whensystem between data re-input |
| **W**aiting | versusbasis time | person versusbasis, versusbasis |
| **O**verproduction | | neededKorean report/ |
| **O**verprocessing | processing | Korean verify stage |
| **D**efects | /re-task | personKorean task |
| **S**kills | talent | qualificationspecialist task |

## quality checklist

| item | standard |
|------|------|
| SIPOC nature also | 5element identification |
| process stage | 5~15stage (exceeding when process minute) |
| person responsible specify | all stage R/A degree |
| time | LT, PT, WT calculation |
| identification | minimum 1items or more improvement point |
