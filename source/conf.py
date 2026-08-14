project = "Sreya Dutta"
author = "Sreya Dutta"
copyright = "2026, Sreya Dutta"

extensions = []

html_theme = "furo"
# No dash or em dash here: Furo appends this to each page title with its
# own " - " separator, so punctuation inside it collides in the <title>.
html_title = "Sreya Dutta's Documentation Portfolio"
html_static_path = []

# Copied verbatim to the site root. Holds llms.txt, which scripts/
# check_llms_txt.py keeps in sync with the case studies.
html_extra_path = ["_extra"]

exclude_patterns = ["_build"]

# Oracle's docs site sometimes rejects automated requests; the linkcheck
# job stays useful for everything else.
linkcheck_ignore = []
linkcheck_timeout = 15
