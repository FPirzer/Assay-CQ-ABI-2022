aminoacids = {
    "D",
    "N",
    "G",
    "W",
    "P",
    "E",
    "M",
    "S",
    "F",
    "H",
    "R",
    "Q",
    "K",
    "C",
    "A",
    "Y",
    "V",
    "T",
    "I",
    "L",
}
import re

for i in range(1, 7):
    with open(f"Mystery Protein{i}.txt.txt", "r") as protein:
        lines = protein.readline()
        print(f"\nProtein length {i} is {len(lines)}")
        for AA in aminoacids:
            acid = len([m.start() for m in re.finditer(str(AA), lines)])
            print(f"{AA} found {acid} times ({round(acid*100/len(lines),2)}%)")
            double = str(AA) + str(AA)
            if len([n.start() for n in re.finditer(str(double), lines)]) > 0:
                print(
                    f"Found the repeat {double} for {len([n.start() for n in re.finditer(str(double), lines)])} times"
                )
