#!/usr/bin/env python3
"""Fail if required directories or their READMEs are missing."""
import sys, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[1]
REQUIRED = [
 "institution",
 "institution/standards",
 "observatory",
 "observatory/argentina",
 "observatory/brazil",
 "observatory/european-union",
 "public-experience",
 "public-experience/learning-center",
 "public-experience/decision-simulator",
 "core/adrs",
 "core/graph",
 "core/glossary",
 "core/metadata",
 "core/ontology","core/taxonomy","core/concepts","core/principles","core/rfcs",
 "governance","model-law","comparative-law","research/working-papers","research/case-studies",
 "registry/artificial-legal-persons","registry/constitutions","bibliography","assets","figures",
 "diagrams/mermaid","scripts","templates","translations/es-AR","translations/pt-BR","website",
 "api","build","releases","archive","tools","tests",".github","examples","downloads","docs",
]
missing = []
for d in REQUIRED:
    p = ROOT / d
    if not p.is_dir(): missing.append(f"missing dir: {d}")
    elif not (p / "README.md").exists() and not (p / ".gitkeep").exists():
        missing.append(f"missing README: {d}")
if missing:
    print("\n".join(missing)); sys.exit(1)
print(f"structure OK ({len(REQUIRED)} required paths present)")
