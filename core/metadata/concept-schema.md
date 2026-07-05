# Concept frontmatter schema (normative — ADR-0001 v2)

Required keys: `id` (concept-NNNN, stable) · `title` · `slug` · `version` (SemVer) · `status`
(draft|review|accepted|superseded) · `complexity` (beginner|intermediate|advanced) · `summary`
(one sentence; feeds glossary) · `relations` {depends-on, related-to, supersedes} ·
`lenses` {citizen, professional, researcher} · `references` (BibTeX keys) · `created` · `updated`.

Required body sections (multi-lens, single source):
`## In one sentence (citizen)` · `## In practice (professional)` · `## Formal definition (researcher)`
· `## Example` · `## Counterexample` · `## Frequently misunderstood` · `## Practical implications`
· `## Visual` · `## See also`.

One concept = one file = one graph node. Lenses are views, never separate files.
