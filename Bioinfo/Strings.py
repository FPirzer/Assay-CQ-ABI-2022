S1 = "This string is an example"
S2 = "Another example for a long string"
S3 = " A third example for a String, this time with punctuation!"

print(len(S1))
print(len(S2))
print(len(S3))
print("")

for i in range(len(S1)):
    print(S1[i],S2[i],S3[i])
print("")

print(S1[5:20])
print(S2[5:20])
print(S3[5:20])
print("")

print(S1[:0])
print(S1[:1])
print(S1[:2])
print(S1[:3])
print(S1[:4])
print("")

Sp1 = S1.split()
Sp2 = S2.split()
Sp3 = S3.split()
print(Sp1)
print(Sp2)
print(Sp3)
print("")

Sp4 = S1.split(",")
Sp5 = S2.split(",")
Sp6 = S3.split(",")
print(Sp4)
print(Sp5)
print(Sp6)
print("")

print(S1.find("a"))
print(S2.find("a"))
print(S3.find("a"))
print("")

import re
Sp7 = re.split(" |,|;",S1)
Sp8 = re.split(" |,|;",S2)
Sp9 = re.split(" |,|;|!",S3)
print(Sp7)
print(Sp8)
print(Sp9)
print("")

I1 = [m.start() for m in re.finditer("a",S1)]
I2 = [m.start() for m in re.finditer("a",S2)]
I3 = [m.start() for m in re.finditer("a",S3)]
print(I1)
print(I2)
print(I3)


print("string" in S1)
print("string" in S2)
print("string" in S3)
print("")

if "string" in S1: print("This word is in your String, Genius")
if "string" in S2: print("This word is in your String, Genius")
if "string" in S3: print("This word is in your String, Genius")
print("")

print(S1.upper())
print(S2.upper())
print(S3.upper())
print("")

print(S1.lower())
print(S2.lower())
print(S3.lower())
print("")

print(S3.strip())
print("")

print(S1.replace("s","W"))
print(S2.replace("s","W"))
print(S3.replace("s","W"))
print("")

S4 = S1 + S2
S5 = S1 + S3
S6 = S2 + S3
print(S4)
print(S5)
print(S6)
print("")

I1 = 4
S7 = "This string contains {} words"
print(S7.format(I1))
I2 = 3
I3 = 567
F1 = 49.95
S8 = "I want {} pieces of item {} for {} dollars."
print(S8.format(I2,I3,F1))
S9 = "I want to pay {2} dollars for {0} pieces of item {1}."
print(S9.format(I2,I3,F1))
print("")