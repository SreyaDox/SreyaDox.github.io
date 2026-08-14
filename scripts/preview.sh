#!/usr/bin/env bash
# Live preview at http://127.0.0.1:8000 — rebuilds and reloads the browser
# whenever a source file changes. Ctrl-C to stop.
#
#   pip install -r requirements-dev.txt   # once
#   ./scripts/preview.sh
#
# This is for looking at the site. To check whether a push will pass CI,
# run ./scripts/check.sh instead.
set -euo pipefail
cd "$(dirname "$0")/.."

exec python3 -m sphinx_autobuild source _site \
  --port 8000 \
  --host 127.0.0.1 \
  --open-browser
