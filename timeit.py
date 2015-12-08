#!/usr/bin/env python3
# Version 1.4 (2015-05-08)


import colorama
import datetime
import subprocess
import sys

bright = colorama.Style.BRIGHT
green = colorama.Fore.GREEN
red = colorama.Fore.RED
reset = colorama.Style.RESET_ALL


def main():
    if len(sys.argv) == 1:
        command = input("Command: ")
    else:
        command = " ".join(sys.argv[1:])

    if not sys.stdout.isatty():
        colorama.init(strip=True)

    start = datetime.datetime.now()
    print("{}{}Start time: {}{}".format(bright, green, reset, start))
    print("{}{}Running command: {}{}".format(bright, red, command, reset))
    subprocess.call(command, shell=True)
    end = datetime.datetime.now()
    print("{}{}End time: {}{}".format(bright, green, reset, end))
    print("{}{}Total time: {}{}".format(bright, green, end - start, reset))


if __name__ == "__main__":
    main()
