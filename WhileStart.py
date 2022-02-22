import random

# List of random range
rng = random.randint(0, 50)
list1 = list(range(rng))

print(list1)

# randomlist = random.sample(range(10, 500), 20)
# print(randomlist)

NrSearch = input("Give me a number to check the list against: ")
i = 0
Found = False
# .isdigit() checkt ob die Variable eine Zahl ist
if NrSearch.isdigit():
    NrSearch = int(NrSearch)

    while i < len(list1):
        if NrSearch == list1[i]:
            print("Number ", NrSearch, " found at Index ", i)
            i += 1
            Found = True
        else:
            i += 1
else:
    print("Your input wasn't a positiv number!")


if not Found:
    print("\033[1;32;6mThe number you are looking for is not here!\033[0m")

testmatrix = [
    list(random.sample(range(10, 500), 5)),
    list(random.sample(range(10, 500), 5)),
    list(random.sample(range(10, 500), 5)),
]
print(testmatrix)

value = 0
for i in range(3):
    for j in range(5):
        matrixNr = testmatrix[i][j]
        if value <= matrixNr:
            value = matrixNr
            storeI = int(i)
            storeJ = int(j)

print(
    "The highest value of the list is",
    testmatrix[storeI][storeJ],
    "at Index",
    storeI,
    storeJ,
)

matrixSum = 0
for i in range(3):
    for j in range(5):
        matrixSum += testmatrix[i][j]

print("Sum of all values inside the matrix is", matrixSum)


testmatrix = [
    list(random.sample(range(10, 500), 5)),
    list(random.sample(range(10, 500), 5)),
    list(random.sample(range(10, 500), 5)),
]

testmatrix2 = [
    list(random.sample(range(10, 500), 5)),
    list(random.sample(range(10, 500), 5)),
    list(random.sample(range(10, 500), 5)),
]

# Matrixmultiplikation (Indexweise)
newMatrix = testmatrix.copy()
for i in range(3):
    for j in range(5):
        newMatrix[i][j] = testmatrix[i][j] * testmatrix2[i][j]

print("Multiplied Matrix is\n\033[1;32;6m", newMatrix, "\033[0m")
print(type(newMatrix))
print(len(newMatrix))

# Random Matrixgenerator
# matrix1 = [list(random.sample(range(10, 500), 5))] * (random.randint(10, 20))
#
# print(matrix1)
