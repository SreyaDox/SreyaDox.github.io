SwiftPay DITA Conversion Workflow (AI Workflow Design)
======================================================

**Artifact:** `github.com/SreyaDox/swiftpay-dita-workflow
<https://github.com/SreyaDox/swiftpay-dita-workflow>`_ — a public,
runnable AI workflow, companion to my `AI Workflow Design blog series
<https://sreyad.medium.com/>`_.

The problem
-----------

Documentation teams receive source content from product managers,
engineers, and support teams in whatever format those teams work in —
Word documents, Confluence pages, JIRA tickets. Converting it into
well-structured DITA topics is repetitive, judgment-heavy work: classify
the topic type, restructure the content, validate the markup, catch
style and terminology issues.

What I built
------------

A Claude Code agent workflow that takes raw source content in any of
those formats and produces DITA XML topics (concept, task, reference, or
troubleshooting), validated and staged for human review. SwiftPay is a
fictional payment platform I created so the workflow could be
demonstrated publicly with realistic content.

The design principles are the point as much as the output:

- **Minimal instructions** — the skills contain only what the model
  doesn't already know; existing DITA knowledge is used, not re-taught.
- **Repo structure as metadata** — folder and file names carry context
  for both the model and the team.
- **Skills as documentation** — the skills, agent instructions, and
  README are the only spec there is.
- **A human-review gate** — converted output lands in a pending-review
  folder; the model never publishes.
- **Examples over templates** — good patterns and antipatterns guide
  output more precisely than rigid templates, and reviewing outputs
  grows the example set over time.

Why it matters
--------------

My production DITA automation work at Oracle is internal and cannot be
shown. This repo is the public demonstration of the same
workflow-design approach — and it is runnable: clone it, open Claude
Code, and convert a sample document yourself. The design principles come
from instructional design as much as engineering: clear objectives,
minimal scaffolding, iterative refinement against real examples.
