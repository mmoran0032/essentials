
# TEXT EDITORS

You switch between multiple editors a lot, so this will help you get
them set up. Right now, you are using `vim` for small edits to single
files and `code` for larger projects. Both are essential tools for your
work.

## VSCode

*Note: I'm trying to move over to VSCodium, which removes the telemetry*
*portion of VSCode. Nothing else should be different.*

VSCode is rapidly becoming an amazing development environment for both
data science work (through its integration with Jupyter kernels) and
package development. You really don't even need the web view for Jupyter
anymore, especially given that the web view has worse linting, editing,
and refactoring functionality. Compared to previous editors (Sublime
Text, Atom), VSCode has a cleaner interface and I've enjoyed working in
it more.

Additonal support in VSCode for Jupyter Notebooks has been extremely
nice as well. It is almost to the point where I wouldn't need to use the
Jupyterlab web interface that much, especially since I'm not doing
anything weird with Dask monitoring or anything more advanced than just
code editing.

*Note: you can also get all of your extensions with:*

```zsh
code --list-extensions | tee ~/vscode-extensions.txt
```

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

- Material Theme `equinusocio.vsc-material-theme`
- Material Theme Icons `equinusocio.vsc-material-theme-icons`

### Windows

With the Windows Subsystem for Linux (WSL), I can use the Linux side of
my machine with the usual Windows interface. After setting up and
installing WSL (see `WINDOWS.md`), you are more or less good to go with
regular Linux installs for coding environments. There are some
additional tweaks to get VSCode working well with WSL:

- Install the *Remote Development extension pack* (see
  [VSCode's website][1] for additional details). Note that the contained
  packages don't appear to be available for install with Codium.
- (Optionally) link directories across the Windows-Linux divide to allow
  for them to be viewable in both places
- Manually copy over the `settings.json` file. Since that file location
  is within the Windows side, the setup script will not push it to the
  correct location.

## Vim

Vim is useful for short edits to files and for longer `git` commit
messages, but past that you usually just use VSCode. The configuration
details include your `.vimrc` file and the `.vim` directory that
contains the additional packages you'll need. All of these are linked
through the basic setup instructions, so there's nothing else to do.

[1]: https://code.visualstudio.com/docs/remote/wsl
