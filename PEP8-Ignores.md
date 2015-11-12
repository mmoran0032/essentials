PEP8 Violations and Why I Ignore Them
=====================================

Before I go any further, I do not ignore *all* PEP8 violations or
non-compliance. I really like code that looks well, and PEP8 is a relatively
good set of coding layout practices for `python`. That said, there are a few
things that I still hold on to, or ignore based on what file it is, but not
without good reason.


Errors
------

**E111 indentation is not a multiple of four**

This harkens back to my Fortran days where I started using two spaces (and I
think the first time I thought seriously about inserting tabs instead of
spaces) in undergrad, circa Fall 2010. I think I liked the compact style of
the code, and at the time my python code was pretty shitty in terms of too
many nests, so dropping down to two-space tabs would let me have my code and
adhere to another style guideline I had just fallen in love with: the 80
character width limit.

The holdover now is mostly because I still like the look of it, plus when
coding in other languages that don't use whitespace as dellimiters, that
code isn't spread out across the screen either. I've considered switching
back to the four-space tab for python, especially since my coding skill has
improved and evolved such that it's been *years* since I had to worry about
a four- or five-deep nested loop/if monstrosity falling onto my editor.

We'll see what happens in the coming years, since it may be one of those
that I have to change to live with.

*Update 2015-11-12:* I think I'm switching over. I can't say exactly what
caused it, but python code seems to look better with extra indentation... I
tried it out in the `WienFilter` code first on a couple of files, and while
it isn't perfect, I think I can get used to it. Right now, I'm leaving
previous codes as is, but I may go on a compliance spree later, converting
all of them over.


Warnings
--------

**W391 blank line at end of file**

I got used to having a blank line at the end of files recently, and I'm not
100% sure why... I think I just liked that added space and ease of keying
down to get to the end and not having to worry about other text, but maybe
that's just me looking back at it.

