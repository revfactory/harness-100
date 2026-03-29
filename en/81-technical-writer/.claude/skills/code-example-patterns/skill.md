---
name: code-example-patterns
description: "Code example pattern library for technical documentation. Referenced by the doc-writer agent when writing code examples and tutorials. Use when 'code example patterns' or 'writing tutorial code' is requested. Actual code compilation and test execution are outside this skill's scope."
---

# Code Example Patterns — Code Example Pattern Library

Patterns that improve the quality of code examples the doc-writer agent includes in technical documentation.

## 5-Step Example Structure

```
1. Goal declaration — "This code performs X"
2. Prerequisites — Libraries, environment variables, configuration
3. Core code — Minimal working example
4. Execution result — Expected output
5. Extension point — "As a next step, you can do Y"
```

## Good Example vs. Bad Example

**Bad example** (no context):
```python
result = client.process(data)
```

**Good example** (self-contained):
```python
# pip install example-sdk
from example_sdk import Client

client = Client(api_key="your-api-key")
data = {"name": "test", "value": 42}
result = client.process(data)
print(result.status)  # "success"
```

## Style Guide by Language

### Python
- Import order: standard library → third-party → local
- Include type hints (Python 3.10+)
- Docstrings: Google style (Args, Returns, Raises)
- Use f-strings; avoid format()

### TypeScript
- Use ESM imports (avoid require)
- Use async/await (avoid Promise chaining)
- Explicitly declare interfaces and types
- Handle errors with try/catch

### cURL
- Use line continuation (`\`) for readability
- Separate sensitive information into environment variables
- Include expected response as a comment

## Tutorial Code Composition Patterns

### Pattern 1: Progressive Build
```
Step 1: Minimal working code
Step 2: Add input handling
Step 3: Add error handling
Step 4: Externalize configuration
Step 5: Production-ready code
```
At each step, **highlight only the changed parts**; abbreviate existing code with `...`.

### Pattern 2: Problem–Solution Pair
```markdown
#### Problem: [Specific problem description]
#### Solution: [Resolution method with code]
```

### Pattern 3: Comparison Table
| Approach | Advantages | Disadvantages | Code |
|----------|------------|---------------|------|
| Synchronous | Simple | Blocking | `result = fetch()` |
| Asynchronous | Performance | Complexity | `result = await fetch()` |

## Code Comment Rules

| Rule | Description |
|------|-------------|
| WHY comments | Explain *why* it was written this way |
| No WHAT comments | *What* is expressed by the code itself |
| Localized comments | Use the document's language for comments |
| No TODO | No incomplete items in examples |
| Hardcoding note | Add "In production, use..." comment |

## Handling Sensitive Information

```python
# Correct: environment variable
api_key = os.environ["API_KEY"]

# Documentation placeholder
api_key = "your-api-key-here"  # Replace with your actual key
```

## Quality Checklist

| Item | Standard |
|------|----------|
| Self-contained | Copy-paste from import to execution and it works |
| Error handling | try/catch included |
| Type information | Types specified for variables / parameters / return values |
| Execution result | Expected output included |
| Sensitive information | No hardcoded secrets |
| Version specified | Language and library version stated |
