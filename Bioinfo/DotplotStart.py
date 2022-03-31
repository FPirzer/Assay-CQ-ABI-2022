import numpy as np
import pylab as pl

with open("Mystery Protein1.txt.txt", "r") as prot1:
    seq1 = prot1.readline()

with open("Mystery Protein2.txt.txt", "r") as prot2:
    seq2 = prot2.readline()

print(seq1)
window = 5
mismatch = 3
x = []
y = []

for i in range(len(seq1) - window):
    for j in range(len(seq2) - window):
        seq1_1 = []
        seq2_1 = []
        score = 0
        seq1_1 = list(seq1[i : i + 5])
        seq2_1 = list(seq2[j : j + 5])
        print(seq1[i : i + window] + " " + seq2[j : j + window])

        for h in range(window):
            if seq1_1[h] == seq2_1[h]:
                score += 1
        if score + mismatch >= window:
            print(score)
            x.append(i)
            y.append(j)
        else:
            print(f"Score:{score} Mismatch:{mismatch}")

# ".k" defines the dots; "." -> makes Dots; "k"-> color black
pl.plot(x, y, ".k")
pl.title("Sequence comparison dotplot")
pl.xlabel("base [sequence 1]")
pl.xticks(np.arange(len(seq1)), seq1)
pl.xlim(left=-1, right=len(seq1))
pl.ylabel("base [sequence 2]")
pl.yticks(np.arange(len(seq2)), seq2)
pl.ylim(bottom=-1, top=len(seq2))
pl.gca().invert_yaxis()
pl.gca().xaxis.tick_top()
pl.gca().xaxis.set_label_position("top")
pl.show()
