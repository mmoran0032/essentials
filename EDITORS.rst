TEXT EDITORS
============

You switch between multiple editors a lot, so this will help you get
them set up. Right now, you are using ``vim`` for small edits to single
files and ``code`` for larger projects.

Code
----

You've recently started using Visual Studio Code from Microsoft as your
main editor (available `here <https://code.visualstudio.com/>`__.
Download and install by clicking on the ``.deb`` package link.

**Code Packages**

-  *ms-python.python*: Python functionality, including embedded
   "notebook" interface
-  *stkb.rewrap*: quickly rewrap text to a column number
-  *shurelia.base16-tomorrow-dark-vscode*: current color scheme


Vim
---

Useful for short edits to files. Get it with ``apt install vim``, and
use the config file in this directory to control the behavior. Since the
``.vim`` directory is within my backup, just copy over the autoload,
bundle, and colors directories to complete installation.

You need *pathogen*, *vim-airline*, and *vim-bufferline*, and you're
using the *distinguished* color scheme. Install these from your external
backup, since installing them the regular Vim way didn't work and I
didn't bother to try to figure out the better way. Additionally since
the packages you're using are older and your colorscheme (may be) is
customized, the "proper" method most likely would still result in a
different setup than you want.
