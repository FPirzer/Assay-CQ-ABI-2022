import numpy as np
import pylab as pl

seq1 = "AGCTCGTAGC"
seq2 = "AGCTCGTAGC"
x = []
y = []

for i in range(len(seq1)):
    for j in range(len(seq2)):
        if seq1[i] == seq2[j]:
            x.append(i)
            y.append(j)

pl.plot(x,y,'.k')
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
print(x)
print(y)