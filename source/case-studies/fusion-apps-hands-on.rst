Learning the Product by Running It (Oracle Fusion Applications)
================================================================

.. note::

   This work was internal to Oracle and delivered through Oracle
   University, so there is no public artifact to link. It is described
   here because the working method, verify the product by operating it
   before writing about it, is how I approach documentation accuracy
   generally.

The problem
-----------

In 2012 I owned the curriculum for Oracle University's inaugural Fusion
Applications Project Management train-the-trainer program, a five-day
in-person session in Redwood Shores. The product was new. It was an
early adopter release, which meant the documentation, the training
material, and the software were all being built at the same time, and
none of them could be assumed correct on the basis of the others.

A five-day hands-on class fails loudly. If an activity does not work in
the environment, thirty people in a room find out simultaneously.

What I did
----------

I planned and set up the environment and its data as part of building
the curriculum, then ran every hands-on activity in it myself before
the class. Testing the activities was how I learned what the product
actually did, and where the written steps and the software diverged.
Where the software had moved, the material changed.

I hit a provisioning blocker before the session: attendees needed
superuser privileges for the labs, and the environment images that
would normally supply them were not available yet. I worked out a group
permission assignment workflow to provision all thirty users without
those images, which unblocked the program.

Across subsequent releases I maintained and extended the curriculum the
same way, reviewing and re-testing hands-on activities against each
new feature, and setting up the environment data required to rebuild
the reusable classroom image every release cycle. The curriculum was
not a document that was written once. It was a system that had to stay
accurate and deployable as the product moved underneath it.

Why it matters
--------------

The habit this built is the one I still rely on: work with the product
directly, and treat your own experience of it as evidence. If a
procedure is confusing when I run it, it will be confusing for the
reader, and I have found that out before publishing rather than after.

It also set the expectation that content has to survive product change.
Documentation and training that are correct at the moment of writing
and never re-verified will drift, and the reader is the one who pays
for it. Re-testing against each release is the cheapest way to stop
that.
