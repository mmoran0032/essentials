#!/usr/bin/env python3


from pathlib import Path

root = Path.home()
config = Path("config").resolve()


def main():
    filepaths = config.iterdir()
    for f in filepaths:
        target_path = determine_target_path(f)
        remove_and_link(f, target_path)
    print("done")


def determine_target_path(f):
    # handle non-root install locations for particular files
    if f.name == "matplotlibrc":
        _path = root / ".config" / "matplotlib" / f.name
    elif f.name == "vscode-settings.json":  # update for VSCode
        _path = root / ".config" / "VSCodium" / "User" / "settings.json"
    else:
        _path = root / f".{f.name}"
    return _path


def remove_and_link(orig, target):
    if target.exists():
        print(f"unlinking {target}")
        target.unlink()
    target.parent.mkdir(exist_ok=True)  # ensure folders are in place
    print(f"linking {target.name}")
    target.symlink_to(orig)


if __name__ == "__main__":
    main()
