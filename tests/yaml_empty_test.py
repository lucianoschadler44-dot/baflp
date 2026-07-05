#!/usr/bin/env python3
"""Fail if any rendered .md/.qmd carries an empty scalar in its YAML frontmatter (Quarto rejects)."""
import re, sys, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[1]
DIRS = ["core","institution","observatory","public-experience","model-law","registry","research","governance","docs"]
SKIP = ("templates/","examples/","archive/","build/","translations/")
files = [p for d in DIRS if (ROOT/d).exists() for p in (ROOT/d).rglob("*.md")] + list(ROOT.glob("*.qmd"))
bad=[]
for f in files:
    rel=str(f.relative_to(ROOT)).replace("\\","/")
    if any(s in rel for s in SKIP): continue
    m=re.match(r"^---\n(.*?)\n---", f.read_text(encoding="utf-8"), re.S)
    if not m: continue
    lines=m.group(1).split("\n")
    for i,l in enumerate(lines):
        km=re.match(r"^([A-Za-z][\w-]*):\s*(#.*)?$", l)
        if not km: continue
        nxt=next((x for x in lines[i+1:] if x.strip() and not x.strip().startswith("#")), "")
        if nxt.startswith((" ","\t")) or nxt.lstrip().startswith("- "): continue
        bad.append(f"{rel}: campo '{km.group(1)}' vazio (linha {i+2})")
if bad:
    print("EMPTY YAML FIELDS:"); [print("  "+b) for b in bad]; sys.exit(1)
print(f"yaml-empty OK ({len(files)} arquivos varridos)")
