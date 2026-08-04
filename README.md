# sreyadox.github.io

My documentation portfolio: case studies of public work I've published,
with links and on-page verification for each.

Built with Sphinx (reStructuredText) and deployed by GitHub Actions:
every push verifies `llms.txt` is in sync with the case studies, builds
the site with warnings-as-errors, checks external links, and publishes
to GitHub Pages on merge to `main`. See
[.github/workflows/build-deploy.yml](.github/workflows/build-deploy.yml).

## llms.txt

[`source/_extra/llms.txt`](source/_extra/llms.txt) is a hand-curated
index of this site for LLMs, following the
[llms.txt](https://llmstxt.org/) convention. Sphinx copies it to the
site root verbatim, which means the build and link checker never read
it — so [`scripts/check_llms_txt.py`](scripts/check_llms_txt.py) runs in
CI to catch a case study that was added, renamed, or removed without
updating it.

Adding a case study? Add it to `llms.txt` too, or CI will tell you.

## Local build

```bash
pip install -r requirements.txt
sphinx-build -b html source _site
```
