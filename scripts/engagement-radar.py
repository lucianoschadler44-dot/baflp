#!/usr/bin/env python3
"""Daily engagement radar: repo traffic, stars, votes; diffs vs yesterday; gov-referrer alerts."""
import json, subprocess, datetime, pathlib, os
ROOT = pathlib.Path(__file__).resolve().parents[1]
REPO = "lucianoschadler44-dot/baflp"
def api(path):
    try: return json.loads(subprocess.run(["gh","api",path],capture_output=True,text=True,check=True).stdout or "{}")
    except Exception: return {}
today = datetime.date.today().isoformat()
meta = api(f"repos/{REPO}")
views = api(f"repos/{REPO}/traffic/views"); clones = api(f"repos/{REPO}/traffic/clones")
refs = api(f"repos/{REPO}/traffic/popular/referrers") or []
paths = api(f"repos/{REPO}/traffic/popular/paths") or []
try: res = json.loads((ROOT/"manifesto/results.json").read_text())
except Exception: res = {"questions":[]}
votes = sum(q.get("votes",0) for q in res["questions"]); comments = sum(q.get("comments",0) for q in res["questions"])
snap = {"date": today, "stars": meta.get("stargazers_count",0), "forks": meta.get("forks_count",0),
 "watchers": meta.get("subscribers_count",0), "views14": views.get("count",0), "uniques14": views.get("uniques",0),
 "clones14": clones.get("count",0), "votes": votes, "comments": comments,
 "referrers": [{"ref":r.get("referrer"),"count":r.get("count"),"uniques":r.get("uniques")} for r in refs][:10],
 "paths": [{"path":p.get("path"),"count":p.get("count")} for p in paths][:10]}
prevf = ROOT/"manifesto/engagement.json"
prev = json.loads(prevf.read_text()) if prevf.exists() else {}
delta = {k: snap[k]-prev.get(k,0) for k in ("stars","forks","watchers","uniques14","votes","comments")}
gov = [r["ref"] for r in snap["referrers"] if r.get("ref") and any(t in r["ref"] for t in (".gob.",".gov",".leg.",".jus.",".senado",".camara","oecd"))]
prevf.write_text(json.dumps(snap,indent=1),encoding="utf-8")
hist = ROOT/"manifesto/engagement-history.jsonl"
with open(hist,"a",encoding="utf-8") as f: f.write(json.dumps(snap)+"\n")
alerts = [f"+{v} {k}" for k,v in delta.items() if v>0]
if gov: alerts.append("REFERRER INSTITUCIONAL: "+", ".join(gov))
L=["---",'title: "Engagement Radar"','subtitle: "Is the world responding? Updated daily by automation."',"toc: false","---","",
f"> Snapshot {today}. Repo traffic covers the GitHub repository (14-day window). Site-wide analytics unlock automatically once research.schadler.tech goes live behind Cloudflare.","",
f"**Stars:** {snap['stars']} · **Forks:** {snap['forks']} · **Watchers:** {snap['watchers']} · **Repo visits (14d):** {snap['views14']} ({snap['uniques14']} uniques) · **Clones (14d):** {snap['clones14']}","",
f"**Consultation:** {votes} votes · {comments} comments across {len(res['questions'])} ballots — [live board](consultation.qmd)",""]
if alerts: L += ["::: {.callout-important appearance=\"simple\"}","**Movement since last snapshot:** "+" · ".join(alerts),":::",""]
if snap["referrers"]:
    L += ["## Where visitors come from","","| Referrer | Visits | Uniques |","|---|---|---|"]
    L += [f"| {r['ref']} | {r['count']} | {r['uniques']} |" for r in snap["referrers"]]
    L.append("")
if snap["paths"]:
    L += ["## Most-viewed repo pages","","| Path | Views |","|---|---|"]
    L += [f"| {p['path']} | {p['count']} |" for p in snap["paths"]]
(ROOT/"radar.qmd").write_text("\n".join(L)+"\n",encoding="utf-8")
print(f"radar: {today} | " + (" · ".join(alerts) if alerts else "sem movimento novo"))
if alerts and os.environ.get("GITHUB_ACTIONS"):
    n = subprocess.run(["gh","issue","list","--label","radar","--state","open","--json","number","-q",".[0].number"],capture_output=True,text=True).stdout.strip()
    body = f"📡 {today}: " + " · ".join(alerts)
    if n: subprocess.run(["gh","issue","comment",n,"--body",body])
    else: subprocess.run(["gh","issue","create","--title","📡 Engagement Radar","--body",body,"--label","radar"])
