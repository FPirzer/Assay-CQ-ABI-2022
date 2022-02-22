Liste = list(range(16))
print(Liste[7])
Sumlist = 0

for i in range(len(Liste)):
    Sumlist = Sumlist + Liste[i]
    if Sumlist < 0:
        pass
    if Sumlist > 100:
        break
    if Sumlist > 50 and Sumlist < 80:
        continue
        print("Range 50-60")
    else:
        if Sumlist < 50:
            print("Under the range of 50-60 (", Sumlist, ") Index:", i)
        elif Sumlist > 80:
            print("Over the range of 50-60 (", Sumlist, ") Index:", i)
