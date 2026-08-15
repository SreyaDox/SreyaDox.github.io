About Me
========

I am a technical writer and content strategist with 25+ years of
experience. I work at Oracle as a Lead Principal Technical Writer, where
I document OCI AI Services like Vision and Big Data, publish
cross-product reference architectures and solution content for the
Architecture Center, and build AI-assisted authoring workflows.

Where I started
---------------

I studied computer science in college (B.Sc. Computer Science, St. Ann's
College for Women, Osmania University, 1997 to 2000), where I learned to
program in C, COBOL, and BASIC. Alongside it I completed a one-year
Diploma in Multimedia and Graphic Design (1999–2000), learning graphic
design in Adobe Photoshop and Illustrator, 2D animation and scripting in
Flash, and 3D animation in 3DS Max. I later completed an M.Sc. in
Information Technology (2001–2004).

Those two tracks, programming and design, came together in my first job.

Building eLearning from scratch, 2000–2005
-------------------------------------------

At Sankhya Infotech I worked as an eLearning developer and instructional
designer, eventually as a project leader, building over 200 hours of
training for aviation clients including Airbus Industrie and Snecma
Moteurs. The courses were used by global flight crews, maintenance
personnel, pilots, and dispatchers. I built the courseware in Macromedia
Authorware and Flash.

For a Finnair course prototype I built the course interface in Flash 5
using its scripting language. Flash 5 had no ready-made components: no
lists, no menus, nothing out of the box. My colleagues and I found code
samples, customized them through scripting, and built every course
interaction and the navigation bar from scratch.

I also designed an XML database to send and retrieve course tracking
statuses to a learning management system (LMS), and built a randomized
question and testing tool on top of it, compliant with the
`AICC <https://www.aicc.org/>`_ and `SCORM
<https://en.wikipedia.org/wiki/Sharable_Content_Object_Reference_Model>`_
standards.

From training to documentation, 2005 onward
--------------------------------------------

After Sankhya I spent close to three years at Progress Software
designing enterprise software elearning courses for Sonic Software, then
joined Oracle in 2008 as a curriculum developer for the Oracle
Communications global unit. I moved into a combined Information
Developer role working on both curriculum and documentation for Oracle
Fusion ERP Cloud Project Management. I transitioned to a manager and led
a documentation team and curriculum team of size 8-10, including hiring
experienced writers in India and US. I was instrumental in designing
interview activities for the college hiring program and managed a team
with a wide range of experience levels.

After I moved to the US in the Bay Area, CA, I spent two years at Clover
(Fiserv) writing API documentation for developers, then returned to
Oracle in 2021.

I spent close to ten years in instructional design before documentation
became my main role. My design training came in handy when our graphics
team was cut, I taught myself Figma and now build the architecture
diagrams our customers download and customize. I have recently also
created an architecture diagram skill in addition to AI DITA
documentation skills.

What instructional design taught me about writing for models
--------------------------------------------------------------

Good curriculum and good model instructions need the same things:
understanding your audience, clear objectives, minimal scaffolding, and
iterative refinement. Excess complexity reliably produces worse outcomes
in both. The job is to deeply grasp complex subjects and transform the
subject into easily learnable content focused on accomplishing the
business goal.

This influences my approach to prompts and skills while working with an
LLM to be minimal and focused on the goal. Start with what the model
needs to know, test it, prune it, refine it. My first blog on this
subject is `Building AI Workflows and Minimalism
<https://sreyad.medium.com/building-ai-workflows-and-minimalism-f6ae7206f627>`_.

There is a more specific overlap than method, and it is the reason the
move from curriculum to documentation felt like continuing the same work
rather than changing fields. Instructional design chunks content by
information type: you classify what you are teaching as a concept, a
procedure, a process, a fact, or a principle, because each one has to be
explained, sequenced, and assessed differently. DITA types topics the
same way, as `concept, task, and reference
<https://dita-lang.org/dita/archspec/base/information-typing>`_.

The two line up meaningfully to achieve the same goal. Both originate
from the `structured writing
<https://en.wikipedia.org/wiki/Structured_writing>`_ research of the
1960s, particularly Robert Horn's Information Mapping, which derived its
types from how people process different kinds of knowledge.

Deciding whether something is a concept or a procedure is the same
judgment in a course outline and in a DITA map, and it is the judgment
that decides where one chunk ends and the next begins. Which is why the
chunking question interests me: the boundary that retrieval research
keeps landing on is the one instructional design settled decades ago. I
built this decision making into my DITA skill.

Why this history matters
------------------------

I have coded in some form throughout my career: course interfaces, XML
data exchange, install guides written by provisioning my own cloud
environments, internal tools. That foundation, plus years working
embedded inside engineering teams and their development processes, is
one of my strong points. In Fusion Apps, information developers
(writers) were deeply embedded in the scrum teams. Our role ranged from
reviewers & approvers of Functional Design documents, UX writing,
product documentation design and publishing, What's New, release notes,
API documentation (SOAP & REST), and curriculum. We had to demonstrate
product knowledge alongside working with various SME roles to be able to
support the full gamut of deliverables for a product and feature.

In Oracle Architecture Center, product knowledge can be more challenging
because of the 'cross-product' nature of the solution architectures. It
requires context switching between domains and products and working with
SMEs to ensure what we document, diagram, and publish are of
high-quality and valuable to customers. This content is directly revenue
generating outside of support revenue to support field personnel and
sell cross-product solutions as customers would use them not as
individual products. This broadened my perspective and understanding of
how customers use Oracle and our partner products in real
implementations and not in isolated product boundaries.

We had multiple reorgs over the years and in one of the early ones I
jumped into Analytics to cover the gap after the loss of our analyst. I
learned Adobe Analytics and Oracle Analytics Cloud and published traffic
metrics. I also looked at search keywords and shared with our internal
partners to help them understand what people were searching for. I also
looked at revenue generated from our call-to-action buttons and it was
direct evidence of our site traffic and the button feature generating
clicks to a trial deployment which sometimes translated into a paid
subscription. It was exciting that our content was visibly contributing
to revenue.

Through the reorgs, we were given access to AI tools in September 2025.
I started by generating each DITA topic manually with Codex and Cline,
adding product and service name references (conkeyrefs) one at a time.
From there I expanded into skills with progressive disclosure and a more
mature workflow. When I needed to scale, I built in tests and
validations. And I learned throughout from a genuinely smart technical
writing community solving the same problems I was.

That progression, manual first, then minimal instructions, then
structure, then tests, is what my `AI Workflow Design series
<https://sreyad.medium.com/>`_ documents, and what the
:doc:`SwiftPay DITA workflow <case-studies/swiftpay-dita-workflow>`
demonstrates in code.

What I'm curious about next
---------------------------

Working in `DITA
<https://dita-lang.org/dita/introduction/dita-release-overview>`_
every day, I keep running into a question I cannot answer cleanly: does
DITA's explicit semantic markup actually improve how well a model
retrieves and acts on content, or does the benefit disappear once
everything is embedded? Retrieval quality looks like a markup problem
before it is a model problem, and I would like to know how far that
holds. I am :doc:`working through the research on it here
<dita-and-retrieval>`.
