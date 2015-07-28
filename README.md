INSTALLATION NOTES
==================

The next time you wipe your hard drive or decide to upgrade and need to start
from scratch, this will help you out tremendously. Honestly, I'm surprised you
made it as far as you did without making one of these. Now it's finally time to
keep this stuff organized.

APT-GET INSTALLATION
====================

For compiling sources and general command line development, you need a few
packages that aren't included in the base install. Most of these are in support
of other primary packages. I've broken them down into those subsets for ease.

- build-essential vim git texlive-full
- *GIT* libssl-dev libcurl4-openssl-dev libexpat1-dev asciidoc xmlto docbook2x
- *PYTHON* libpython3-dev python3-setuptools python3-psutil
- *MATPLOTLIB* libpng12-dev libfreetype6-dev python3-dateutil python3-pyparsing
  python3-cairo-dev libffi-dev python3-tk tk-dev
- *SCIPY* gfortran liblapack-dev
- *ROOT* libxpm-dev
- libgtk2.0-dev

Previously, I installed them I got to them, but since they are all collected
here (and for 99% of them essential to my current stack), there's no reason to
not just install them all right away.
