---
name: refactoring-catalog
description: "Code refactoring catalog. An extension skill for architecture-reviewer/performance-analyst that provides Martin Fowler-based refactoring patterns, code smell detection-to-refactoring mapping, SOLID principle violation identification, and complexity measurement criteria. Use when reviewing code structure improvement involving 'refactoring', 'code smells', 'SOLID violations', 'complexity', 'design patterns', 'code quality', etc. Note: direct code modification and security analysis are outside the scope of this skill."
---

# Refactoring Catalog — Code Refactoring Catalog

A reference of code smell-to-refactoring mappings, SOLID violation identification, and complexity metrics used by the architecture-reviewer and performance-analyst agents during code structure analysis.

## Target Agents

- `architecture-reviewer` — Applied when suggesting refactoring based on design patterns and SOLID principles
- `performance-analyst` — Applied when suggesting refactoring related to complexity analysis and performance

## Code Smell to Refactoring Mapping

### Size-Related Smells

| Code Smell | Symptoms | Refactoring Technique |
|-----------|----------|----------------------|
| **Long Method** | 20+ lines | Extract Method, Replace Temp with Query |
| **Large Class** | 300+ lines or 10+ fields | Extract Class, Extract Subclass |
| **Long Parameter List** | 4+ parameters | Introduce Parameter Object, Builder Pattern |
| **Data Clumps** | Same field groups repeated | Extract Class |
| **Primitive Obsession** | Domain concepts as primitives | Value Object, Enum |

### Structure-Related Smells

| Code Smell | Symptoms | Refactoring Technique |
|-----------|----------|----------------------|
| **Feature Envy** | Excessive use of another class's data | Move Method |
| **Data Class** | Class with only getters/setters | Move behaviour into class |
| **Shotgun Surgery** | One change affects multiple classes | Move Method/Field, Inline Class |
| **Divergent Change** | One class changes for multiple reasons | Extract Class (SRP) |
| **Duplicated Code** | Identical/similar code repeated | Extract Method, Template Method |
| **Middle Man** | Class that only delegates | Remove Middle Man, Inline Class |
| **Inappropriate Intimacy** | Excessive coupling between classes | Move Method/Field, Extract Class |
| **Switch/If Chain** | Long conditional branching | Replace Conditional with Polymorphism, Strategy |
| **Refused Bequest** | Inherited but unused methods | Replace Inheritance with Delegation |
| **Comments** | Complex logic explained by comments | Extract Method (self-documenting code) |

## SOLID Principle Violation Identification

### S — Single Responsibility Principle
| Violation Signal | Identification Criteria | Refactoring |
|-----------------|------------------------|-------------|
| Class name contains "And", "Manager" | Implies multiple responsibilities | Extract Class |
| 2+ reasons to change | "If X changes this class changes, and if Y changes this class also changes" | Separate classes by responsibility |
| Highly diverse imports | Imports DB, HTTP, UI, logging all together | Layer separation |

### O — Open/Closed Principle
| Violation Signal | Identification Criteria | Refactoring |
|-----------------|------------------------|-------------|
| Switch/if modified when adding new types | Existing code modification required | Strategy Pattern, Polymorphism |
| Hardcoded branching | Code added for each new condition | Plugin/Registry pattern |

### L — Liskov Substitution Principle
| Violation Signal | Identification Criteria | Refactoring |
|-----------------|------------------------|-------------|
| Override throws exception in child class | `NotImplementedError`, `UnsupportedOperationException` | Interface segregation, Inheritance to Composition |
| Type checking then casting | `instanceof` / `typeof` branching | Redesign with polymorphism |

### I — Interface Segregation Principle
| Violation Signal | Identification Criteria | Refactoring |
|-----------------|------------------------|-------------|
| Empty interface implementations | `pass`, `{}`, `noop` | Interface segregation |
| "Fat" interface | 10+ methods | Split into Role Interfaces |

### D — Dependency Inversion Principle
| Violation Signal | Identification Criteria | Refactoring |
|-----------------|------------------------|-------------|
| Direct concrete class instantiation | Hardcoded `new ConcreteService()` | Dependency Injection |
| Upper module imports lower module | Business logic directly uses DB library | Interface/Port abstraction |

## Complexity Measurement Criteria

### Cyclomatic Complexity
Branch points (if/else/switch/for/while/catch) + 1

| Score | Complexity | Action |
|-------|-----------|--------|
| 1-5 | Low | Appropriate |
| 6-10 | Medium | Review with care |
| 11-20 | High | Refactoring recommended |
| 21+ | Very high | Refactoring required |

### Cognitive Complexity
Difficulty of human code comprehension. Weight increases with deeper nesting.

| Element | Base Increment | Nesting Bonus |
|---------|---------------|---------------|
| if/else/switch | +1 | +nesting level |
| for/while/do | +1 | +nesting level |
| catch | +1 | +nesting level |
| break/continue to label | +1 | - |
| Logical operator chain (&&, ||) | +1 | - |
| Recursive call | +1 | - |

### Recommended Thresholds
| Metric | Method/Function | Class/File |
|--------|----------------|-----------|
| Lines of code | Under 20 | Under 300 |
| Cyclomatic complexity | 10 or less | - |
| Cognitive complexity | 15 or less | - |
| Parameter count | 4 or less | - |
| Nesting depth | 3 levels or less | - |
| Dependency count | - | 10 or less |

## Design Pattern Application Guide

### Smell to Pattern Mapping

| Problem Situation | Applicable Pattern | Effect |
|------------------|-------------------|--------|
| Behavioural branching via conditionals | **Strategy** | OCP compliance, easy to add new behaviours |
| Complex object creation logic | **Factory Method/Builder** | Encapsulate creation logic |
| Same algorithm skeleton, different details | **Template Method** | Remove duplication, isolate change points |
| Behaviour changes based on state | **State** | Remove conditionals, clarify state transitions |
| Event propagation to multiple objects | **Observer** | Loose coupling |
| Integrating incompatible interfaces | **Adapter** | Integration without modifying existing code |
| Simplifying complex subsystems | **Facade** | Interface simplification |
| Dynamically adding features to objects | **Decorator** | Feature extension without inheritance |

## Refactoring Priority Decision

### Impact-Difficulty Matrix

| | Low Difficulty | High Difficulty |
|--|---------------|----------------|
| **High Impact** | Do immediately | Plan then execute |
| **Low Impact** | When time allows | Defer (low cost-benefit) |

### Refactoring Suggestion Format
```
[Severity] Code Smell: [Smell Name]
Location: [File:Line]
Current State: [Problem description]
Refactoring: [Technique name]
Expected Effect: [How it improves]
Estimated Difficulty: [Low/Medium/High]
```
