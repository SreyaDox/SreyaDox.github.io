#!/usr/bin/env bash
# Run the same gates CI runs, in the same order, before pushing.
# Mirrors .github/workflows/build-deploy.yml.
#
#   ./scripts/check.sh
#
# Linkcheck reports but does not fail, matching continue-on-error in CI.
set -uo pipefail
cd "$(dirname "$0")/.."

fail=0

echo "==> llms.txt in sync with the case studies"
if ! python3 scripts/check_llms_txt.py; then
  fail=1
fi

echo
echo "==> Build (warnings are errors)"
if ! python3 -m sphinx -W -b html source _site; then
  fail=1
fi

echo
echo "==> External links (reports only, does not block)"
python3 -m sphinx -b linkcheck source _linkcheck || true
if [ -f _linkcheck/output.txt ] && [ -s _linkcheck/output.txt ]; then
  echo "--- broken or redirected links ---"
  cat _linkcheck/output.txt
fi

echo
if [ "$fail" -ne 0 ]; then
  echo "FAILED — CI would reject this push."
  exit 1
fi
echo "PASSED — safe to push. Preview it with ./scripts/preview.sh"
