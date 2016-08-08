#!/usr/bin/env python3


import os
import subprocess

config = '/home/mikemoran/bin/essentials/config/'
home = '/home/mikemoran/'


def main():
    files = os.listdir()
    files.remove('setup.py')
    for f in files:
        subprocess.call(
            ['ln', '-s', '{}{}'.format(config, f), '{}.{}'.format(home, f)])


if __name__ == '__main__':
    main()
