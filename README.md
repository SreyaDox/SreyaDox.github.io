# sreyadox.github.io

My career portfolio: case studies of public work I've published, with
links and on-page verification for each.

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

## Preview before you push

Pushing to `main` deploys the live site, so preview and check locally
first.

Install the dev dependencies once:

```bash
pip install -r requirements-dev.txt
```

**Look at it.** Live preview at http://127.0.0.1:8000, rebuilding and
reloading the browser as you edit. Ctrl-C to stop.

```bash
./scripts/preview.sh
```

**Check it will pass CI.** Runs the same gates as
[build-deploy.yml](.github/workflows/build-deploy.yml), in the same
order: the `llms.txt` sync check, the build with warnings-as-errors, and
linkcheck. Exits non-zero if a push would fail.

```bash
./scripts/check.sh
```

Linkcheck reports without blocking, matching CI. Medium is excluded via
`linkcheck_ignore` because it returns 403 to all automated requests.

## Plain build

```bash
pip install -r requirements.txt
sphinx-build -b html source _site
```
