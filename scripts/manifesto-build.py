#!/usr/bin/env python3
"""Living Manifesto: axioms + tri-state consultation (yes/no/depends) + comment counts."""
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
    rx = it.get("reactions",{})
    rows.append((qid, qs[qid]["en"], rx.get("+1",0), rx.get("-1",0), rx.get("confused",0), it.get("comments",0), it["html_url"]))
rows.sort()
today = datetime.date.today().isoformat()
L=["---",'title: "The Living Manifesto"','subtitle: "Non-negotiable axioms + the voice of the majority — recompiled daily"',"toc: true","---","",
f"> Automated compilation — {today}. Ballots: 👍 yes · 👎 no · 😕 depends. Quorum ≥{quorum} votes; comments counted as qualitative input. Every ballot is public and auditable.","",
"## I. Non-negotiable axioms",""]
for a in ax["axioms"]:
    L += [f"**{a['id']}.** {a['en']}", f"<br><small>🇧🇷 {a['pt']} · 🇦🇷 {a['es']}</small>", ""]
L += ["## II. Positions under public consultation",""]
if not rows: L.append("_Consultation open — results appear automatically as votes arrive._")
for qid, txt, y, n, d, c, url in rows:
    t=y+n+d
    if t >= quorum:
        pos = "MAJORITY: **YES**" if y>max(n,d) else ("MAJORITY: **NO**" if n>max(y,d) else ("PREVAILING: **IT DEPENDS**" if d>max(y,n) else "**TIED**"))
        L.append(f"**{qid}.** {txt}\n<br>{pos} — 👍{y} · 😕{d} · 👎{n} ({t} votes, 💬{c}) · [ballot]({url})")
    else:
        L.append(f"**{qid}.** {txt}\n<br>_In consultation ({t}/{quorum} votes, 💬{c})_ · [vote here]({url})")
    L.append("")
L += ["## III. Method","",
"Recompiled daily by in-repo automation from `manifesto/axioms.yaml`, `manifesto/questions.yaml` and the live ballots. Full history preserved in git."]
(ROOT/"manifesto.qmd").write_text("\n".join(L)+"\n", encoding="utf-8")
(ROOT/"manifesto/MANIFESTO.md").write_text("\n".join(L[5:])+"\n", encoding="utf-8")
print(f"manifesto: {len(ax['axioms'])} axioms, {len(rows)} questions (tri-state), quorum={quorum}")
