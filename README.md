
# INSTALLATION NOTES

*Updated for reinstalling Linux in early 2019*

The next time you wipe your hard drive or decide to upgrade and need to
start from scratch, this will help you out tremendously. Honestly, I'm
surprised you made it as far as you did without making one of these. Now
it's finally time to keep this stuff organized.

Install history:

- 2019-02-19: Linux
- 2017-12-17: Linux
- 2017-10-16: Mac
- 2016-05-03: Linux

For Mac installs, you're mostly onlly going to care about the your
`bash_profile`, VSCode settings, and Anaconda/`python`. Since the Mac
installations are for your work computers, their setup will be very
different than your personal computer. In the near future, you should
separate out the Mac instructions into their own document to avoid this
one from bloating.

Your special utility `conda_autoenv` currently works, but breaks the
short path name in `PS1`, so I have to combine those together (probably
by putting the autoenv code within Xrc directly).

## Beginning Installation

Once your computer boots, you need to install the basics. These installs
are split between *applications* (e.g. Chrome, VSCode) and *utilities*
(e.g. `gcc`, `vim`). Before doing any installation, you'll want to make
sure that your current setup is up-to-date. You can do this either with
`apt update && apt upgrade` or by using the Update Manager.

### Utilities

These utilities are primarily command line tools and adjustments. Some
of these are actual tools and others are for your particular style.

1.  Install command line basics:

        apt install build-essential git rsync tree unzip vim xclip

2.  Create a new SSH key:

        ssh-keygen -t rsa -b 4096 -C "mmoran0032@gmail.com"

3.  Install `python` with Anaconda by following the instructions in
    `PYTHON.md` for your primary development work.

4.  Run `python setup.py` to link your bash profile, aliases, etc. to
    the required locations.

5.  Install python utilities:

        conda install -c conda-forge autopep8 doc8 glances

--

Adjust any computer settings (Terminal background and scrollback,
sounds, user picture, etc) and download any files from the backed-up
external drive that you want.







Additional Installs
-------------------

Since Linux is free, you need to install some drivers for things like
DVD playback and mp3 decoding:

    apt install ubuntu-restricted-extras libdvdread4
    sudo /usr/share/doc/libdvdread4/install-css.sh

Once you have those, you can grab a few more important programs:

    apt install skype audacious luckybackup texlive-full pavucontrol
        soundconverter pandoc direnv

For `luckybackup`, you'll need to set up the actual backup location and
make sure that there aren't weird file duplicates from copying things
over.

Additional `apt` installs:

-   ffmpeg



OPT Directory Contents
----------------------

The following utilities are not necessary for day-to-day work, but are
good to have for day-to-day life. Your `/opt/` directory will get full
with a few things before these (conda, chrome, etc), so the directory
should already be there and set up for your work. Any additional
utilities will most likely be put here, including non-specific ones I
have repositories on GitHub for.

### Games

[Mednafen](http://mednafen.fobby.net/releases/), a multi-system
emulator. Install it with:

    apt install libsndfile1-dev libsdl1.2-dev
    ./configure && make -j 9 && sudo make install

Your two SNES controllers can be used for the input. You'll want to
check that the input can actually be read (for all required controllers)
with:

    sudo chmod 666 /dev/input/js0
    jstest /dev/input/js0

to make sure everything is registering. After installing, you need to
edit the config file (`~/.mednafen/mednafen.cfg`) so that `sounddevice`
is `sexyal-literal-default`. The sound seems to be staticy for the first
minute or two, but calms down after. You will probably have to
reconfigure the controller buttons as well:

1.  Plug in all controllers tha you wish to use
2.  Starting with the first controller, hit `alt+shift+1` and follow the
    prompts for button presses
3.  Additional controllers are handled with `alt-shift+X`, up to your
    maximum port number or four

You can also switch between fullscreen and windowed by pressing
`Alt+Enter`.

[RFTG](http://keldon.net/rftg/), the computer version of the card game.
Includes the *Alien Artifacts* expansion, but not *Xeno Invasion*. Since
the last update was a while ago, I have no idea if it will be updated to
include it, but who knows? Install with:

    apt install libgtk2.0-dev
    ./configure && make -j 9 && sudo make install

[Steam](http://store.steampowered.com/about/), the all-in-one gaming
source. It is available through apt, but if I remember correctly it
didn't work quite right when I used that version. So, download it from
the website, start it up, and re-download all of your old games. You can
also copy some save data over from your external, so keep track the next
time you do that.

Docker
------

Use [Docker](https://www.docker.com/) for your encapsulated projects.
Since most of these are python-based, you'll end up doing similar work
to building out environments. All of your docker files are in `docker`.
To build an image, run:

    docker build -t mmoran0032/image:0.0.0 - < file

Replace the image name, version, and file name with the required values.
To run an image, run:

    docker run -it --rm mmoran0032/image:0.0.0

Any additional arguments to the container can be passed in. For example,
if you are running a Jupyter server in the docker image, you can connect
to it by running:

    docker run -it --rm --expose 8888 -p 8888:8888 mmoran0032/jupyter:0.0.0

This command allows you to connect to the Jupyter server based on the
address used in the docker image. Copy-paste the provided address, then
replace the host with `localhost`.
