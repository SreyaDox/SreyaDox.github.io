# sreyadox.github.io

My documentation portfolio: case studies of public work I've published,
with links and on-page verification for each.

Built with Sphinx (reStructuredText) and deployed by GitHub Actions:
every push builds the site with warnings-as-errors, checks external
links, and publishes to GitHub Pages on merge to `main`. See
[.github/workflows/build-deploy.yml](.github/workflows/build-deploy.yml).

## Local build

```bash
pip install -r requirements.txt
sphinx-build -b html source _site
```
