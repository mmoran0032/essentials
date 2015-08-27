CLEAN CODE
==========

Following the principles set up in *Clean Code* (Robert C. Martin, Pearson
Education, 2009), this is my list of what make my code clean. For the most part,
it is section titles from the book, but with my own personal take on them. Ideas
from the book that I've never needed to worry about (e.g. "Using Puns") are left
out of the lists. Things that don't (at least, currently) pertain to what type
of programs I write are likewise excluded.

These are my personal guidelines.


Meaningful Names
----------------

- Use intention-revealing, descriptive names that make meaningful distinctions
  between themselves and others

- Avoid disinformation, encodings, and mental mappings

- Use pronounceable and searchable names

- Use nouns for class names and verbs for method names


Functions
---------

- Should be small, do one thing, and contain one level of abstraction

- Should have few (or no) arguments

- Have no side effects

- Don't repeat yourself in multiple places


Comments
--------

- Explain yourself in code, not comments

- When used, comments should be informative and well-written


Formatting
----------

- Follow the "newspaper" metaphor: main points at the top and details at the
  bottom of the file/class

- Related items should be vertically close and ordered properly

- If on a team, set and follow team rules


Objects and Data Structures
---------------------------

- Express data in abstract terms such that the implementation is hidden

- **Law of Demeter:** a method *f* of a class *C* should only call the methods
  of *C*, an object created by *f*, an object passed as an argument to *f*, and
  an object held in an instance variable of *C*


Error Handling
--------------

- Use exceptions instead of error/return codes

- Don't return or pass null


Unit Tests
----------

- Write unit tests *before* production code

- Keep tests clean and well maintained

- Use a single concept and one assert per test

- Tests should be Fast, Independent, Repeatable, Self-Validating, and Timely
  (FIRST principle)


Classes
-------

- Should be organized, small, and handle a single responsibility

- Aim for high cohesion (variables used in a majority of functions, no more
  functions than are absolutely necessary)


Systems
-------

- Separate constructing a system from using it


Emergence
---------

- Design must produce a system that acts as intended

- Final code base must be refactored to fully clean it up

- Remove duplication

- Be expressive

- Minimize the number of classes and methods


Successive Refinement
---------------------

- Write code and clean it up

- Maintaining tests help ensure refactoring didn't break the code

- Make edits incrementally, and test frequently
