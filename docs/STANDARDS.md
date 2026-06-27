# Engineering Standards

- Every folder has a `README.md` (Purpose, Contents, Dependencies, Future evolution).
- Every concept has complete YAML frontmatter; CI enforces it (`tests/frontmatter_test.py`).
- Every script is documented and lives in `scripts/`. No undocumented scripts.
- No broken links, no build warnings. Diagrams are code (Mermaid/SVG), not opaque images.
- References are centralised in `bibliography/`; never duplicated inline.
