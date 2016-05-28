INSTALLATION NOTES
==================

The next time you wipe your hard drive or decide to upgrade and need to start
from scratch, this will help you out tremendously. Honestly, I'm surprised you
made it as far as you did without making one of these. Now it's finally time to
keep this stuff organized.

*Updated for reinstalling on 2016-05-03*


Beginning Installation
======================

While you're still using System76 computers, you'll want to grab their drivers.
This step will only matter if you get a computer with a graphics card or some
other extra thing that you haven't used before, but it's good to have anyway.
```
sudo apt-add-repository ppa:system76-dev/stable
apt update
apt install system76-driver
```

You'll want to make sure that everything is install and upgraded before doing
any of the specialized steps below. Simply run `apt upgrade` and allow it to
install the huge block of files, and sit back and wait. Finally, install some
extremely helpful command line tools.
```
apt install build-essential cmake git rsync tree unzip vim xclip
```

Adjust any computer settings (Terminal background and scrollback, sounds, user
picture, etc) and download any files from the backed-up external drive that you
want. In particular (to avoid replacing all of your keys), the .ssh directory
should be copied over.

Uninstall the few applications that you don't want, and download and install
[Google Chrome](https://www.google.com/chrome/browser/desktop/index.html). I do
not uninstall Firefox, since it is good to have a backup browser (and some web
tests work better with Firefox, from my previous experience). This creates the
`/opt/` directory if you haven't already, so for the rest of the work you'll
want to transfer ownership over to you.
```
sudo chown -R mikemoran /opt/
```

From here, you can take the steps in any order, since they are (mostly)
independent of each other. For the most part, the python portion is the most
important part for your work and your future work.


Config Files
------------

Most of these files replace the hidden configuration files of the same name in
the home directory. First, remove those old files (only `.bashrc` and `.vimrc`
may be there, plus possibly the `.git*` files), then link these over using
```bash
ln -s ~/bin/essentials/FILENAME ~/.FILENAME
```
You have to include the `~/bin/essntials/` portion, otherwise the linking will
not be done properly.

If everything goes right, you should have everything in place at the next launch
of the Terminal. Note that you'll get a warning at every Terminal launch until
you either install ROOT or remove the ROOT sourcing line from your bashrc.


Pairing Logitech Mouse/Keyboard
-------------------------------

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
and follow the prompts to pair your devices. You can then remove the `ltunify`
directory created from the clone if you desire.


Git
---

The version of git installed through apt is not the most up-to-date version, so
once you have any git installed (and after making sure your ssh keys are in
place), you'll want to grab the source and install the newer version. There are
a few libraries necessary for compiling to progress.
```
git clone git@github.com:git/git.git
apt install asciidoc docbook2x libcurl4-openssl-dev libexpat1-dev libssl-dev xmlto
make -j 9 prefix=/usr/local all doc info
sudo make -j 9 prefix=/usr/local install install-doc install-html install-info
```

As with all git-based installations, this is done in the `/opt/` directory.


Sublime Text 3
--------------

[Sublime Text 3](https://www.sublimetext.com/) is available within the package
manager, so you do not need to download the installer or source. Run `apt
install sublime-text` to get it.

There are a few additional steps before ST3 works the same as you're used to.
You'll want to (roughly) follow the guide
[here](https://realpython.com/blog/python/setting-up-sublime-text-3-for-full-stack-python-development/), which is mostly installing
Package Control and then Anaconda. You'll also want to grab the *Gloom* theme,
which you've really liked, directly from
[here](https://raw.githubusercontent.com/petervaro/python/master/themes/Gloom.tmTheme).
Move that file into `~/.config/sublime-text-3/Packages` and update your settings
file if necessary.

Your settings file is the one within `~/bin/essentials`, so you'll want to make
sure that ST3 is actually using this.
```
ln -s ~/bin/essentials/sublimePreferences ~/.config/sublime-text-3/Packages/User/Preferences.sublime-settings
```


Additional Installs
-------------------

Since Linux is free, you need to install some drivers for things like DVD
playback and mp3 decoding.
```
apt install ubuntu-restricted-extras libdvdread4
sudo /usr/share/doc/libdvdread4/install-css.sh
```

Once you have those, you can grab a few more important programs.
```
apt install skype audacious luckybackup texlive-full
```

For `luckybackup`, you'll need to set up the actual backup location and make
sure that there aren't weird file duplicates from copying things over.


Miniconda and Python
====================

After only a few minutes, I've already fallen in love with Anaconda and the
small Miniconda distribution. It is easy to use, and installation is quick and
easy. It is awesome!

To get my entire development stack up and running, including Jupyter, run
```
conda install beautifulsoup4 colorama cython flake8 flask h5py jupyter
              matplotlib mpmath numexpr numpy pandas patsy psutil pymc requests
              scikit-learn scipy seaborn setuptools statsmodels sympy
```
And that's it! The above is a mix of scientific, data science, and extra helpers
installed with python3. There are a few utilities that you can't get through
Anaconda, so you will need to use the standard install method for those.

Since Continuum Analytics partners with different businesses and research
organizations, there are some packages that aren't a part of their standard
distribution that you can still install with `conda`. I'll denote those as I
come across them.


Additional Python Packages
--------------------------

These packages are installed via the standard `python3 setup.py install --user`.

**autopep8** (`git@github.com:hhatto/autopep8.git`), a utility that
automatically converts code to be compliant with PEP8 guidelines. Every so often
I want to use this, since it is a quick swipe across everything. For the most
part, my code follows PEP8 pretty closely, so I don't use this as much.

**flask-script** (`git@github.com:smurfix/flask-script.git`), adding in basic
command line parsing to running flask applications.

**progressbar** (`git@github.com:coagulant/progressbar-python3.git`), a wrapper
for loops that displays the progress of that loop in the terminal. Nice for when
I write longer, non-interactive analysis scripts, but not necessary.


OPT Directory Contents
======================

The following utilities are not necesary for day-to-day work, but are good to
have for day-to-day life. Your `/opt/` directory will get full with a few things
before these (conda, chrome, etc), so the directory should already be there and
set up for your work. Any additional utilities will most likely be put here,
including non-specific ones I have repositories on GitHub for.


ROOT
----

ROOT (`git@github.com:root-mirror/root`), the data analysis framework developed
at CERN, is annoying. It only works with Python 2.X right now, and I tried to
get it to work with 3.X with a completely fresh install of everything to no
avail. As such, it can only be imported when using `python` to start a program,
not `python3`.

My new favorite thing, Anaconda, also currently does not play well with ROOT.
Since I'm using python3, conda says that both `python3` and `python` are the
python3 interpreter, which is silly. I can overwrite it, but I currently do not
know if it installs correctly, since I haven't rerun the installation.

Since I will no longer (hopefully) be in the academic run-around when I
graduate, this should not be a problem and I won't be doing any work with ROOT.
For now though, I have to deal with it (and I know enough about it currently
that it is not too bad).

Just like with the Python stuff above, this is a "local" install. I put that in
quotes only because it's a little different, since I'm sourcing the compiled
location in my `.bashrc` to make it work. The python variables are to get around
Anaconda's schenanigans. *THIS CURRENTLY DOES NOT WORK*
```bash
apt install libxpm-dev freeglut3-dev
mkdir /opt/root6 && cd /opt/root6
cmake -Dhttp=ON -DPYTHON_EXECUTABLE=/usr/bin/python2 -DPYTHON_INCLUDE_DIRS=/usr/include/python2.7 -DPYTHON_LIBRARY=/usr/lib/python2.7 ../root
make -j 9
. bin/thisroot.sh
```

The last line is only if you want to start working with it right now. Otherwise,
you'll source that location with your next Terminal.

The Jupyter kernel for ROOT doesn't work when you use a C++ kernel. My C++ is
already pretty shaky, so I probably won't get much use out of it. To use it, you
need to install metakernel with `conda install -c ioos metakernel=0.12.4`, then
copy over the kernel to Jupyter's directory.
```
cp -r $ROOTSYS/etc/notebook/kernels/root ~/.local/share/jupyter/kernels
```


Games
-----

[Mednafen](http://mednafen.fobby.net/releases/), a multi-system emulator.
```bash
apt install libsndfile1-dev libsdl1.2-dev
./configure && make -j 9 && sudo make install
```
Your two SNES controllers can be used for the input. You'll want to check that
the input can actually be read (for all required controllers) with
```
sudo chmod 666 /dev/input/js0
jstest /dev/input/js0
```
to make sure everything is registering. After installing, you need to edit the
config file (`~/.mednafen/mednafen.cfg`) so that `sounddevice` is
`sexyal-literal-default`. The sound seems to be staticy for the first minute or
two, but calms down after. You will probably have to reconfigure the controller
buttons as well:

1. Plug in all controllers tha you wish to use
1. Starting with the first controller, hit `alt+shift+1` and follow the prompts for button presses
1. Additional controllers are handled with `alt-shift+X`, up to your maximum port number or four

[RFTG](http://keldon.net/rftg/), the computer version of the card game. Includes
the *Alien Artifacts* expansion, but not Xeno Invasion. Since the last update
was a while ago, I have no idea if it will be updated to include it, but who
knows? Install with
```
apt install libgtk2.0-dev
./configure && make -j 9 && sudo make install
```

[Steam](http://store.steampowered.com/about/), the all-in-one gaming source. It
is available through apt, but if I remember correctly it didn't work quite right
when I used that version. So, download it from the website, start it up, and
redownload all of your old games.


APT Installs
============

During regular usage, you'll add in some additional software through the
regular `apt` channel. Log that here.

- soundconverter: converts between audio file formats

