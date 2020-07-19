#!/usr/bin/env python3

from pathlib import Path
from typing import Tuple

root = Path.home()
config = Path("config").resolve()


def main() -> None:
    filepaths = config.iterdir()
    for f in filepaths:
        target_path, name = determine_target_path(f)
        remove_and_link(f, target_path / name)
    print("done")


def determine_target_path(f: Path) -> Tuple[Path, str]:
    # handle non-root install locations for particular files
    if f.name == "matplotlibrc":
        _path = root / ".config" / "matplotlib" / f.name
        _name = f.name
    elif f.name == "vscode-settings.json":  # update for VSCode
        _path = root / ".config" / "VSCodium" / "User"
        _name = "settings.json"
    else:
        _path = root
        _name = f".{f.name}"
    return _path, _name


def remove_and_link(orig: Path, target: Path) -> None:
    if target.exists():
        print(f"unlinking {target}")
        target.unlink()
    target.parent.mkdir(exist_ok=True, parents=True)
    print(f"linking {target.name}")
    target.symlink_to(orig)


if __name__ == "__main__":
    main()
