import argparse
import re


def match(prohibited_strings, filename):
    contents = None
    ret = 0
    with open(filename) as fd:
        contents = fd.read()
    if contents:
        for prohibit in prohibited_strings:
            ret |= re.search(prohibit, contents)
    return ret


def main(argv=None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--prohibit-strings', dest="prohibit_strings",
        nargs='+', help='Prohibited strings', default=[])
    parser.add_argument('filenames', nargs='*', help='Filenames to run')
    args = parser.parse_args(argv)

    prohibited_strings = args.prohibit_strings
    for filename in args.filenames:
        ret = match(prohibited_strings, filename)

    return ret


if __name__ == "__main__":
    exit(main())