# concepts

> Part of **BAFLP** — The Buenos Aires Framework for Artificial Legal Personhood.
> This README is mandatory metadata. Do not delete.

## Purpose
The knowledge-object layer. Each concept (Artificial Identity, Legal Continuity, Artificial Registry, Governance, Liability, Audit, ...) exists EXACTLY ONCE here and is referenced everywhere.

## Contents
One Markdown file per concept with mandatory YAML frontmatter (id, version, status, relations). A `_TEMPLATE.md` and metadata-only stubs (no doctrine yet).

## Dependencies
Depends on `ontology/` (relations) and `taxonomy/` (category). Bibliography keys from `bibliography/`.

## Future evolution
Each concept versions independently; cross-references resolved automatically at build time.
