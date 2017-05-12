#!/usr/bin/env python3


import os
import subprocess

extensions = ('aux', 'bbl', 'blg', 'fdb_latexmk', 'fls',
              'lis', 'lof', 'log', 'lot', 'nav', 'out',
              'snm', 'spl', 'syn', 'toc')
directories = ('__pycache__', 'build', 'dist')
special_dirs = ('egg-info', 'ipynb_checkpoints', 'cache')


def main(start='.'):
    filecount = 0
    dircount = 0
    for directory, subdirs, files in os.walk(start):
        subdirs[:], files = ignore_hidden(subdirs, files)
        filecount += clean_files(directory, files)
        subdirs[:], number = clean_directories(directory, subdirs)
        dircount += number
    print('== Files deleted: {}'.format(filecount))
    print('== Directories deleted: {}'.format(dircount))


def ignore_hidden(subdirs, files):
    subdirs_new = [d for d in subdirs if not d.startswith('.')]
    subdirs_new.extend(d for d in subdirs if d.split('.')[-1] in special_dirs)
    files = [f for f in files if not f.startswith('.')]
    return subdirs_new, files


def clean_files(directory, files):
    filtered = [f for f in files if f.split('.')[-1] in extensions]
    for f in filtered:
        scrub_item(directory, f)
    return len(filtered)


def clean_directories(directory, subdirs):
    filtered = [d for d in subdirs if d in directories]
    filtered.extend(d for d in subdirs if d.split('.')[-1] in special_dirs)
    for d in filtered:
        scrub_item(directory, d)
        subdirs.remove(d)
    return subdirs, len(filtered)


def scrub_item(directory, item):
    name = '{}/{}'.format(directory, item)
    print('Deleting: {}'.format(name))
    subprocess.run('rm -rf {}'.format(name), shell=True)


if __name__ == '__main__':
    main()
