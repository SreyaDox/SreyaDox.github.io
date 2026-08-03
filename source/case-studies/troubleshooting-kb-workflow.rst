Troubleshooting Knowledge Workflow (Oracle, internal)
=====================================================

.. note::

   This workflow is internal to Oracle, so there is no public artifact
   to link. It is described here because the design — one semantic
   structure serving human readers, external LLMs, and an internal bot
   — is central to how I approach content. Its public analog is the
   :doc:`SwiftPay DITA workflow <swiftpay-dita-workflow>`.

The problem
-----------

Support teams accumulate knowledge articles in a knowledge management
platform, written free-form. The knowledge is real, but the structure
is not: a reader, an LLM, or a support bot consuming those articles
cannot reliably tell the problem from its cause from its fix.

What I built
------------

An AI workflow that converts support knowledge articles into DITA
troubleshooting topics. The troubleshooting template makes the
semantics explicit, and the workflow reads each source article and
decides what belongs where:

- ``<title>`` and ``<shortdesc>`` — the problem and its context
- ``<cause>`` — the documented root cause of the issue
- ``<remedy>`` — the steps that resolve the problem

The output is published with this explicit markup so that external
LLMs can consume it reliably, and so the internal Slack support bot
can ground its answers in structured cause-and-remedy pairs instead of
free-form prose.

Why it matters
--------------

Retrieval quality is a markup problem before it is a model problem.
When the cause and the fix live in explicitly labeled elements, a bot
does not have to guess which sentence is the solution — and the same
structure that helps the machine also helps the human skimming for the
remedy. This is the dual-interface principle in practice: don't write
content twice for two audiences; structure it once so both can use it.
