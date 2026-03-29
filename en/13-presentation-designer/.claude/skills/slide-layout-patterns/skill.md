---
name: slide-layout-patterns
description: "A slide layout pattern library for presentations. An extension skill for visual-designer that provides optimal layouts for 20 slide types (title, content, data, comparison, timeline, etc.), margin and grid rules, and color/typography systems. Use for 'slide layout', 'slide pattern', 'design system', 'grid', 'typography', 'color palette', and similar slide visual design tasks. Note: actual PPT/Keynote file generation and animations are outside the scope of this skill."
---

# Slide Layout Patterns — Slide Layout Pattern Library

Layout patterns, grid systems, and design token references used by the visual-designer agent when producing slide decks.

## Target Agent

`visual-designer` — Directly applies the layout patterns and design tokens from this skill to slide design.

## Grid System

### Base Grid (16:9 = 1920x1080px)
- **Margins**: 80px on all sides
- **Columns**: 12 columns (127px each, 20px gutter)
- **Rows**: 6 rows (153px each, 20px gutter)
- **Safe zone**: Inner 120px (to prevent projector clipping)

### Content Area Allocation
| Element | Position | Height |
|---------|----------|--------|
| Title area | Top 80–230px | 150px |
| Content area | Center 250–880px | 630px |
| Footer bar | Bottom 900–1000px | 100px (page number, logo) |

## 20 Slide Layout Patterns

### 1. Title Slide
- Center-aligned, title 56–72px, subtitle 24–32px
- Background: solid color / gradient / full-bleed image + overlay
- Logo: bottom-left or bottom-right

### 2. Section Divider
- Section name centered at 48–56px, section number at top-left in 120px numerals
- Background: brand accent color or image

### 3. Text Only (Big Idea)
- Single sentence, center-aligned, 36–48px
- Maximize whitespace; use font weight for impact
- Maximum 20 words

### 4. Text + Image (Left/Right Split)
- Left 6 columns text + right 6 columns image (or reversed)
- Image: full height, flush to edge
- Text: vertically centered

### 5. Bullet List
- Title + 3–5 bullets (no more than 7)
- Each bullet: icon (24px) + heading (20px bold) + description (16px regular)
- Line height: 1.6–1.8

### 6. Number Highlight (Key Metric)
- 1–3 key figures in large typography (80–120px)
- Unit/context in smaller text (18px) below
- Background color for emphasis

### 7. Two-Column Comparison
- Left/right or top/bottom split, symmetrical structure
- "vs" icon or divider line at center
- Suitable for Before/After, competitive comparisons

### 8. Three-Column Card
- 3 equal-size cards (4 columns each)
- Card: icon/image at top + title + description
- Suitable for feature introductions, team profiles

### 9. Timeline (Horizontal)
- Horizontal line + 3–6 nodes
- Node: date/phase + description
- Left → right temporal flow

### 10. Process Flow
- 3–5 steps connected by arrows
- Each step: number + icon + title
- Linear or circular structure

### 11. Matrix (2x2)
- Four quadrants with X/Y axis labels
- Items placed in each quadrant
- Positioning map, priority matrix

### 12. Full-Bleed Image + Text Overlay
- Image at 100%, semi-transparent overlay (40–60% opacity)
- Text: bottom-left or centered, white

### 13. Quote / Testimonial
- Large quotation mark icon (60px)
- Quote text 28–36px italic
- Attribution: name, title, company (16px)

### 14. Data Table
- Maximum 5 columns × 7 rows
- Header row highlighted with background color
- Cell padding 12px, left-aligned (numbers right-aligned)

### 15. Agenda / Table of Contents
- Number + section name, current section highlighted
- Left vertical list or center grid

### 16. Icon Grid
- 4–9 icons + labels in a grid (2×2, 3×3)
- Uniform icon size (48–64px)
- Feature overview, service lineup

### 17. Pyramid / Hierarchy
- 3–5 tier pyramid shape
- Top: narrow core → Bottom: broad base
- Strategy hierarchy, frameworks

### 18. Closing / CTA
- Key message, center-aligned
- Contact info / URL / QR code at bottom
- Thank you + Next Steps

### 19. App UI / Mockup Showcase
- Device mockup (phone / tablet / laptop) centered
- Feature callout arrows on left and right

### 20. Roadmap
- Horizontal or diagonal timeline
- Past (gray) → Present (accent color) → Future (dashed)
- Quarterly milestones labeled

## Design Token System

### Typography Scale
| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| Slide title | 36–44px | Bold | 1.2 |
| Section title | 28–32px | SemiBold | 1.3 |
| Body text | 18–22px | Regular | 1.6 |
| Caption / footnote | 14–16px | Light | 1.4 |
| Data figures | 72–120px | Bold | 1.0 |

### Recommended Fonts
| Usage | Korean | English |
|-------|--------|---------|
| Headings | Pretendard Bold | Inter Bold |
| Body | Pretendard Regular | Inter Regular |
| Data | Pretendard Bold | DM Sans Bold |
| Code | D2Coding | JetBrains Mono |

### Color System
| Role | Token | Usage |
|------|-------|-------|
| Primary | Brand main color | Primary emphasis, CTA |
| Secondary | Supporting color | Section dividers, icons |
| Neutral-900 | Near black | Heading text |
| Neutral-600 | Mid gray | Body text |
| Neutral-200 | Light gray | Backgrounds, dividers |
| Success | Green tones | Positive data |
| Warning | Orange tones | Cautionary data |
| Danger | Red tones | Negative data |

### Slide Density Rules
| Rule | Standard |
|------|----------|
| Text | Maximum 40 words per slide (6 lines) |
| Bullets | Maximum 5; one concept per line |
| Colors | Maximum 3 per slide (primary + neutral + accent) |
| Font size | Minimum 16px (readability from back of room) |
| Whitespace | Content area 60%, whitespace 40% |
