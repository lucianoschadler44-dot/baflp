#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
num="${1:?usage: new-paper.sh <NNNN> <slug>}"; slug="${2:?provide a slug}"
dir="research/working-papers/WP-${num}-${slug}"
mkdir -p "$dir/assets"
sed "s/WP-XXXX/WP-${num}/" templates/working-paper.qmd > "$dir/index.qmd"
echo "created $dir"
