#!/usr/bin/env python3


import os
from pathlib import Path
import subprocess

root = Path.home()
config = Path('config').resolve()
config_mac = Path('config_mac').resolve()
config_linux = Path('config_linux').resolve()


def main():
    files, atom, mpl = get_config_files()
    link_config_files(files, atom, mpl)


def get_config_files():
    files = os.listdir()
    atom = 'init.coffee'
    mpl = 'matplotlibrc'
    files.remove('setup.py')  # this file
    files.remove(atom)
    files.remove(mpl)
    return files, atom, mpl


# adjust the below to use pathlib
def link_config_files(standard, atom, mpl):
    for f in standard:
        subprocess.run('ln -s {1}/{0} {2}/.{0}'.format(f, config, root),
                       shell=True)
    # special handling for Atom
    subprocess.run('ln -s {1}/{0} {2}/.atom/{0}'.format(atom, config, root),
                   shell=True)
    # special handling for matplotlib
    subprocess.run('ln -s {1}/{0} {2}/.config/{3}/{0}'.format(mpl, config, root,
                   mpl[:-2]), shell=True)


if __name__ == '__main__':
    main()
