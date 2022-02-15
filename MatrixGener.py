# # Quadratische Matrix
# Matrix1 = [list(range(6))] * 6
# # Rechteckig 6 Reihen 5 Spalten
# Matrix2 = [list(range(5))] * 6
# # Rechteckig 5 Reihen 6 Spalten
# Matrix3 = [list(range(6))] * 5
#
# print(Matrix1)
# print(Matrix2)
# print(Matrix3)

Spalte = int(input("How many coloumes do you want? "))
Reihe = int(input("How many rows do you want? "))

UserMatrix = [list(range(Spalte))] * Reihe
print(UserMatrix)

ExampleMatrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

ExampleMatrix[0].remove(UserMatrix[1][2])
print(ExampleMatrix)
