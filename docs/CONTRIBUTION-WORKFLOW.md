# Contribution Workflow
1. Branch from `main`: `feature/<area>`.
2. Conceptual change → RFC in `core/rfcs/` (Architect review, Chief Editor approval).
3. Engineering change → PR with the full template.
4. `scripts/validate.sh` green, CI green.
5. Squash-merge with a descriptive message; tag releases with SemVer.
