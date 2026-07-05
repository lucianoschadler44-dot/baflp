#!/usr/bin/env python3
"""Living Manifesto: axioms (non-negotiable) + majority positions from the public consultation.
Deterministic generator, runs daily in CI. Labeled as automated compilation."""
import yaml, json, subprocess, datetime, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[1]
ax = yaml.safe_load((ROOT/"manifesto/axioms.yaml").read_text())
qs = {q["id"]: q for q in yaml.safe_load((ROOT/"manifesto/questions.yaml").read_text())["questions"]}
quorum = ax.get("quorum_per_question", 10)
try:
    issues = json.loads(subprocess.run(["gh","api","repos/lucianoschadler44-dot/baflp/issues?labels=consultation&state=open&per_page=100"],capture_output=True,text=True,check=True).stdout)
except Exception:
    issues = []
rows=[]
for it in issues:
    qid = it["title"].split("]")[0].strip("[")
    if qid not in qs: continue
    y = it.get("reactions",{}).get("+1",0); n = it.get("reactions",{}).get("-1",0)
    rows.append((qid, qs[qid]["en"], y, n, it["html_url"]))
rows.sort()
today = datetime.date.today().isoformat()
L=["---",'title: "The Living Manifesto"','subtitle: "Non-negotiable axioms + the voice of the majority — recompiled daily"',"toc: true","---","",
f"> Automated compilation — {today}. Axioms are fixed by the Framework; majority positions enter only with quorum (≥{quorum} votes). One GitHub account = one vote; every ballot is public and auditable.","",
"## I. Non-negotiable axioms",""]
for a in ax["axioms"]:
    L.append(f"**{a['id']}.** {a['en']}")
    L.append(f"<br><small>🇧🇷 {a['pt']} · 🇦🇷 {a['es']}</small>"); L.append("")
L += ["## II. Positions under public consultation",""]
if not rows:
    L.append("_Consultation just opened — results appear here automatically as votes arrive._")
for qid, txt, y, n, url in rows:
    t=y+n
    if t >= quorum:
        pos = "MAJORITY: **YES**" if y>n else ("MAJORITY: **NO**" if n>y else "**TIED**")
        L.append(f"**{qid}.** {txt}\n<br>{pos} — {y} yes / {n} no ({t} votes) · [ballot]({url})")
    else:
        L.append(f"**{qid}.** {txt}\n<br>_In consultation ({t}/{quorum} votes for quorum)_ · [vote here]({url})")
    L.append("")
L += ["## III. Method","",
"This document is recompiled every day by an automated process inside the repository (GitHub Actions), from `manifesto/axioms.yaml` and the live ballots. History is preserved in git — every version of this Manifesto, forever."]
(ROOT/"manifesto.qmd").write_text("\n".join(L)+"\n", encoding="utf-8")
(ROOT/"manifesto/MANIFESTO.md").write_text("\n".join(L[5:])+"\n", encoding="utf-8")
print(f"manifesto: {len(ax['axioms'])} axioms, {len(rows)} questions, quorum={quorum}")
