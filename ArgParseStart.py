import argparse

parser = argparse.ArgumentParser(description="Concatenate strings.")
parser.add_argument(
    "strings", metavar="S", type=str, nargs="+", help="a string for the parser"
)
parser.add_argument("--conc", action="store_true", help="Concatenate all strings")
parser.add_argument(
    "-y", "--yellow", action="store_true", help="print out the string in yellow"
)
parser.add_argument(
    "-b", "--blue", action="store_true", help="print out the string in blue"
)
# If you define multiple parameters for the same function the second needs "--"
parser.add_argument(
    "-g", "--green", action="store_true", help="print out the string in green"
)


args = parser.parse_args()
Concatenate = ""

for string in args.strings:
    Concatenate += string
if args.conc:
    if args.yellow:
        print("\033[1;33;1m", Concatenate, "\033[0m")
    elif args.blue:
        print("\033[1;34;1m", Concatenate, "\033[0m")
    elif args.green:
        print("\033[1;32;1m", Concatenate, "\033[0m")
    else:
        print(Concatenate)
