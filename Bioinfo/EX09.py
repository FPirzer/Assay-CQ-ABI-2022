import numpy as np
import pylab as pl

Window = 2
Error = 0
seq1 = "AGTTGT"
seq2 = "AGTTTGG"
x = []
y = []

for i in range(len(seq1)):
    for j in range(len(seq2)):
        Count = 0
        for k in range(len(seq1[i : i + Window])):
            if i + k < len(seq1) and j + k < len(seq2):
                if seq1[i + k] == seq2[j + k]:
                    Count += 1
        if Window - Count <= Error:
            x.append(i)
            y.append(j)
pl.plot(x, y, ".k")
pl.title("LEK dotplot")
pl.xlabel("Seq1 nucleotides")
pl.xticks(np.arange(len(seq1)), seq1)
pl.xlim(left=-1, right=len(seq1))
pl.ylabel("Seq2 nucleotides")
pl.yticks(np.arange(len(seq2)), seq2)
pl.ylim(bottom=-1, top=len(seq2))
pl.gca().invert_yaxis()
pl.gca().xaxis.tick_top()
pl.gca().xaxis.set_label_position("top")
pl.show()
pl.show()
