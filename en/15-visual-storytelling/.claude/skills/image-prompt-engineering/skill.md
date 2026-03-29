---
name: image-prompt-engineering
description: "AI image prompt engineering guide for Gemini/DALL-E/Midjourney. Provides composition-based prompt structures, style keywords, consistency techniques, and prompt patterns as an image-prompter extension skill. Use for 'image prompt', 'AI image style', 'prompt writing', 'composition design', 'style consistency', etc. Note: actual image generation is outside the scope of this skill."
---

# Image Prompt Engineering — AI Image Prompt Writing Guide

Prompt structure, style keywords, and consistency technique references used by the image-prompter agent when generating AI images.

## subject Agent

`image-prompter` — of Prompt Patternand Image in apply.

## Prompt Structure Formula

### 5-Layer Prompt Structure
```
[1. media/Style] + [2. composition/] + [3. ] + [4. /background] + [5. /]
```

#### Layer 1: media/Style
| | | and |
|---------|--------|------|
| photography | "editorial photography", "professional photo" | |
| illustration | "digital illustration", "vector art" | graphic |
| | "watercolor painting", "soft watercolor" | |
| | "oil painting", "impressionist oil" | |
| | "minimalist flat design", "simple clean" | |
| when | "cinematic still", "movie scene" | |
| | "anime style", "Studio Ghibli inspired" | |
| 3D | "3D render", "isometric 3D" | |

#### Layer 2: composition/
| composition | | |
|------|--------|------|
| and | "wide shot", "establishing shot" | , scale |
| | "medium shot", "waist-up" | , vs |
| to | "close-up", "macro detail" | Emotion, |
| | "bird's eye view", "top-down" | total Structure, |
| to | "low angle shot", "worm's eye" | , |
| | "over-the-shoulder" | vs Scene |
| vs | "symmetrical composition" | , Formality |
| | "golden ratio composition" | when |

#### Layer 3: 
- **specific > **: "woman" → "30-year-old Korean woman with short black hair"
- ** **: "standing" → "leaning against a wall, reading a book"
- ** when**: "smiling softly with closed eyes"
- **of **: "wearing a dark navy wool coat"

#### Layer 4: /background
| | and |
|--------|------|
| "blurred background, bokeh" | |
| "detailed urban environment" | when context |
| "vast empty landscape" | / |
| "cozy indoor setting" | |
| "abstract gradient background" | , |

#### Layer 5: /
| | and | Scene |
|--------|------|----------|
| "golden hour light" | | , |
| "blue hour" | | , |
| "dramatic chiaroscuro" | | , etc. |
| "soft diffused light" | | , daily life |
| "neon glow" | | when, SF |
| "moonlight" | | , |
| "overcast, flat lighting" | lean | , daily life |

## Style Consistency technique

### when when Consistency core
1. ** **: Prompt in Style 
 ```
 "Soft watercolor illustration style, muted pastel palette, 
 Noto Serif Korean typography feel, [Scene ]"
 ```

2. **color palette **: Color when
 ```
 "Color palette: dusty rose (#D4A5A5), sage green (#9CAF88), 
 cream (#FFF8E7), charcoal (#36454F)"
 ```

3. ** **: Emotion/ 
 ```
 "melancholic yet hopeful atmosphere, nostalgic feeling"
 ```

4. **/ratio **: before Image 
 ```
 "--ratio 16:9 --size 2K" ( application)
 ```

## Prompt Pattern

### 
```
"NO text, NO watermark, NO signature, NO border, NO frame"
```

### photography 
```
"NO distorted faces, NO extra fingers, NO deformed hands, 
NO unnatural proportions, NO uncanny valley"
```

### background
```
"NO cluttered background, NO distracting elements, 
NO busy patterns"
```

### Text 
```
"Text MUST be in Korean: ' Text'"
(Text Image) "Absolutely NO text, NO letters, NO words, NO captions"
```

## Emotionper Prompt 

| Emotion | | Color | composition | |
|------|------|------|------|-----------|
| **** | golden hour, warm | , , | to, and | "ascending", "opening" |
| **** | blue hour, dim | , | and, | "isolated figure", "vast space" |
| **** | harsh, chiaroscuro | , | to, | "sharp shadows", "contrast" |
| **** | soft diffused | , | and, vs | "serene", "still", "gentle" |
| **** | overcast, rain | , | , | "rain", "muted", "quiet" |
| **** | backlight, dramatic | , | to, and | "majestic", "awe-inspiring" |
| **** | candlelight, warm | , | to, | "cozy", "intimate", "soft" |

## Scene typeper Prompt 

### in
```
"[Style] [whenbetweenvs] [] landscape. [/].
[before element]. [during element]. [ element].
[]. [ ]. NO text, NO people."
```

### 
```
"[Style] [composition] portrait of [ ].
[/]. [of]. [background].
[]. []. []."
```

### /
```
"[Style] [composition] [ ].
[placement/composition]. [background/].
[: soft diffused]. []. NO text."
```

### concept/
```
"[Style: illustration/abstract] visual metaphor for [concept].
[Visual element ]. [color palette].
[]. Clean composition, NO text."
```

## Image ratio Guide

| ratio | | description |
|------|------|------|
| 16:9 | , banner | |
| 3:2 | photography, | |
| 1:1 | SNS to, | |
| 4:5 | Instagram | to between |
| 9:16 | Story, , to banner | lean |
| 21:9 | when, to banner | traand |
