---
name: portfolio-site
description: >-
  Build, edit, and deploy Sreya's documentation portfolio at
  sreyadox.github.io. Use this skill for ANY work on this site — adding or
  revising a case study, editing the landing page, updating llms.txt,
  changing the Sphinx config or CI pipeline, or fixing how a project is
  described — even if the request is just "add my new project to the
  portfolio" or names a repo, blog post, or published artifact to feature.
  Critical: this site makes public claims about her work, so the accuracy
  rules below (internal vs. public work, what may be linked) matter more
  than anything else here.
---

# Portfolio site (sreyadox.github.io)

A Sphinx site presenting case studies of Sreya's work. Live at
https://sreyadox.github.io/, source at
https://github.com/SreyaDox/SreyaDox.github.io.

Why it exists: her evidence was real but scattered across Oracle docs
pages, a Write the Docs guide, a blog series, and a GitHub repo.
Searchable is not presented — this site is the curation layer, and its
own build pipeline is part of the evidence.

## Accuracy rules — the highest-stakes part of this repo

Employers read this site. A claim that overstates what is public is worse
than no claim, and CI cannot catch it. Get these right:

- **Internal work is describable, never linkable.** Her Oracle DITA
  automation, the troubleshooting knowledge workflow, and the Figma Make
  converter are internal tools. Describe them, label them internal, and
  link a public analog (usually the SwiftPay repo). Never imply a public
  artifact exists.
- **The SVG-to-draw.io converter is internal; its *output* is public.**
  What ships publicly is the editable draw.io file behind the *Download
  Diagram* button on Oracle solution pages. Never write that the
  converter is publicly available or "running in production" on the site.
- **SwiftPay is a fictional platform** she created for public
  demonstration. Keep that explicit; it is not an Oracle production
  system.
- **Clover documentation cannot be linked.** She wrote it in 2019-2021,
  but five years of edits by others mean she cannot claim current pages.
- **Oracle Architecture Center authorship is verifiable** — her name is
  in each solution's Acknowledgments. Point readers there rather than
  asserting authorship.
- Every factual claim must trace to something she has stated or to the
  fact base in the my-job-search repo. Do not infer, upgrade, or round up.

## Adding or revising a case study

1. Confirm the facts with her, and note whether the artifact is public.
2. Write `source/case-studies/<slug>.rst` using the structure below.
3. Add it to the `toctree` in `source/index.rst` (or in
   `source/case-studies/oracle-solutions.rst` if it is another Oracle
   Architecture Center solution).
4. Add it to `source/_extra/llms.txt` in the section that fits — CI fails
   the build otherwise.
5. Build, verify, commit, push, confirm the deploy:

   ```bash
   python3 scripts/check_llms_txt.py
   python3 -m sphinx -W -b html source _site
   git add -A && git commit && git push
   gh run list --limit 1
   ```

6. If the piece is new evidence, also record it in the my-job-search
   repo's `.claude/skills/resume-docx/references/evidence.md` so resume
   planning can cite it. New *facts* about her work belong in that repo's
   generic resume first — it is the fact base for both repos.

## Case study structure

Keep the shape consistent; readers compare pieces across the site.

```rst
Title (Context)
===============

**Artifact:** link, or a note that the work is internal.

The problem
-----------
What was wrong or missing, in the reader's terms.

What I built / The work
-----------------------
Her role and process, concretely.

Why it matters
--------------
What the piece demonstrates about how she works.
```

Internal pieces open with a `.. note::` labeling them internal and
linking the public analog. Cross-reference other case studies with
`:doc:` so the `-W` build catches broken links.

## Voice

First person, plain register, and the same rules as her resumes: one idea
per sentence, concrete nouns over abstractions, no marketing vocabulary
("leveraging", "spanning", "high-value"), and no em-dashes in prose.
Prefer stating what she did and letting the reader draw the conclusion.
The strongest lines on this site are the plainest — "The AI accelerates
the mechanical steps; the diagrams, the editorial judgment, and the final
authoring are mine."

## Site mechanics

- **Build:** `python3 -m sphinx -W -b html source _site` (warnings are
  errors, locally and in CI).
- **Theme:** Furo, no custom CSS. Keep it that way unless she asks.
- **`source/_extra/`** is copied verbatim to the site root by
  `html_extra_path`; `llms.txt` lives there, which is why the CI check
  exists — the build and linkcheck never read it.
- **CI** (`.github/workflows/build-deploy.yml`): llms.txt check → build
  with `-W` → external linkcheck (non-blocking, since other sites are
  outside our control) → deploy to Pages on merge to `main`.
- **Deploy** is automatic on push to `main`. Verify with `gh run list`
  and a `curl` against the live URL rather than assuming.

## Keep out of this repo

It is public. Job-search strategy — which artifact to lead with for which
employer, gap analysis, per-role positioning — belongs in the private
my-job-search repo's evidence inventory, not here. This repo presents the
work; that one decides how to pitch it.
