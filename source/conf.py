project = "Sreya Dutta"
author = "Sreya Dutta"
copyright = "2026, Sreya Dutta"

extensions = []

html_theme = "furo"
# No dash or em dash here: Furo appends this to each page title with its
# own " - " separator, so punctuation inside it collides in the <title>.
html_title = "Sreya Dutta's Career Portfolio"
html_static_path = []

# Copied verbatim to the site root. Holds llms.txt, which scripts/
# check_llms_txt.py keeps in sync with the case studies.
html_extra_path = ["_extra"]

exclude_patterns = ["_build"]

# Oracle's docs site sometimes rejects automated requests; the linkcheck
# job stays useful for everything else.
#
# Medium returns 403 to every automated request, so its links always fail
# linkcheck even though they resolve fine in a browser. Ignoring them
# keeps the report free of known false positives — if the whole report is
# noise, nobody reads it.
linkcheck_ignore = [
    r"https://.*\.?medium\.com/.*",
]
linkcheck_timeout = 15
