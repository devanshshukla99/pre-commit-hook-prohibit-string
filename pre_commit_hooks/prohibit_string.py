import re
import argparse


def match(prohibited_strings, filename):
    contents = None
    ret = 0
    with open(filename) as fd:
        contents = fd.read()
    if contents:
        for prohibit in prohibited_strings:
            regx = re.compile(prohibit, re.MULTILINE)
            for match in regx.finditer(contents):
                start_lineno = contents[0:match.start()].count("\n")
                print(f"{filename}:{start_lineno}: Prohibited string ({prohibit})")
                ret = 1
    return ret


def main(argv=None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'filenames', nargs='*', help='Filenames to run')
    parser.add_argument(
        '--prohibit-strings', dest="prohibit_strings", type=str,
        help='Prohibited strings', default="")
    args = parser.parse_args(argv)
    prohibited_strings = args.prohibit_strings.split(",")
    retv = 0
    for filename in args.filenames:
        retv |= match(prohibited_strings, filename)

    return retv


if __name__ == "__main__":
    print(exit(main()))
