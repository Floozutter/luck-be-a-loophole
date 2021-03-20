"""
a save editor for Luck Be a Landlord!
"""

from . import Save
from argparse import ArgumentParser

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

def main(insavefile: str, outsavefile: str) -> None:
    with open(insavefile, "r") as ifile:
        save = Save(ifile.read())
    save.coins = 2**32
    with open(outsavefile, "w") as ofile:
        ofile.write(str(save).strip() + "\n")

if __name__ == "__main__":
    main(*parse_args())
