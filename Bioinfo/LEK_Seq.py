import numpy as np
import pylab as pl

seq1 = "AGTTGT"
seq2 = "AGTTTGG"

window = 2
mismatch = 0
x = []
y = []

for i in range(len(seq1) - window + 1):
    for j in range(len(seq2) - window + 1):
        seq1_1 = []
        seq2_1 = []
        score = 0
        seq1_1 = list(seq1[i : i + window])
        seq2_1 = list(seq2[j : j + window])
        print(seq1[i : i + window] + " " + seq2[j : j + window])

        for h in range(window):
            if seq1_1[h] == seq2_1[h]:
                score += 1
        if score + mismatch >= window:
            x.append(i)
            y.append(j)


# ".k" defines the dots; "." -> makes Dots; "k"-> color black
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
