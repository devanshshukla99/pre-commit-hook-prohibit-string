import re
import argparse


def match(prohibited_string, filename):
    ret = 0
    with open(filename) as fd:
        contents = fd.read()
        if contents:
            regx = re.compile(prohibited_string, re.MULTILINE)
            for match in regx.finditer(contents):
                start_lineno = contents[0 : match.start()].count("\n") + 1
                print(f"{filename}:{start_lineno}: Prohibited string ({match.group()})")
                ret = 1
    return ret


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("filenames", nargs="*", help="Filenames to run")
    parser.add_argument(
        "--prohibit-string",
        dest="prohibit_string",
        type=str,
        help='Prohibited strings ("str1,str2,...")',
    )
    args = parser.parse_args(argv)
    retv = 0
    if args.prohibit_string:
        prohibited_strings = args.prohibit_string.replace(",", "|")
        for filename in args.filenames:
            retv |= match(prohibited_strings, filename)
    return retv


if __name__ == "__main__":
    exit(main())
