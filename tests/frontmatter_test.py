#!/usr/bin/env python3
"""Every concept must carry the mandatory frontmatter keys."""
import sys, pathlib, re
ROOT = pathlib.Path(__file__).resolve().parents[1]
KEYS = ["id","title","version","status","summary","relations"]
bad = []
for f in (ROOT/"core/concepts").glob("*.md"):
    if f.name.startswith("_") or f.name == "README.md": continue
    text = f.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---", text, re.S)
    if not m: bad.append(f"{f.name}: no frontmatter"); continue
    fm = m.group(1)
    for k in KEYS:
        if not re.search(rf"^{k}\s*:", fm, re.M): bad.append(f"{f.name}: missing '{k}'")
if bad:
    print("\n".join(bad)); sys.exit(1)
print("frontmatter OK")
