
# PYTHON INSTALLATION

You've modernized your view of python virtual environments to follow
some best practices (e.g. everything in a separate environment). The
final step would be using Docker containers, but that's only necessary
if you are setting up a production system, so can be ignored here.

## Anaconda

You've moved from the Miniconda distribution to the full Anaconda
distribution. The `base` environment has all of the standard packages
already installed, so there is no need to specify a separate "default"
environment for general work.

Download the 3.X distribution from their
[website](https://www.anaconda.com/distribution/). You can either use
the graphical installer or the command line utility. I personally prefer
the command line version, but the end result is identical. You can
either keep the installation location to be your home directory or
somewhere else, such as `/opt/`, but this choice doesn't matter much.

Your `.bashrc` is already set up to point to the installation in your
home directory, so if that is your choice, you do not need to add the
sourcing commands to your profile. Launching a new terminal should show
that `conda` is available and the `base` environment is active.

## Environment Setup

Environments are used used to isolate Python versions and packages, and
managed by Anaconda. Environments are specified by an `environment.yml`
file, which includes the conda channels and packages necessary to fully
specify the environment. Specific versions or version ranges can also be
specified, and for a production system should be specified.

The environments that I use are contained in `environments/` in order
for them to be properly versioned and monitored. With the slightly
modified `conda_autoenv.sh` script (adapted from the
[original GitHub source](https://github.com/chdoig/conda-auto-env)), you
do not need to remember the specifics of creating new environments.
Simply define a new `environment.yml` file in the directory, then run
`autoenv`.

When you update an environment from the command line, the environment
file does not update. You have to do that manually so that the
environment and the specification do not get out of sync.
