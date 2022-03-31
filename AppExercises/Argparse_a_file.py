import argparse

parser = argparse.ArgumentParser(
    description="Example for the usage of argparse w a file"
)

# # positional argument mandatory
parser.add_argument("infile", type=argparse.FileType("r"), help=("input CVS file"))

# optional arguments
# # parser.add_argument(
# #     "-x", "--xvalue", action="store", type=int, default=0, help="The first value"
# # )
# # parser.add_argument(
# #     "-y", "--yvalue", action="store", type=int, default=0, help="The second value"

args = parser.parse_args()

# read the file line by line and make a nested list from it
with args.infile as file:
    new_list = []
    # line = file.splitlines()
    for line in file:
        clean = line.strip("\n") # remove \n from lines
        new_list.append(clean.split(",")) # split by commas

print("cvs as list array", new_list)
