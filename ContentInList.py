Veggy = ["tomato", "onion", "garlic", "chillis", "potatoe"]

Ans = input("Name one of the top 5 veggies for cooking! ")

if Ans.lower() in Veggy:
    print("Absolutly right! You have impeccable taste!")
else:
    print("Sorry but wrong. Search for the depth of flavor!")

Item = input("What do you want to put on the list? ")
Index = int(input("On which position do you want to put " + Item + " ? "))

if Item in Veggy:
    print("Sorry thats already on the list. Choose something else.")
else:
    # list.insert(index, item) fügt Item an der Position Index der Liste Veggy hinzu
    Veggy.insert(Index - 1, Item.lower())

print(Veggy)
