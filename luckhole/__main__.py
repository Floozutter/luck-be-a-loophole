"""
a save editor for Luck Be a Landlord!
"""

from . import Save
from argparse import ArgumentParser
from typing import Callable, Optional

def parse_args() -> tuple[str, str]:
    parser = ArgumentParser(description = __doc__)
    parser.add_argument(
        "insavefile",
        type = str,
        help = "path to input savefile to edit, such as `LBAL.save`"
    )
    parser.add_argument(
        "outsavefile",
        type = str,
        help = "path to write the savefile edit to (can be same as insavefile)"
    )
    args = parser.parse_args()
    return args.insavefile, args.outsavefile

def prompt(
    name: str,
    default: Optional[str] = None,
    valid: Callable[[str], bool] = lambda s: True
) -> str:
    text = f"{name} [{default}]: " if default is not None else f"{name}: "
    while True:
        value = input(text)
        if default is not None and not value:
            return default
        elif valid(value):
            return value

def menu(save: Save) -> None:
    """handles main menu i/o. returns True to write, and False to discard."""
    save.coins = int(prompt("coins", str(save.coins), lambda s: s.isdigit()))
    return True

def main(insavefile: str, outsavefile: str) -> None:
    # read encoded save from insavefile
    print(f"reading from `{insavefile}`...", end = " ")
    with open(insavefile, "r") as ifile:
        itext = ifile.read()
    print("done.")
    # decode input save
    print(f"decoding data...", end = " ")
    save = Save(itext)
    print("done.")
    # edit save with menu
    write = menu(save)
    # write edited save to outsavefile
    if write:
        print(f"writing to `{outsavefile}`...", end = " ")
        with open(outsavefile, "w") as ofile:
            ofile.write(str(save).strip() + "\n")
        print("done.")
    else:
        print(f"edit discarded without write.")

if __name__ == "__main__":
    main(*parse_args())
