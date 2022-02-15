Einkauf = [
    ["Apple", "Pear", "Grape"],
    ["Tomato", "Onion", "Garlic"],
    ["Cookies", "Marshmellow", "Chocolate"],
]
# print(Einkauf)


StillNeed = [
    ["Lemon", "Grapefruite", "Coconut"],
    ["Tomato", "Potato", "Avocado"],
    ["Ice", "Sirup", "Soda"],
]

StillNeed[1].remove(Einkauf[1][0])
print(StillNeed)
