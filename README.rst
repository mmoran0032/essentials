INSTALLATION NOTES
==================

The next time you wipe your hard drive or decide to upgrade and need to start
from scratch, this will help you out tremendously. Honestly, I'm surprised you
made it as far as you did without making one of these. Now it's finally time to
keep this stuff organized.

*Updated for reinstalling on 2016-05-03*


Beginning Installation
----------------------

While you're still using System76 computers, you'll want to grab their drivers.
This step will only matter if you get a computer with a graphics card or some
other extra thing that you haven't used before, but it's good to have anyway::

    sudo apt-add-repository ppa:system76-dev/stable
    apt update
    apt install system76-driver

You'll want to make sure that everything is installed and upgraded before doing
any of the specialized steps below. Simply run ``apt upgrade`` and allow it to
install the huge block of files, and sit back and wait. Finally, install some
extremely helpful command line tools::

    apt install build-essential cmake git rsync tree unzip vim xclip

Adjust any computer settings (Terminal background and scrollback, sounds, user
picture, etc) and download any files from the backed-up external drive that you
want. In particular (to avoid replacing all of your keys), the ``.ssh``
directory should be copied over.

Uninstall the few applications that you don't want, and download and install
`Google Chrome <https://www.google.com/chrome/browser/desktop/index.html>`__. I
do not uninstall Firefox, since it is good to have a backup browser (and some
web tests work better with Firefox, from my previous experience). This creates
the ``/opt/`` directory if you haven't already, so for the rest of the work
you'll want to transfer ownership over to you::

    sudo chown -R mikemoran /opt/

From here, you can take the steps in any order, since they are (mostly)
independent of each other. For the most part, the python portion is the most
important part for your work and your future work.


Config Files
------------

Most of these files replace the hidden configuration files of the same name in
the home directory. First, remove those old files (only ``.bashrc`` and
``.vimrc`` may be there, plus possibly the ``.git*`` files), then link these
over by running ``setup.py`` in the config directory.


Pairing Logitech Mouse/Keyboard
-------------------------------

The Logitech wireless mouse and keyboard I currently have, and all future ones,
have a pairing software included that only works with Windows. Thankfully,
someone has already developed a way to get this to work in Linux, creating the
``ltunify`` utility. Download and install it using::

    git clone https://git.lekensteyn.nl/ltunify.git
    cd ltunify
    make install-home

Once everything is set, an executable names ``ltunify`` will be in ``~/bin``.
Change to this directory and run::

    sudo ./ltunify pair

and follow the prompts to pair your devices. You can then remove the
``ltunify`` directory created from the clone if you desire.


Git
---

The version of git installed through apt is not the most up-to-date version, so
once you have any git installed (and after making sure your ssh keys are in
place), you'll want to grab the source and install the newer version. There are
a few libraries necessary for compiling to progress::

    apt install asciidoc docbook2x libcurl4-openssl-dev libexpat1-dev libssl-dev xmlto
    git clone git@github.com:git/git.git
    make -j 9 prefix=/usr/local all doc info
    sudo make -j 9 prefix=/usr/local install install-doc install-html install-info

As with all git-based installations, this is done in the ``/opt/`` directory.


Additional Installs
-------------------

Since Linux is free, you need to install some drivers for things like DVD
playback and mp3 decoding::

    apt install ubuntu-restricted-extras libdvdread4
    sudo /usr/share/doc/libdvdread4/install-css.sh

Once you have those, you can grab a few more important programs::

    apt install skype audacious luckybackup texlive-full pavucontrol soundconverter pandoc

For ``luckybackup``, you'll need to set up the actual backup location and make
sure that there aren't weird file duplicates from copying things over.

Julia, a high-level, high-performance computing language, is a newer language
that I may add into my repertoire for programming and data science. Since it is
still young, any initial work with it would be to learn the language and get
used to how it runs. Install it with::

    apt install julia


OPT Directory Contents
----------------------

The following utilities are not necessary for day-to-day work, but are good to
have for day-to-day life. Your ``/opt/`` directory will get full with a few
things before these (conda, chrome, etc), so the directory should already be
there and set up for your work. Any additional utilities will most likely be
put here, including non-specific ones I have repositories on GitHub for.


ROOT
^^^^

ROOT (``git@github.com:root-mirror/root``), the data analysis framework
developed at CERN, is annoying. It only works with Python 2.X right now, and I
tried to get it to work with 3.X with a completely fresh install of everything
to no avail. As such, it can only be imported when using ``python`` to start a
program, not ``python3``.

According to `this
site <https://nlesc.gitbooks.io/cern-root-conda-recipes/content/index.html>`__,
I *can* use Conda to install binaries for ROOT, rootpy, and root-numpy! Plus, it
claims to work with Python3, so I'm doing it! Just in case, I'm copying the
steps below for getting it set up.

You need to add their channel to make sure the packages are downloaded from the
correct place, and to keep it simple I'm going to use Anaconda's environment
manager to keep things sane::

    conda config --add channels https://conda.anaconda.org/NLeSC
    conda create --name=cern root=6 python=3
    source activate cern


Games
^^^^^

`Mednafen <http://mednafen.fobby.net/releases/>`__, a multi-system emulator.
Install it with::

    apt install libsndfile1-dev libsdl1.2-dev
    ./configure && make -j 9 && sudo make install

Your two SNES controllers can be used for the input. You'll want to check that
the input can actually be read (for all required controllers) with::

    sudo chmod 666 /dev/input/js0
    jstest /dev/input/js0

to make sure everything is registering. After installing, you need to edit the
config file (``~/.mednafen/mednafen.cfg``) so that ``sounddevice`` is
``sexyal-literal-default``. The sound seems to be staticy for the first minute
or two, but calms down after. You will probably have to reconfigure the
controller buttons as well:

1.  Plug in all controllers tha you wish to use
2.  Starting with the first controller, hit ``alt+shift+1`` and follow the
    prompts for button presses
3.  Additional controllers are handled with ``alt-shift+X``, up to your maximum
    port number or four

You can also switch between fullscreen and windowed by pressing ``Alt+Enter``.

`RFTG <http://keldon.net/rftg/>`__, the computer version of the card game.
Includes the *Alien Artifacts* expansion, but not *Xeno Invasion*. Since the
last update was a while ago, I have no idea if it will be updated to include
it, but who knows? Install with::

    apt install libgtk2.0-dev
    ./configure && make -j 9 && sudo make install

`Steam <http://store.steampowered.com/about/>`__, the all-in-one gaming source.
It is available through apt, but if I remember correctly it didn't work quite
right when I used that version. So, download it from the website, start it up,
and re-download all of your old games. You can also copy some save data over
from your external, so keep track the next time you do that.


Organization will set you free
------------------------------
