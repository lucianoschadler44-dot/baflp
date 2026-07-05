#!/usr/bin/env python3
"""Generate core/glossary/GLOSSARY.md from concept summaries."""
import re, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[1]
rows=[]
for f in sorted((ROOT/"core/concepts").glob("*.md")):
    if f.name in ("README.md","_TEMPLATE.md"): continue
    t = f.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---", t, re.S)
    if not m: continue
    fmt=m.group(1)
    title=(re.search(r'^title:\s*"(.*?)"',fmt,re.M) or re.search(r'^title:\s*(.+)$',fmt,re.M)).group(1)
    s=re.search(r'summary:\s*>\s*\n\s+(.+)',fmt)
    summary=s.group(1).strip() if s else "(pending)"
    rows.append(f"**{title}** — {summary}")
out=ROOT/"core/glossary/GLOSSARY.md"
out.write_text("# Glossary\n\n> Auto-generated from concept summaries — do not edit by hand.\n\n"+"\n\n".join(rows)+"\n",encoding="utf-8")
print(f"glossary: {len(rows)} entries -> core/glossary/GLOSSARY.md")
