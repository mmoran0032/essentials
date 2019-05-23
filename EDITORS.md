
# TEXT EDITORS

You switch between multiple editors a lot, so this will help you get
them set up. Right now, you are using `vim` for small edits to single
files and `code` for larger projects. Both are essential tools for your
work.

## VSCode

VSCode is rapidly becoming an amazing development environment for both
data science work (through its integration with Jupyter kernels) and
package development. You really don't even need the web view for Jupyter
anymore, especially given that the web view has worse linting, editing,
and refactoring functionality. Compared to previous editors (Sublime
Text, Atom), VSCode has a cleaner interface and I've enjoyed working in
it more.

Your main user preferences are linked over during the basic setup. You
will need to install the following packages through the included package
manager for your main development work:

### General

- Docker `peterjausovec.vscode-docker`
- gitignore `codezombiech.gitignore`
- markdownlint `davidanson.vscode-markdownlint`
- Prettify JSON `mohsen1.prettify-json`
- reStructuredText `lextudio.restructuredtext`
- Rewrap `stkb.rewrap`
- Sort lines `tyriar.sort-lines`

### Python

- Python `ms-python.python`

### Theme Changes

- Base16 Tomorrow Dark+ `shurelia.base16-tomorrow-dark-vscode`
- Material Theme `equinusocio.vsc-material-theme`
- Material Theme Icons `equinusocio.vsc-material-theme-icons`


## Vim

Vim is useful for short edits to files and for longer `git` commit
messages, but past that you usually just use VSCode. The configuration
details include your `.vimrc` file and the `.vim` directory that
contains the additional packages you'll need. All of these are linked
through the basic setup instructions, so there's nothing else to do.
