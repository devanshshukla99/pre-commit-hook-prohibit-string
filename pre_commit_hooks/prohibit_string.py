import argparse
import re


def match(prohibited_strings, filename):
    contents = None
    ret = 0
    with open(filename) as fd:
        contents = fd.read()
    if contents:
        for prohibit in prohibited_strings:
            # print(prohibit)
            if re.search(prohibit, contents):
                print(prohibit)
                ret = 1
    return ret


def main(argv=None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--prohibit-strings', dest="prohibit_strings",
        nargs='+', help='Prohibited strings', default=[])
    parser.add_argument('filenames', nargs='*', help='Filenames to run')
    args = parser.parse_args(argv)

    prohibited_strings = args.prohibit_strings
    retv = 0
    for filename in args.filenames:
        # print(filename)
        retv += match(prohibited_strings, filename)

    return retv


# if __name__ == "__main__":
exit(main())
# print(main())