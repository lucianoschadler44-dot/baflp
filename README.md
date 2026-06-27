# The Buenos Aires Framework for Artificial Legal Personhood (BAFLP)

A permanent international research framework on the legal personhood of artificial entities.
**This repository is the single source of truth.** The website, PDFs, DOCX and EPUB are all
*generated* from these files — content is never duplicated in an output format.

> **Why "Buenos Aires".** In late May 2026 the Argentine Executive sent Congress a reform of the
> *Ley General de Sociedades* introducing the *sociedad automatizada* and the *corporación no humana* —
> entities with legal personality operated by AI. The global debate this opened (legal continuity,
> liability, registry, audit, governance) is exactly the problem space this Framework engineers a
> durable, auditable answer for. The Framework is **descriptive and infrastructural**, not advocacy.

## What this is — and is not
- It is **not** a book, white paper or manifesto.
- It is a versioned, modular, reusable knowledge base built to outlive any single document or author.
- Information is organised as **knowledge objects** (each concept exists exactly once and is referenced
  everywhere), **not** as chapters.

## Repository map
| Area | Folder |
|---|---|
| Canonical source of truth | `core/` (ontology · taxonomy · concepts · principles · rfcs) |
| Governance & process | `governance/` |
| Proposed model legislation | `model-law/` |
| Jurisdiction comparison | `comparative-law/` |
| Scholarship | `research/` (working-papers · case-studies) |
| Registry reference architecture | `registry/` |
| Centralised references | `bibliography/` |
| Media & diagrams | `assets/` · `figures/` · `diagrams/` |
| Build & automation | `scripts/` · `.github/` · `build/` · `tools/` · `tests/` |
| Editions | `translations/` (es-AR · pt-BR) |
| Visualization layer | `website/` |
| Handbook | `docs/` |

Every folder contains a `README.md` documenting its Purpose, Contents, Dependencies and Future evolution.

## Build (one command)
```bash
scripts/build.sh        # renders website + PDF + DOCX + EPUB into build/ via Quarto
scripts/validate.sh     # structure, frontmatter, links, references
```
See `docs/PUBLISHING.md` for the full pipeline.

## Governance in one line
Chief Editor (Luciano Schadler) holds final authority. The Chief Research Architect owns ontology,
taxonomy, concepts and doctrine. The Chief Engineering Officer (Claude Code) owns the repository,
build, site and releases. See `governance/AUTHORITY.md`.

## Versioning
Semantic versioning across the Framework; history is preserved forever (no overwrite, no deletion —
superseded material moves to `archive/`). See `CHANGELOG.md`.

## Licensing
- **Content** (`core/`, `research/`, `model-law/`, `comparative-law/`, docs): CC BY 4.0 — see `LICENSE-CONTENT`.
- **Code & scripts** (`scripts/`, `tools/`, `tests/`, build config): MIT — see `LICENSE-CODE`.

## Cite this work
See `CITATION.cff` (GitHub renders a "Cite this repository" button).
