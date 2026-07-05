#!/usr/bin/env python3
"""Plain Language Policy check: citizen lens must stay readable (warn-only until corpus exists)."""
import re, pathlib, sys
ROOT = pathlib.Path(__file__).resolve().parents[1]
def grade(text):
    words = re.findall(r"[a-zA-ZÀ-ÿ]+", text); sents = max(1, len(re.findall(r"[.!?]+", text)))
    if not words: return 0.0
    syll = sum(max(1, len(re.findall(r"[aeiouyáéíóúàâêôãõ]+", w.lower()))) for w in words)
    return 0.39*(len(words)/sents) + 11.8*(syll/len(words)) - 15.59
bad=[]
for f in (ROOT/"core/concepts").glob("*.md"):
    if f.name in ("README.md","_TEMPLATE.md"): continue
    t=f.read_text(encoding="utf-8")
    m=re.search(r"## In one sentence \(citizen\)\n(.*?)(?=\n## )", t, re.S)
    if not m: continue
    body=re.sub(r"<!--.*?-->","",m.group(1),flags=re.S).strip()
    if body in ("","(pending)","(pending — see governance/AUTHORITY.md)"): continue
    g=grade(body)
    if g>12: bad.append(f"{f.name}: grade {g:.1f} (>12)")
print("readability:", "WARN\n  "+"\n  ".join(bad) if bad else "OK (all citizen lenses within target)")
sys.exit(0)
