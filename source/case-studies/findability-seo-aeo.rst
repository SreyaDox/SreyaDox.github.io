Findability by Design: SEO and AEO at the Oracle Architecture Center
=====================================================================

**Artifact:** `Oracle Architecture Center
<https://docs.oracle.com/solutions/>`_ reference architectures and
solution playbooks, several of which name me in their Acknowledgments.

The problem
-----------

Solution content only earns its cost if the people who need it can find
it. Architecture Center content competes for attention against vendor
blogs, partner posts, and general search results, and the reader is
usually mid-problem: they have a specific architecture question and no
patience for a landing page that answers a different one.

The usual failure is publishing a large, well-written document that
ranks for nothing in particular, because it is one URL trying to be
about eight topics at once.

What we did
-----------

Findability was a design constraint, not a post-publication activity,
and it was built in partnership with marketing rather than handed to
them afterward.

**Structure that produces addressable content.** The DITA templates for
reference architectures and solution playbooks are modular. Each
content piece publishes to its own URL under a common basepath, so a
solution is not a single monolithic page but a set of individually
addressable topics. That means a search engine has something specific
to rank for a specific query, and a reader lands on the piece that
answers their question rather than on a document containing it.

**Metadata used deliberately.** DITA's ``<shortdesc>``, wrapped in
``<abstract>``, is what summarizes each publication to the search
engine. Writing that element well is search work: it is the summary
that gets surfaced, and it is authored as part of the topic rather
than bolted on as a meta tag afterward.

**Coordinated amplification.** Marketing stakeholders led timed PR
announcements linking to the published content, reinforced by LinkedIn
and social promotion. Modularity made this more effective, not less,
because a campaign could point at exactly the relevant topic.

**Measurement.** I am the metrics point of contact for our content,
using Adobe Analytics and Oracle Analytics Cloud to evaluate
performance, map friction points in content journeys, and publish
dashboards that connect content to adoption, sales enablement, and
revenue. Findability is a claim you can check, so I check it.

From SEO to AEO
---------------

The same properties that made this content rank now make it usable to
answer engines and agents, which is the more interesting half.

Modular topics with clean URLs are already chunked at a sensible
boundary, so a retrieval system does not have to guess where one idea
ends. A well-authored ``<shortdesc>`` is a precision anchor that helps
retrieval select the right topic before the model reads the body.

Semantic markup goes further than retrieval, into execution. DITA
distinguishes a ``<uicontrol>`` from a code phrase from a command from
a variable, and those are different kinds of thing to act on. When an
agent reads "click **Save**" as marked-up UI control rather than as
bolded prose, the action target is explicit rather than inferred. An
agent executing a procedure needs to know which token is a button,
which is a literal command to run, and which is a placeholder the user
must substitute. Markup that already encodes those distinctions gives
that away for free.

Why it matters
--------------

Documentation findability and machine-readability turn out to be the
same engineering problem approached from two directions. Structure the
content into addressable, semantically explicit pieces and you get
search ranking, retrieval precision, and agent execution from one body
of work.

The corollary is that this is not a formatting preference. Content that
is one long page of undifferentiated prose is hard to rank, hard to
retrieve against, and ambiguous to act on — and no amount of promotion
downstream fixes a structural problem upstream.
