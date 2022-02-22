List = list(range(0, 25))
print(List)


def ListRevert(a):
    forSum = 0
    Reverse = list()
    for i in reversed(range(len(a))):
        forSum = forSum + i
        Reverse.append(i)
    return forSum, Reverse


print(ListRevert(List))
