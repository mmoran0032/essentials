#!/usr/bin/env python3


import os
import subprocess


extensions = ('aux', 'log', 'nav', 'out', 'snm', 'spl', 'syn', 'toc')
directories = ('__pycache__', 'build', 'dist')


def clean_files(directory, files):
    filtered = (f for f in files if f.split('.')[-1] in extensions)
    for f in filtered:
        scrub_item(directory, f)


def clean_directories(directory, subdirs):
    filtered = (d for d in subdirs if d in directories)
    for d in filtered:
        scrub_item(directory, d)
        subdirs.remove(d)
    return subdirs


def scrub_item(directory, item):
    name = '{}/{}'.format(directory, item)
    _ = subprocess.call(['echo', 'Deleting: {}'.format(name)])
    _ = subprocess.call(['rm', '-rf', '{}'.format(name)])


if __name__ == "__main__":
    start = '.'
    print('=== CHECK ===')
    for directory, subdirs, files in os.walk(start):
        print(directory, subdirs, files)

    for directory, subdirs, files in os.walk(start):
        print('=======')
        print(directory, subdirs, files)
        clean_files(directory, files)
        subdirs = clean_directories(directory, subdirs)

    print('=== CHECK ===')
    for directory, subdirs, files in os.walk(start):
        print(directory, subdirs, files)

