# Character Design System

Use for character sheets and image prompt consistency.

## Character Sheet Requirements

Include enough stable traits that the same character can be recognized across panels:

- Front full-body view.
- Side and back views when useful.
- Face close-up, preferably 3/4 angle.
- Expression chart for the main emotions.
- Default outfit and important variants.
- Props or accessories.

## Character Template

```markdown
## [캐릭터명]

### 기본 정보
- 나이:
- 성별:
- 키/체형:
- 역할:

### 외형 핵심 특징
- 머리카락:
- 눈:
- 체형:
- 특이사항:

### 의상
- 기본:
- 변형:

### 프롬프트 고정 문구
"[gender] [age range], [hair], [eyes], [body type], [clothing], [distinctive feature]"
```

Copy the fixed phrase into every panel prompt where the character appears.

## Silhouette Test

Characters should remain identifiable when reduced to a silhouette.

Differentiate by:

- Body size and posture.
- Hair silhouette.
- Habitual pose.
- Always-carried prop.
- Clothing outline, such as coat, hood, cape, or bag.

Checklist:

- Can the main cast be identified side by side by silhouette alone?
- Are they still distinct in black and white?
- Are they readable as thumbnails?

## Expression Chart

| Emotion | Eyes | Brows | Mouth | Extra |
|---|---|---|---|---|
| Joy | crescent, narrowed | raised | smile/open | blush |
| Sadness | drooping, wet | inner ends raised | downturned | tears |
| Anger | sharp, narrowed | V shape | clenched/open | vein mark |
| Fear | wide, small pupils | raised | open | sweat |
| Surprise | wide, enlarged pupils | raised | O shape | leaning back |
| Contempt | half-lidded | one raised | smirk | turned head |

## AI Consistency Rules

- Anchor phrase: repeat fixed external traits exactly.
- Style anchor: repeat one art style label throughout.
- Negative prompt idea: avoid different face, inconsistent design, changed outfit.
- If reference images exist, use them consistently.
- When changing outfits, start with `same character, new outfit:`.

## Failure Fixes

| Problem | Likely Cause | Fix |
|---|---|---|
| Face changes | Missing external details | Reinsert anchor phrase and reference |
| Body changes | Angle distortion | Restate body type |
| Outfit changes | Outfit omitted | Include outfit every time |
| Color changes | Lighting ambiguity | State fixed colors, e.g. `always red jacket` |
