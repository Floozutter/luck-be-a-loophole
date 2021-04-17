"""
a save editor for Luck Be a Landlord!
"""

from luckhole.menu import menu
from luckhole import Save
from json import JSONDecodeError
from argparse import ArgumentParser
from sys import exit
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

def main(insavefile: str, outsavefile: str) -> int:
    # read encoded save from insavefile
    print(f"reading from `{insavefile}`...", end = " ")
    try:
        with open(insavefile, "r") as ifile:
            itext = ifile.read()
    except OSError as e:
        print(f"os error: `{e}`!")
        return 1
    else:
        print("done.")
    # decode input save
    print(f"decoding data...", end = " ")
    try:
        save = Save(itext)
    except JSONDecodeError as e:
        print(f"decode error: `{e}`!")
        return 1
    else:
        print("done.")
    # edit save with menu
    print("entering edit menu...")
    write = menu(save)
    # write edited save to outsavefile if not discarded
    if write:
        print(f"writing to `{outsavefile}`...", end = " ")
        try:
            with open(outsavefile, "w") as ofile:
                ofile.write(str(save).strip() + "\n")
        except OSError as e:
            print(f"os error: `{e}`!")
            return 1
        else:
            print("done. >:3c")
    else:
        print(f"edit discarded without write.")
    return 0

if __name__ == "__main__":
    exit(main(*parse_args()))
