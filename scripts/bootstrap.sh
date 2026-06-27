#!/usr/bin/env bash
# One-shot local bootstrap: validate structure and (optionally) render if Quarto is present.
set -euo pipefail
cd "$(dirname "$0")/.."
python3 tests/structure_test.py && python3 tests/frontmatter_test.py
command -v quarto >/dev/null 2>&1 && quarto render || echo "Quarto not found locally; CI will render."
