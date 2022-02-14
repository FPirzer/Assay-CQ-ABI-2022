# # Range from 0 to 25 (excluding 26!!!)
# Number1 = list(range(26))
# print(Number1)
#
# # Range starting from 5 and till 25
# Number2 = list(range(5, 26))
# print(Number2)
#
# # Range from 2 to 25 in Viererschritten
# Number3 = list(range(2, 26, 4))
# print(Number3)

Length = int(input("How long should the list be? "))
Start = int(input("Where should the list start? "))
Incriment = int(input("What should the increment be? "))
List1 = list(range(Start, Length, Incriment))
print(List1)
print("The length of the list is " + str(len(List1)))

List2 = list(range(2, 25, 7))
# Fügt die gesamte List2 als einzelnes Element ein
List1.append(List2)
print(List1)
# Fügt die gesamte List2 hinten in List1 ein
List1.extend(List2)
print(List1)
