
# INSTALLATION NOTES

## *Updated for reinstalling Linux in early 2019*

The next time you wipe your hard drive or decide to upgrade and need to
start from scratch, this will help you out tremendously. Honestly, I'm
surprised you made it as far as you did without making one of these. Now
it's finally time to keep this stuff organized.

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

1. Install command line basics:

        apt install build-essential git rsync tree unzip vim xclip

2. Create a new SSH key:

        ssh-keygen -t rsa -b 4096 -C "mmoran0032@gmail.com"

3. Install `python` with Anaconda by following the instructions in
   `PYTHON.md` for your primary development work.

4. Run `python setup.py` to link your bash profile, aliases, etc. to
   the required locations.

5. Install python utilities:

        conda install -c conda-forge autopep8 doc8 glances

6. (Optional) Install Julia (from the
   [Downloads page](https://julialang.org/downloads/)) and extract::

        tar zxvf julia-1.1.0-linux-x86_64.tar.gz
        mv julia-1.1.0 ~/julia

### Applications

The applications listed below are installed by downloading the
application from the respective website. These applications are your
default applications in the respective area.

- Google Chrome: <https://www.google.com/chrome/>
- Spotify: <https://www.spotify.com/us/download/linux/>
- VSCode: <https://code.visualstudio.com/>

Spotify does not have any additional configuration beyond signing in.
The Chrome Extensions that you use are linked to your account and should
also be installed automatically when you sign in to Chrome. Additional
steps for setting up VSCode are given in `EDITORS.md`.

Adjust any computer settings (Terminal background and scrollback,
sounds, user picture, etc) and download any files from the backed-up
external drive that you want.

## Additional Installs

Since Linux is free, you need to install some drivers for things like
DVD playback and mp3 decoding:

    apt install ubuntu-restricted-extras libdvdread4
    sudo /usr/share/doc/libdvdread4/install-css.sh

Once you have those, you can grab a few more important programs:

    apt install skype audacious luckybackup texlive-full pavucontrol
        soundconverter

For `luckybackup`, you'll need to set up the actual backup location and
make sure that there aren't weird file duplicates from copying things
over.

## Docker

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

## Install History

Log of the installations you've done using this package. For
completeness, the partial Mac installs are also listed below, even
though they don't use the entirety of this repository and are not the
focus of tracking installations.

- 2019-02-19: `ARES-3` (Linux Mint 19 desktop)
- 2019-01-15: *White Ops* Macbook
- 2017-12-17: `ARES-2m` (Linux Mint 18 laptop)
- 2017-10-16: *Gartner* Macbook
- 2016-05-03: `ARES-2` (Ubuntu 16 laptop)
