---
name: license-compatibility-matrix
description: "Open source license compatibility matrix, per-license obligations, dual licensing strategy, and SPDX identifier guide. Use this skill when making decisions related to open source licensing involving 'license compatibility', 'license selection', 'MIT', 'Apache', 'GPL', 'LGPL', 'BSD', 'dual license', 'SPDX', or 'license conflict'. Enhances the license analysis capabilities of license-specialist. Note: legal advice and actual license file generation are outside the scope of this skill."
---

# License Compatibility Matrix — Open Source License Compatibility Guide

A practical guide for open source license selection, compatibility analysis, and resolving dependency license conflicts.

## Major License Comparison

| License | Type | Commercial Use | Modification Disclosure | Patent Protection | Network Clause |
|---------|------|---------------|------------------------|------------------|----------------|
| MIT | Permissive | O | X | X | X |
| Apache 2.0 | Permissive | O | X | O | X |
| BSD 2-Clause | Permissive | O | X | X | X |
| BSD 3-Clause | Permissive | O | X | X | X |
| MPL 2.0 | Weak Copyleft | O | Per file | O | X |
| LGPL 2.1/3.0 | Weak Copyleft | O | Library only | X | X |
| GPL 2.0/3.0 | Strong Copyleft | Conditional | O (full) | O (v3) | X |
| AGPL 3.0 | Strong Copyleft | Conditional | O (full) | O | O |

## Compatibility Matrix

```
Project License ↓  |  Dependency License →
                    | MIT | Apache | BSD | MPL | LGPL | GPL | AGPL
────────────────────┼─────┼────────┼─────┼─────┼──────┼─────┼──────
MIT                 | ✅  | ✅     | ✅  | ✅  | ✅   | ❌  | ❌
Apache 2.0          | ✅  | ✅     | ✅  | ✅  | ✅   | ❌  | ❌
BSD                 | ✅  | ✅     | ✅  | ✅  | ✅   | ❌  | ❌
MPL 2.0             | ✅  | ✅     | ✅  | ✅  | ✅   | ✅* | ❌
LGPL 3.0            | ✅  | ✅     | ✅  | ✅  | ✅   | ✅  | ❌
GPL 3.0             | ✅  | ✅     | ✅  | ✅  | ✅   | ✅  | ❌
AGPL 3.0            | ✅  | ✅     | ✅  | ✅  | ✅   | ✅  | ✅

✅ Compatible | ❌ Incompatible | ✅* Conditionally compatible
```

**Key Rules:**
- Using a GPL dependency → the entire project must be GPL-licensed (viral effect)
- Using an AGPL dependency → network services are also subject to source disclosure obligations
- Apache 2.0 ↔ GPL 2.0 are incompatible (patent clause conflict)

## License Selection Decision Tree

```
Project Goal
├── Maximize adoption → MIT or Apache 2.0
│   ├── Patent protection needed → Apache 2.0
│   └── Maximum simplicity → MIT
├── Require disclosure of modifications (per file) → MPL 2.0
├── Library; allow linking → LGPL 3.0
├── Require all derivatives to be open → GPL 3.0
├── Require disclosure including SaaS → AGPL 3.0
└── Dual license (OSS + commercial) → GPL + Commercial
```

## Dependency License Conflict Resolution

### Conflict Patterns and Resolutions

| Conflict | Problem | Resolution |
|----------|---------|-----------|
| MIT project + GPL dependency | GPL propagation | Find alternative package or switch to GPL |
| Apache + GPL 2.0 | Patent clause incompatibility | Use GPL 3.0 version |
| Commercial product + AGPL dependency | Source disclosure obligation | Find alternative package or purchase a license |
| Mixed multiple GPL versions | Version compatibility | Use "GPL 2.0 or later" |

### License Audit Tools

```bash
# Node.js
npx license-checker --json --production

# Python
pip-licenses --format=json --with-urls

# Go
go-licenses check ./...

# General purpose
scancode-toolkit --json-pp output.json src/
```

## SPDX License Expressions

```
# Single license
SPDX-License-Identifier: MIT

# OR (user's choice)
SPDX-License-Identifier: MIT OR Apache-2.0

# AND (must comply with both licenses)
SPDX-License-Identifier: MIT AND BSD-3-Clause

# WITH (includes exception)
SPDX-License-Identifier: GPL-2.0-only WITH Classpath-exception-2.0
```

## Dual Licensing Strategy

```
Community Edition: AGPL 3.0
├── Free to use
├── Source disclosure required when distributing modifications or providing as a service
└── Suitable for individual/small open source projects

Enterprise Edition: Commercial License
├── AGPL obligations waived
├── Additional features/support included
└── Targeted at enterprise customers

Success examples: MongoDB (SSPL), Redis (RSALv2), MySQL (GPL+Commercial)
```

## License Obligations Checklist

```markdown
Before distributing the project, verify:
- [ ] Licenses identified for all dependencies
- [ ] License compatibility matrix verification complete
- [ ] All third-party licenses included in the LICENSE file
- [ ] Copyright notice (NOTICE) file prepared (required for Apache 2.0)
- [ ] Source disclosure prepared when using GPL dependencies
- [ ] SPDX identifiers included in source files
- [ ] License field specified in package.json/pyproject.toml
```
