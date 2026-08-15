DITA and Retrieval: An Open Question I'm Working On
=====================================================

This page is research in progress rather than finished work. I am
keeping it public because the question is genuinely unresolved and I
would rather be corrected than quietly wrong.

The question
------------

Most content reaching an LLM today is Markdown, or HTML converted to
Markdown. That format carries almost no semantics: ``**Save**`` means
bold, not "this is a UI control." Meanwhile DITA has spent two decades
encoding exactly those distinctions, and the `DITA 1.3 specification
<https://docs.oasis-open.org/dita/dita/v1.3/dita-v1.3-part1-base.html>`_
defines a typed vocabulary for them — concepts, tasks, and references
at the topic level, and inside a task, elements that separate a
prerequisite from a step from a result, or a UI control from a command
from a variable.

So the question I keep coming back to: **does that explicit markup
measurably improve retrieval, or does it stop mattering once the
content is embedded?**

Not rhetorically. I think the honest answer right now is "partly, and
it depends where in the pipeline you look."

Why DITA is an interesting test case
------------------------------------

Four properties look relevant to retrieval, and they are properties of
the authoring discipline rather than of any tool:

- **Topics are chunked at authored boundaries.** A DITA topic is
  self-contained by design, so the chunk boundary was decided by
  someone who understood the content, not by a character count. The
  Architecture Center content I publish works this way in production:
  reference architectures and solution playbooks are chunked at the
  page level, each page maps to a concept or task topic in DITA, and so
  the retrieval chunk and the authored topic are the same boundary. No
  splitter runs over it afterward.
- **``<shortdesc>`` is a summary written for the topic.** It behaves
  like a precision anchor: retrieval can select on it before the model
  reads the body.
- **Relationship tables are an explicit graph.** Related topics are
  declared, not inferred from co-occurrence.
- **Reuse is by ID.** Where a component is referenced tells you how
  broadly it applies, which is signal that duplication destroys. Reuse
  also forces self-containment: a topic that will be dropped into
  contexts you have not seen yet cannot say "as described above" or
  inherit meaning from its surroundings. That is the same property a
  retrieved chunk needs, since it arrives with no neighbors. Designing
  for reuse and designing for retrieval are close to the same problem —
  `SCORM <https://scorm.com/scorm-explained/>`_ reached it from the
  eLearning side with the sharable content object, assembled by a
  manifest much as DITA topics are assembled by a map.

Michael Iantosca argues the strong form of this in `DITA = Context!
<https://medium.com/@nc_mike/dita-context-ee2b24797a28>`_: that context
is "structured meaning, governed classification, explicit
relationships, and computable knowledge," and that vector chunking
"discards structure, breaks semantic boundaries." His `piece on
deterministic and agentic architectures
<https://medium.com/@nc_mike/deterministic-and-agentic-ai-architectures-for-technical-documentation-3fb2956a1334>`_
extends it into an enterprise architecture built on semantic markup,
knowledge graphs, and validation.

What the evidence supports, and what it doesn't
-----------------------------------------------

The case for structure at the pipeline level is reasonably strong.
Chunking studies consistently find that boundaries aligned to logical
topics beat fixed-size splitting, and the industry has converged on
that independently of DITA — the `2026 chunking benchmarks
<https://www.firecrawl.dev/blog/best-chunking-strategies-rag>`_ and
`production RAG guidance
<https://www.premai.io/blog/rag-chunking-strategies-the-2026-benchmark-guide/>`_
both land there. `Ontology-grounded retrieval
<https://www.thecontentwrangler.com/p/what-is-ontology-grounded-retrieval>`_
and `GraphRAG <https://microsoft.github.io/graphrag/get_started/>`_ go
further, anchoring retrieval in declared relationships instead of
statistical similarity, which is close to what a DITA relationship
table already is. And `metadata is increasingly treated as the semantic
layer AI actually interacts with
<https://www.firstsanfranciscopartners.com/blog/metadata-is-the-new-gold-standard-for-ai/>`_.

The honest counterweight is that the model does not see the XML. The
Content Wrangler puts it directly: `AI may not need XML in the prompt
window, but it still needs structured content
<https://www.thecontentwrangler.com/p/ai-may-not-need-xml-in-the-prompt>`_.
The structure does its work upstream, in how content is chunked,
selected, and related — not as tags in the context window. Which means
the benefit is real but indirect, and it can be replicated by any
format with the same discipline applied. DITA is the most mature
implementation of that discipline, not the only possible one.

Where I think it gets interesting: execution
---------------------------------------------

Retrieval is only half of it. An agent that has retrieved the right
procedure still has to act on it, and there the distinctions matter
again in a way that summarization does not smooth over. Knowing which
token is a button to click, which is a literal command to run, and
which is a placeholder the reader must substitute is the difference
between executing a procedure and guessing at it. Bolded prose does not
encode that. Typed markup does.

This is the part I have not seen tested properly, and it is what I most
want to find out.

Adjacent work worth watching
-----------------------------

Several efforts are converging on machine-readable documentation from
different directions:

- `AFDocs <https://afdocs.dev/>`_, an open spec defining checks for
  agent-readable documentation, and the `Agent Score
  <https://buildwithfern.com/agent-score>`_ tool that grades a docs site
  against it.
- The `llms.txt specification <https://llmstxt.org/>`_ for giving models
  a curated index of a site. This portfolio publishes one.
- Dachary Carey's `agent reading test
  <https://dacharycarey.com/2026/04/06/designing-agent-reading-test/>`_,
  which found that agents cannot reliably self-report what they read —
  a useful caution for anyone evaluating this by asking a model how it
  did.

Related work of mine
--------------------

- :doc:`Findability by design <case-studies/findability-seo-aeo>` — the
  same structure serving search ranking and retrieval.
- :doc:`Troubleshooting knowledge workflow
  <case-studies/troubleshooting-kb-workflow>` — explicit cause and
  remedy markup so a support bot can ground its answers.
- :doc:`SwiftPay DITA workflow <case-studies/swiftpay-dita-workflow>` —
  the conversion pipeline, public and runnable.
