Clover Developer Documentation (Fiserv)
========================================

**Artifact:** `Billing for apps
<https://docs.clover.com/dev/docs/billing-for-apps>`_, app billing on the
legacy Developer Dashboard.

.. note::

   I wrote that billing documentation section in full during my time in
   Developer Relations at Clover. The page is still live and has been
   maintained since I left in May 2021, and I have no visibility into
   what changed after that. It documents the legacy Developer Dashboard;
   Clover has since introduced a billing API built around events rather
   than static account statuses.

   I also owned the Orders API documentation, described below. Those
   pages have been revised enough since 2021 that I do not claim the
   current versions, so they are not linked here.

Rebuilding the billing documentation from the code
--------------------------------------------------

I joined Clover as a technical writer in Developer Relations and was
assigned a few tickets to update the developer billing documentation
within my first three months. Reading the existing docs against the
actual product, the two did not match. The documentation described
behavior the platform no longer had.

The reason was institutional. There were no accurate PRDs or design
documents to work from. The people who had built developer billing were
gone, and the product knowledge had left with them. There was nothing
authoritative to write from except the running system and the code
behind it.

So I stopped treating it as a ticket and treated it as a
reconstruction. Working with the engineer who owned the service, I read
the code to establish what the billing flow actually did, end to end. I
diagrammed it in Lucidchart so the team had a shared picture, and
rewrote the documentation against verified behavior rather than against
the previous documentation.

The subject matter is genuinely intricate, which is why the drift
mattered so much. App billing ran two models at once. Metered billing
charged in arrears against logged merchant events, and subscription
billing charged in advance against a monthly price with proration. On
top of that sat a merchant account lifecycle of active, lapsed,
suppressed, and inactive states, each with its own consequences for
whether and how a developer got paid, plus payment delays,
reactivation, and regional differences between US and European
merchants. A developer who follows an inaccurate document through that
does not get a confusing result. They get a revenue bug.

Owning the Orders API documentation
-----------------------------------

Separately, I owned documentation for the Orders API, which became one
of the platform's most heavily used surfaces in 2020 when merchants
moved to online ordering during COVID.

The pressure here was different from billing. The content was not
wrong, but developers were integrating fast and under real business
urgency, so the job was getting someone to a working order quickly
while being precise about the pieces they would otherwise discover by
trial and error: line items, modifiers, discounts, taxes, service
charges, and how an order total actually resolves once all of them
apply.

Closing the loop with developers
--------------------------------

As part of Developer Relations I answered developer and partner
questions directly, including from partners such as Google. Every
question that was hard to answer pointed at either a documentation gap
or a product gap, and I logged both, filing bugs and feature gaps from
a developer-facing point of view and following them through to a fix. I
was still finding and filing those issues on my last day.

I also began experimenting with Readme.io's Recipes feature to build
interactive, step-through walkthroughs. The feature was early then and
considerably less capable than it is now, but the intent is one I would
still argue for: get the developer to a first success inside the
documentation rather than sending them elsewhere to find out whether it
works.

Why it matters
--------------

Two things here are the substance of developer documentation rather
than adjacent to it.

The first is that when the documentation and the product disagree, the
only reliable source of truth is the running system and the code behind
it. Writing accurately meant reading that code with an engineer, not
paraphrasing a stale document.

The second is the loop. Answering real developer questions is the
measurement instrument for documentation: the questions that keep
recurring tell you exactly where the docs fail, and the ones that
cannot be answered at all tell you where the product does. Treating
support friction as the input to the next revision is what kept the
documentation converging on what developers actually needed.
