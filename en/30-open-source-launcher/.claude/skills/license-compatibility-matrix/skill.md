---
name: license-compatibility-matrix
description: "Open source license compatibility matrix, per-license obligations, dual-licensing strategy, and SPDX identifier guide. Use this skill for open source license decisions such as 'license compatibility', 'license selection', 'MIT', 'Apache', 'GPL', 'LGPL', 'BSD', 'dual license', 'SPDX', or 'license conflict'. It strengthens the license-specialist's license analysis capability. However, legal counsel and the actual generation of license files are outside this skill's scope."
---

# License Compatibility Matrix — Open Source License Compatibility Guide

A practical guide for open source license selection, compatibility analysis, and resolving dependency license conflicts.

## Major License Comparison

| License | Type | Commercial use | Modification disclosure | Patent protection | Network clause |
|---------|------|----------|----------|----------|-------------|
| MIT | Permissive | O | X | X | X |
| Apache 2.0 | Permissive | O | X | O | X |
| BSD 2-Clause | Permissive | O | X | X | X |
| BSD 3-Clause | Permissive | O | X | X | X |
| MPL 2.0 | Weak copyleft | O | Per file | O | X |
| LGPL 2.1/3.0 | Weak copyleft | O | Library only | X | X |
| GPL 2.0/3.0 | Strong copyleft | Conditional | O (entire) | O(v3) | X |
| AGPL 3.0 | Strong copyleft | Conditional | O (entire) | O | O |

## Compatibility Matrix

```
Project license ↓  |  Dependency license →
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

**Core rules:**
- Using a GPL dependency → the entire project becomes GPL-licensed (viral effect)
- Using an AGPL dependency → network services must also disclose their source
- Apache 2.0 ↔ GPL 2.0 are incompatible (patent clause conflict)

## License Selection Decision Tree

```
Project goal
├── Want maximum adoption → MIT or Apache 2.0
│   ├── Patent protection needed → Apache 2.0
│   └── Maximum simplicity → MIT
├── Want modified versions disclosed (per file) → MPL 2.0
├── Library, linking allowed → LGPL 3.0
├── Want all derivatives disclosed → GPL 3.0
├── Want disclosure including SaaS → AGPL 3.0
└── Dual license (OSS + commercial) → GPL + Commercial
```

## Resolving Dependency License Conflicts

### Conflict Patterns and Resolutions

| Conflict | Problem | Resolution |
|------|------|------|
| MIT project + GPL dependency | GPL propagation | Find a replacement package or switch to GPL |
| Apache + GPL 2.0 | Patent clause incompatibility | Use the GPL 3.0 version |
| Commercial product + AGPL dependency | Source disclosure obligation | Replace the package or purchase a license |
| Mixing multiple GPL versions | Version compatibility | Use "GPL 2.0 or later" |

### License Audit Tools

```bash
# Node.js
npx license-checker --json --production

# Python
pip-licenses --format=json --with-urls

# Go
go-licenses check ./...

# General-purpose
scancode-toolkit --json-pp output.json src/
```

## SPDX License Expressions

```
# Single license
SPDX-License-Identifier: MIT

# OR (selectable)
SPDX-License-Identifier: MIT OR Apache-2.0

# AND (comply with both licenses)
SPDX-License-Identifier: MIT AND BSD-3-Clause

# WITH (exception included)
SPDX-License-Identifier: GPL-2.0-only WITH Classpath-exception-2.0
```

## Dual-Licensing Strategy

```
Community Edition: AGPL 3.0
├── Free to use
├── Source disclosure required when providing modifications + services
└── Suitable for individuals/small open source projects

Enterprise Edition: Commercial license
├── Exemption from AGPL obligations
├── Additional features/support included
└── Targeted at enterprise customers

Success cases: MongoDB(SSPL), Redis(RSALv2), MySQL(GPL+Commercial)
```

## License Obligations Checklist

```markdown
Before project release, confirm:
- [ ] All dependency licenses identified
- [ ] License compatibility matrix verified
- [ ] All third-party licenses included in the LICENSE file
- [ ] Copyright notice (NOTICE) file written (required for Apache 2.0)
- [ ] Source disclosure prepared when using GPL dependencies
- [ ] SPDX identifiers included in source files
- [ ] License field specified in package.json/pyproject.toml
```
