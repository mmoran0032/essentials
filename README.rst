INSTALLATION NOTES
==================

The next time you wipe your hard drive or decide to upgrade and need to start
from scratch, this will help you out tremendously. Honestly, I'm surprised you
made it as far as you did without making one of these. Now it's finally time to
keep this stuff organized.

*Updated for reinstalling Linux on 2017-12-17*

Install history:
-   2017-12-17 - Linux
-   2017-10-16 - Mac
-   2016-05-03 - Linux

NOTE: ``conda_autoenv`` currently works, but breaks the short path name in
``PS1``, so I have to combine those together (probably by putting the
autoenv code within Xrc directly).


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

    apt install build-essential cmake git rsync tree unzip vim direnv

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
the home directory. To link those files to your current versions, run::

    setup.py [--mac]

where the argument specifies whether or not you're using Linux (default) or on
a Mac. The program will delete any configuration files that exist, then link
yours in place.


Git
---

The version of git installed through apt is not the most up-to-date version, so
once you have any git installed (and after making sure your ssh keys are in
place), you'll want to grab the source and install the newer version. There are
a few libraries necessary for compiling to progress::

    apt install asciidoc docbook2x libcurl4-openssl-dev libexpat1-dev \
        libssl-dev xmlto
    git clone git@github.com:git/git.git
    make -j 9 prefix=/usr/local all doc info
    sudo make -j 9 prefix=/usr/local install install-doc install-html install-info

As with all git-based installations, this is done in the ``/opt/`` directory.

On your Mac, you installed Homebrew and installed Git through that.


Additional Installs
-------------------

Since Linux is free, you need to install some drivers for things like DVD
playback and mp3 decoding::

    apt install ubuntu-restricted-extras libdvdread4
    sudo /usr/share/doc/libdvdread4/install-css.sh

Once you have those, you can grab a few more important programs::

    apt install skype audacious luckybackup texlive-full pavucontrol
        soundconverter pandoc direnv

For ``luckybackup``, you'll need to set up the actual backup location and make
sure that there aren't weird file duplicates from copying things over.

Additional ``apt`` installs:

-   ffmpeg

Apache Spark is a distributed computing framework with Python bindings, using
Java and Scala on the backend. To get it to work, follow the guide
`here <https://www.tutorialspoint.com/apache_spark/apache_spark_installation.htm>`__,
with minor modifications.


OPT Directory Contents
----------------------

The following utilities are not necessary for day-to-day work, but are good to
have for day-to-day life. Your ``/opt/`` directory will get full with a few
things before these (conda, chrome, etc), so the directory should already be
there and set up for your work. Any additional utilities will most likely be
put here, including non-specific ones I have repositories on GitHub for.


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
