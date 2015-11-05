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
```bash
ln -s ~/bin/essentials/FILENAME ~/.FILENAME
```

If everything goes right, you should have everything in place at the next launch
of the Terminal. Note that you'll get a warning at every Terminal launch until
you either install ROOT or remove the ROOT sourcing line from your bashrc.


PAIRING LOGITECH MOUSE/KEYBOARD
===============================

The Logitech wireless mouse and keyboard I currently have, and all future ones,
have a pairing software included that only works with Windows. Thankfully,
someone has already developed a way to get this to work in Linux, creating the
`ltunify` utility. Download and install it using:
```bash
git clone https://git.lekensteyn.nl/ltunify.git
cd ltunify
make install-home
```
Once everything is set, an executable names `ltunify` will be in `~/bin`. Change
to this directory and run
```bash
sudo ./ltunify pair
```
and follow the prompts to pair your devices.


APT-GET INSTALLATION
====================

For compiling sources and general command line development, you need a few
packages that aren't included in the base install. Most of these are in support
of other primary packages. I've broken them down into those subsets for ease.

- build-essential vim git texlive-full cmake rsync unzip mercurial cloc
  libhdf5-serial-dev
- **GIT** libssl-dev libcurl4-openssl-dev libexpat1-dev asciidoc xmlto docbook2x
- **PYTHON** libpython3-dev python3-setuptools python3-psutil python3-pip

  Some utilities can also be cross-compiled for python2, so just run the above
  without the `3` to get this functionality.
- **MATPLOTLIB** libpng12-dev libfreetype6-dev python3-dateutil
  python3-pyparsing python3-cairo-dev libffi-dev python3-tk tk-dev
- **SCIPY** gfortran liblapack-dev
- **ROOT** libxpm-dev freeglut3-dev
- libgtk2.0-dev
- **IPYTHON** nodejs-legacy npm
- **ANDROID** openjdk-7-jdk qemu-kvm libvirt-bin bridge-utils
- **PYGLET** libavbin-dev libavbin0

Previously, I installed them as I got to them, but since they are all collected
here (and for 99% of them essential to my current stack), there's no reason to
not just install them all right away.


MINICONDA
=========

I've downloaded `conda` (3.16.0, and specifically the Miniconda distribution) so
that, in the future, I can use that for my scientific python work. For now, I do
not know how it will interact with my current python installs (including python
itself), but it is something to think about.

In terms of usage, I left the install directory (`/home/mikemoran/.miniconda3`)
*off* of my path, just to avoid any conflicts, but the `conda` executable (as
well as its own python interpreters and other executables) is contained in the
`bin` subdirectory in the install directory.

When figuring these things out, it may be better to work from a clean install
so as to avoid any dependency issues and read more of the documentation.


PYGLET
======

As a fun little side project thing of mine, I'm distracting myself with `pyglet`
instead of either pygame or SDL. So far, I've liked the syntax of it, since it
feels cleaner than what I remember from those two. So far I'm still at pretty
simple stuff, but maybe as a break I'll keep adding to it.

To install, I just used the source provided at
`http://pyglet.googlecode.com/archive/tip.zip`, but it should also be available
at the [BitBucket](https://bitbucket.org/pyglet/pyglet/wiki/Home) page. I tried
to install that version first, but did it improperly, so went with the Google
one.

To actually install, run `python3 setup.py install --version` from the root
directory. One thing to note is that you have to make sure that, should you also
want to compile it for python2, you need to purge the `build` directory before
running the above.

`apt-get` sources are just for playback of compressed audio formats.


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

[android-studio](https://developer.android.com/sdk/installing/index.html), for
android application development. There are some additional install steps,
detailed on the website.

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

[Mednafen](http://mednafen.fobby.net/releases/), a multi-system emulator.
Requires `libsndfile1-dev` and `libsdl1.2-dev` to compile from source. Using the
USB SNES controller, you can check input with
```bash
sudo chmod 666 /dev/input/js0
jstest /dev/input/js0
```
to make sure everything is registering. After installing, you need to edit the
config file (`~/.mednafen/mednafen.cfg`) so that `sounddevice` is
`sexyal-literal-default`. The sound seems to be staticy for the first minute or
two, but calms down after. You will probably have to reconfigure the controller
buttons as well.

[RFTG](http://keldon.net/rftg/), the computer version of the card game. Includes
the *Alien Artifacts* expansion. Requires `libgtk2.0-dev` to compile.

[Sublime Text 3](https://www.sublimetext.com/), the all-purpose text editor.
Since I also use `vim`, this is for larger projects and not one-off quick edits.

- Most settings are changed via the user preferences file. After installation,
  point that file to the one in this directory:

```bash
ln -s ~/bin/essentials/sublimePreferences ~/.config/sublime-text-3/Packages/User/Preferences.sublime-settings
```

[Toggl](https://support.toggl.com/toggl-on-my-desktop/), the productivity
tracker which also has a mobile application. Install the `.deb` package.


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

- statsmodels: `git@github.com:statsmodels/statsmodels.git`

- requests: `git@github.com:kennethreitz/requests.git`

- requests-oauthlib: `git@github.com:requests/requests-oauthlib.git`

- simplejson: `git@github.com:simplejson/simplejson.git`

- patsy: `git@github.com:pydata/patsy.git`

- numexpr: `git@github.com:pydata/numexpr.git`

- h5py: `git@github.com:h5py/h5py.git`

- psutil: `git@github.com:giampaolo/psutil.git`

Any additional packages that I need will just get tacked onto the end of this
list since, if they compile and can be imported, the order is fine.

I recently switched from dealing with global installs to using local installs.
For all of the packages above, just compile and install them using
```bash
python3 setup.py install --user
```
from within the directory in question. Note the `python3` part, since I've
completely switched over (except for one case, below).

Note that `psutil` is listed in both apt-get and here. The version is apt-get is
1.2.1, while the current version is 3.2.3, with a few years' difference between
them. Skip using the apt-get source and just stick with this one, but at the
same time since it is just being used for `glances`, you don't really need it.
Your call.


**Python Helpers**

These don't quite fit into the actual development stack, so instead I am listing
them here. These are just utilities that aide in development but aren't
necessary for it. I'm also including descriptions of them, so that it's easier
for me to guage their necessity in the future.

- flake8 (`git@gitlab.com:pycqa/flake8.git`), a code analyzer that checks
  compliance against PEP8 standards.

- npyscreen (`hg clone ssh://hg@bitbucket.org/npcole/npyscreen`), a wrapper for
  `curses` and related libraries that provides a more-pythonic way to create
  terminal-based applications.

- progressbar (`git@github.com:coagulant/progressbar-python3.git`), a wrapper
  for loops that displays the progress of that loop in the terminal.

- colorama (`git@github.com:tartley/colorama.git`), provides easy color output
  for scripts.


JUPYTER AND IPYTHON
-------------------

OK, so IPython/Jupyter *did* work yesterday, but is no longer working today, so
I'm seeing if I can get it working from source. I think this is futher proof
that eventually switching over to Anaconda, but for now everything is fine.
Here's how to get it working, or at least, how I just got it working.

*Note: IPython was working, in the Terminal, but not in the webserver format, so
all of this is really just to get that. I also think that this is possibly the
worst way to do it, but for now I don't care too much.*

1. Install the dependencies above. Honestly, I don't know if they are really
   needed, but I did install them and things work.
2. Download the 3.0.0 tarball from
   [GitHub](https://github.com/ipython/ipython/releases), extract, and move to
   `/opt`
3. Run the standard `python3 setup.py install --user`
4. Using `pip3` (yes, I told you it was awful), install `jsonschema` and
   `tornado`. One or both of these may have to be upgraded, depending on what
   else you did, but in general you're going to run
   ```bash
   sudo pip3 install [--upgrade] jsonschema
   sudo pip3 install [--upgrade] tornado
   ```
5. Test it out! Everything should work.

But, remember how awful this is, and don't do this again. Plus, everything is
migrating over to Jupyter anyway, so by the time you have to redo this stuff,
you'll just be using Jupyter. So, maybe Anaconda will be your next thing?


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
```bash
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
