from Bio import AlignIO
align = AlignIO.read("clustalw2.aln", "clustal")

print(align)
print("")
print(len(align))
print("")

for record in align:
    print("%s %i" % (record.id, len(record)))

print("")
print(align[0])
print(align[0].seq)