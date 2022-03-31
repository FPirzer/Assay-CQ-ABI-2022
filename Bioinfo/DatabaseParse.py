Proteinbank = {}
Proteinbank["C-alpha"] = {}
seqsum = []
alphasum = []

Genombank = {}
origin = False

with open("1kim.pdb", "r") as proteindb:
    lines = proteindb.readlines()
    for line in lines:
        if line[0:6] == "SEQRES":
            seqsum.append(line)
            Proteinbank["Sequence"] = seqsum
        if line[13:15] == "CA":

            if line[21] not in Proteinbank["C-alpha"]:
                alphasum = []
            alphasum.append(line[23:26])
            Proteinbank["C-alpha"][line[21]] = alphasum


with open("455373.gb", "r") as genomdb:
    seqsum = []
    lines = genomdb.readlines()

    for line in lines:

        if line[0:2] == "//":
            origin = False
        if origin == True:
            parts = line.split()
            print(parts)
            seqsum.append("".join(parts[1:]))
            Genombank["Sequence"] = "".join(seqsum)
        if line[0:6] == "ORIGIN":
            origin = True
print(Genombank)
