#!/usr/bin/env python3


import os
import subprocess
import sys


if __name__ == "__main__":
    out = subprocess.check_output("git diff --cached --name-only", shell=True)
    out = out.decode()
    files = [x for x in out.split("\n") if x.endswith(".py") and
             os.path.exists(x)]

    failed = False
    for path in files:
        ret = subprocess.call("python3 -m flake8 {}".format(path), shell=True)
        if ret != 0:
            failed = True
    if failed:
        sys.exit("commit aborted: code not PEP8 compliant")
