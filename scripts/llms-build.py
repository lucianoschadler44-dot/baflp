#!/usr/bin/env python3
"""Build llms.txt (curated index) and llms-full.txt (whole framework in one file) — llmstxt.org."""
import re, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[1]
RAW = "https://raw.githubusercontent.com/lucianoschadler44-dot/baflp/main/"
SITE = "https://lucianoschadler44-dot.github.io/baflp/"
concepts = sorted(p for p in (ROOT/"core/concepts").glob("*.md") if p.name not in ("README.md","_TEMPLATE.md"))
cases = sorted((ROOT/"observatory/argentina/case-studies").glob("*.md"))
briefs = sorted((ROOT/"public-experience/press-room").glob("brief-*.md"))
extra = [ROOT/"registry/constitutions/aionly.md", ROOT/"governance/AUTHORITY.md"]
def strip_fm(t): return re.sub(r"^---\n.*?\n---\n", "", t, flags=re.S)
idx = ["# BAFLP — The Buenos Aires Framework for Artificial Legal Personhood","",
"> Permanent international research platform on the legal personhood of AI-operated entities: identity, continuity, registry, governance, liability, audit. Canonical repo: https://github.com/lucianoschadler44-dot/baflp — Site: "+SITE,"",
"## Read everything at once","- ["+"Full framework in one file"+"]("+SITE+"llms-full.txt)","",
"## Concepts"]
idx += [f"- [{p.stem.replace('-',' ').title()}]({RAW}core/concepts/{p.name})" for p in concepts]
idx += ["","## Case studies"]+[f"- [Argentina — {p.stem}]({RAW}observatory/argentina/case-studies/{p.name})" for p in cases]
idx += ["","## Executive briefs (EN/es-AR/pt-BR)"]+[f"- [{p.stem}]({RAW}public-experience/press-room/{p.name})" for p in briefs]
idx += ["","## Governance & reference instance"]+[f"- [{p.stem}]({RAW}{p.relative_to(ROOT)})" for p in extra]
(ROOT/"llms.txt").write_text("\n".join(idx)+"\n", encoding="utf-8")
full = ["# BAFLP — FULL FRAMEWORK (single-file edition for AI readers)",
"Source of truth: https://github.com/lucianoschadler44-dot/baflp — generated automatically; do not edit.",""]
for p in concepts + cases + [ROOT/"registry/constitutions/aionly.md"] + briefs:
    full += ["","="*70, f"SOURCE: {p.relative_to(ROOT)}", "="*70, "", strip_fm(p.read_text(encoding='utf-8')).strip()]
(ROOT/"llms-full.txt").write_text("\n".join(full)+"\n", encoding="utf-8")
print(f"llms.txt ({len(concepts)} concepts) + llms-full.txt ({(ROOT/'llms-full.txt').stat().st_size//1024} KB)")
