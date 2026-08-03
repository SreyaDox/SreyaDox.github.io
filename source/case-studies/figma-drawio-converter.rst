SVG-to-draw.io Converter (Figma Make)
=====================================

**Artifact:** the editable draw.io diagrams available from the *Download
Diagram* button below each architecture diagram on solutions I publish —
for example, `Provision Private Connectivity from Oracle Integration to
Oracle AI Database@AWS
<https://docs.oracle.com/en/solutions/private-connectivity-oi-db-at-aws/index.html>`_.
The converter itself is an internal authoring tool; what ships publicly
is its output.

The problem
-----------

Oracle Architecture Center publishes architecture diagrams customers want
to adapt for their own designs. A static SVG or PNG forces customers to
redraw from scratch; the alternative was manually rebuilding each diagram
in draw.io, which does not scale across a growing catalog.

What I built
------------

I built an app in Figma Make that converts the SVG architecture
diagrams into editable draw.io files as part of my authoring workflow.
The converted files ship with each solution and are served by the
*Download Diagram* button below the diagram, so customers get an
editable file that matches the published architecture.

Why it matters
--------------

The tool is internal, but its output is public and verifiable: open a
solution page, click *Download Diagram* below the diagram, and open the
file in draw.io. Every editable diagram a customer downloads from my
solutions came through this converter. It is also how I approach
documentation generally — when the manual path does not scale, build
the tool.
