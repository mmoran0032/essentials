#!/usr/bin/env python3


import argparse
import os
from pathlib import Path

root = Path.home()
config = Path('config').resolve()
config_mac = Path('config_mac').resolve()
config_linux = Path('config_linux').resolve()


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--mac', default=False, action='store_true')
    args = p.parse_args()
    files = get_config_files(args.mac)
    link_config_files(files)


def get_config_files(use_mac_files):
    files = list(config_linux.iterdir())
    if use_mac_files:
        files = list(config_mac.iterdir())
    files.extend(config.iterdir())
    return files


# adjust the below to use pathlib: Path.symlink_to(target)
def link_config_files(filepaths):
    for f in filepaths:
        os.symlink(f'{config}/{f}', f'{root}/.{f}')
    # special handling for non-root install locations
    os.symlink(f'{root}/.init.coffee', f'{root}/.atom/init.coffee')
    os.symlink(f'{root}/.matplotlibrc',
               f'{root}/.config/matplotlib/matplotlibrc')


if __name__ == '__main__':
    main()
