#!/usr/bin/env python3
"""Usage: graph-impact.py <concept-id> — list every document affected if that concept changes."""
import json, sys, pathlib
g = json.loads((pathlib.Path(__file__).resolve().parents[1]/"core/graph/graph.json").read_text())
target = sys.argv[1] if len(sys.argv)>1 else sys.exit("usage: graph-impact.py <concept-id>")
nodes = {n["id"]: n for n in g["nodes"]}
if target not in nodes: sys.exit(f"unknown id: {target}")
impacted, frontier = set(), {target}
while frontier:
    nxt = {e["from"] for e in g["edges"] if e["to"] in frontier} - impacted - {target}
    impacted |= nxt; frontier = nxt
print(f"If {target} ({nodes[target]['title']}) changes, affected ({len(impacted)}):")
for i in sorted(impacted): print(f"  - {i}: {nodes[i]['title']}  [{nodes[i]['path']}]")
