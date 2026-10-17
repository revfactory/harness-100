---
name: intent-taxonomy-builder
description: "Methodology for systematically designing a chatbot's intent classification taxonomy. Use this skill for 'intent taxonomy design', 'intent system', 'NLU intent list', 'entity dictionary', 'slot design', and other chatbot intent classification taxonomy design tasks. Note: actual NLU model training and cloud NLU service deployment are outside the scope of this skill."
---

# Intent Taxonomy Builder — Intent Classification Taxonomy Design Methodology

A skill that enhances intent classification design for the nlu-developer and conversation-designer.

## Target Agents

- **nlu-developer** — Used when designing intent/entity/slot systems
- **conversation-designer** — Used when mapping conversation scenarios to intents

## Intent Classification Taxonomy Design Framework

### Step 1: Domain Intent Collection

```
Collect user utterances > Group > Derive intent candidates

Collection sources:
- Existing FAQ documents
- Customer service inquiry logs
- Competitor chatbot analysis
- User interviews/surveys
- Domain expert brainstorming
```

### Step 2: Intent Hierarchy

```
Level 0 (Domain)
├── Level 1 (Category)
│   ├── Level 2 (Specific intent)
│   └── Level 2
└── Level 1
    └── Level 2

Example (E-commerce):
commerce
├── order
│   ├── order.place — "I want to place an order"
│   ├── order.status — "Check my order status"
│   ├── order.cancel — "Cancel my order"
│   └── order.modify — "I want to change my order"
├── product
│   ├── product.search — "Do you have this kind of product?"
│   ├── product.detail — "Details about this product"
│   └── product.compare — "Compare these two products"
├── payment
│   ├── payment.method — "What payment methods are available?"
│   ├── payment.refund — "Refund request"
│   └── payment.receipt — "Issue a receipt"
└── general
    ├── general.greeting — "Hello"
    ├── general.goodbye — "Thank you"
    └── general.fallback — (unrecognized)
```

### Step 3: Intent Quality Checklist

| Criterion | Description | Pass Condition |
|-----------|------------|----------------|
| Mutual exclusivity | No overlap between intents | 1 utterance = 1 intent |
| Completeness | Covers all user scenarios | fallback < 10% |
| Balance | Even training data per intent | Minimum 20 utterances/intent |
| Clarity | Purpose clear from name alone | `verb.noun` format |
| Appropriate count | Manageable range | 20-50 (small-scale), 50-150 (large-scale) |

## Entity Design Methodology

### Entity Types

| Type | Description | Examples |
|------|------------|---------|
| System entity | Platform built-in | @sys.date, @sys.number, @sys.email |
| Dictionary entity | Domain fixed list | Menu items, sizes, colours |
| Pattern entity | Regex-based | Order number (`ORD-\d{8}`), phone number |
| Composite entity | Entity combinations | Address (city+district+street), date range |

### Entity-Slot Mapping

```
Intent: order.place
Required slots:
  - product_name (@product) — "Americano"
  - quantity (@sys.number) — "two"
Optional slots:
  - size (@size) — "tall size"
  - option (@option) — "less ice"
  - takeout (@boolean) — "to go"

When slot is unfilled > Prompt:
  - product_name missing: "What would you like to order?"
  - quantity missing: "How many would you like?"
```

## Training Data Generation Guide

### Utterance Variation Patterns

```
Original: "I want to cancel my order"

Variation strategies:
1. Ending variation: "Please cancel", "Cancel this", "I'd like to cancel please"
2. Expression substitution: "Revoke order", "Undo order", "I don't want my order anymore"
3. Context addition: "Cancel the order I just placed", "Cancel what I ordered earlier"
4. Typos/abbreviations: "cancle order", "cancel plz", "cxl"
5. Indirect expression: "I don't want to receive my order", "I changed my mind"
6. With entity: "Cancel ORD-12345678"
```

### Utterance Count Guide

| Intent Complexity | Minimum Utterances | Recommended Utterances |
|------------------|-------------------|----------------------|
| Simple (greeting/goodbye) | 10 | 20 |
| Medium (lookup/confirmation) | 20 | 50 |
| Complex (order/modification) | 30 | 80 |
| Easily confused (similar intents) | 50 | 100+ |

## Intent Confusion Matrix Analysis

```
High-confusion pair examples:
- order.cancel <> payment.refund (cancel vs refund)
- product.search <> product.detail (search vs detail)
- order.modify <> order.cancel (modify vs cancel)

Resolution strategies:
1. Add distinguishing utterances (strengthen unique keywords for each intent)
2. Merge intents (when distinction is unnecessary)
3. Context-dependent separation (based on dialog state)
4. Clarifying question ("Do you want to cancel or get a refund?")
```

## Deliverable Template

```yaml
intent_taxonomy:
  - intent: order.place
    description: "Place a new order"
    examples:
      - "I'd like to order two Americanos"
      - "I want to order this"
    required_slots:
      - name: product_name
        entity: "@product"
        prompt: "What would you like to order?"
    optional_slots:
      - name: quantity
        entity: "@sys.number"
        default: 1
    responses:
      success: "Your order for {quantity} {product_name}(s) has been placed."
      slot_missing: "Please tell me what you'd like to order."
```
