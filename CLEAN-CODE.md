MEANINGFUL NAMES
----------------

  Use intention-revealing names
  Avoid disinformation, encodings, mental mappings
  Make meaningful distinctions
  Use pronounceable/searchable names
  Class names are nouns, method names are verbs
  Don't be cute or use puns

FUNCTIONS
---------

  Should be small, do one thing, and contain one level of abstraction
  Use descriptive names
  Have few (or no) arguments
  Have no side effects
  Use exceptions instead of error codes
  Don't repeat

COMMENTS
--------

  Explain yourself in code, not comments
  When used, should be informative and well-written

FORMATTING
----------

  Follow the "newspaper" metaphor (main points at top, details at bottom)
  Related items should be vertically close and ordered
  If on a team, set and follow team rules

OBJECTS AND DATA STRUCTURES
---------------------------

  Express data in abstract terms (hide implementation)
  Law of Demeter: a method f of a class C should only call the methods of
    C, an object created by f, an object passed as an argument to f, and an
    object held in an instance variable of C

ERROR HANDLING
--------------

  Use exceptions instead of return codes
  Don't return or pass null

UNIT TESTS
----------

  Write unit tests before production code
  Keep tests clean and well maintained
  Use a single concept and one assert per test
  Tests should be Fast, Independent, Repeatable, Self-Validating, and Timely

CLASSES
-------

  Should be organized, small, and handle a single responsibility
  Aim for high cohesion (variables used in a majority of functions)

SYSTEMS
-------

  Separate constructing a system from using it

EMERGENCE
---------

  Design must produce a system that acts as intended
  Must be refactored to clean up
  Remove duplication
  Be expressive
  Minimize the number of classes and methods

SUCCESSIVE REFINEMENT
---------------------

  Write code and clean it up
  Maintaining tests help ensure refactoring didn't break the code
  Make edits incrementally, and test frequently

WHY CODE SHOULD CHANGE
----------------------

  COMMENTS
    C1: Inappropriate information
    C2: Obsolete comment
    C3: Redundant comment
    C4: Poorly-written comment
    C5: Commented-out code removed
  ENVIRONMENT
    E1: Build requires more than one step
    E2: Tests require more than one step
  FUNCTIONS
    F1: Too many arguments
    F2: Remove output arguments
    F3: Remove flag arguments
    F4: Remove dead (no longer used) function
    F5: Should only do one thing
    F6: Should contain only one level of abstraction
  GENERAL
    G1: Multiple languages in one source file
    G2: Obvious behavior is unimplemented
    G3: Incorrect behavior at boundaries
    G4: Don't override safeties
    G5: Remove duplication
    G6: Code at wrong level of abstraction
    G7: Base classes shouldn't depend on their derivatives
    G8: Too much information (restrict what is known or can be done)
    G9: Remove dead (not executed) code
    G10: Fix vertical separation
    G11: Fix inconsistencies
    G12: Remove clutter
    G13: Avoid artificial coupling
    G14: Avoid feature envy (methods of one class manipulating an object
         from another class)
    G15: Don't use selector arguments
    G16: Avoid obscured intent
    G17: Fix misplaced responsibility
    G19: Use explanatory variables
    G20: Function names should say what they do
    G21: Understand the algorithm used
    G22: Make logical dependencies physical
    G23: Prefer polymorphism to If/Else or Switch/Case
    G24: Follow standard conventions
    G25: Replace magic numbers with named constants
    G26: Be precise
    G27: Prefer structure over convention
    G28: Encapsulate Conditionals
    G29: Avoid negative conditionals
    G31: Avoid hidden temporal couplings
    G32: Don't be arbitrary
    G33: Encapsulate boundary conditions
    G35: Keep configurable data at high levels
    G36: Avoid transitive navigation
  NAMES
    N1: Choose descriptive names
    N2: Choose names at the appropriate level of abstraction
    N3: Use standard nomenclature where possible
    N4: Use unambiguous names
    N5: Length of name should reflect length of scope
    N6: Avoid encodings
    N7: Names should describe side-effects
  TESTS
    T1: Have sufficient tests
    T2: Use a coverage tool
    T3: Don't skip trivial tests
    T5: Test boundary conditions
    T6: Exhaustively test near bugs
    T7: Patterns of failure should be revealing
    T8: Test coverage patterns can be revealing
    T9: Tests should be fast
