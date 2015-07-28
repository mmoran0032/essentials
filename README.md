INSTALLATION NOTES
==================

The next time you wipe your hard drive or decide to upgrade and need to start
from scratch, this will help you out tremendously. Honestly, I'm surprised you
made it as far as you did without making one of these. Now it's finally time to
keep this stuff organized.

CONFIG FILES
============

Most of these files replace the hidden configuration files of the same name in
the home directory. First, remove those old files (only `.bashrc` and `.vimrc`
may be there, plus possibly the `.git*` files), then link these over using
```
  ln -s ~/bin/essentials/FILENAME ~/.FILENAME
```

If everything goes right, you should have everything in place at the next launch
of the Terminal.

APT-GET INSTALLATION
====================

For compiling sources and general command line development, you need a few
packages that aren't included in the base install. Most of these are in support
of other primary packages. I've broken them down into those subsets for ease.

- build-essential vim git texlive-full
- **GIT** libssl-dev libcurl4-openssl-dev libexpat1-dev asciidoc xmlto docbook2x
- **PYTHON** libpython3-dev python3-setuptools python3-psutil
- **MATPLOTLIB** libpng12-dev libfreetype6-dev python3-dateutil
  python3-pyparsing python3-cairo-dev libffi-dev python3-tk tk-dev
- **SCIPY** gfortran liblapack-dev
- **ROOT** libxpm-dev
- libgtk2.0-dev

Previously, I installed them I got to them, but since they are all collected
here (and for 99% of them essential to my current stack), there's no reason to
not just install them all right away.

OPT DIRECTORY CONTENTS
======================

First, actually make an `/opt` directory to hold all of this stuff. When
downloading Google Chrome, it may do this for you, but I haven't tried it out.
Most of these can be found on GitHub, but a few will just require going to the
website and installing it that way. Most of these are related to Python
development.

Any additional installation notes will be given after.

Non-Python Development
----------------------

**git** (`git@github.com:git/git.git`), the simple version tracking software.
Since the version installed via `apt-get` is a little old, grab this one with it
immediately after.

**glances** (`git@github.com:nicolargo/glances`), a Terminal-based system
monitor. I haven't been using it as much anymore, but I think I will be in the
near future when I'm doing more computationally-intense work. Install this by
running `sudo python setup.py install` from within the directory.

[Google Chrome](https://www.google.com/chrome/browser/desktop/index.html), the
web browser, for obvious reasons. Linux Mint comes with Firefox by default, so
you'll have to grab this from there.

**mdPresent** (`git@github.com:mmoran0032/mdPresent.git`), a lightweight
presentation tool using Markdown to generate slides. My personal fork of the
project.

[RFTG](http://keldon.net/rftg/), the computer version of the card game. Includes
the *Alien Artifacts* expansion. Requires `libgtk2.0-dev` to compile.

[Sublime Text 3](https://www.sublimetext.com/), the all-purpose text editor.
Since I also use `vim`, this is for larger projects and not one-off quick edits.

- Most settings are changed via the user preferences file. After installation,
  point that file to the one in this directory:

  `ln -s ~/bin/essentials/sublimePreferences ~/.config/sublime-text-3/Packages/User/Preferences.sublime-settings`

Python Development
------------------

Since my work mostly involves using `python`, this may be the most important
section. First, order is *very* important here, since most of the libraries
rely on other ones (like almost everything needing `cython` and `numpy`). Keep
to this order, and you should be fine.

- cython: `git@github.com:cython/cython.git`

- numpy: `git@github.com:numpy/numpy`

- scipy: `git@github.com:scipy/scipy.git`

- mpmath: `git@github.com:fredrik-johansson/mpmath.git`

- sympy: `git@github.com:sympy/sympy.git`

- matplotlib: `git@github.com:matplotlib/matplotlib.git`

- pandas: `git@github.com:pydata/pandas`

- pymc: `git@github.com:pymc-devs/pymc.git`

- scikit-learn: `git@github.com:scikit-learn/scikit-learn`

- seaborn: `git@github.com:mwaskom/seaborn.git`

Any additional packages that I need will just get tacked onto the end of this
list since, if they compile and can be imported, the order is fine.

I recently switched from dealing with global installs to using local installs.
For all of the packages above, just compile and install them using
```
    python3 setup.py install --user
```
from within the directory in question. Note the `python3` part, since I've
completely switched over (except for one case, below).

ROOT
----

ROOT (`git@github.com:root-mirror/root`), the data analysis framework developed
at CERN, is annoying. It only works with Python 2.X right now, and I tried to
get it to work with 3.X with a completely fresh install of everything to no
avail. As such, it can only be imported when using `python` to start a program,
not `python3`.

Since I will no longer (hopefully) be in the academic run-around when I
graduate, this should not be a problem and I won't be doing any work with ROOT.
For now though, I have to deal with it (and I know enough about it currently
that it is not too bad).

Just like with the Python stuff above, this is a "local" install. I put that in
quotes only because it's a little different, since I'm sourcing the compiled
location in my `.bashrc` to make it work. This follows the "fixed location
install" on the ROOT website. Run the following:
```
    ./configure linuxx8664gcc
    make -j 9
    . bin/thisroot.sh
```

The last line is only if you want to start working with it right now. Otherwise,
you'll source that location with your next Terminal.

The only idea I have right now is, if I'm working with ROOT objects and *really*
want to change them over into Python ones, I can also compile `numpy` for
Python 2.X, write a script that converts ROOT files to numpy arrays, write those
arrays to a file, then use my Python 3.X code to do more processing. That isn't
the best solution, so I think I'll just stick with the 2.X full route with the
ROOT internals taking place of the SciPy/etc. routines.
