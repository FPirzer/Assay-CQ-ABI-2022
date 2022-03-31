file = open("Unknown.fasta", "r")
lines = file.readlines()

for i in range(len(lines)):
    lines[i] = lines[i].lower()
print(lines)

seqlist = []
for line in lines:
    if line[0] != ">":
        print(line)
        seqlist.append(line.replace("\n", ""))

print(seqlist)
file.close()
