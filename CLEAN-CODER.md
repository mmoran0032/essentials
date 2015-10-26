CLEAN CODER
===========

Since I want to be a software professional, I have to act like one with my code.
That means treating my work and estimates in a way that make it more likely that
what I'm doing will be trusted and taken seriously. This description is based on
snippets from Robert C. Martin's *Clean Coder* in the same way that
CLEAN-CODE.md is.


Estimates
---------

Timeline estimates should be based on a trivariate analysis: an optimistic,
nominal, and pessimistic estimate.

- **Optimistic** should be wildly optimistic, where everything goes right and
  there are no other hiccups. This should be roughly a 1-in-1000 chance of
  actually happening

- **Nominal** should be the greatest chance of success, so at the peak of a bell
  curve for the outcomes.

- **Pessimistic** should be wildly pessimistic, where everything goes wrong and
  everything gets in the way (ignore natural disasters here). Again, there
  should be a roughly 1-in-1000 chance of this happening.

Taking these time estimates, you can figure out roughly how long the task will
take from the following equations. The expected duration of the task is
```
    mu = (O + 4N + P)/6,
```
while the uncertainty of that expected duration is
```
    sigma = (P - O)/6.
```
Suppose the estimates are O:1, N:3, P:12, the expected duration is 4.2 +/- 1.8
days. In most cases, this total estimate will be somewhat pessimistic since the
pessimistic tail of the estimates is longer than the optimistic one.

With multiple tasks, you can still find the expected duration. You take the
expected durations of each individual task and add them; this is your total
expected duration. The uncertainties must be added in quadrature, so
```
    sigma_total = sqrt(sum(sigma**2))
```

What this estimation scheme does is add *realism* to the estimate. Since only
relying on optimistic estimates can harm your reputation (In the example above,
it is very likely for the task to take *six times* longer than the optimistic
estimate) by appearing to always be finished later than you think. If you are
always late, you can't be trusted to finish anything on time, and anything else
that is relying on your portion being on time will also be delayed.
