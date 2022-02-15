List1 = list(range(21))
print(List1)
Start = int(input("Start of the List: "))
End = int(input("End of the List: "))
Steps1 = int(input("Every n-th element of the List: "))
Steps2 = int(input("Every n-th element of the List: "))
Remove = int(input("Which Index should be removed: "))

print("")


# Gibt jedes Element ab Index "End" wieder
print("List with start at Index" + str(Start) + ":")
print(List1[Start::])
print("")

# Gibt jedes Element bis Index "End" wieder
print("List with end at Index " + str(End) + ":")
print(List1[:End:])
print("")

# Gibt nur jedes "Step1"-nte Element der Liste wieder
print("List with every " + str(Steps1) + ". element:")
print(List1[::Steps1])

print("")
print("List with every " + str(Steps2) + ". element:")
print(List1[::Steps2])

print("")
print("List with Index " + str(Remove) + "removed:")
List1.remove(Remove)
print(List1)

# To remove multiple entries use:
# del List1[2:6]
