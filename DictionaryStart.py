Dict = {}
Dict["Eintrag1"] = "Wert1"
Dict["Eintrag2"] = "Wert2"
Dict["Eintrag3"] = "Wert3"
Dict["Eintrag4"] = "Wert4"
Dict["Eintrag5"] = "Wert5"
Dict["Eintrag6"] = "Wert6"
Dict["Eintrag7"] = "Wert7"
Dict["Eintrag8"] = "Wert8"
Dict["Eintrag9"] = "Wert9"
Dict["Eintrag10"] = "Wert10"
DictCopy = Dict.copy()
print(Dict)

# UserEintrag = input("What entry you want to add? ")
# UserWert = input("What value should the entry have? ")
# Dict[UserEintrag] = UserWert
#
# print(Dict)
#
# RemoveEintrag = input("What entry you want to remove? ")
# del Dict[RemoveEintrag]
# print(Dict)

Search1 = input("What entry you are looking for? ")

if Search1 in Dict:
    #    print(Dict.keys())
    Update1 = input("Please update this entry: ")
    Dict[Search1] = Update1
else:
    Update1 = input("What value should this entry have? ")
    Dict[Search1] = Update1

# Search2 = input("What other entry are you looking for? ")
#
# if Search2 in Dict:
#     #    print(Dict.keys())
#     Update2 = input("Please update this entry: ")
#     Dict[Search2] = Update2
# else:
#     Update2 = input("What value should this entry have? ")
#     Dict[Search2] = Update2
#
# Search3 = input("What other other entry are you looking for? ")
#
# if Search3 in Dict:
#     #    print(Dict.keys())
#     Update3 = input("Please update this entry: ")
#     Dict[Search3] = Update3
# else:
#     Update3 = input("What value should this entry have? ")
#     Dict[Search3] = Update3

print(DictCopy)
print(Dict)
