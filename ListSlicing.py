List1 = list(range(11))
print(List1)
print(len(List1))

List2 = list(range(11, 15))
LowEnd1 = int(input("At what position do you want to start your slice for list 1? "))
HighEnd1 = int(input("At what position do you want to end your slice for list 1? "))
if (LowEnd1 > (len(List1) - 1)) or (HighEnd1 > (len(List1) - 1)):
    print("Your numbers are too big. Please select them again.")
    LowEnd1 = int(
        input("At what position do you want to start your slice for list 1? ")
    )
    HighEnd1 = int(input("At what position do you want to end your slice for list 1? "))
else:
    print(List1[LowEnd1:HighEnd1])

# print(List2)
# print(len(List2))
#
# LowEnd2 = int(input("At what position do you want to start your slice for list 2? "))
# HighEnd2 = int(input("At what position do you want to end your slice for list 2? "))
# if (LowEnd2 > (len(List2) - 1)) or (HighEnd2 > (len(List2) - 1)):
#     print("Your numbers are too big. Please select them again.")
#     LowEnd2 = int(
#         input("At what position do you want to start your slice for list 1? ")
#     )
#     HighEnd2 = int(input("At what position do you want to end your slice for list 1? "))
# else:
#     print(List2[LowEnd2:HighEnd2])
