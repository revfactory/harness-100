#!/usr/bin/env python3
"""Static lint for harness folders (<root>/<harness>/.claude/{agents,skills,CLAUDE.md}).

Stdlib only, deterministic, read-only. Usage: harness_lint.py <root> [--au] [-v]
Exit 1 if any ERROR. Rules are our own, written from the rule names only.
  ERROR SKILL_FILENAME   skill dir lacks exactly-cased SKILL.md (Linux is case-sensitive)
  ERROR FRONTMATTER      agent/skill file lacks a --- block with name + description
  WARN  NAME_MISMATCH    frontmatter name != agent file stem / skill dir name
  WARN  ABSOLUTE_PATHS   hard-coded /Users/, /home/ or C:\\ path
  WARN  DOC_DRIFT        agents listed in CLAUDE.md tree != agents on disk
  WARN  FOREIGN_REF      (--au) leftover GDPR/CCPA/PIPA/KIPRIS/USPTO/CAN-SPAM/KRW/Korea terms
"""
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

ABS = re.compile(r"(?:/Users/|/home/|[A-Z]:\\)\w")
FOREIGN = re.compile(r"\b(?:GDPR|CCPA|PIPA|KIPRIS|USPTO|CAN-SPAM|KRW|Korea)\b")


def frontmatter(text):
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    if not m:
        return None
    return dict(l.split(":", 1) for l in m.group(1).split("\n") if ":" in l and not l.startswith(" "))


def check_file(path, expect_name, add):
    text = path.read_text(encoding="utf-8", errors="replace")
    fm = frontmatter(text)
    if not fm or not fm.get("name", "").strip() or not fm.get("description", "").strip():
        add("ERROR", "FRONTMATTER", path, "missing name/description block")
    elif fm["name"].strip().strip("\"'") != expect_name:
        add("WARN", "NAME_MISMATCH", path, "name=%r expected %r" % (fm["name"].strip(), expect_name))
    return text


def lint(root, au):
    out = []
    add = lambda lvl, code, p, msg: out.append((lvl, code, p, msg))
    for h in sorted(p for p in root.iterdir() if (p / ".claude").is_dir()):
        c = h / ".claude"
        texts = []
        adir, sdir = c / "agents", c / "skills"
        agents = {a.stem for a in adir.glob("*.md")} if adir.is_dir() else set()
        for a in sorted(adir.glob("*.md")) if adir.is_dir() else []:
            texts.append((a, check_file(a, a.stem, add)))
        for s in sorted(p for p in sdir.iterdir() if p.is_dir()) if sdir.is_dir() else []:
            f = s / "SKILL.md"
            if f.exists():
                texts.append((f, check_file(f, s.name, add)))
            else:
                add("ERROR", "SKILL_FILENAME", s, "no SKILL.md (found: %s)" % sorted(x.name for x in s.glob("*.md")))
                for x in s.glob("*.md"):  # still lint the misnamed file's content
                    texts.append((x, check_file(x, s.name, add)))
        cm = c / "CLAUDE.md"
        if cm.exists():
            body = cm.read_text(encoding="utf-8", errors="replace")
            texts.append((cm, body))
            lines = body.split("\n")
            try:  # tree section between the 'agents/' and 'skills/' lines
                i = next(n for n, l in enumerate(lines) if "agents/" in l)
                j = next(n for n, l in enumerate(lines) if n > i and "skills/" in l)
                listed = {m for l in lines[i + 1:j] for m in re.findall(r"([\w-]+)\.md", l)}
                if listed and listed != agents:
                    add("WARN", "DOC_DRIFT", cm, "listed-not-on-disk=%s on-disk-not-listed=%s"
                        % (sorted(listed - agents), sorted(agents - listed)))
            except StopIteration:
                pass
        for p, t in texts:
            if ABS.search(t):
                add("WARN", "ABSOLUTE_PATHS", p, "hard-coded absolute path")
            if au and FOREIGN.search(t):
                add("WARN", "FOREIGN_REF", p, "%d hit(s)" % len(FOREIGN.findall(t)))
    return out


def main(argv):
    args = [a for a in argv[1:] if not a.startswith("-")]
    out = lint(Path(args[0]), "--au" in argv)
    by = defaultdict(Counter)
    for lvl, code, _, _ in out:
        by[code][lvl] += 1
    for code, c in sorted(by.items()):
        print("%-15s %s %d" % (code, "ERROR" if c["ERROR"] else "WARN ", sum(c.values())))
    if "-v" in argv:
        for lvl, code, p, msg in out:
            print("%s %s %s %s" % (lvl, code, p, msg))
    errs = sum(1 for o in out if o[0] == "ERROR")
    print("total: %d finding(s), %d error(s)" % (len(out), errs))
    return 1 if errs else 0


def demo():  # one runnable self-check: python3 harness_lint.py --demo
    import tempfile
    with tempfile.TemporaryDirectory() as d:
        c = Path(d) / "h" / ".claude"
        (c / "agents").mkdir(parents=True)
        (c / "skills" / "s").mkdir(parents=True)
        (c / "agents" / "a.md").write_text("no frontmatter /Users/x/y\n")
        (c / "skills" / "s" / "skill.md").write_text("---\nname: s\ndescription: d\n---\n")
        codes = {(o[0], o[1]) for o in lint(Path(d), True)}
        assert ("ERROR", "FRONTMATTER") in codes and ("ERROR", "SKILL_FILENAME") in codes
        assert ("WARN", "ABSOLUTE_PATHS") in codes
    print("demo ok")


if __name__ == "__main__":
    if "--demo" in sys.argv:
        demo()
    else:
        sys.exit(main(sys.argv))
