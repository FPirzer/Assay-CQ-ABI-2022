# Create sets with the set() function
set1 = set(range(int(input("Give me the range for the 1st set: "))))
set2 = set(range(int(input("Give me the range for the 2nd set: "))))
set3 = set(range(int(input("Give me the range for the 3rd set: "))))
set4 = set(range(int(input("Give me the range for the 4th set: "))))
print(set1)
print(type(set1))
# print(set2)
# print(set3)
# print(set4)

# Another way of creating a set
set5 = {1, 2, 3, 4, 5, 5}
print(set1)
pop1 = set1.pop()
print("After first pop: " + str(set1))
pop2 = set1.pop()
print("After second pop: " + str(set1))
set1.add(pop1)
print("Added first pop: " + str(set1))
set1.add(pop2)
print("Added second pop: " + str(set1))
