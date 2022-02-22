# # def Addition(a, b):
# #     Summe = a + b
# #     return Summe
# #
# #
# # def Subtraktion(a, b):
# #     Differenz = a - b
# #     return Differenz
# #
# #
# # def Multiplikation(a, b):
# #     Produkt = a * b
# #     return Produkt
# #
# #
# # def Division(a, b):
# #     Quotient = a / b
# #     return Quotient
# #
# #
# # print(Addition(4, 3))
# # print(Addition(-2, 7))
# # print(Addition(-14, -10))
# #
# # print(Subtraktion(4, 3))
# # print(Subtraktion(-2, 7))
# # print(Subtraktion(-14, -10))
# #
# # print(Multiplikation(4, 3))
# # print(Multiplikation(-2, 7))
# # print(Multiplikation(-14, -10))
# #
# # print(Division(4, 3))
# # print(Division(-2, 7))
# # print(Division(-14, -10))

# Diese Funktionen können auch zusammengefasst werden


def MathOperationsBasic(a, b):
    Summe = a + b
    Differenz = a - b
    Produkt = a * b
    Quotient = a / b
    return Summe, Differenz, Produkt, Quotient


print(MathOperationsBasic(164, 2))
print(MathOperationsBasic(1337, 42))
print(MathOperationsBasic(3.14, 21))
print(MathOperationsBasic(25, 5))

#
# def ListSumme(a):
#     forSum = 0
#     for i in range(len(a)):
#         forSum = forSum + i
#     return forSum
#
#
# List1 = list(range(7))
# print("\n\033[1;32;6m", ListSumme(List1), "\033[0m")
#
#
# def ListReverse(a):
#     Reverse = []
#     for i in reversed(range(len(a))):
#         Reverse += [i]
#     return Reverse
#
#
# List2 = list(range(9))
# print("\n\033[1;32;6m", ListReverse(List2), "\033[0m")

#
# import random
#
# testmatrix = [
#     list(random.sample(range(10, 500), 5)),
#     list(random.sample(range(10, 500), 5)),
#     list(random.sample(range(10, 500), 5)),
# ]
# print(testmatrix)
#
#
# def MatrixMax(a):
#     value = 0
#     for i in range(len(a)):
#         for j in range(len(a[i])):
#             matrixNr = a[i][j]
#             if value <= matrixNr:
#                 value = matrixNr
#     return value
#
#
# print(MatrixMax(testmatrix))
#
#
# def MatrixSumme(a):
#     matrixSum = 0
#     for i in range(len(a)):
#         for j in range(len(a[i])):
#             matrixSum += a[i][j]
#     return matrixSum
#
#
# print(MatrixSumme(testmatrix))
#
#
# def MatrixMulti(a, b):
#     newMatrix = a.copy()
#     for i in range(len(a)):
#         for j in range(len(a[i])):
#             newMatrix[i][j] = a[i][j] * b[i][j]
#     return newMatrix
#
#
# print(MatrixMulti(testmatrix, testmatrix))
