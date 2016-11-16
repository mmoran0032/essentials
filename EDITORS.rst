TEXT EDITORS
============

You switch between multiple editors a lot, so this will help you get them set
up. Right now, you are using ``vim`` for small edits to single files and
``atom`` for larger projects.

Atom
----

Install the ``.deb`` package from `here <https://atom.io/>`__ with
``sudo dpkg -i atom-amd64.deb``. Atom comes out-of-the-box set up for your
Python work, so there isn't too much you need to do initially. You'll need to
have your Python environment already set up before.

You are using 4 spaces per tab, the *one-dark-ui* and
*base16-tomorrow-dark-theme* themes, and even tab sizing. There may be a few
other settings to change, but mostly the defaults are fine.

Atom packages
^^^^^^^^^^^^^

-  *git-plus*: ``git`` stuff without the command line
-  *language-restructuredtext*: syntax highlighting for ``.rst`` files
-  *latex* and *language-latex*: LaTeX support
-  *linter* and *linter-flake8*: provides highlighting to follow style guides
-  *minimap* and *minimap-cursorline*: shows minimap of the current file
-  *pdf-view*: view PDF files in Atom
-  *project-manager*: manages projects
-  *rst-preview-pandoc*: show preview with ctrl-shift-E
-  *script*: run scripts with ctrl+shift+B


Vim
---

Useful for short edits to files. Get it with ``apt install vim``, and use the
config file in this directory to control the behavior. Since the ``.vim``
directory is within my backup, just copy over the autoload, bundle, and colors
directories to complete installation. If that doesn't work, then look up how
to install vim packages.

You need *pathogen*, *vim-airline*, and *vim-bufferline*, and you're using the
*distinguished* color scheme.

