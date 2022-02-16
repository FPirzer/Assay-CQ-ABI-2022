template = {}
adress_book = {}
template["Adress"] = ""
template["Tele"] = ""
template["Email"] = ""
template["Bday"] = ""

adress_book["Name1"] = {}
# adress_book["Name2"]={}
adress_book["Name3"] = {}

adress_book["Name1"]["Adress"] = "Beispielweg1"
adress_book["Name1"]["Tele"] = 12345
adress_book["Name1"]["Email"] = "asd@asd.de"
adress_book["Name1"]["Bday"] = "01.01.1980"

adress_book["Name2"] = template

adress_book["Name3"]["Adress"] = "Beispielweg2"
adress_book["Name3"]["Tele"] = 54321
adress_book["Name3"]["Email"] = "qwe@qwe.com"
adress_book["Name3"]["Bday"] = "12.12.2001"

print(adress_book)
print("\n \n")

Mode = input("Do you want to add, edit or delete an entry? ")

if Mode == "edit":
    print(adress_book.keys())
    EntrySelect = input("Which entry do you want to change? ")
    if EntrySelect in adress_book:
        print(adress_book[EntrySelect])
        TypeSelect = input("Which field do you want to change ?")
        InfoSelect = input("What is the new information for this field? ")
        adress_book[EntrySelect][TypeSelect] = InfoSelect
        print(adress_book[EntrySelect])
    else:
        print("Entry not found!")
elif Mode == "add":
    EntrySelect = input("Name the entry you want to add? ")
    TypeSelect = input("Which field do you want to add ? ")
    InfoSelect = input("What is the new information for this field? ")
    adress_book[EntrySelect] = {}
    adress_book[EntrySelect][TypeSelect] = InfoSelect
    print(adress_book[EntrySelect])
    # Only feasable with loops otherwise you ask 100 if loops...
    # ChoiceSelect=input("Do you want to add another field? (yes/no) ")
    #     if ChoiceSelect=="yes":
    print(adress_book)
elif Mode == "delete":
    deleteSelect = input("Delete an entry or field in an entry? (entry OR field) ")
    if deleteSelect == "entry":
        print(adress_book.keys())
        EntrySelect = input("Which entry do you want to remove? ")
        if EntrySelect in adress_book:
            del adress_book[EntrySelect]
            print(adress_book)
        else:
            print("Entry not found! ")
    elif deleteSelect == "field":
        print(adress_book.keys())
        EntrySelect = input("Of which entry do you want to remove a field? ")
        if EntrySelect in adress_book:
            print(adress_book[EntrySelect])
            TypeSelect = input("Which field you want to delete from here? ")
            if TypeSelect in adress_book[EntrySelect]:
                del adress_book[EntrySelect][TypeSelect]
            else:
                print("Field not found!")
        else:
            print("Entry not found! ")
        print(adress_book)
