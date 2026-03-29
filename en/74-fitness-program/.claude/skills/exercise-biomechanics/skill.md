---
name: exercise-biomechanics
description: "Biomechanical analysis of exercise movements and safe execution guides. When the 'exercise-guide' agent explains exercise movements and presents alternative exercises, it must utilize the muscle activation data, joint load analysis, and injury prevention guides from this skill. Use for 'exercise form guide', 'muscle activation', 'injury prevention', 'alternative exercises', etc. However, program design and nutrition strategy are outside the scope of this skill."
---

# Exercise Biomechanics — Exercise Biomechanics Guide

Analyzes muscle activation, joint load, correct form, and alternative exercises for major movements.

## Major Strength Exercise Analysis

### Squat

```
Primary movers: Quadriceps, gluteus maximus
Synergists: Hamstrings, adductors, erector spinae, abdominals

Joint load:
  Knee: High (patellar tendon stress)
  Lower back: Medium~High (shear force)
  Hip: Medium

Correct form:
  - Foot width: Shoulder-width or slightly wider
  - Knee direction: Aligned with toe direction (slight external rotation)
  - Depth: Femur minimum parallel (based on hip crease)
  - Back: Maintain neutral spine, avoid excessive forward lean
  - Gaze: Slightly above horizontal

Prohibited movements:
  ✗ Knee valgus collapse
  ✗ Excessive forward lean (butt wink)
  ✗ Heel rise
  ✗ Knees excessively tracking past toes
```

**Alternative exercises by injury history**:

| Injury site | Alternative exercise | Reason |
|-------------|---------------------|--------|
| Knee | Leg press (shallow angle), hip thrust | Reduces patellar tendon load |
| Lower back | Goblet squat, belt squat | Reduces spinal load |
| Shoulder | Front squat, safety bar | No shoulder mobility required |
| Hip | Box squat (depth limited) | ROM restriction |

### Deadlift

```
Primary movers: Erector spinae, gluteus maximus, hamstrings
Synergists: Trapezius, latissimus dorsi, forearms, quadriceps

Joint load:
  Lower back: Very high (compression + shear)
  Hip: High
  Knee: Medium

Variation characteristics:
| Variation | Lower back load | Primary target | Suitable for |
|-----------|----------------|----------------|--------------|
| Conventional | High | Full posterior chain | Intermediate+ |
| Sumo | Medium | Adductors + glutes | Long torso |
| Romanian (RDL) | Medium | Hamstrings | Beginner+ |
| Trap bar | Low | Evenly distributed | Beginner recommended |
| Rack pull | Low | Upper back | Lower back protection |
```

### Bench Press

```
Primary movers: Pectoralis major
Synergists: Anterior deltoid, triceps

Joint load:
  Shoulder: High (rotator cuff)
  Wrist: Medium
  Thoracic spine: Low

Differences by grip width:
  Narrow grip: Triceps emphasis, reduced shoulder load
  Medium grip: Balanced activation
  Wide grip: Chest emphasis, increased shoulder load

Shoulder protection form:
  - Scapular retraction and depression (shoulder blade squeeze)
  - Elbow angle 45-75 degrees (90 degrees prohibited)
  - Arch: Natural thoracic arch
  - Bar path: Diagonal from clavicle to lower chest
```

## Exercise Selection Guide by Muscle Group

### Upper Body

| Muscle | Beginner | Intermediate | Advanced | Equipment limited |
|--------|----------|--------------|----------|-------------------|
| Chest | Machine chest press | Bench press | Incline DB press | Push-up variations |
| Back | Lat pulldown | Barbell row | Weighted pull-up | Inverted row |
| Shoulder | Machine shoulder press | DB shoulder press | Military press | Pike push-up |
| Biceps | Machine curl | Barbell curl | Incline DB curl | Chin-up (supinated) |
| Triceps | Cable pushdown | Dips | Close-grip bench | Diamond push-up |

### Lower Body

| Muscle | Beginner | Intermediate | Advanced | Equipment limited |
|--------|----------|--------------|----------|-------------------|
| Quadriceps | Leg press | Barbell squat | Front squat | Bulgarian split squat |
| Hamstrings | Leg curl | RDL | Nordic curl | Sliding leg curl |
| Glutes | Bodyweight hip thrust | Barbell hip thrust | Single-leg RDL | Glute bridge |
| Calves | Bodyweight calf raise | Standing calf raise | Seated calf raise | Stair calf raise |

## Warm-up & Cool-down Protocol

### Pre-workout Dynamic Warm-up (5–10 min)

```
1. Full body: Jogging / jump rope (2 min)
2. Hip: Leg swings front/back and side/side (10 reps each)
3. Thoracic spine: Thoracic rotation (8 reps each side)
4. Shoulder: Arm circles + band pull-apart (10 reps each)
5. Knee: Bodyweight squat (10 reps)
6. Activation: 2 sets at 50% of working weight for target exercise
```

### Post-workout Static Stretching (5–10 min)

```
Hold each position 20–30 seconds, within pain-free range

Chest: Doorframe stretch
Back: Child's pose
Shoulder: Cross-body stretch
Quadriceps: Standing quad stretch
Hamstrings: Seated forward fold
Hip: Pigeon stretch
```

## References

- Based on NSCA and ACSM guidelines
- Detailed movement analysis: See `references/exercise-details.md`
