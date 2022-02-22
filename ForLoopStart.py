forSum = 0
forEven = 0
forEvenCheat = 0
Reverse = list()
for i in range(0, 22):
    forSum = forSum + i


for i in range(0, 22, 2):
    forEven = forEven + i


# for i in range(22, -1, -1):
#     Reverse.append(i)

for i in reversed(range(0, 22)):
    Reverse += [i]
    # print(Reverse)

for i in range(0, 22):
    forEvenCheat = ((i - 1) / 2) * (((i - 1) / 2) + 1)

# print(forEvenCheat)
# print(Reverse)
# print(forEven)
# print(forSum)
# Summe = sum(range(0, 22))
# print(Summe)


# Thanks to Google for the number generator
import random

# using list comprehension + randrange()
# to generate random number list
RNG = [random.randrange(1, 50, 1) for i in range(20)]
print(RNG)


RNGsum = 0
for i in RNG:
    RNGsum = RNGsum + i
print("Sum of the random mess is " + str(RNGsum))

SizeCompare = input("Give me a number to check the list against: ")
print(i)
# .isdigit() checkt ob die Variable eine Zahl ist
if SizeCompare.isdigit():
    SizeCompare = int(SizeCompare)
    for i in RNG:
        if i > SizeCompare:
            print(str(i) + " is bigger then " + str(SizeCompare))
        elif i == SizeCompare:
            print(str(i) + " is equal to " + str(SizeCompare))
        elif i < SizeCompare:
            print(str(i) + " is smaller then " + str(SizeCompare))
else:
    print("Your input wasn't a number!")
