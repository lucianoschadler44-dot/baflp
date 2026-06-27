# Contributing

1. **Never work on `main`.** Branch: `feature/<area>` (e.g. `feature/ontology`, `feature/model-law`).
2. **Conceptual change?** Open an RFC in `core/rfcs/` first (use `0000-template.md`).
3. **Engineering change?** Open a PR using `PULL_REQUEST_TEMPLATE.md` (purpose, files, reason,
   impact, dependencies, risk, rollback).
4. Run `scripts/validate.sh` before pushing. CI must be green.
5. Conceptual PRs require Chief Research Architect review; merges require Chief Editor approval.
6. One concept = one file. Never duplicate a definition; reference the canonical object instead.

See `docs/NAMING.md` and `docs/STANDARDS.md`.
