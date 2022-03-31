import re

lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

print(len(lorem))
print(len(lorem.split()))

ABC = list("abcdefghijklmnopqrstuvwxyz")
print(ABC)
for L in ABC:
    nr = len([m.start() for m in re.finditer(L, lorem)])
    print(f"Amount of {L} is {nr}")

for word in ["minim", "anim", "caesar", "brutus", "duis"]:
    if word in lorem:
        print(f"Yes, {word} is in the string")
    else:
        print(f"No, {word} is not in the string")


print(lorem.replace("et", "at"))
print(lorem.replace("in", "on"))
print(lorem.replace("eu", "au"))

lowrem = lorem.lower()
lorup = lorem.upper()
