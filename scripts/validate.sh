#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
python3 tests/structure_test.py
python3 tests/frontmatter_test.py
python3 tests/yaml_empty_test.py
if command -v lychee >/dev/null 2>&1; then
  lychee --config tools/lychee.toml './**/*.md' './**/*.qmd' || true
else
  echo "[BAFLP] lychee not installed locally; link check runs in CI."
fi
python3 tests/readability_test.py
echo "[BAFLP] validation OK"
