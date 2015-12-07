#!/usr/bin/env python3
# Version 1.4 (2015-05-08)


import colorama
import datetime
import subprocess
import sys


def main():
    if len(sys.argv) == 1:
        command = input("Command: ")
    else:
        command = " ".join(sys.argv[1:])

    if not sys.stdout.isatty():
        colorama.init(strip=True)

    fore = colorama.Fore

    start = datetime.datetime.now()
    print("{}Start time: {}{}".format(fore.GREEN, fore.RESET, start))
    print("Running command: {}".format(command))
    subprocess.call(command, shell=True)
    end = datetime.datetime.now()
    print("{}End time: {}{}".format(fore.GREEN, fore.RESET, end))
    print("{}Total time: {}{}".format(fore.GREEN, end - start, fore.RESET))


if __name__ == "__main__":
    main()

