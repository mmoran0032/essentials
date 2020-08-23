
Actively maintained on GitLab: https://gitlab.com/mmoran0032/essentials

# INSTALLATION NOTES

Updated for reinstalling Linux in early 2019

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

   ```bash
   apt install build-essential git rsync tree unzip vim xclip
   ```

1. Create a new SSH key:

   ```bash
   ssh-keygen -t ed25519 -C "mmoran0032@gmail.com"
   ```

1. Install `python` with Anaconda by following the instructions in
   `PYTHON.md` for your primary development work.

1. Run `python setup.py` to link your bash profile, aliases, etc. to the
   required locations.

1. Install python utilities:

   ```bash
   conda install -c conda-forge autopep8 doc8 glances
   ```

1. Install Docker by following the instructions on [Linux Hint][1].
   There is an additional setp from [idroot][2] to add your user to the
   `docker` group so that Docker commands can be run without using
   `sudo`:

   ```bash
   sudo usermod -aG docker $USER
   sudo reboot
   ```

   Note that the second command will reboot your computer. Otherwise,
   you can wait until the next time you log in for the change to take
   effect.

### Applications

The applications listed below are installed by downloading the
application from the respective website. These applications are your
default applications in the respective area.

<!-- - Google Chrome: <https://www.google.com/chrome/> -->
<!-- - Spotify: <https://www.spotify.com/us/download/linux/> -->
- VSCode: <https://code.visualstudio.com/>
- Firefox: <https://www.mozilla.org/en-US/firefox/new/>
- Pandora: <https://www.pandora.com/desktop>

Additional steps for setting up VSCode are given in `EDITORS.md`.

Adjust any computer settings (Terminal background and scrollback,
sounds, user picture, etc) and download any files from the backed-up
external drive that you want.

You have started using Firefox more, due to your increased awareness of
what Google collects and uses. You haven't started taking very hard
stances on technical tools yet (e.g. you still host code on Github), but
that is a growing part of how you think about your technical life.

## Docker

Use [Docker](https://www.docker.com/) for your encapsulated projects.
Since most of these are python-based, you'll end up doing similar work
to building out environments. All of your docker files are in `docker`.
To build an image, run:

```bash
docker build -t mmoran0032/image:0.0.0 - < file
```

Replace the image name, version, and file name with the required values.
To run an image, run:

```bash
docker run -it --rm mmoran0032/image:0.0.0
```

Any additional arguments to the container can be passed in. For example,
if you are running a Jupyter server in the docker image, you can connect
to it by running:

```bash
docker run -it --rm --expose 8888 -p 8888:8888 mmoran0032/jupyter:0.0.0
```

This command allows you to connect to the Jupyter server based on the
address used in the docker image. Copy-paste the provided address, then
replace the host with `localhost`.

## LaTeX

You are not using LaTeX anymore, since you aren't in academia. Your
documents are reports are either:

- raw Markdown/RestructuredText files directly next to code
- internal documents produced through a GSuite application

There is limited use for having LaTeX installed at this point, but I am
keeping the notes here for now.

For compiling PDFs from Markdown/RST files using `pandoc`, you need
LaTeX installed. Run

```bash
apt install texlive-latex-base lmodern texlive-fonts-recommended
```

## Install History

Log of the installations you've done using this package. For
completeness, the partial Mac installs are also listed below, even
though they don't use the entirety of this repository and are not the
focus of tracking installations.

- 2020-07-19: `ARES-4` (Windows 10 + Windows Subsystem for Linux)
- 2019-02-19: `ARES-3` (Linux Mint 19 desktop)
- 2019-01-15: *White Ops* Macbook
- 2017-12-17: `ARES-2m` (Linux Mint 18 laptop)
- 2017-10-16: *Gartner* Macbook
- 2016-05-03: `ARES-2` (Ubuntu 16 laptop)

Previous installations and refreshes of Ubuntu and Linux Mint were not
recorded at the time, so the log is only complete for recent dates. For
instance, I had repeairs done on the `ARES-2*` laptop in July 2014, and
likely did a wipe-and-replace on the harddrive around that time.

[1]: https://linuxhint.com/install_docker_linux_mint/
[2]: https://idroot.us/install-docker-linux-mint-19/
