#!/usr/bin/env python3


import argparse
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


def link_config_files(filepaths):
    for f in filepaths:
        # special handling for non-root install locations
        if f.name == 'init.coffee':
            f.symlink_to(root / '.atom' / f.name)
        elif f.name == 'matplotlibrc':
            f.symlink_to(root / '.config' / 'matplotlib' / f.name)
        f.symlink_to(root / f'.{f.name}')


if __name__ == '__main__':
    main()
