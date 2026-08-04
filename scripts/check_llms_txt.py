#!/usr/bin/env python3
"""Verify llms.txt lists every case study, and only real ones.

Sphinx copies llms.txt verbatim via html_extra_path, so neither the HTML
build nor linkcheck ever reads it. Without this check it would quietly go
stale the first time a case study is added or renamed — and a portfolio
that claims editorial rigor cannot afford a stale index of itself.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LLMS_TXT = ROOT / "source" / "_extra" / "llms.txt"
CASE_STUDIES = ROOT / "source" / "case-studies"
BASE_URL = "https://sreyadox.github.io/case-studies/"


def main() -> int:
    pages = {path.stem for path in CASE_STUDIES.glob("*.rst")}
    listed = set(re.findall(rf"{re.escape(BASE_URL)}([\w-]+)\.html",
                            LLMS_TXT.read_text()))

    missing = sorted(pages - listed)
    stale = sorted(listed - pages)

    if not missing and not stale:
        print(f"OK: llms.txt lists all {len(pages)} case studies.")
        return 0

    if missing:
        print("Case studies missing from llms.txt:")
        for name in missing:
            print(f"  - {name} ({BASE_URL}{name}.html)")
    if stale:
        print("llms.txt links case studies that no longer exist:")
        for name in stale:
            print(f"  - {name}")
    print(f"\nUpdate {LLMS_TXT.relative_to(ROOT)} to match "
          f"{CASE_STUDIES.relative_to(ROOT)}/.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
