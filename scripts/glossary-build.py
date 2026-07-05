#!/usr/bin/env python3
import re, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[1]
rows=[]
for f in sorted((ROOT/"core/concepts").glob("*.md")):
    if f.name in ("README.md","_TEMPLATE.md"): continue
    t=f.read_text(encoding="utf-8"); m=re.match(r"^---\n(.*?)\n---", t, re.S)
    if not m: continue
    fmt=m.group(1)
    title=(re.search(r'^title:\s*"(.*?)"',fmt,re.M) or re.search(r'^title:\s*(.+)$',fmt,re.M)).group(1)
    slug=re.search(r'^slug:\s*(.+)$',fmt,re.M).group(1).strip()
    s=re.search(r'summary:\s*>\s*\n\s+(.+)',fmt); summary=s.group(1).strip() if s else "(pending)"
    rows.append((title,slug,summary))
(ROOT/"core/glossary/GLOSSARY.md").write_text("# Glossary (generated)\n\n"+ "\n\n".join(f"**{t}** — {s}" for t,_,s in rows)+"\n",encoding="utf-8")
(ROOT/"glossary.qmd").write_text('---\ntitle: "Glossary"\ntoc: false\n---\n\n'+"\n\n".join(f"**[{t}](core/concepts/{sl}.qmd)** — {s}" for t,sl,s in rows)+"\n",encoding="utf-8")
print(f"glossary: {len(rows)} entries")
