from argparse import ArgumentParser

def parse_args() -> str:
    parser = ArgumentParser(description = __doc__)
    parser.add_argument(
        "savefile",
        type = str,
        help = "path to savefile, such as `LBAL.save`"
    )
    return parser.parse_args().savefile

def main(savefile: str) -> None:
    with open(savefile, "r+") as file:
        print(file.read())

if __name__ == "__main__":
    main(parse_args())
