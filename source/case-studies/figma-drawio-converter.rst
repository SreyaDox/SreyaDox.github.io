SVG-to-draw.io Converter (Figma Make)
=====================================

**Artifact:** the "download diagram" button on Oracle Architecture Center
solutions I publish — for example, `Provision Private Connectivity from
Oracle Integration to Oracle AI Database@AWS
<https://docs.oracle.com/en/solutions/private-connectivity-oi-db-at-aws/index.html>`_.

The problem
-----------

Oracle Architecture Center publishes architecture diagrams customers want
to adapt for their own designs. A static SVG or PNG forces customers to
redraw from scratch; the alternative was manually rebuilding each diagram
in draw.io, which does not scale across a growing catalog.

What I built
------------

I built an app in Figma Make that converts our published SVG diagrams
into editable draw.io files. The converted files are what the download
button below each diagram serves, so customers get an editable diagram
that matches the published one.

Why it matters
--------------

This is my tooling running in production on Oracle's public
documentation site, and it is verifiable in one click: open the solution
page, press the download button under the diagram, and open the file in
draw.io. It is also how I approach documentation generally — when the
manual path does not scale, build the tool.
