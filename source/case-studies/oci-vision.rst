OCI Vision Service Documentation (Oracle Cloud Infrastructure)
==============================================================

**Artifact:** `OCI Vision documentation
<https://docs.oracle.com/en-us/iaas/Content/vision/using/home.htm>`_,
published on Oracle Cloud Infrastructure docs.

The work
--------

I document OCI Vision, Oracle's AI image analysis service that enables
developers to detect objects, classify scenes, extract text, and analyze
images using pretrained and custom models. The documentation covers the
full developer surface: service concepts, API reference, SDK usage, REST
calls, model training workflows, and end-to-end quickstart guides.

This work requires staying close to the product engineering team — the
service ships fast, APIs change, and the documentation needs to reflect
what the service actually does, not what it was planned to do. I verify
behavior hands-on, reproduce errors, and work directly with engineers to
surface the gaps between what is implemented and what is documented.

What makes this domain challenging
------------------------------------

AI product documentation has an accuracy problem that other categories
don't: the outputs are probabilistic, confidence thresholds vary by model
and input, and user expectations shaped by general AI familiarity don't
match how a specific model actually behaves. Writing about detection
accuracy, confidence scores, and model limitations without either
overpromising or underselling the capability is a core editorial
challenge on this product.

The audience spans developers building applications and operators
deploying and monitoring them — two groups with overlapping but distinct
needs. Getting the documentation architecture right for both, without
creating two parallel doc sets, is the structural challenge I work
through on every major feature.

How the documentation is built
------------------------------

This is a docs-as-code process, with one honest qualification. I author
in DITA and manage the source in git, committing and pushing from the
command line to Oracle's DevOps SCM, the company's own git-based
DevSecOps product, where the documentation build and publish pipeline
picks it up. Source control, branching, review, and an automated
publish path are all part of the daily loop.

What I do not have is the repository the service itself is built from.
Oracle restricts proprietary source code to engineering, so the
documentation does not live next to the code and I cannot open a pull
request against the feature that changed. Accuracy has to come from
somewhere else: working hands-on with the service, reproducing
behavior, and going directly to the engineers who own it. It is
docs-as-code in toolchain and workflow, and deliberately not
docs-in-the-same-repo.

Why it matters
--------------

AI service documentation is a trust document as much as a reference
document. If the docs misrepresent what a model can and can't do,
developers build systems that fail in predictable ways. The
documentation that ships with OCI Vision is the primary interface
between Oracle's AI engineering team and the developers who build on it.
Getting that right — technically accurate, structurally clear, honest
about limitations — is the job.
