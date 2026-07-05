#!/usr/bin/env python3
"""Build core/graph/graph.json from all frontmatter (nodes=objects, edges=relations+references)."""
import re, json, pathlib, sys
ROOT = pathlib.Path(__file__).resolve().parents[1]
SCAN = ["core/concepts","observatory","registry","model-law","research"]
def fm(p):
    m = re.match(r"^---\n(.*?)\n---", p.read_text(encoding="utf-8"), re.S)
    return m.group(1) if m else ""
def get(fmt, key):
    m = re.search(rf"^{key}\s*:\s*(.+)$", fmt, re.M)
    return m.group(1).strip().strip('"') if m else None
def get_list(fmt, key):
    m = re.search(rf"{key}\s*:\s*\[(.*?)\]", fmt, re.S)
    return [x.strip().strip('"\'') for x in m.group(1).split(",") if x.strip()] if m else []
nodes, edges = {}, []
for base in SCAN:
    d = ROOT / base
    if not d.exists(): continue
    for f in d.rglob("*.md"):
        if f.name in ("README.md","_TEMPLATE.md") or "/archive/" in str(f): continue
        t = fm(f)
        nid = get(t, "id")
        if not nid: continue
        nodes[nid] = {"id": nid, "title": get(t,"title") or f.stem, "path": str(f.relative_to(ROOT)),
                      "status": get(t,"status") or "unknown", "complexity": get(t,"complexity")}
        for dep in get_list(t, "depends-on"): edges.append({"from": nid, "to": dep, "type": "depends-on"})
        for rel in get_list(t, "related-to"): edges.append({"from": nid, "to": rel, "type": "related-to"})
        for ref in get_list(t, "referenced-concepts") + re.findall(r"`(concept-\d{4})`", f.read_text(encoding="utf-8")):
            if ref != nid: edges.append({"from": nid, "to": ref, "type": "references"})
seen=set(); edges=[e for e in edges if not (t:=(e["from"],e["to"],e["type"])) in seen and not seen.add(t)]
out = ROOT/"core/graph/graph.json"
out.write_text(json.dumps({"nodes": list(nodes.values()), "edges": edges}, indent=2), encoding="utf-8")
print(f"graph: {len(nodes)} nodes, {len(edges)} edges -> core/graph/graph.json")
bad = [e for e in edges if e["to"].startswith("concept-") and e["to"] not in nodes]
if bad:
    print("BROKEN EDGES:", *[f'{e["from"]} -> {e["to"]}' for e in bad], sep="\n  "); sys.exit(1)
print("graph integrity OK")
