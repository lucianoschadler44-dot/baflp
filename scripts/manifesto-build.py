#!/usr/bin/env python3
"""Living Manifesto — merged tally: comment votes (SIM/NAO/DEPENDE...) override reactions; 1 account = 1 vote."""
import yaml, json, subprocess, datetime, pathlib, re
ROOT = pathlib.Path(__file__).resolve().parents[1]
REPO = "lucianoschadler44-dot/baflp"
ax = yaml.safe_load((ROOT/"manifesto/axioms.yaml").read_text())
qs = {q["id"]: q for q in yaml.safe_load((ROOT/"manifesto/questions.yaml").read_text())["questions"]}
quorum = ax.get("quorum_per_question", 10)
def api(path):
    try: return json.loads(subprocess.run(["gh","api",path,"--paginate"],capture_output=True,text=True,check=True).stdout or "[]")
    except Exception: return []
WORD = {"SIM":"y","YES":"y","SI":"y","SÍ":"y","S":"y","Y":"y","NAO":"n","NÃO":"n","NO":"n","N":"n",
        "DEPENDE":"d","DEPENDS":"d","DEPEND":"d","COMPLICADO":"d","COMPLICATED":"d",":+1:":"y",":-1:":"n",":CONFUSED:":"d","👍":"y","👎":"n","😕":"d"}
def comment_vote(body):
    t = re.sub(r"[*_`>#\-\.,!\?¡¿]", " ", (body or "")).strip().upper()
    tok = t.split()[0] if t.split() else ""
    return WORD.get(tok)
issues = api(f"repos/{REPO}/issues?labels=consultation&state=open&per_page=100")
rows=[]
for it in issues:
    qid = it["title"].split("]")[0].strip("[")
    if qid not in qs: continue
    n = it["number"]; votes = {}
    for r in api(f"repos/{REPO}/issues/{n}/reactions?per_page=100"):
        v = {"+1":"y","-1":"n","confused":"d"}.get(r.get("content"))
        u = (r.get("user") or {}).get("login")
        if v and u and not u.endswith("[bot]"): votes[u] = v
    ncom = 0
    for c in api(f"repos/{REPO}/issues/{n}/comments?per_page=100"):
        u = (c.get("user") or {}).get("login"); ncom += 1
        if not u or u.endswith("[bot]"): continue
        v = comment_vote(c.get("body"))
        if v: votes[u] = v          # comentario prevalece; ultimo vale
    y = sum(1 for v in votes.values() if v=="y"); no = sum(1 for v in votes.values() if v=="n"); d = sum(1 for v in votes.values() if v=="d")
    rows.append({"id":qid,"en":qs[qid]["en"],"number":n,"url":it["html_url"],"yes":y,"no":no,"dep":d,"votes":y+no+d,"comments":ncom})
rows.sort(key=lambda r: r["id"])
today = datetime.date.today().isoformat()
(ROOT/"manifesto/results.json").write_text(json.dumps({"generated":today,"quorum":quorum,"questions":rows},indent=1),encoding="utf-8")
L=["---",'title: "The Living Manifesto"','subtitle: "Non-negotiable axioms + the voice of the majority — recompiled automatically"',"toc: true","---","",
f"> Automated compilation — {today}. Vote by comment (SIM/NÃO/DEPENDE) or reaction (👍/👎/😕); one account = one vote, comment prevails. Quorum ≥{quorum}. Every ballot public and auditable.","",
"## I. Non-negotiable axioms",""]
for a in ax["axioms"]:
    L += [f"**{a['id']}.** {a['en']}", f"<br><small>🇧🇷 {a['pt']} · 🇦🇷 {a['es']}</small>", ""]
L += ["## II. Positions under public consultation",""]
if not rows: L.append("_Consultation open — results appear automatically._")
for r in rows:
    t=r["votes"]
    if t >= quorum:
        m=max(r["yes"],r["no"],r["dep"])
        pos = "MAJORITY: **YES**" if r["yes"]==m and r["yes"]>max(r["no"],r["dep"]) else ("MAJORITY: **NO**" if r["no"]==m and r["no"]>max(r["yes"],r["dep"]) else ("PREVAILING: **IT DEPENDS**" if r["dep"]==m and r["dep"]>max(r["yes"],r["no"]) else "**TIED**"))
        L.append(f"**{r['id']}.** {r['en']}\n<br>{pos} — 👍{r['yes']} · 😕{r['dep']} · 👎{r['no']} ({t} votes, 💬{r['comments']}) · [ballot]({r['url']})")
    else:
        L.append(f"**{r['id']}.** {r['en']}\n<br>_In consultation ({t}/{quorum} votes, 💬{r['comments']})_ · [vote here]({r['url']})")
    L.append("")
L += ["## III. Method","",
"Merged tally: comment votes and reactions, one account one vote (comment prevails, latest counts). Compiled by in-repo automation into this page and `manifesto/results.json`. Full history in git."]
(ROOT/"manifesto.qmd").write_text("\n".join(L)+"\n",encoding="utf-8")
(ROOT/"manifesto/MANIFESTO.md").write_text("\n".join(L[5:])+"\n",encoding="utf-8")
print(f"manifesto: {len(rows)} questions merged; results.json written")
