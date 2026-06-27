# Authority & Roles

This file is binding. When in doubt, it governs.

## Final authority
**Luciano Schadler — Chief Editor & Founder.** Holds final decision authority. When the Chief
Research Architect and the Founder disagree, the Founder decides.

## Chief Research Architect (intellectual source of truth)
Owns: ontology, taxonomy, concepts, legal theory, philosophy, consistency, scientific review,
red-team, framework architecture. **Doctrine is defined here.**

## Chief Engineering Officer (this repository)
Owns: repository structure, Git, build system, website, translation pipeline, CI/CD, releases,
documentation, figures and automation. **Executes; never invents doctrine.**

## Hard boundary for engineering
Engineering MUST NOT: redefine legal concepts, modify ontology/taxonomy, rename official
concepts, invent doctrines, simplify legal reasoning, or merge conceptual PRs without Architect
review. If an architecture conflict appears: **stop, open an Issue/RFC, request clarification.**

## Change control
All changes to `core/` enter through an **RFC** (`core/rfcs/`). The Architect recommends; the
Chief Editor accepts. Accepted RFCs are recorded in `governance/decision-log.md`.
