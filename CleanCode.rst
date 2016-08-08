CLEAN CODE
==========

Following the principles set up in *Clean Code* (Robert C. Martin,
Pearson Education, 2009), this is my list of what make my code clean.
For the most part, it is section titles from the book, but with my own
personal take on them. Ideas from the book that I've never needed to
worry about (e.g. "Using Puns") are left out of the lists. Things that
don't (at least, currently) pertain to what type of programs I write are
likewise excluded.

These are my personal guidelines.

Meaningful Names
----------------

-  Use intention-revealing, descriptive names that make meaningful
   distinctions between themselves and others
-  Avoid disinformation, encodings, and mental mappings
-  Use pronounceable and searchable names
-  Use nouns for class names and verbs for method names

Functions
---------

-  Should be small, do one thing, and contain one level of abstraction
-  Should have few (or no) arguments
-  Have no side effects
-  Don't repeat yourself in multiple places

Comments
--------

-  Explain yourself in code, not comments
-  When used, comments should be informative and well-written

Formatting
----------

-  Follow the "newspaper" metaphor: main points at the top and details
   at the bottom of the file/class
-  Related items should be vertically close and ordered properly
-  If on a team, set and follow team rules

Objects and Data Structures
---------------------------

-  Express data in abstract terms such that the implementation is hidden
-  **Law of Demeter:** a method *f* of a class *C* should only call the
   methods of *C*, an object created by *f*, an object passed as an
   argument to *f*, and an object held in an instance variable of *C*

Error Handling
--------------

-  Use exceptions instead of error/return codes
-  Don't return or pass null

Unit Tests
----------

-  Write unit tests *before* production code
-  Keep tests clean and well maintained
-  Use a single concept and one assert per test
-  Tests should be Fast, Independent, Repeatable, Self-Validating, and
   Timely (FIRST principle)

Classes
-------

-  Should be organized, small, and handle a single responsibility
-  Aim for high cohesion (variables used in a majority of functions, no
   more functions than are absolutely necessary)

Systems
-------

-  Separate constructing a system from using it

Emergence
---------

-  Design must produce a system that acts as intended
-  Final code base must be refactored to fully clean it up
-  Remove duplication
-  Be expressive
-  Minimize the number of classes and methods

Successive Refinement
---------------------

-  Write code and clean it up
-  Maintaining tests help ensure refactoring didn't break the code
-  Make edits incrementally, and test frequently


CLEAN CODER
===========

Since I want to be a software professional, I have to act like one with
my code. That means treating my work and estimates in a way that make it
more likely that what I'm doing will be trusted and taken seriously.
This description is based on snippets from Robert C. Martin's *Clean
Coder* in the same way that CLEAN-CODE.md is.

Estimates
---------

Timeline estimates should be based on a trivariate analysis: an
optimistic, nominal, and pessimistic estimate.

-  **Optimistic** should be wildly optimistic, where everything goes
   right and there are no other hiccups. This should be roughly a
   1-in-1000 chance of actually happening

-  **Nominal** should be the greatest chance of success, so at the peak
   of a bell curve for the outcomes.

-  **Pessimistic** should be wildly pessimistic, where everything goes
   wrong and everything gets in the way (ignore natural disasters here).
   Again, there should be a roughly 1-in-1000 chance of this happening.

Taking these time estimates, you can figure out roughly how long the
task will take from the following equations. The expected duration of
the task is

.. math::

        \mu = \frac{O + 4N + P}{6},

while the uncertainty of that expected duration is

.. math::

        \sigma = \frac{P - O}{6}.

Suppose the estimates are :math:`O=1`, :math:`N=3`, and :math:`P=12`, then the
expected duration is :math:`4.2 \pm 1.8` days. In most cases, this total
estimate will be somewhat pessimistic since the pessimistic tail of the
estimates is longer than the optimistic one.

With multiple tasks, you can still find the expected duration. You take
the expected durations of each individual task and add them; this is
your total expected duration. The uncertainties must be added in
quadrature, so

.. math::

        \sigma_{\textrm{total}} = \sqrt{\sum \sigma^2}

What this estimation scheme does is add *realism* to the estimate. Since
only relying on optimistic estimates can harm your reputation (In the
example above, it is very likely for the task to take *six times* longer
than the optimistic estimate) by appearing to always be finished later
than you think. If you are always late, you can't be trusted to finish
anything on time, and anything else that is relying on your portion
being on time will also be delayed.
