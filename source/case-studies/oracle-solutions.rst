Solution Architectures Published (Oracle Architecture Center)
=============================================================

The four solutions below are published on the Oracle Architecture
Center and were produced with an internal AI authoring workflow I
built. The workflow itself is internal to Oracle; its public analog is
the :doc:`SwiftPay DITA workflow <swiftpay-dita-workflow>`, which
demonstrates the same design openly.

How each piece is produced
--------------------------

- **Diagrams:** I create every architecture diagram by hand in Figma,
  based on Oracle's brand standards and diagram templates. Out of that
  hands-on work with Oracle's branded library objects, I have written a
  first draft of an architecture diagram skill that encodes the
  conventions I apply by hand. It is in testing now, and I expect to
  keep iterating on it as I find where it holds up and where it
  doesn't.
- **Review:** I take the SME content and review it twice — manually,
  and through the AI workflow, which connects the diagram to the
  content to find gaps between what the architecture shows and what
  the text says.
- **DITA generation:** the workflow generates the DITA source and
  checks it against Oracle's style guide, terminology, and policies,
  staging it for manual review.
- **Authoring and publishing:** I author the reviewed DITA in Oxygen
  and publish to the Architecture Center.

The AI accelerates the mechanical steps; the diagrams, the editorial
judgment, and the final authoring are mine.

.. toctree::
   :maxdepth: 1

   multicloud-connectivity
   hpc-platform
   video-knowledge-agents
   network-topology
