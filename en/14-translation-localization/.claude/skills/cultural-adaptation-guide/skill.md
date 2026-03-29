---
name: cultural-adaptation-guide
description: "Cultural adaptation guide for localization. Provides cultural dimensions by major market (Japan, China, USA, Europe), color/number/gesture taboos, date/currency/units of measurement conversions, and idiom substitution strategies as an extended skill for the localizer agent. Use when cultural context conversion is needed for 'cultural adaptation', 'localization guide', 'taboo expressions', 'date formats', 'cultural differences', 'idiom translation', etc. Note: performing translation itself or calculating quality scores is outside the scope of this skill."
---

# Cultural Adaptation Guide — Cultural Adaptation & Localization Reference

Market-specific cultural dimensions, format conversions, and taboo references used by the localizer agent when applying localization.

## Target Agent

`localizer` — Applies the cultural adaptation knowledge in this skill directly to localization work.

## Market-Specific Format Conversion Matrix

### Date/Time
| Market | Date Format | Time | Week Start | Example |
|--------|------------|------|-----------|---------|
| Korea | YYYY년 MM월 DD일 / YYYY.MM.DD | 24h (AM/PM also used) | Sunday | 2025년 3월 15일 |
| Japan | YYYY年MM月DD日 | 24h | Sunday | 2025年3月15日 |
| China | YYYY年MM月DD日 | 24h | Monday | 2025年3月15日 |
| USA | MM/DD/YYYY | 12h (AM/PM) | Sunday | 03/15/2025 |
| UK | DD/MM/YYYY | 24h | Monday | 15/03/2025 |
| Germany | DD.MM.YYYY | 24h | Monday | 15.03.2025 |

### Numbers/Currency
| Market | Thousands Separator | Decimal | Currency Symbol | Position | Example |
|--------|--------------------|---------|-----------------|---------|---------|
| Korea | , | . | ₩ | Before | ₩1,234,567 |
| Japan | , | . | ¥ / 円 | Before | ¥1,234,567 |
| USA | , | . | $ | Before | $1,234.56 |
| Germany | . | , | € | After (space) | 1.234,56 € |
| France | (space) | , | € | After (space) | 1 234,56 € |

### Units of Measurement
| Market | Distance | Weight | Temperature | Paper Size |
|--------|---------|--------|------------|-----------|
| Korea/Japan/Europe | km, m | kg, g | °C | A4 |
| USA | mi, ft, in | lb, oz | °F | Letter |
| UK | mi (roads), m (official) | kg (official), st/lb (everyday) | °C | A4 |

### Address Format
| Market | Order | Example |
|--------|-------|---------|
| Korea | Postal code → Province/City → District → Street → Detail | 06164 서울특별시 강남구 테헤란로 |
| Japan | 〒Postal code → Prefecture → City/Ward → Block number | 〒100-0001 東京都千代田区 |
| USA | Detail → City, State abbreviation Postal code | 123 Main St, San Francisco, CA 94105 |

## Adaptation Strategy by Cultural Dimension

### Applying Hofstede's Cultural Dimensions

| Dimension | High-Score Markets | Low-Score Markets | Content Adaptation |
|-----------|-------------------|------------------|-------------------|
| **Power Distance** | Korea, Japan, China | USA, Northern Europe | High: Strengthen honorifics; Low: Casual tone |
| **Individualism** | USA, Australia, UK | Korea, Japan, China | Individual: "Your success"; Collective: "Our team's achievement" |
| **Uncertainty Avoidance** | Japan, Korea, Germany | USA, UK, India | High: Emphasize detailed specs/guarantees; Low: Emphasize innovation/adventure |
| **Long-term Orientation** | Korea, Japan, China | USA, UK | Long-term: "10 years of trust"; Short-term: "Right now" |

## Color/Number/Image Taboos

### Color Meaning Differences
| Color | Korea | Japan | China | Western |
|-------|-------|-------|-------|---------|
| Red | Passion, danger | Celebration, strength | Luck, prosperity | Danger, love |
| White | Purity, mourning | Purity, mourning | Funeral, grief | Purity, wedding |
| Yellow | Royalty, caution | Courage | Royalty, pornographic (slang) | Happiness, caution |
| Green | Nature, growth | Nature, eternity | Health, infidelity | Nature, environment |
| Black | Formality, death | Formality, mystery | Darkness, evil | Formality, luxury |

### Number Taboos
| Market | Unlucky Numbers | Lucky Numbers | Application |
|--------|----------------|--------------|------------|
| Korea | 4 (死) | 3, 7, 8 | Avoid 4 in prices/packages |
| Japan | 4 (死), 9 (苦) | 7, 8 | Hotel floors, product numbers |
| China | 4 (死) | 6, 8 (發), 9 | Price 888, phone numbers |
| Western | 13 | 7 | Skip 13th floor |

## Idiom/Metaphor Substitution Strategy

### Substitution Principles
1. **Equivalent idiom exists** → Replace with the culturally equivalent expression
2. **No equivalent + meaning is transparent** → Translate by unpacking the meaning
3. **No equivalent + culturally specific** → Retain the original + parenthetical explanation

### Major English Idiom Substitution Examples

| English Source | Korean | Japanese | Literal Translation (Forbidden) |
|---------------|--------|----------|--------------------------------|
| "piece of cake" | "식은 죽 먹기" | "朝飯前" | "a piece of cake" |
| "break the ice" | "분위기를 풀다" | "場を和ませる" | "break the ice" |
| "ball is in your court" | "이제 네 차례야" | "あなた次第です" | "the ball is in your court" |
| "think outside the box" | "고정관념을 깨다" | "既成概念にとらわれない" | "think outside the box" |
| "hit the nail on the head" | "정곡을 찌르다" | "図星を指す" | "hit the nail on the head" |

## Text Expansion/Contraction Factors

Translation changes in text length must be reflected in UI design.

| Source Language | Target Language | Expansion Rate | Notes |
|----------------|----------------|---------------|-------|
| English | Korean | +10~15% | Hangul syllable structure |
| English | Japanese | -10~20% | Compression of kanji |
| English | Chinese | -20~30% | High density of kanji |
| English | German | +20~35% | Compound words (Zusammensetzung) |
| English | French | +15~25% | Articles, prepositions |
| English | Arabic | +25% | RTL — right-to-left attention required |

## RTL (Right-to-Left) Language Checklist

When localizing for Arabic, Hebrew, Persian, and other RTL languages:

- [ ] Text direction: Switch to RTL
- [ ] Layout mirroring: Reverse left-to-right placement to right-to-left
- [ ] Icons: Mirror directional icons (arrows, play buttons)
- [ ] Numbers: Keep Arabic numerals in LTR direction (bidirectional text)
- [ ] Progress bars: Right-to-left direction
- [ ] Scroll: Reverse navigation direction

## Do Not Translate (DNT) Rules

| Type | Examples | Rule |
|------|---------|------|
| Brand names | Apple, Samsung, Google | Retain original |
| Product names | iPhone, Galaxy, Chrome | Retain original |
| Technical terms | API, SDK, OAuth | Retain original (parenthetical explanation if needed) |
| Code/Variables | `{username}`, `%d` | Never change |
| URLs/Emails | https://..., info@... | Replace with local URL if available |
| Legal names | GDPR, CCPA | Retain original + note local equivalent |
