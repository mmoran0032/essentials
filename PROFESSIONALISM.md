
# Professionalism

Following the principles set up in *Clean Code* and *Clean Coder*, both
by Robert C. Martin, this file describes what I should do as a software
professional. The two main sections describe what my code needs to be
like and who I need to be like.

## Code

The main ideas for writing code can be organized into the following:

1. Write code and clean it up
2. Maintain tests to ensure refactoring doesn't break the code
3. Make edits incrementally, and test frequently

These are my personal guidelines.

### Naming

- Use intention-revealing, descriptive names that make meaningful
  distinctions between themselves and others
- Avoid disinformation, encodings, and mental mappings
- Use pronounceable and searchable names
- Use nouns for class names and verbs for method names

### Functions

- Should be small, do one thing, and contain one level of abstraction
- Should have few (or no) arguments
- Have no side effects
- Don't repeat yourself in multiple places

### Comments

- Explain yourself in code, not comments
- When used, comments should be informative and well-written

### Formatting

- Follow the "newspaper" metaphor: main points at the top and details at
  the bottom of the file/class
- Related items should be vertically close and ordered properly
- If on a team, set and follow team rules

### Objects and Data Structures

- Express data in abstract terms such that the implementation is hidden
- **Law of Demeter:** a method *f* of a class *C* should only call the
  methods of *C*, an object created by *f*, an object passed as an
  argument to *f*, and an object held in an instance variable of *C*

### Error Handling

- Use exceptions instead of error/return codes
- Don't return or pass null

### Unit Tests

- Write unit tests *before* production code
- Keep tests clean and well maintained
- Use a single concept and one assert per test
- Tests should be Fast, Independent, Repeatable, Self-Validating, and
  Timely (FIRST principle)

### Classes

- Should be organized, small, and handle a single responsibility
- Aim for high cohesion (variables used in a majority of functions, no
  more functions than are absolutely necessary)

### Systems

- Separate constructing a system from using it

### Emergence

- Design must produce a system that acts as intended
- Final code base must be refactored to fully clean it up
- Minimize the number of classes and methods


## Personal

As a software professional, your work is not just the code you write but
also who you are as a person and how you interact with other people. You
can only be a good developer and team member if you are professional in
your interactions with other people and treat your work professionally.
This section focuses on the personal aspect of being a developer.

### Time Estimates

Timeline estimates should be based on a trivariate analysis: an
optimistic, nominal, and pessimistic estimate.

- **Optimistic** should be wildly optimistic, where everything goes
  right and there are no other hiccups. This should be roughly a
  1-in-1000 chance of actually happening
- **Nominal** should be the greatest chance of success, so at the peak
  of a bell curve for the outcomes.
- **Pessimistic** should be wildly pessimistic, where everything goes
  wrong and everything gets in the way (ignore natural disasters here).
  Again, there should be a roughly 1-in-1000 chance of this happening.

Taking these time estimates, you can figure out roughly how long the
task will take from the following equations. The expected duration of
the task is

    mu = (O + 4N + P) / 6

while the uncertainty of that expected duration is

    sigma = (P - O) / 6

Suppose the estimates are `O = 1`, `N = 3`, and `P = 12`, then the
expected duration is `4.2 +/- 1.8` days. In most cases, this total
estimate will be somewhat pessimistic since the pessimistic tail of the
estimates is longer than the optimistic one.

With multiple tasks, you can still find the expected duration. You take
the expected durations of each individual task and add them; this is
your total expected duration. The uncertainties must be added in
quadrature, so

    sigma_total = sigma_1**2 + sigma_2**2 + ...

What this estimation scheme does is add *realism* to the estimate. Since
only relying on optimistic estimates can harm your reputation (In the
example above, it is very likely for the task to take *six times* longer
than the optimistic estimate) by appearing to always be finished later
than you think. If you are always late, you can't be trusted to finish
anything on time, and anything else that is relying on your portion
being on time will also be delayed.
