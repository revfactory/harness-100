---
name: cultural-adaptation-guide
description: "Localisation when Cultural adaptation Guide. major marketper(, during, , ) , Color/number/gesture taboo, Date/Currency/Units of measurement conversion, Idioms substitution Strategy localiser Extended Skill. 'Cultural adaptation', 'Localisation Guide', 'taboo expression', 'Date Format', ' ', 'Idioms Translation' etc. context conversion . , Translation Quality score calculation of ."
---

# Cultural Adaptation Guide — Cultural Adaptation & Localisation Reference

Market-specific cultural dimensions, format conversions, and taboo references used by the localiser agent when applying localisation.

## subject Agent

`localizer` — of Cultural adaptation Localisation in apply.

## marketper Format conversion matrix

### Date/whenbetween
| market | Date Format | whenbetween | when | when |
|------|----------|------|--------|------|
| | YYYY MM DD / YYYY.MM.DD | 24whenbetween (before/after ) | | 2025 3 15 |
| | YYYY年MM月DD日 | 24whenbetween | | 2025年3月15日 |
| during | YYYY年MM月DD日 | 24whenbetween | | 2025年3月15日 |
| | MM/DD/YYYY | 12whenbetween (AM/PM) | | 03/15/2025 |
| | DD/MM/YYYY | 24whenbetween | | 15/03/2025 |
| | DD.MM.YYYY | 24whenbetween | | 15.03.2025 |

### number/Currency
| market | | | Currency | | when |
|------|--------|--------|----------|------|------|
| | , | . | ₩ | | ₩1,234,567 |
| | , | . | ¥ / 円 | | ¥1,234,567 |
| | , | . | $ | | $1,234.56 |
| | . | , | € | () | 1.234,56 € |
| | () | , | € | () | 1 234,56 € |

### Units of measurement
| market | | | | |
|------|------|------|------|----------|
| // | km, m | kg, g | °C | A4 |
| | mi, ft, in | lb, oz | °F | Letter |
| | mi (to), m (Formula) | kg (Formula), st/lb (daily life) | °C | A4 |

### Format
| market | sequence | when |
|------|------|------|
| | → /when → → /to → detailed | 06164 perwhen to |
| | 〒 → → when → | 〒100-0001 東京都千代田区 |
| | detailed → when, abbreviations | 123 Main St, San Francisco, CA 94105 |

## per Strategy

### Hofstede utilisation

| | market | market | |
|------|-----------|-----------|-----------|
| ** ** | , , during | , | : / , : |
| **of** | , , | , , during | : "of ", : " of and" |
| ** ** | , , | , , | : detailed / , : / |
| ** ** | , , during | , | : "10 ", : " to" |

## Color/number/Image taboo

### Colour of 
| Colour | | | during | |
|------|------|------|------|------|
| | , | , | , | , |
| | , | , | , | , |
| | , of | | , () | , of |
| seconds | , | , | , | , |
| | Formality, | Formality, | , | Formality, |

### number taboo
| market | number | number | application |
|------|-----------|----------|------|
| | 4 (死) | 3, 7, 8 | /in 4 |
| | 4 (死), 9 (苦) | 7, 8 | , |
| during | 4 (死) | 6, 8 (發), 9 | 888, before |
| | 13 | 7 | 13 |

## Idioms/metaphors substitution Strategy

### substitution 
1. **etc. Idioms ** → of etc. expressionto substitution
2. **etc. None + of ** → of Translation
3. **etc. None + ** → Source text + description

### major Idioms substitution when

| Source text | | | Translation () |
|----------|--------|--------|----------------|
| "piece of cake" | " " | "朝飯前" | " " |
| "break the ice" | " " | "場を和ませる" | " " |
| "ball is in your court" | " " | "あなた次第です" | " in" |
| "think outside the box" | " " | "既成概念にとらわれない" | " from " |
| "hit the nail on the head" | " " | "図星を指す" | " " |

## Text / 

Translation when Text UI Designin reflected .

| Source text language | Target language | | |
|----------|----------|--------|------|
| | | +10~15% | Structure |
| | | -10~20% | of |
| | during | -20~30% | of |
| | | +20~35% | (Zusammensetzung) |
| | | +15~25% | , before |
| | | +25% | → RTL of |

## RTL (Right-to-Left) language st

, , when etc. RTL language Localisation when:

- [ ] Text : RTLto before
- [ ] Layout : → placement →to
- [ ] icon: icon (, )
- [ ] number: number LTR ( Text)
- [ ] : → 
- [ ] : before

## Do Not Translate (DNT) 

| type | when | |
|------|------|------|
| brand names | Apple, Samsung, Google | Source text |
| | iPhone, Galaxy, Chrome | Source text |
| Terminology | API, SDK, OAuth | Source text (when description) |
| / | `{username}`, `%d` | vs |
| URL/ | https://..., info@... | URL substitution |
| | Privacy Act 1988 (Cth), APPs | Source text + |
