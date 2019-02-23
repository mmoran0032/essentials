#!/usr/bin/env python3


import argparse
from itertools import chain
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
    files = config_linux.iterdir()
    if use_mac_files:
        files = config_mac.iterdir()
    return chain(files, config.iterdir())


def link_config_files(filepaths):
    for f in filepaths:
        # special handling for non-root install locations
        if f.name == 'matplotlibrc':
            mpl_path = root / '.config' / 'matplotlib' / f.name
            remove_and_link(f, mpl_path)
        else:
            remove_and_link(f, root / f'.{f.name}')


def remove_and_link(orig, target):
    if target.exists():
        target.unlink()
    target.symlink_to(orig)


if __name__ == '__main__':
    main()
