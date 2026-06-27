#!/usr/bin/env bash
# Build every output format from the single source of truth.
set -euo pipefail
cd "$(dirname "$0")/.."
echo "[BAFLP] validating..."; python3 tests/structure_test.py; python3 tests/frontmatter_test.py
echo "[BAFLP] rendering website..."; quarto render
echo "[BAFLP] rendering PDF/DOCX/EPUB..."
quarto render --to pdf  || echo "  (pdf skipped: install tinytex)"
quarto render --to docx || echo "  (docx skipped)"
quarto render --to epub || echo "  (epub skipped)"
echo "[BAFLP] done -> build/_site"
