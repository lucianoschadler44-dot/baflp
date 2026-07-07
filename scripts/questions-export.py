#!/usr/bin/env python3
import yaml, json, subprocess, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[1]
qs = yaml.safe_load((ROOT/"manifesto/questions.yaml").read_text())["questions"]
try:
    issues = json.loads(subprocess.run(["gh","issue","list","--label","consultation","--state","open","--json","number,title,url","--limit","100"],capture_output=True,text=True).stdout or "[]")
except Exception: issues=[]
urls = {i["title"].split("]")[0].strip("["): i["url"] for i in issues if i["title"].startswith("[Q")}
out = [{"id":q["id"],"pt":q["pt"],"es":q["es"],"en":q["en"],"gh":urls.get(q["id"],"https://github.com/lucianoschadler44-dot/baflp/issues")} for q in qs]
(ROOT/"manifesto/questions.json").write_text(json.dumps(out,ensure_ascii=False,indent=1),encoding="utf-8")
print(f"questions.json: {len(out)} perguntas")
