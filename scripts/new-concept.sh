#!/usr/bin/env bash
# Scaffold a new knowledge object from the canonical template.
set -euo pipefail
cd "$(dirname "$0")/.."
slug="${1:?usage: new-concept.sh <slug> \"Title\"}"; title="${2:?provide a title}"
dest="core/concepts/${slug}.md"
[ -e "$dest" ] && { echo "exists: $dest"; exit 1; }
sed -e "s/Concept Title/${title}/" -e "s/concept-title/${slug}/" templates/concept.md > "$dest"
echo "created $dest  (remember: doctrine requires an accepted RFC)"
